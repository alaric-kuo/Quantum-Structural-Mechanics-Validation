# Optional Path Override Patch for `src/QSM_Validation.py`

This patch keeps the author's actual working paths while allowing other users to run the script without editing the author's paths directly.

## Replace the current `RAW_ROOT` and `OUT_ROOT` block with:

```python
import os

RAW_ROOT = Path(os.environ.get(
    "QSM_RAW_ROOT",
    r"D:\OneDrive\文件\Quantum Structural Mechanics\Validation"
    r"\data_shakeTableTest_SlidingBearing_PulseLikeGMs"
    r"\data_earthquakeSpectra\raw data"
))

OUT_ROOT = Path(os.environ.get(
    "QSM_OUT_ROOT",
    r"D:\OneDrive\文件\Quantum Structural Mechanics\Validation"
    r"\QSM_Validation_V25_AllGroups"
))
```

## Windows PowerShell Example

```powershell
$env:QSM_RAW_ROOT="C:\Users\your_name\Documents\QSM_Validation\data_shakeTableTest_SlidingBearing_PulseLikeGMs\data_earthquakeSpectra\raw data"
$env:QSM_OUT_ROOT="C:\Users\your_name\Documents\QSM_Validation\QSM_Validation_V25_AllGroups"
python src/QSM_Validation.py
```

## macOS / Linux Example

```bash
export QSM_RAW_ROOT="/Users/your_name/Documents/QSM_Validation/data_shakeTableTest_SlidingBearing_PulseLikeGMs/data_earthquakeSpectra/raw data"
export QSM_OUT_ROOT="/Users/your_name/Documents/QSM_Validation/QSM_Validation_V25_AllGroups"
python src/QSM_Validation.py
```
