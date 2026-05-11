# -*- coding: utf-8 -*-
r"""
QSM Validation V25 - clean article evidence pipeline

This file keeps the stable input/data extraction logic and removes legacy output
experiments.  It only exports the current article structure:

Root summary, using Group1~Group4:
    Fig01_core_power_viewpoint_transformation.png
    Fig02_qsm_power_frequency_group_contact_combined.png
    ALL_GROUPS_V25_post_table.csv
    ALL_GROUPS_V25_raw.csv
    V25_group_color_map.csv

Each Group folder:
    GroupX_Fig01_core_power_viewpoint_transformation.png
    GroupX_Fig02_qsm_power_frequency_group_contact_combined.png
    GroupX_V25_post_table.csv
    GroupX_V25_raw.csv
    V25_group_color_map.csv

Each record:
    <record_id>_V25_core_diagnosis.png       # exactly ten panels
    <record_id>_V25_post_table.csv
    <record_id>_V25_raw.csv

Reading rule:
    Input motion -> QSM Power P(t)=a(t)v(t) -> Power packet -> interface
    Power/Work exchange -> upper-lower displacement response -> QSM Power
    / interface Power / IsoDisp response frequency-group closure with effective isolation-frequency groups.

Only the agreed article figures and CSV files are generated in V25.
"""

from __future__ import annotations

from pathlib import Path
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.transforms import blended_transform_factory

from scipy.signal import butter, filtfilt, welch, hilbert
from scipy.integrate import cumulative_trapezoid
from scipy.stats import pearsonr, spearmanr

warnings.filterwarnings("ignore", category=RuntimeWarning)

# ============================================================
# 0. User settings
# ============================================================

RAW_ROOT = Path(
    r"D:\OneDrive\文件\Quantum Structural Mechanics\Validation"
    r"\data_shakeTableTest_SlidingBearing_PulseLikeGMs"
    r"\data_earthquakeSpectra\raw data"
)

OUT_ROOT = Path(
    r"D:\OneDrive\文件\Quantum Structural Mechanics\Validation"
    r"\QSM_Validation_V25_AllGroups"
)

GROUPS = ["Group1", "Group2", "Group3", "Group4", "Group5"]
ARTICLE_MAIN_GROUPS = ["Group1", "Group2", "Group3", "Group4"]

GROUP_COLOR_MAP = {
    "Group1": "#d62728",  # red
    "Group2": "#ff7f0e",  # orange
    "Group3": "#2ca02c",  # green
    "Group4": "#1f77b4",  # blue
    "Group5": "#9467bd",  # purple, external stress-test only
}

G = 9.80665
EPS = 1e-12
TEFF_SEC = 3.7
PACKET_WINDOW_SEC = 1.0
LOCAL_WINDOW_SEC = 8.0
LOCAL_MIN_SAMPLES = 64
FFT_PEAK_BAND = (0.05, 20.0)
FFT_TOP_N = 8
FFT_MIN_REL_AMP = 0.08
TEFF_FREQ_GROUP_MULTIPLIERS = [0.5, 1.0, 2.0, 3.0, 4.0]
TEFF_CONTACT_TOLERANCE_RATIO = 0.12

OUT_ROOT.mkdir(parents=True, exist_ok=True)


def group_color(group: str) -> str:
    """Return the fixed article color for a Group."""
    return GROUP_COLOR_MAP.get(str(group), "#7f7f7f")


def draw_group_color_strip(fig, groups, y=0.955, fontsize=10):
    """Place a fixed group-color strip under the main figure title.

    Root, Group, and record figures all use this same color-strip grammar so
    the reader does not need to hunt for moving legends inside subplots.
    """
    groups = [str(g) for g in groups if str(g) in GROUP_COLOR_MAP]
    if not groups:
        return
    spacing = 0.095 if len(groups) > 1 else 0.0
    start_x = 0.5 - spacing * (len(groups) - 1) / 2
    for i, g in enumerate(groups):
        x = start_x + i * spacing
        fig.text(x - 0.012, y, "●", color=group_color(g), ha="right", va="center", fontsize=fontsize + 2)
        fig.text(x, y, g, color="black", ha="left", va="center", fontsize=fontsize)


def groups_present_in(df: pd.DataFrame):
    """Return groups present in a DataFrame using the fixed article order.

    Root summary receives only Group1~Group4. Group folders, including Group5,
    receive their own available group so the same plotting functions work for
    both article figures and stress-test figures.
    """
    if df is None or len(df) == 0 or "group" not in df.columns:
        return []
    present = set(df["group"].astype(str))
    return [g for g in GROUPS if g in present]


def format_f_eff_label(multiplier: float) -> str:
    """Return a mathtext label for effective isolation-frequency references."""
    if abs(multiplier - 0.5) < 1e-12:
        return r"$0.5 f_{\mathrm{eff}}$"
    if abs(multiplier - 1.0) < 1e-12:
        return r"$f_{\mathrm{eff}}$"
    return rf"${int(multiplier)} f_{{\mathrm{{eff}}}}$"


def set_relative_amplitude_axis(ax, ymax=1.18):
    """Keep visual headroom while labeling the physical relative-amplitude range only."""
    ax.set_ylim(0, ymax)
    ax.set_yticks(np.linspace(0.0, 1.0, 6))


# ============================================================
# 1. Generic utilities
# ============================================================

def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [str(c).strip().replace("\ufeff", "") for c in df.columns]
    return df


def read_txt_auto(path: Path) -> pd.DataFrame:
    """Read tab/comma/whitespace table and normalize column names."""
    if not path.exists():
        raise FileNotFoundError(path)
    for sep in ["\t", ",", r"\s+"]:
        try:
            df = pd.read_csv(path, sep=sep, engine="python")
            df = clean_columns(df)
            if df.shape[1] >= 2:
                return df
        except Exception:
            pass
    raise ValueError(f"Cannot read table: {path}")


def find_time_col(df: pd.DataFrame):
    for c in df.columns:
        cl = str(c).lower()
        if cl in ["time", "time_s", "t", "sec", "second", "seconds"] or "time" in cl:
            return c
    return df.columns[0]


def find_col_contains(df: pd.DataFrame, keys, exclude=None):
    keys = [k.lower() for k in keys]
    exclude = [e.lower() for e in (exclude or [])]
    for c in df.columns:
        cl = str(c).lower()
        if all(k in cl for k in keys) and not any(e in cl for e in exclude):
            return c
    return None


def numeric_series(df: pd.DataFrame, col):
    return pd.to_numeric(df[col], errors="coerce").to_numpy(dtype=float)


def estimate_fs(t):
    dt = np.diff(np.asarray(t, dtype=float))
    dt = dt[np.isfinite(dt) & (dt > 0)]
    if len(dt) == 0:
        return np.nan
    return 1.0 / np.median(dt)


def interp_to_time(t_src, y_src, t_new):
    mask = np.isfinite(t_src) & np.isfinite(y_src)
    t_src = np.asarray(t_src)[mask]
    y_src = np.asarray(y_src)[mask]
    if len(t_src) < 2:
        return np.full_like(t_new, np.nan, dtype=float)
    order = np.argsort(t_src)
    t_src = t_src[order]
    y_src = y_src[order]
    uniq, idx = np.unique(t_src, return_index=True)
    return np.interp(t_new, uniq, y_src[idx])


def bandpass_or_lowpass(y, fs, low=None, high=None, order=3):
    y = np.nan_to_num(np.asarray(y, dtype=float))
    if not np.isfinite(fs) or fs <= 0:
        return y
    nyq = 0.5 * fs
    try:
        if low is not None and high is not None:
            low_n = max(low / nyq, 1e-5)
            high_n = min(high / nyq, 0.999)
            if low_n >= high_n:
                return y
            b, a = butter(order, [low_n, high_n], btype="band")
        elif high is not None:
            b, a = butter(order, min(high / nyq, 0.999), btype="low")
        elif low is not None:
            b, a = butter(order, max(low / nyq, 1e-5), btype="high")
        else:
            return y
        return filtfilt(b, a, y)
    except Exception:
        return y


def moving_abs_integral(y, t, window_sec=1.0):
    """Moving integral of |y| over a time window."""
    y_abs = np.abs(np.nan_to_num(np.asarray(y, dtype=float)))
    fs = estimate_fs(t)
    if not np.isfinite(fs) or fs <= 0:
        return np.full_like(y_abs, np.nan)
    nwin = max(2, int(round(window_sec * fs)))
    dt = np.median(np.diff(t))
    return np.convolve(y_abs, np.ones(nwin) * dt, mode="same")


def safe_corr(x, y, method="pearson"):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    mask = np.isfinite(x) & np.isfinite(y)
    if mask.sum() < 3:
        return np.nan
    if np.nanstd(x[mask]) < EPS or np.nanstd(y[mask]) < EPS:
        return np.nan
    try:
        if method == "spearman":
            return float(spearmanr(x[mask], y[mask]).correlation)
        return float(pearsonr(x[mask], y[mask])[0])
    except Exception:
        return np.nan


def sanitize_units_mm(x):
    """Conservative V8 displacement normalization: if tiny, assume meter; else mm."""
    x = np.asarray(x, dtype=float)
    if np.nanmax(np.abs(x)) < 3:
        return x * 1000.0
    return x


def envelope_signal(y):
    return np.abs(hilbert(np.nan_to_num(np.asarray(y, dtype=float))))


def get_peak_time_and_value(t, y, abs_peak=True):
    y = np.asarray(y, dtype=float)
    if len(y) == 0 or np.all(~np.isfinite(y)):
        return np.nan, np.nan
    idx = np.nanargmax(np.abs(y)) if abs_peak else np.nanargmax(y)
    return float(t[idx]), float(y[idx])


# ============================================================
# 2. File reading and column inference
# ============================================================

def read_group_record(group: str, filename: str):
    return (
        read_txt_auto(RAW_ROOT / "mocap" / group / filename),
        read_txt_auto(RAW_ROOT / "sensor" / group / filename),
        read_txt_auto(RAW_ROOT / "shakingTable" / group / filename),
    )


def infer_acc_column(shake: pd.DataFrame, sensor: pd.DataFrame):
    for df in [shake, sensor]:
        for keys in [["acc", "x"], ["accx"], ["acceleration", "x"], ["ax"]]:
            c = find_col_contains(df, keys)
            if c is not None:
                return df, c
    for df in [shake, sensor]:
        tcol = find_time_col(df)
        for c in df.columns:
            if c != tcol and pd.to_numeric(df[c], errors="coerce").notna().sum() > 10:
                return df, c
    raise KeyError("Cannot infer acceleration column.")


def infer_shake_disp_column(shake: pd.DataFrame):
    for keys in [["disp", "x"], ["dispx"], ["displacement", "x"]]:
        c = find_col_contains(shake, keys)
        if c is not None:
            return c
    return find_col_contains(shake, ["disp"])


def infer_mocap_columns(mocap: pd.DataFrame):
    direct_iso = find_col_contains(mocap, ["iso"])
    direct_upper = find_col_contains(mocap, ["upper"])
    direct_frame = find_col_contains(mocap, ["frame"])
    lavg = gavg = f1avg = None
    for c in mocap.columns:
        cl = str(c).lower()
        if ("lavg" in cl or "load" in cl) and "x" in cl:
            lavg = c
        if ("gavg" in cl or "ground" in cl) and "x" in cl:
            gavg = c
        if ("1favg" in cl or "upper" in cl or "1f" in cl) and "x" in cl:
            f1avg = c
    return {"direct_iso": direct_iso, "direct_upper": direct_upper, "direct_frame": direct_frame, "lavg": lavg, "gavg": gavg, "f1avg": f1avg}


def infer_load_cell_total_x(sensor: pd.DataFrame):
    lc_cols = []
    for c in sensor.columns:
        cl = str(c).lower()
        if "lc" in cl and "x" in cl and pd.to_numeric(sensor[c], errors="coerce").notna().sum() > 10:
            lc_cols.append(c)
    if lc_cols:
        return lc_cols
    for c in sensor.columns:
        cl = str(c).lower()
        if "force" in cl and "x" in cl:
            return [c]
    return []


def list_group_files(group: str):
    sensor_dir = RAW_ROOT / "sensor" / group
    if not sensor_dir.exists():
        raise FileNotFoundError(sensor_dir)
    files = sorted(p.name for p in sensor_dir.glob("*.txt"))
    return [f for f in files if all((RAW_ROOT / sub / group / f).exists() for sub in ["mocap", "sensor", "shakingTable"])]


# ============================================================
# 3. Frequency-group extraction
# ============================================================

def local_window_mask(t, center_time, window_sec=LOCAL_WINDOW_SEC):
    if not np.isfinite(center_time):
        return np.ones_like(t, dtype=bool)
    half = 0.5 * window_sec
    mask = (t >= center_time - half) & (t <= center_time + half)
    if mask.sum() < LOCAL_MIN_SAMPLES:
        return np.ones_like(t, dtype=bool)
    return mask


def fft_peak_group(y, t, fs, center_time=None, window_sec=LOCAL_WINDOW_SEC, band=FFT_PEAK_BAND, top_n=FFT_TOP_N):
    """Return top local FFT peaks as a frequency group, not as a single dominant frequency."""
    y = np.nan_to_num(np.asarray(y, dtype=float))
    mask = local_window_mask(t, center_time, window_sec)
    yy = y[mask]
    if len(yy) < 16 or not np.isfinite(fs) or fs <= 0:
        return []
    yy = yy - np.nanmean(yy)
    win = np.hanning(len(yy))
    spec = np.abs(np.fft.rfft(yy * win))
    freqs = np.fft.rfftfreq(len(yy), d=1.0 / fs)
    bmask = (freqs >= band[0]) & (freqs <= band[1]) & np.isfinite(spec)
    if bmask.sum() == 0:
        return []
    ff = freqs[bmask]
    ss = spec[bmask]
    if np.nanmax(ss) <= EPS:
        return []
    rel = ss / np.nanmax(ss)

    idxs = []
    for i in range(1, len(rel) - 1):
        if rel[i] >= rel[i - 1] and rel[i] >= rel[i + 1] and rel[i] >= FFT_MIN_REL_AMP:
            idxs.append(i)
    if not idxs:
        idxs = list(np.where(rel >= FFT_MIN_REL_AMP)[0])
    idxs = sorted(idxs, key=lambda i: rel[i], reverse=True)

    peaks = []
    for i in idxs:
        f = float(ff[i])
        if f <= 0:
            continue
        if any(abs(f - p["freq_Hz"]) / max(f, p["freq_Hz"], EPS) < 0.08 for p in peaks):
            continue
        peaks.append({"freq_Hz": f, "period_s": 1.0 / f, "rel_amp": float(rel[i])})
        if len(peaks) >= top_n:
            break
    return peaks


def peaks_to_string(peaks, key="freq_Hz", ndigits=3):
    if not peaks:
        return ""
    return ";".join(f"{p.get(key, np.nan):.{ndigits}f}" for p in peaks)


def add_peak_columns(row: dict, prefix: str, peaks):
    for i in range(FFT_TOP_N):
        p = peaks[i] if i < len(peaks) else {}
        row[f"{prefix}_peak{i+1}_freq_Hz"] = p.get("freq_Hz", np.nan)
        row[f"{prefix}_peak{i+1}_period_s"] = p.get("period_s", np.nan)
        row[f"{prefix}_peak{i+1}_rel_amp"] = p.get("rel_amp", np.nan)
    return row


def teff_contact_candidates(peaks, f_eff, tolerance=TEFF_CONTACT_TOLERANCE_RATIO):
    """List QSM Power peaks near 0.5/1/2/3/4 f_eff without creating a score."""
    out = []
    if not peaks or not np.isfinite(f_eff) or f_eff <= 0:
        return out
    for p in peaks:
        f = p.get("freq_Hz", np.nan)
        if not np.isfinite(f):
            continue
        for m in TEFF_FREQ_GROUP_MULTIPLIERS:
            target = m * f_eff
            rel_err = abs(f - target) / target if target > 0 else np.nan
            if np.isfinite(rel_err) and rel_err <= tolerance:
                label = "0.5f_eff" if abs(m - 0.5) < 1e-12 else f"{int(m)}f_eff"
                out.append({
                    "freq_Hz": f,
                    "rel_amp": p.get("rel_amp", np.nan),
                    "target_Hz": target,
                    "target_label": label,
                    "rel_error": rel_err,
                })
    return sorted(out, key=lambda r: (r["rel_error"], -r.get("rel_amp", 0)))


def contact_text(peaks, f_eff, max_items=8):
    candidates = teff_contact_candidates(peaks, f_eff)
    parts = [f"{r['freq_Hz']:.3g}Hz~{r['target_label']}" for r in candidates[:max_items]]
    return "; ".join(parts)


# ============================================================
# 4. Plot helpers
# ============================================================

def draw_effective_frequency_lines(ax, f_eff, top_frac=0.965, fontsize=8):
    """Draw f_eff reference lines with mathtext labels inside the plotting area.

    V25 keeps labels inside each subplot and renders f_eff as a scientific
    symbol. The y-position is in axes coordinates, so the same function works
    for displacement maps and relative-amplitude maps.
    """
    if not np.isfinite(f_eff) or f_eff <= 0:
        return
    trans = blended_transform_factory(ax.transData, ax.transAxes)
    for m in TEFF_FREQ_GROUP_MULTIPLIERS:
        x = m * f_eff
        label = format_f_eff_label(m)
        ax.axvline(
            x,
            linestyle="--" if abs(m - 1.0) < 1e-12 else ":",
            color="#1f77b4",
            linewidth=1.2,
            alpha=0.9,
        )
        ax.text(
            x,
            top_frac,
            label,
            transform=trans,
            rotation=90,
            ha="center",
            va="top",
            fontsize=fontsize,
            clip_on=True,
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.78, pad=0.5),
        )

def expand_y_axis_for_labels(ax, top_pad_frac=0.16, bottom_pad_frac=0.02):
    """Add vertical headroom so annotations do not collide with data or axes."""
    ymin, ymax = ax.get_ylim()
    span = max(ymax - ymin, EPS)
    ax.set_ylim(ymin - bottom_pad_frac * span, ymax + top_pad_frac * span)


def expand_x_axis_for_labels(ax, left_pad_frac=0.035, right_pad_frac=0.08):
    """Add horizontal room for edge labels inside the plotting frame."""
    xmin, xmax = ax.get_xlim()
    span = max(xmax - xmin, EPS)
    ax.set_xlim(xmin - left_pad_frac * span, xmax + right_pad_frac * span)


def plot_frequency_group_bars(ax, peaks, title, color, prefix="Q"):
    ax.set_title(title)
    ax.set_xlabel("Frequency [Hz]")
    ax.set_ylabel("Relative amplitude")
    ax.grid(True, alpha=0.25)
    if not peaks:
        ax.text(0.5, 0.5, "No frequency peaks", transform=ax.transAxes, ha="center", va="center")
        return
    for i, p in enumerate(peaks, start=1):
        f = p.get("freq_Hz", np.nan)
        a = p.get("rel_amp", np.nan)
        if np.isfinite(f) and np.isfinite(a):
            ax.scatter([f], [a], s=55, color=color, alpha=0.82)
            ax.vlines(f, 0, a, color=color, alpha=0.35, linewidth=1.2)
            ax.text(
                f, a, f"{prefix}{i}",
                fontsize=8, ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", alpha=0.62, pad=0.25),
            )
    set_relative_amplitude_axis(ax, ymax=1.18)


def record_short_name(record_id: str) -> str:
    rid = str(record_id)
    return rid.split("_")[0] if "_" in rid else rid


def annotate_scatter_records(ax, df: pd.DataFrame, xcol: str, ycol: str = "IsoDisp_peak_abs_mm", label_col: str = "record_id"):
    """Annotate record points without letting labels escape the frame.

    Labels near the left edge are pushed right; labels near the right edge are
    pushed left.  Labels near the top are pushed downward.  A small white bbox
    keeps the text readable over grid lines and markers.
    """
    if len(df) == 0 or xcol not in df.columns or label_col not in df.columns:
        return
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    x_span = max(xmax - xmin, EPS)
    y_span = max(ymax - ymin, EPS)

    for _, row in df.iterrows():
        x = row.get(xcol, np.nan)
        y = row.get(ycol, np.nan)
        if not (np.isfinite(x) and np.isfinite(y)):
            continue
        label = record_short_name(row.get(label_col, ""))

        # Clamp the anchor point into a safe interior band.
        x_safe = min(max(x, xmin + 0.018 * x_span), xmax - 0.018 * x_span)
        y_safe = min(max(y, ymin + 0.025 * y_span), ymax - 0.10 * y_span)

        if x <= xmin + 0.16 * x_span:
            dx, ha = 5, "left"
        elif x >= xmax - 0.16 * x_span:
            dx, ha = -5, "right"
        else:
            dx, ha = 4, "left"

        if y >= ymax - 0.20 * y_span:
            dy, va = -7, "top"
        else:
            dy, va = 4, "bottom"

        ax.annotate(
            label,
            xy=(x_safe, y_safe),
            xytext=(dx, dy),
            textcoords="offset points",
            fontsize=7,
            ha=ha,
            va=va,
            clip_on=True,
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.65, pad=0.35),
        )


def annotate_row_source_labels(ax, peak_df: pd.DataFrame, xcol: str = "freq_Hz", ycol: str = "IsoDisp_peak_abs_mm"):
    """Put one record label per horizontal response row near the right edge."""
    if len(peak_df) == 0 or "record_id" not in peak_df.columns:
        return
    xmax = ax.get_xlim()[1]
    xmin = ax.get_xlim()[0]
    ymin, ymax = ax.get_ylim()
    x_text = xmax - 0.018 * max(xmax - xmin, EPS)
    min_sep = 0.024 * max(ymax - ymin, EPS)
    grouped = (
        peak_df.groupby("record_id", as_index=False)
        .agg(**{ycol: (ycol, "first")})
        .sort_values(ycol)
        .reset_index(drop=True)
    )
    adjusted = []
    for y in grouped[ycol].astype(float).tolist():
        y_adj = min(max(y, ymin + 0.04 * (ymax - ymin)), ymax - 0.12 * (ymax - ymin))
        if adjusted and y_adj - adjusted[-1] < min_sep:
            y_adj = adjusted[-1] + min_sep
        adjusted.append(min(y_adj, ymax - 0.06 * (ymax - ymin)))
    grouped["label_y"] = adjusted
    for _, row in grouped.iterrows():
        ax.text(
            x_text,
            row["label_y"],
            record_short_name(row["record_id"]),
            fontsize=7,
            ha="right",
            va="center",
            clip_on=True,
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.62, pad=0.35),
        )


# ============================================================
# 5. Record computation and record output
# ============================================================

def make_record_core_diagnosis(bundle: dict, out_path: Path):
    """Make the one-record 10-panel core diagnosis figure."""
    group = bundle["group"]
    record_id = bundle["record_id"]
    c = group_color(group)
    t = bundle["t"]
    f_eff = bundle["f_eff_Hz"]

    fig, axes = plt.subplots(5, 2, figsize=(18, 22))
    ax = axes.ravel()
    local_t0 = bundle["local_t0_s"]
    local_t1 = bundle["local_t1_s"]
    packet_t = bundle["QSM_packet_peak_time_s"]
    iso_t = bundle["IsoDisp_peak_time_s"]

    # A. input acceleration
    ax[0].plot(t, bundle["acc_g"], color=c, lw=1.0, label="a(t)")
    ax[0].axvspan(local_t0, local_t1, color=c, alpha=0.08, label="QSM local window")
    ax[0].axvline(packet_t, color="black", ls="--", lw=1, label="QSM packet peak")
    ax[0].axvline(iso_t, color="gray", ls=":", lw=1, label="IsoDisp peak")
    ax[0].set_title("A. Input acceleration a(t)")
    ax[0].set_ylabel("g")
    ax[0].grid(True, alpha=0.25)
    ax[0].legend(fontsize=8, loc="upper right")

    # B. acceleration frequency group
    plot_frequency_group_bars(ax[1], bundle["acc_peaks"], "B. Acceleration frequency group", c, prefix="A")
    draw_effective_frequency_lines(ax[1], f_eff, top_frac=0.965)

    # C. input velocity
    ax[2].plot(t, bundle["vel"], color=c, lw=1.0, label="v(t)")
    ax[2].axvspan(local_t0, local_t1, color=c, alpha=0.08)
    ax[2].axvline(packet_t, color="black", ls="--", lw=1)
    ax[2].axvline(iso_t, color="gray", ls=":", lw=1)
    ax[2].set_title("C. Input velocity v(t)")
    ax[2].set_ylabel("m/s")
    ax[2].grid(True, alpha=0.25)
    ax[2].legend(fontsize=8, loc="upper right")

    # D. velocity frequency group
    plot_frequency_group_bars(ax[3], bundle["vel_peaks"], "D. Velocity frequency group", c, prefix="V")
    draw_effective_frequency_lines(ax[3], f_eff, top_frac=0.965)

    # E. QSM Power
    ax[4].plot(t, bundle["P_signed"], color=c, lw=1.0, label="P(t)=a(t)v(t)")
    ax[4].plot(t, bundle["P_env"], color="black", lw=1.0, alpha=0.55, label="Power envelope")
    ax[4].axvspan(local_t0, local_t1, color=c, alpha=0.08)
    ax[4].axvline(packet_t, color="black", ls="--", lw=1)
    ax[4].axvline(iso_t, color="gray", ls=":", lw=1)
    ax[4].set_title("E. Input-side QSM Power P(t)=a(t)v(t)")
    ax[4].set_ylabel("W/kg")
    ax[4].grid(True, alpha=0.25)
    ax[4].legend(fontsize=8, loc="upper right")

    # F. QSM Power frequency group
    plot_frequency_group_bars(ax[5], bundle["P_peaks"], "F. QSM Power frequency group", c, prefix="Q")
    draw_effective_frequency_lines(ax[5], f_eff, top_frac=0.965)

    # G. QSM Power packet
    ax[6].plot(t, bundle["P_packet_1s"], color=c, lw=1.2, label="1s ∫|a·v|dt packet")
    ax[6].plot(t, bundle["P_abs_integral"], color="black", lw=1.0, alpha=0.55, label="cumulative ∫|a·v|dt")
    ax[6].axvline(packet_t, color="black", ls="--", lw=1)
    ax[6].axvline(iso_t, color="gray", ls=":", lw=1)
    ax[6].set_title("G. QSM Power packet and cumulative |P| integral")
    ax[6].set_ylabel("J/kg")
    ax[6].grid(True, alpha=0.25)
    ax[6].legend(fontsize=8, loc="upper right")

    # H. interface exchange
    interface_work_curve = cumulative_trapezoid(np.abs(np.nan_to_num(bundle["interface_power_kW"])), t, initial=0.0)
    ax[7].plot(t, bundle["interface_power_kW"], color=c, lw=0.9, alpha=0.65, label="Interface Power F·v_rel")
    ax[7].plot(t, bundle["interface_packet_1s"], color="black", lw=1.1, alpha=0.75, label="1s interface packet")
    ax[7].plot(t, interface_work_curve, color="gray", lw=1.0, alpha=0.75, label="cumulative interface Work")
    ax[7].axvline(packet_t, color="black", ls="--", lw=1)
    ax[7].axvline(iso_t, color="gray", ls=":", lw=1)
    ax[7].set_title("H. Interface Power / Work exchange")
    ax[7].set_ylabel("kW / kJ")
    ax[7].grid(True, alpha=0.25)
    ax[7].legend(fontsize=8, loc="upper right")

    # I. measured response
    ax[8].plot(t, bundle["iso_mm"], color=c, lw=1.2, label="u_iso = upper-lower")
    ax[8].plot(t, bundle["upper_mm"], color="black", lw=0.9, alpha=0.55, label="upper displacement")
    ax[8].plot(t, bundle["frame_mm"], color="gray", lw=0.9, alpha=0.70, label="frame relative")
    ax[8].axvline(packet_t, color="black", ls="--", lw=1)
    ax[8].axvline(iso_t, color="gray", ls=":", lw=1)
    ax[8].set_title("I. Measured upper-lower displacement response")
    ax[8].set_xlabel("Time [s]")
    ax[8].set_ylabel("mm")
    ax[8].grid(True, alpha=0.25)
    ax[8].legend(fontsize=8, loc="upper right")

    # J. Frequency-domain closure map.
    # This panel no longer plots frequency against a single IsoDisp peak value,
    # because a single response peak makes the map collapse into a horizontal
    # line.  Instead, it compares the frequency groups of three layers:
    # input-side QSM Power, measured interface Power, and measured IsoDisp
    # response.  The effective isolation-frequency group lines remain only as
    # reference lines.
    ax[9].set_title("J. QSM / Interface / IsoDisp frequency-group closure")

    def plot_closure_peaks(peaks, marker, label, edgecolor=None, facecolor=None, y_offset=0.0):
        for i, p in enumerate(peaks, start=1):
            f = p.get("freq_Hz", np.nan)
            a = p.get("rel_amp", np.nan)
            if np.isfinite(f) and np.isfinite(a):
                y = min(1.0, max(0.0, a + y_offset))
                ax[9].scatter(
                    [f], [y],
                    s=55 + 120 * a,
                    marker=marker,
                    edgecolors=edgecolor if edgecolor is not None else c,
                    facecolors=facecolor if facecolor is not None else c,
                    linewidths=1.0,
                    alpha=0.78,
                    label=label if i == 1 else None,
                )
                ax[9].text(
                    f, y, f"{label[0]}{i}",
                    fontsize=7, ha="center", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", alpha=0.68, pad=0.25),
                )

    plot_closure_peaks(bundle["P_peaks"], "o", "QSM Power", edgecolor=c, facecolor=c, y_offset=0.00)
    plot_closure_peaks(bundle["interface_power_peaks"], "s", "Interface Power", edgecolor=c, facecolor="none", y_offset=-0.015)
    plot_closure_peaks(bundle["iso_resp_peaks"], "^", "IsoDisp response", edgecolor="black", facecolor=c, y_offset=-0.030)
    set_relative_amplitude_axis(ax[9], ymax=1.18)
    draw_effective_frequency_lines(ax[9], f_eff, top_frac=0.965)
    ax[9].set_xlabel("Frequency [Hz]")
    ax[9].set_ylabel("Relative amplitude [0-1]")
    ax[9].grid(True, alpha=0.25)
    ax[9].legend(fontsize=8, loc="upper right")

    fig.suptitle(f"{group} / {record_id} - V25 QSM Power mechanism diagnosis", fontsize=16, y=0.982)
    draw_group_color_strip(fig, [group], y=0.958, fontsize=10)
    fig.tight_layout(rect=[0, 0, 1, 0.935])
    assert len(fig.axes) == 10, f"V25 record diagnosis must have 10 panels; got {len(fig.axes)}"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=180, bbox_inches="tight")
    plt.close(fig)


def build_record_post_table(bundle: dict) -> pd.DataFrame:
    """Human-readable table aligned with the 10-panel record figure.

    V25 purpose:
    - This is the post/article table, not the debug dump.
    - A and C are no longer blank; they show baseline kinematic peak values.
    - G/H include packet magnitude and lag so the timing relation can be read
      without reopening the raw audit table.
    """
    rows = [
        {
            "panel": "A",
            "figure_item": "Input acceleration a(t)",
            "role_in_argument": "kinematic baseline",
            "what_to_read": "upstream acceleration peak magnitude",
            "key_value": bundle["Acceleration_peak_abs_g"],
            "unit": "g",
            "note": "baseline input motion; not a Power quantity",
        },
        {
            "panel": "B",
            "figure_item": "Acceleration frequency group",
            "role_in_argument": "frequency baseline",
            "what_to_read": "top local acceleration frequency peaks",
            "key_value": peaks_to_string(bundle["acc_peaks"]),
            "unit": "Hz",
            "note": "local window around QSM packet peak",
        },
        {
            "panel": "C",
            "figure_item": "Input velocity v(t)",
            "role_in_argument": "kinematic baseline",
            "what_to_read": "upstream velocity peak magnitude",
            "key_value": bundle["Velocity_peak_abs_mps"],
            "unit": "m/s",
            "note": "velocity layer before QSM Power conversion",
        },
        {
            "panel": "D",
            "figure_item": "Velocity frequency group",
            "role_in_argument": "frequency baseline",
            "what_to_read": "top local velocity frequency peaks",
            "key_value": peaks_to_string(bundle["vel_peaks"]),
            "unit": "Hz",
            "note": "local window around QSM packet peak",
        },
        {
            "panel": "E",
            "figure_item": "Input-side QSM Power P(t)=a(t)v(t)",
            "role_in_argument": "Power viewpoint transformation",
            "what_to_read": "instantaneous input-side QSM Power shock",
            "key_value": bundle["QSM_peak_abs_W_per_kg"],
            "unit": "W/kg",
            "note": "a(t) and v(t) are multiplied into an upstream Power proxy",
        },
        {
            "panel": "F",
            "figure_item": "QSM Power frequency group",
            "role_in_argument": "Power frequency-group map",
            "what_to_read": "QSM Power peaks kept as a group",
            "key_value": peaks_to_string(bundle["P_peaks"]),
            "unit": "Hz",
            "note": "frequency group is not compressed into a scalar score",
        },
        {
            "panel": "G",
            "figure_item": "QSM Power packet",
            "role_in_argument": "upstream Power packet",
            "what_to_read": "1s ∫|a·v|dt and lag to IsoDisp peak",
            "key_value": f"{bundle['QSM_packet_1s_J_per_kg']:.6g}; lag={bundle['QSM_packet_to_Iso_peak_lag_s']:.6g}",
            "unit": "J/kg; s",
            "note": "positive lag means IsoDisp peak occurs after QSM packet peak",
        },
        {
            "panel": "H",
            "figure_item": "Interface Power / Work exchange",
            "role_in_argument": "measured interface exchange",
            "what_to_read": "1s ∫|F·v_rel|dt and lag to IsoDisp peak",
            "key_value": f"{bundle['Interface_packet_1s_kJ']:.6g}; lag={bundle['Interface_packet_to_Iso_peak_lag_s']:.6g}",
            "unit": "kJ; s",
            "note": "measured exchange layer at the isolation interface",
        },
        {
            "panel": "I",
            "figure_item": "Upper-lower displacement response",
            "role_in_argument": "measured response",
            "what_to_read": "upper-lower isolation displacement peak and peak time",
            "key_value": f"{bundle['IsoDisp_peak_abs_mm']:.6g}; t={bundle['IsoDisp_peak_time_s']:.6g}",
            "unit": "mm; s",
            "note": "response variable used in summary figures",
        },
        {
            "panel": "J",
            "figure_item": "QSM / Interface / IsoDisp frequency-group closure",
            "role_in_argument": "frequency-domain closure map",
            "what_to_read": "Compare QSM Power, interface Power, and measured IsoDisp response peaks with effective isolation-frequency group lines",
            "key_value": (
                "QSM=" + peaks_to_string(bundle["P_peaks"]) +
                " | Interface=" + peaks_to_string(bundle["interface_power_peaks"]) +
                " | IsoDisp=" + peaks_to_string(bundle["iso_resp_peaks"])
            ),
            "unit": "Hz",
            "note": "relation map: x=frequency, y=relative amplitude; no scalar compression",
        },
    ]
    return pd.DataFrame(rows)


def audit_row(section, key, value, unit="", panel="", description="", source=""):
    """One long-form raw audit row.

    The record raw CSV is intentionally long-form in V25 so a person or an AI
    can trace each figure panel back to its value without decoding 100+ wide
    columns.
    """
    return {
        "section": section,
        "panel": panel,
        "key": key,
        "value": value,
        "unit": unit,
        "description": description,
        "source": source,
    }


def best_av_candidate_for_qsm(qsm_peak, acc_peaks, vel_peaks):
    """Find the nearest A/V sum or difference-frequency candidate for one QSM peak.

    This audit is diagnostic only.  It does not claim that every QSM peak must
    be explained by a single A/V pair, because P(t)=a(t)v(t) can also contain
    packet-envelope and interface-modulated components.
    """
    fq = qsm_peak.get("freq_Hz", np.nan)
    best = None
    for ia, ap in enumerate(acc_peaks, start=1):
        fa = ap.get("freq_Hz", np.nan)
        if not np.isfinite(fa):
            continue
        for iv, vp in enumerate(vel_peaks, start=1):
            fv = vp.get("freq_Hz", np.nan)
            if not np.isfinite(fv):
                continue
            candidates = [
                ("sum", fa + fv),
                ("diff", abs(fa - fv)),
            ]
            for ctype, fc in candidates:
                if not np.isfinite(fc) or fc <= 0:
                    continue
                err = abs(fq - fc)
                rel_err = err / max(fq, fc, EPS)
                row = {
                    "candidate_type": ctype,
                    "candidate_freq_Hz": fc,
                    "candidate_error_Hz": err,
                    "candidate_error_ratio": rel_err,
                    "A_rank": ia,
                    "A_freq_Hz": fa,
                    "A_rel_amp": ap.get("rel_amp", np.nan),
                    "V_rank": iv,
                    "V_freq_Hz": fv,
                    "V_rel_amp": vp.get("rel_amp", np.nan),
                }
                if best is None or rel_err < best["candidate_error_ratio"]:
                    best = row
    if best is None:
        return {
            "candidate_type": "none",
            "candidate_freq_Hz": np.nan,
            "candidate_error_Hz": np.nan,
            "candidate_error_ratio": np.nan,
            "A_rank": np.nan,
            "A_freq_Hz": np.nan,
            "A_rel_amp": np.nan,
            "V_rank": np.nan,
            "V_freq_Hz": np.nan,
            "V_rel_amp": np.nan,
            "interpretation": "unmatched; inspect packet envelope or nonlinear/interface modulation",
        }
    rel = best["candidate_error_ratio"]
    if rel <= 0.08:
        interpretation = f"matched by A/V {best['candidate_type']}-frequency candidate"
    elif rel <= 0.18:
        interpretation = "near A/V candidate; inspect packet/envelope modulation"
    else:
        interpretation = "unmatched; inspect packet envelope or nonlinear/interface modulation"
    best["interpretation"] = interpretation
    return best


def build_record_raw_audit_table(bundle: dict, summary_raw: dict) -> pd.DataFrame:
    """Build a long-form, self-checkable record raw audit table.

    This table is meant to be paired with the 10-panel diagnosis figure.  Every
    important number shown in the figure/post table appears here with section,
    panel, unit, and a short description.
    """
    rows = []
    add = rows.append

    # Metadata and extraction settings.
    for key in ["group", "record_id", "filename"]:
        add(audit_row("metadata", key, summary_raw.get(key, ""), "", "", "record identity", "process_record"))
    add(audit_row("metadata", "fs_Hz", summary_raw.get("fs_Hz"), "Hz", "", "estimated sampling frequency", "estimate_fs"))
    add(audit_row("metadata", "Acceleration_col", summary_raw.get("Acceleration_col"), "", "A", "source acceleration column", "infer_acc_column"))
    add(audit_row("window", "qsm_local_window_start_s", bundle["local_t0_s"], "s", "A/C/E", "local frequency extraction window start", "local_window_mask"))
    add(audit_row("window", "qsm_local_window_end_s", bundle["local_t1_s"], "s", "A/C/E", "local frequency extraction window end", "local_window_mask"))
    add(audit_row("window", "packet_window_sec", PACKET_WINDOW_SEC, "s", "G/H", "moving packet integration window", "moving_abs_integral"))
    add(audit_row("window", "fft_peak_band_low_Hz", FFT_PEAK_BAND[0], "Hz", "B/D/F/J", "frequency group extraction lower bound", "fft_peak_group"))
    add(audit_row("window", "fft_peak_band_high_Hz", FFT_PEAK_BAND[1], "Hz", "B/D/F/J", "frequency group extraction upper bound", "fft_peak_group"))
    add(audit_row("window", "fft_top_n", FFT_TOP_N, "count", "B/D/F/J", "maximum peaks kept in each frequency group", "fft_peak_group"))

    # Effective frequency reference lines.
    add(audit_row("effective_frequency", "Teff_s", summary_raw.get("Teff_s"), "s", "B/D/F/J", "effective isolation period", "constant TEFF_SEC"))
    add(audit_row("effective_frequency", "f_eff_Hz", summary_raw.get("f_eff_Hz"), "Hz", "B/D/F/J", "effective isolation frequency = 1/Teff", "constant TEFF_SEC"))
    f_eff = bundle.get("f_eff_Hz", np.nan)
    for m in TEFF_FREQ_GROUP_MULTIPLIERS:
        label = "0.5f_eff" if abs(m - 0.5) < 1e-12 else f"{int(m)}f_eff"
        add(audit_row("effective_frequency", label, m * f_eff if np.isfinite(f_eff) else np.nan, "Hz", "B/D/F/J", f"vertical reference line {label}", "draw_effective_frequency_lines"))

    # Figure panel values.
    panel_items = [
        ("A", "signal_peak", "Acceleration_peak_abs_g", summary_raw.get("Acceleration_peak_abs_g"), "g", "absolute input acceleration peak"),
        ("C", "signal_peak", "Velocity_peak_abs_mps", summary_raw.get("Velocity_peak_abs_mps"), "m/s", "absolute input velocity peak"),
        ("E", "power_peak", "QSM_PowerFlow_peak_abs_W_per_kg", summary_raw.get("QSM_PowerFlow_peak_abs_W_per_kg"), "W/kg", "absolute input-side QSM Power peak"),
        ("G", "packet", "QSM_PowerFlow_abs_packet_1s_peak_J_per_kg", summary_raw.get("QSM_PowerFlow_abs_packet_1s_peak_J_per_kg"), "J/kg", "peak 1s input-side QSM Power packet"),
        ("G", "timing", "QSM_PowerFlow_abs_packet_1s_peak_time_s", summary_raw.get("QSM_PowerFlow_abs_packet_1s_peak_time_s"), "s", "QSM packet peak time"),
        ("G", "timing", "QSM_PowerFlow_packet_to_Iso_peak_lag_s", summary_raw.get("QSM_PowerFlow_packet_to_Iso_peak_lag_s"), "s", "IsoDisp peak time minus QSM packet peak time"),
        ("H", "interface", "Interface_power_peak_abs_kW", summary_raw.get("Interface_power_peak_abs_kW"), "kW", "absolute interface Power peak"),
        ("H", "interface", "Interface_power_packet_1s_peak_kJ", summary_raw.get("Interface_power_packet_1s_peak_kJ"), "kJ", "peak 1s measured interface Power/Work packet"),
        ("H", "timing", "Interface_power_packet_1s_peak_time_s", summary_raw.get("Interface_power_packet_1s_peak_time_s"), "s", "interface packet peak time"),
        ("H", "timing", "Interface_packet_to_Iso_peak_lag_s", summary_raw.get("Interface_packet_to_Iso_peak_lag_s"), "s", "IsoDisp peak time minus interface packet peak time"),
        ("H", "interface", "Interface_abs_work_kJ", summary_raw.get("Interface_abs_work_kJ"), "kJ", "accumulated absolute interface Work"),
        ("I", "response", "IsoDisp_peak_abs_mm", summary_raw.get("IsoDisp_peak_abs_mm"), "mm", "measured upper-lower displacement peak"),
        ("I", "response", "IsoDisp_peak_time_s", summary_raw.get("IsoDisp_peak_time_s"), "s", "time of measured upper-lower displacement peak"),
        ("A/C", "input_displacement", "Measured_input_disp_peak_abs_mm", summary_raw.get("Measured_input_disp_peak_abs_mm"), "mm", "measured input displacement peak from shaking table file if available"),
        ("C", "input_displacement", "CalcDisp_from_velocity_peak_abs_mm", summary_raw.get("CalcDisp_from_velocity_peak_abs_mm"), "mm", "velocity-integrated input displacement peak"),
    ]
    for panel, section, key, value, unit, desc in panel_items:
        add(audit_row(section, key, value, unit, panel, desc, "process_record"))

    # Frequency group summaries and individual peaks.
    peak_sets = [
        ("B", "Acceleration", bundle["acc_peaks"], "local acceleration frequency group"),
        ("D", "Velocity", bundle["vel_peaks"], "local velocity frequency group"),
        ("F", "QSM_Power", bundle["P_peaks"], "local input-side QSM Power frequency group"),
        ("J", "Interface_Power", bundle["interface_power_peaks"], "local interface Power frequency group"),
        ("J", "IsoDisp_Response", bundle["iso_resp_peaks"], "local measured upper-lower displacement response frequency group"),
    ]
    for panel, prefix, peaks, desc in peak_sets:
        add(audit_row("frequency_group", f"{prefix}_frequency_group_Hz", peaks_to_string(peaks), "Hz", panel, desc, "fft_peak_group"))
        for i, p in enumerate(peaks, start=1):
            add(audit_row("frequency_peak", f"{prefix}_peak{i}_freq_Hz", p.get("freq_Hz", np.nan), "Hz", panel, f"{desc}: peak {i} frequency", "fft_peak_group"))
            add(audit_row("frequency_peak", f"{prefix}_peak{i}_period_s", p.get("period_s", np.nan), "s", panel, f"{desc}: peak {i} period", "fft_peak_group"))
            add(audit_row("frequency_peak", f"{prefix}_peak{i}_rel_amp", p.get("rel_amp", np.nan), "0-1", panel, f"{desc}: peak {i} relative amplitude", "fft_peak_group"))

    # Contact text with effective isolation-frequency groups.
    add(audit_row("frequency_contact", "QSM_near_effective_isolation_frequency_groups", summary_raw.get("QSM_near_effective_isolation_frequency_groups", ""), "", "F", "QSM Power peaks near 0.5/1/2/3/4 f_eff", "teff_contact_candidates"))
    add(audit_row("frequency_contact", "Interface_Power_near_effective_isolation_frequency_groups", summary_raw.get("Interface_Power_near_effective_isolation_frequency_groups", ""), "", "J", "Interface Power peaks near 0.5/1/2/3/4 f_eff", "teff_contact_candidates"))
    add(audit_row("frequency_contact", "IsoDisp_response_near_effective_isolation_frequency_groups", summary_raw.get("IsoDisp_response_near_effective_isolation_frequency_groups", ""), "", "J", "measured IsoDisp response peaks near 0.5/1/2/3/4 f_eff", "teff_contact_candidates"))

    # Diagnostic A/V -> QSM candidate audit.
    for iq, qp in enumerate(bundle["P_peaks"], start=1):
        best = best_av_candidate_for_qsm(qp, bundle["acc_peaks"], bundle["vel_peaks"])
        prefix = f"QSM_peak{iq}"
        add(audit_row("av_to_qsm_frequency_audit", f"{prefix}_freq_Hz", qp.get("freq_Hz", np.nan), "Hz", "F", "QSM Power peak being audited", "fft_peak_group"))
        add(audit_row("av_to_qsm_frequency_audit", f"{prefix}_rel_amp", qp.get("rel_amp", np.nan), "0-1", "F", "QSM Power peak relative amplitude", "fft_peak_group"))
        for key, unit, desc in [
            ("candidate_type", "", "nearest A/V candidate type: sum or diff"),
            ("candidate_freq_Hz", "Hz", "nearest A/V candidate frequency"),
            ("candidate_error_Hz", "Hz", "absolute frequency error"),
            ("candidate_error_ratio", "ratio", "relative frequency error"),
            ("A_rank", "rank", "acceleration peak rank used by candidate"),
            ("A_freq_Hz", "Hz", "acceleration peak frequency used by candidate"),
            ("A_rel_amp", "0-1", "acceleration peak relative amplitude"),
            ("V_rank", "rank", "velocity peak rank used by candidate"),
            ("V_freq_Hz", "Hz", "velocity peak frequency used by candidate"),
            ("V_rel_amp", "0-1", "velocity peak relative amplitude"),
            ("interpretation", "", "audit interpretation; diagnostic only"),
        ]:
            add(audit_row("av_to_qsm_frequency_audit", f"{prefix}_{key}", best.get(key, np.nan), unit, "F", desc, "best_av_candidate_for_qsm"))

    return pd.DataFrame(rows)


def process_record(group: str, filename: str, out_group: Path):
    """Compute one record and export its one 10-panel figure plus two CSVs."""
    record_id = filename.replace(".txt", "")
    mocap, sensor, shake = read_group_record(group, filename)

    # Time and acceleration.
    shake_tcol = find_time_col(shake)
    t = numeric_series(shake, shake_tcol)
    t = t - np.nanmin(t)
    fs = estimate_fs(t)
    if not np.isfinite(fs):
        raise ValueError(f"Cannot estimate fs for {record_id}")

    acc_df, acc_col = infer_acc_column(shake, sensor)
    acc_t = numeric_series(acc_df, find_time_col(acc_df))
    acc_t = acc_t - np.nanmin(acc_t)
    acc_raw = numeric_series(acc_df, acc_col)
    acc = interp_to_time(acc_t, acc_raw, t)
    if np.nanmax(np.abs(acc)) < 5:
        acc_g = acc
        acc_mps2 = acc * G
    else:
        acc_mps2 = acc
        acc_g = acc / G
    acc_mps2_hp = bandpass_or_lowpass(acc_mps2, fs, low=0.03)

    # Velocity and QSM Power.
    vel = cumulative_trapezoid(acc_mps2_hp, t, initial=0.0)
    vel = bandpass_or_lowpass(vel, fs, low=0.03, high=20.0)
    P_signed = acc_mps2_hp * vel
    P_env = envelope_signal(P_signed)
    P_abs = np.abs(P_signed)
    P_packet_1s = moving_abs_integral(P_signed, t, PACKET_WINDOW_SEC)
    P_abs_integral = cumulative_trapezoid(P_abs, t, initial=0.0)
    P_packet_peak_time, _ = get_peak_time_and_value(t, P_packet_1s, abs_peak=True)

    # Input displacement, kept for raw audit.
    shake_disp_col = infer_shake_disp_column(shake)
    if shake_disp_col is not None:
        shake_disp_mm = sanitize_units_mm(numeric_series(shake, shake_disp_col))
    else:
        shake_disp_mm = cumulative_trapezoid(vel, t, initial=0.0) * 1000.0
    shake_disp_mm = shake_disp_mm - np.nanmedian(shake_disp_mm[: max(5, int(fs))])
    calc_disp_from_v_mm = cumulative_trapezoid(vel, t, initial=0.0) * 1000.0
    calc_disp_from_v_mm = calc_disp_from_v_mm - np.nanmedian(calc_disp_from_v_mm[: max(5, int(fs))])

    # Mocap response.
    tm = numeric_series(mocap, find_time_col(mocap))
    tm = tm - np.nanmin(tm)
    mcols = infer_mocap_columns(mocap)
    if mcols["direct_iso"] is not None:
        iso_raw = numeric_series(mocap, mcols["direct_iso"])
    elif mcols["lavg"] is not None and mcols["gavg"] is not None:
        iso_raw = numeric_series(mocap, mcols["lavg"]) - numeric_series(mocap, mcols["gavg"])
    else:
        iso_raw = None
        tcol = find_time_col(mocap)
        for c in mocap.columns:
            if c != tcol and pd.to_numeric(mocap[c], errors="coerce").notna().sum() > 10:
                iso_raw = numeric_series(mocap, c)
                break
        if iso_raw is None:
            raise KeyError(f"Cannot infer isolation displacement for {record_id}")

    iso_mm = sanitize_units_mm(interp_to_time(tm, iso_raw, t))
    iso_mm = iso_mm - np.nanmedian(iso_mm[: max(5, int(fs))])

    if mcols["direct_upper"] is not None:
        upper_raw = numeric_series(mocap, mcols["direct_upper"])
    elif mcols["f1avg"] is not None and mcols["gavg"] is not None:
        upper_raw = numeric_series(mocap, mcols["f1avg"]) - numeric_series(mocap, mcols["gavg"])
    else:
        upper_raw = iso_raw
    upper_mm = sanitize_units_mm(interp_to_time(tm, upper_raw, t))
    upper_mm = upper_mm - np.nanmedian(upper_mm[: max(5, int(fs))])

    if mcols["direct_frame"] is not None:
        frame_raw = numeric_series(mocap, mcols["direct_frame"])
    elif mcols["f1avg"] is not None and mcols["lavg"] is not None:
        frame_raw = numeric_series(mocap, mcols["f1avg"]) - numeric_series(mocap, mcols["lavg"])
    else:
        frame_raw = upper_raw - iso_raw if isinstance(upper_raw, np.ndarray) else iso_raw * 0
    frame_mm = sanitize_units_mm(interp_to_time(tm, frame_raw, t))
    frame_mm = frame_mm - np.nanmedian(frame_mm[: max(5, int(fs))])

    iso_peak_time, iso_peak_val = get_peak_time_and_value(t, iso_mm, abs_peak=True)
    iso_peak_abs_mm = abs(iso_peak_val)

    # Interface Power / Work exchange.
    ts = numeric_series(sensor, find_time_col(sensor))
    ts = ts - np.nanmin(ts)
    lc_cols = infer_load_cell_total_x(sensor)
    if lc_cols:
        lc_total = np.zeros_like(ts, dtype=float)
        for c in lc_cols:
            lc_total += numeric_series(sensor, c)
        lc_total_interp = interp_to_time(ts, lc_total, t)
    else:
        lc_total_interp = np.zeros_like(t)
    force_dynamic_kN = lc_total_interp - np.nanmedian(lc_total_interp[-max(10, int(fs)):])
    force_N = force_dynamic_kN * 1000.0
    v_iso = np.gradient(iso_mm / 1000.0, t)
    interface_power_kW = (force_N * v_iso) / 1000.0
    interface_packet_1s = moving_abs_integral(interface_power_kW, t, PACKET_WINDOW_SEC)
    interface_abs_work_kJ = np.trapezoid(np.abs(interface_power_kW), t)
    interface_packet_peak_time, _ = get_peak_time_and_value(t, interface_packet_1s, abs_peak=True)

    # Frequency groups around the QSM Power packet.
    local_mask = local_window_mask(t, P_packet_peak_time, LOCAL_WINDOW_SEC)
    local_t0 = float(np.nanmin(t[local_mask]))
    local_t1 = float(np.nanmax(t[local_mask]))
    acc_peaks = fft_peak_group(acc_mps2_hp, t, fs, P_packet_peak_time)
    vel_peaks = fft_peak_group(vel, t, fs, P_packet_peak_time)
    P_peaks = fft_peak_group(P_signed, t, fs, P_packet_peak_time)
    interface_power_peaks = fft_peak_group(interface_power_kW, t, fs, interface_packet_peak_time)
    iso_resp_peaks = fft_peak_group(iso_mm, t, fs, iso_peak_time)
    f_eff = 1.0 / TEFF_SEC if TEFF_SEC > 0 else np.nan

    bundle = {
        "group": group,
        "record_id": record_id,
        "t": t,
        "fs_Hz": fs,
        "f_eff_Hz": f_eff,
        "Teff_s": TEFF_SEC,
        "acc_g": acc_g,
        "vel": vel,
        "P_signed": P_signed,
        "P_env": P_env,
        "P_packet_1s": P_packet_1s,
        "P_abs_integral": P_abs_integral,
        "interface_power_kW": interface_power_kW,
        "interface_packet_1s": interface_packet_1s,
        "interface_abs_work_kJ": interface_abs_work_kJ,
        "iso_mm": iso_mm,
        "upper_mm": upper_mm,
        "frame_mm": frame_mm,
        "acc_peaks": acc_peaks,
        "vel_peaks": vel_peaks,
        "P_peaks": P_peaks,
        "interface_power_peaks": interface_power_peaks,
        "iso_resp_peaks": iso_resp_peaks,
        "local_t0_s": local_t0,
        "local_t1_s": local_t1,
        "QSM_packet_peak_time_s": P_packet_peak_time,
        "IsoDisp_peak_time_s": iso_peak_time,
        "Interface_packet_peak_time_s": interface_packet_peak_time,
        "Acceleration_peak_abs_g": np.nanmax(np.abs(acc_g)),
        "Velocity_peak_abs_mps": np.nanmax(np.abs(vel)),
        "QSM_peak_abs_W_per_kg": np.nanmax(P_abs),
        "QSM_packet_1s_J_per_kg": np.nanmax(P_packet_1s),
        "QSM_packet_to_Iso_peak_lag_s": iso_peak_time - P_packet_peak_time,
        "Interface_power_peak_abs_kW": np.nanmax(np.abs(interface_power_kW)),
        "Interface_packet_1s_kJ": np.nanmax(interface_packet_1s),
        "Interface_packet_to_Iso_peak_lag_s": iso_peak_time - interface_packet_peak_time,
        "IsoDisp_peak_abs_mm": iso_peak_abs_mm,
    }

    # Required record outputs: one 10-panel figure + two CSV files.
    out_group.mkdir(parents=True, exist_ok=True)
    make_record_core_diagnosis(bundle, out_group / f"{record_id}_V25_core_diagnosis.png")
    build_record_post_table(bundle).to_csv(out_group / f"{record_id}_V25_post_table.csv", index=False, encoding="utf-8-sig")

    raw = {
        "group": group,
        "record_id": record_id,
        "filename": filename,
        "fs_Hz": fs,
        "Teff_s": TEFF_SEC,
        "f_eff_Hz": f_eff,
        "IsoDisp_peak_abs_mm": iso_peak_abs_mm,
        "IsoDisp_peak_time_s": iso_peak_time,
        "Acceleration_col": acc_col,
        "Acceleration_peak_abs_g": np.nanmax(np.abs(acc_g)),
        "Velocity_peak_abs_mps": np.nanmax(np.abs(vel)),
        "QSM_PowerFlow_peak_abs_W_per_kg": np.nanmax(P_abs),
        "QSM_PowerFlow_abs_packet_1s_peak_J_per_kg": np.nanmax(P_packet_1s),
        "QSM_PowerFlow_abs_integral_J_per_kg": np.nanmax(P_abs_integral),
        "QSM_PowerFlow_abs_packet_1s_peak_time_s": P_packet_peak_time,
        "QSM_PowerFlow_packet_to_Iso_peak_lag_s": iso_peak_time - P_packet_peak_time,
        "Interface_power_peak_abs_kW": np.nanmax(np.abs(interface_power_kW)),
        "Interface_power_packet_1s_peak_kJ": np.nanmax(interface_packet_1s),
        "Interface_power_packet_1s_peak_time_s": interface_packet_peak_time,
        "Interface_packet_to_Iso_peak_lag_s": iso_peak_time - interface_packet_peak_time,
        "Interface_abs_work_kJ": interface_abs_work_kJ,
        "Measured_input_disp_peak_abs_mm": np.nanmax(np.abs(shake_disp_mm)),
        "CalcDisp_from_velocity_peak_abs_mm": np.nanmax(np.abs(calc_disp_from_v_mm)),
        "Acceleration_frequency_group_Hz": peaks_to_string(acc_peaks),
        "Velocity_frequency_group_Hz": peaks_to_string(vel_peaks),
        "QSM_Power_frequency_group_Hz": peaks_to_string(P_peaks),
        "Interface_Power_frequency_group_Hz": peaks_to_string(interface_power_peaks),
        "IsoDisp_response_frequency_group_Hz": peaks_to_string(iso_resp_peaks),
        "QSM_near_effective_isolation_frequency_groups": contact_text(P_peaks, f_eff),
        "Interface_Power_near_effective_isolation_frequency_groups": contact_text(interface_power_peaks, f_eff),
        "IsoDisp_response_near_effective_isolation_frequency_groups": contact_text(iso_resp_peaks, f_eff),
    }
    add_peak_columns(raw, "Acceleration", acc_peaks)
    add_peak_columns(raw, "Velocity", vel_peaks)
    add_peak_columns(raw, "QSM_Power", P_peaks)
    add_peak_columns(raw, "Interface_Power", interface_power_peaks)
    add_peak_columns(raw, "IsoDisp_Response", iso_resp_peaks)

    # V25 record raw output is a long-form audit table. The wide `raw` dict
    # is still returned upward for Group/Root summary plots and raw summary CSVs.
    build_record_raw_audit_table(bundle, raw).to_csv(
        out_group / f"{record_id}_V25_raw.csv", index=False, encoding="utf-8-sig"
    )

    peak_rows = []
    for p in P_peaks:
        peak_rows.append({
            "group": group,
            "record_id": record_id,
            "freq_Hz": p.get("freq_Hz", np.nan),
            "period_s": p.get("period_s", np.nan),
            "rel_amp": p.get("rel_amp", np.nan),
            "IsoDisp_peak_abs_mm": iso_peak_abs_mm,
            "f_eff_Hz": f_eff,
            "Teff_s": TEFF_SEC,
        })
    return raw, peak_rows


# ============================================================
# 6. Summary and Group figures / tables
# ============================================================

def save_group_color_map(out_dir: Path):
    rows = [{"group": g, "color_hex": c, "role": "article" if g in ARTICLE_MAIN_GROUPS else "external"} for g, c in GROUP_COLOR_MAP.items()]
    pd.DataFrame(rows).to_csv(out_dir / "V25_group_color_map.csv", index=False, encoding="utf-8-sig")


def scatter_by_group(ax, df, xcol, title, xlabel, ylabel="Measured upper-lower displacement, IsoDisp [mm]"):
    for g in groups_present_in(df):
        d = df[df["group"].astype(str) == g]
        if len(d) == 0 or xcol not in d.columns:
            continue
        ax.scatter(d[xcol], d["IsoDisp_peak_abs_mm"], label=g, color=group_color(g), alpha=0.75)

    # Add plotting headroom before correlation text and record labels are placed.
    expand_y_axis_for_labels(ax, top_pad_frac=0.20, bottom_pad_frac=0.03)
    expand_x_axis_for_labels(ax, left_pad_frac=0.04, right_pad_frac=0.08)

    r = safe_corr(df[xcol], df["IsoDisp_peak_abs_mm"])
    rho = safe_corr(df[xcol], df["IsoDisp_peak_abs_mm"], method="spearman")
    ax.text(
        0.025,
        0.965,
        f"Pearson r={r:.3f}\nSpearman rho={rho:.3f}",
        transform=ax.transAxes,
        va="top",
        ha="left",
        fontsize=9,
        bbox=dict(facecolor="white", edgecolor="none", alpha=0.72, pad=0.5),
    )
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, alpha=0.25)


def make_fig01(df: pd.DataFrame, out_path: Path, title_prefix="Figure 1", annotate_records=False):
    fig, axes = plt.subplots(2, 3, figsize=(18, 11))
    ax = axes.ravel()
    panels = [
        ("Acceleration_peak_abs_g", "A. input acceleration peak", "Acceleration peak |a| [g]"),
        ("Velocity_peak_abs_mps", "B. input velocity peak", "Velocity peak |v| [m/s]"),
        ("QSM_PowerFlow_peak_abs_W_per_kg", "C. input-side QSM Power peak", "Input-side QSM Power peak |a·v| [W/kg]"),
        ("QSM_PowerFlow_abs_packet_1s_peak_J_per_kg", "D. input-side QSM Power packet", "Input-side QSM 1s Power packet ∫|a·v|dt [J/kg]"),
        ("Interface_power_packet_1s_peak_kJ", "E. measured interface Power/Work packet", "Interface 1s Power/Work packet ∫|F·v_rel|dt [kJ]"),
        ("Interface_abs_work_kJ", "F. measured accumulated interface Work", "Accumulated interface Work [kJ]"),
    ]
    for a, (col, title, xlabel) in zip(ax, panels):
        scatter_by_group(a, df, col, title, xlabel)
        if annotate_records:
            annotate_scatter_records(a, df, col)
    fig.suptitle(f"{title_prefix}. Core evidence for QSM Power viewpoint transformation", fontsize=15, y=0.972)
    present_groups = groups_present_in(df)
    draw_group_color_strip(fig, present_groups, y=0.945, fontsize=10)
    fig.tight_layout(rect=[0, 0, 1, 0.915])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=220, bbox_inches="tight")
    plt.close(fig)


def make_fig02(peak_df: pd.DataFrame, out_path: Path, title_prefix="Figure 2", annotate_rows=False):
    fig, axes = plt.subplots(2, 1, figsize=(14, 13))
    configs = [
        (axes[0], None, "A. full QSM Power frequency-group contact map"),
        (axes[1], (0, 1.5), "B. zoom near effective isolation-frequency groups"),
    ]
    for ax, xlim, subtitle in configs:
        for g in groups_present_in(peak_df):
            d = peak_df[peak_df["group"].astype(str) == g]
            if len(d) == 0:
                continue
            sizes = 28 + 110 * pd.to_numeric(d["rel_amp"], errors="coerce").fillna(0.5).clip(0, 1)
            ax.scatter(d["freq_Hz"], d["IsoDisp_peak_abs_mm"], s=sizes, color=group_color(g), alpha=0.68, label=g)
        ax.set_title(subtitle)
        ax.set_xlabel("QSM Power Flow peak frequency [Hz]")
        ax.set_ylabel("Measured upper-lower displacement, IsoDisp [mm]")
        ax.grid(True, alpha=0.25)
        if xlim:
            ax.set_xlim(*xlim)
        else:
            ax.set_xlim(left=0)
        expand_y_axis_for_labels(ax, top_pad_frac=0.22, bottom_pad_frac=0.03)
        draw_effective_frequency_lines(ax, 1.0 / TEFF_SEC, top_frac=0.965)
        if annotate_rows:
            annotate_row_source_labels(ax, peak_df if xlim is None else peak_df[peak_df["freq_Hz"] <= xlim[1]])
    fig.suptitle(f"{title_prefix}. QSM Power frequency-group contact with effective isolation-frequency groups", fontsize=15, y=0.972)
    present_groups = groups_present_in(peak_df)
    draw_group_color_strip(fig, present_groups, y=0.945, fontsize=10)
    fig.tight_layout(rect=[0, 0, 1, 0.915])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=220, bbox_inches="tight")
    plt.close(fig)


def make_post_table(scope_name: str, df: pd.DataFrame, peak_df: pd.DataFrame, out_path: Path):
    rows = []
    fig1_panels = [
        ("A", "input acceleration peak", "Acceleration_peak_abs_g", "Acceleration alone is the baseline motion view."),
        ("B", "input velocity peak", "Velocity_peak_abs_mps", "Velocity is closer to displacement demand than acceleration."),
        ("C", "input-side QSM Power peak", "QSM_PowerFlow_peak_abs_W_per_kg", "Instantaneous QSM Power shows upstream Power shock."),
        ("D", "input-side QSM Power packet", "QSM_PowerFlow_abs_packet_1s_peak_J_per_kg", "The 1s packet reads short-window incoming QSM Power."),
        ("E", "measured interface Power/Work packet", "Interface_power_packet_1s_peak_kJ", "The interface packet is the measured exchange layer."),
        ("F", "measured accumulated interface Work", "Interface_abs_work_kJ", "Accumulated Work is the response-side exchange context."),
    ]
    for panel, item, col, note in fig1_panels:
        rows.append({
            "scope": scope_name,
            "figure": "Fig01",
            "panel": panel,
            "figure_item": item,
            "x_column": col,
            "y_column": "IsoDisp_peak_abs_mm",
            "pearson_r": safe_corr(df[col], df["IsoDisp_peak_abs_mm"]),
            "spearman_rho": safe_corr(df[col], df["IsoDisp_peak_abs_mm"], method="spearman"),
            "reading_note": note,
        })
    rows.append({
        "scope": scope_name,
        "figure": "Fig02",
        "panel": "A/B",
        "figure_item": "QSM Power frequency-group contact map",
        "x_column": "QSM Power peak frequency [Hz]",
        "y_column": "IsoDisp_peak_abs_mm",
        "pearson_r": np.nan,
        "spearman_rho": np.nan,
        "reading_note": "Frequency-group contact is a relation map. It is not reduced to a score.",
    })
    pd.DataFrame(rows).to_csv(out_path, index=False, encoding="utf-8-sig")


def export_scope(scope_name: str, df: pd.DataFrame, peak_df: pd.DataFrame, out_dir: Path, root=False):
    out_dir.mkdir(parents=True, exist_ok=True)
    save_group_color_map(out_dir)
    if root:
        fig1 = "Fig01_core_power_viewpoint_transformation.png"
        fig2 = "Fig02_qsm_power_frequency_group_contact_combined.png"
        post = "ALL_GROUPS_V25_post_table.csv"
        raw = "ALL_GROUPS_V25_raw.csv"
        title1 = "Figure 1"
        title2 = "Figure 2"
    else:
        fig1 = f"{scope_name}_Fig01_core_power_viewpoint_transformation.png"
        fig2 = f"{scope_name}_Fig02_qsm_power_frequency_group_contact_combined.png"
        post = f"{scope_name}_V25_post_table.csv"
        raw = f"{scope_name}_V25_raw.csv"
        title1 = f"{scope_name} Figure 1"
        title2 = f"{scope_name} Figure 2"
    make_fig01(df, out_dir / fig1, title_prefix=title1, annotate_records=(not root))
    make_fig02(peak_df, out_dir / fig2, title_prefix=title2, annotate_rows=(not root))
    make_post_table(scope_name, df, peak_df, out_dir / post)
    df.to_csv(out_dir / raw, index=False, encoding="utf-8-sig")


# ============================================================
# 7. Batch runner
# ============================================================

def process_group(group: str):
    out_group = OUT_ROOT / group
    out_group.mkdir(parents=True, exist_ok=True)
    rows, peaks, failures = [], [], []
    for filename in list_group_files(group):
        try:
            rec, peak_rows = process_record(group, filename, out_group)
            rows.append(rec)
            peaks.extend(peak_rows)
            print(f"[OK] {group} / {filename}")
        except Exception as e:
            failures.append({"group": group, "filename": filename, "error": repr(e)})
            print(f"[FAIL] {group} / {filename}: {e}")
    gdf = pd.DataFrame(rows)
    gpeak = pd.DataFrame(peaks)
    if len(gdf):
        export_scope(group, gdf, gpeak, out_group, root=False)
    if failures:
        pd.DataFrame(failures).to_csv(out_group / f"{group}_V25_failures.csv", index=False, encoding="utf-8-sig")
    return gdf, gpeak, failures


def main():
    all_rows, all_peaks, all_failures = [], [], []
    save_group_color_map(OUT_ROOT)
    for group in GROUPS:
        gdf, gpeak, failures = process_group(group)
        if len(gdf):
            all_rows.append(gdf)
        if len(gpeak):
            all_peaks.append(gpeak)
        all_failures.extend(failures)

    all_df = pd.concat(all_rows, ignore_index=True) if all_rows else pd.DataFrame()
    peak_df = pd.concat(all_peaks, ignore_index=True) if all_peaks else pd.DataFrame()
    if len(all_failures):
        pd.DataFrame(all_failures).to_csv(OUT_ROOT / "ALL_GROUPS_V25_failures.csv", index=False, encoding="utf-8-sig")
    if len(all_df) == 0:
        print("No records processed.")
        return

    article_df = all_df[all_df["group"].isin(ARTICLE_MAIN_GROUPS)].copy()
    article_peak_df = peak_df[peak_df["group"].isin(ARTICLE_MAIN_GROUPS)].copy()
    export_scope("ALL_GROUPS", article_df, article_peak_df, OUT_ROOT, root=True)

    # Sanity checks for output contract.
    required = [
        OUT_ROOT / "Fig01_core_power_viewpoint_transformation.png",
        OUT_ROOT / "Fig02_qsm_power_frequency_group_contact_combined.png",
        OUT_ROOT / "ALL_GROUPS_V25_post_table.csv",
        OUT_ROOT / "ALL_GROUPS_V25_raw.csv",
        OUT_ROOT / "V25_group_color_map.csv",
    ]
    missing = [str(p) for p in required if not p.exists()]
    if missing:
        raise RuntimeError("Missing required V25 outputs:\n" + "\n".join(missing))

    print("\n=== V25 CLEAN DONE ===")
    print(f"Output root: {OUT_ROOT}")
    print("Output contract: root 2 figures + 2 CSVs, each Group 2 figures + 2 CSVs, each record 1 ten-panel figure + 2 CSVs.")


if __name__ == "__main__":
    main()
