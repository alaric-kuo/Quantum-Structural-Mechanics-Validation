# Validating Quantum Structural Mechanics with Spherical Sliding Isolation Test Data

**Author: Han-Jung Kuo**  
**Date: 2026.05.10**

## Abstract

This article uses the public experimental data from *An Experimental Study of a Spherical Sliding Isolation System Subjected to Pulse-Like Ground Motions* to re-read the mechanism by which seismic waves produce isolation displacement through the viewpoint of Quantum Structural Mechanics (QSM). The original study has already made an important point: for isolation systems, acceleration alone, or the average spectral acceleration, is not sufficient to explain the measured isolation displacement. Velocity pulse, pulse period, and the effective period of the isolation system must be considered together.

This article follows that empirical conclusion and moves one step further. The first layer of checking shows that the correlation between Input Acceleration Peak and Isolation Displacement Peak is weak. The second layer shows that the relationship between Input Velocity Peak and Isolation Displacement becomes much clearer. The article then combines acceleration and velocity into Input-Side QSM Power Flow, written as $P_{\mathrm{in}}(t)=a(t)v(t)$ , and further observes the 1s Power Packet, Interface Power / Work Exchange, Accumulated Interface Work, and the contact relationship between the QSM Power Frequency Group and the Effective Isolation Frequency Group.

The results show that the quantity closest to the isolation displacement response is not a single input acceleration peak or a single input velocity peak. The clearer relationship appears after the input power-potential enters the isolation interface and forms Interface Power / Work Exchange. The summary figure across Case Groups Group1–4 shows that the Measured Interface Power/Work Packet has the clearest relationship with the Measured Upper-Lower Isolation Displacement Peak. The frequency-group maps also show that the isolation response should not be reduced to one effective frequency or one effective period. $f_{\mathrm{eff}}$ is an entry scale, but behind it there is still a conversion relationship among the QSM Power Frequency Group, Interface Frequency Group, and Displacement Response Frequency Group. In the Frequency-Group Closure comparison of individual Diagnosis Figures, high-displacement cases often show displacement response frequencies close to $f_{\mathrm{eff}}$ and its orderly harmonic sequence. This indicates that the effective frequency is not a single control value, but a family of entry frequencies that can be contacted, converted, and manifested by the incoming power-potential.

The core conclusion is that, for an isolation system, a seismic wave can be viewed as a power-potential field entering the structure. When this field cannot be converted smoothly by the isolation system into a stable channel, it forms work exchange at the interface and manifests as observable isolation displacement. This is the QSM interpretation of the original experimental data, and it is also the first attempt to build mechanism-based validation for Quantum Structural Mechanics using real experimental data.

---

## Terminology

**Quantum Structural Mechanics (QSM)**  
The structural-analysis viewpoint used in this article. It treats a seismic wave as a wavefunction-like input and treats a structure as a system in which power-potential enters, transmits, exchanges, dissipates, and manifests, rather than only as a stiffness system that receives external force and produces displacement.

**Isolation Displacement (IsoDisp)**  
The relative displacement between the upper structure and the lower base. It is the displacement response actually received and manifested by the isolation layer. This article mainly compares the Measured Upper-Lower Isolation Displacement Peak.

**Input Acceleration Peak**  
The peak value in the input acceleration time history. It is one of the common input-intensity descriptions in earthquake engineering. The analysis in this article shows that this value alone is not sufficient to explain isolation displacement.

**Input Velocity Peak**  
The peak value in the input velocity time history. For an isolation system, velocity peak is closer to displacement demand than acceleration peak because isolation displacement depends on whether the seismic wave can continuously push the isolation layer into sliding.

**QSM Power Flow**  
This article uses $P_{\mathrm{in}}(t)=a(t)v(t)$ as a proxy for input-side power-potential flow per unit mass. It is not the conventional total power. It combines the motion-changing capability represented by acceleration and the pushing / transmission direction represented by velocity into a power-flow indicator.

**Input-Side QSM Power Flow**  
The QSM Power Flow formed by the input-side $a(t)$ and $v(t)$ of the seismic record. It describes the power-flow state that has already formed at the input side before the seismic wave enters the isolation system.

**Input-Side QSM Power Peak**  
The peak value in the Input-Side QSM Power Flow time history. It is used to observe whether the seismic input forms a clear instantaneous power-potential impact.

**Power Packet**  
A concentrated QSM Power Flow within a short time window. This article uses a one-second window to observe whether the power-potential concentrates into an event capable of pushing the isolation layer. In later sections, 1s Power Packet refers to this one-second power-potential packet.

**Interface Power / Work Exchange**  
The quantity $F_{\mathrm{interface}}(t)v_{\mathrm{rel}}(t)$ at the isolation interface and its time integral. It describes the exchange and work done after the input power-potential actually enters the isolation interface. In later sections, Interface Power, Interface Work, and Interface Power/Work Packet all refer to this interface-level power and work response.

**Measured Interface Power/Work Packet**  
The short-time interface power / work exchange obtained from measured interface data. The cross-case-group summary shows that this quantity has the clearest relationship with the Measured Upper-Lower Isolation Displacement Peak.

**Accumulated Interface Work**  
The total accumulated value of Interface Power / Work Exchange over time. It can reflect overall work at the interface. The results in this article show that, in some Case Groups, the short-time interface work packet is closer to displacement peak than accumulated work.

**Effective Isolation Period ( $T_{\mathrm{eff}}$ )**  
The main period scale of the isolation system under an equivalent description. The original study treats it as an important parameter for understanding isolation response. This article further converts it into an effective isolation frequency.

**Effective Isolation Frequency ( $f_{\mathrm{eff}}$ )**  
The frequency scale corresponding to the Effective Isolation Period $T_{\mathrm{eff}}$ . This article uses $f_{\mathrm{eff}}=1/T_{\mathrm{eff}}$ .

**Effective Isolation Frequency Group**  
A frequency family extended from $f_{\mathrm{eff}}$ , including $0.5f_{\mathrm{eff}}$ , $f_{\mathrm{eff}}$ , $2f_{\mathrm{eff}}$ , $3f_{\mathrm{eff}}$ , and $4f_{\mathrm{eff}}$ . This article treats it as an entry-frequency family of the isolation system, not as one unique control frequency.

**QSM Power Frequency Group**  
A set of main frequencies obtained by applying frequency analysis to the Input-Side QSM Power Flow. It is used to observe that the seismic power-potential does not enter the system through one frequency only, but through a set of frequency components that contact the isolation system.

**Interface Frequency Group**  
A set of main frequencies obtained by applying frequency analysis to the Interface Power / Work Exchange. It is used to observe which frequency components are retained, converted, or amplified after the input power-potential enters the isolation interface.

**Displacement Response Frequency Group**  
The main frequency group of the isolation displacement response $u_{\mathrm{iso}}(t)$ . This article pays special attention to whether the displacement response frequencies in high-displacement cases are close to $f_{\mathrm{eff}}$ and its harmonic sequence.

**Case Group**  
The Group1–4 classification used in this article according to the original experimental data. In this article, Group1–4 are called Case Groups. Only Frequency Group refers to a frequency group.

**Frequency-Group Contact Map**  
The frequency-group relation map shown in the summary figure and in each Case Group Figure 2. It is used to observe how the QSM Power Frequency Group contacts the Effective Isolation Frequency Group, rather than compressing the frequency relation into one scalar score.

**Diagnosis Figure**  
The ten-panel diagnostic figure drawn for each individual ground-motion record. It presents acceleration, velocity, QSM Power Flow, Power Packet, Interface Power / Work Exchange, Isolation Displacement, and Frequency-Group Closure. When this article later refers to the J panel, it means the last panel in the Diagnosis Figure, where the QSM Power Frequency Group, Interface Frequency Group, and Displacement Response Frequency Group are compared.

**Frequency-Group Closure**  
The comparison panel in the individual Diagnosis Figure that compares the QSM Power Frequency Group, Interface Frequency Group, and Displacement Response Frequency Group. Its point is not only whether the three frequency groups are close to each other, but whether the displacement response forms an orderly sequence close to $f_{\mathrm{eff}}$ and its harmonics. If such a sequence appears in a high-displacement case, it means the isolation system is not receiving power-potential only from one effective frequency, but is being driven through a family of effective-frequency entries.

**Lag**  
The time difference between two event peaks, such as the lag between the QSM Power Packet peak and the isolation displacement peak. This article uses it to judge whether the power event and the displacement event are close in time.

**QSM Power Shock**  
A sharp instantaneous power-potential peak in the QSM Power Flow time history. It can indicate a strong short-time power-potential impact in the seismic input, but this article does not treat it as the only criterion.

**Input Motion**  
The acceleration, velocity, and power-potential time histories at the seismic input side. The conclusion uses this term to summarize the motion-data layer of the seismic input.

**Frequency-Group Manifestation**  
The phenomenon in which power-potential, after conversion through the input side and the interface, appears as an identifiable sequence in the Displacement Response Frequency Group.

**Figure Label Convention**  
The main text uses English terms because the output figures also use English labels. Terms such as QSM Power Flow, Power Packet, Interface Power / Work Exchange, QSM Power Frequency Group, Interface Frequency Group, and Displacement Response Frequency Group are retained after being defined so that the text, figures, and future journal version can remain consistent.

---

# 1. Research Starting Point: Following the Original Paper Further

The most important contribution of the original study is that it uses experimental data to show a key issue in isolation design: acceleration alone, or average spectral acceleration alone, cannot sufficiently describe isolation displacement demand.

This conclusion matters and should be respected. In conventional structural design and earthquake engineering, acceleration and response spectra have long been the dominant language. They provide design scales and allow different ground motions to be compared within a common engineering coordinate system. However, once the subject becomes a spherical sliding isolation system, the issue becomes more detailed. The core response of an isolation system is relative displacement, and displacement is not a direct result of an instantaneous acceleration peak. If a seismic wave is to push the isolation layer open, velocity pulse, duration, interface friction, and the effective period of the system must act together.

The position of this article is therefore clear: it continues along the path opened by the original paper. The original paper has already shown that acceleration alone is insufficient. This article then asks: if acceleration alone is insufficient, can we find a data-reading path that is closer to the mechanism by which displacement is generated?

This path is divided into five steps:

1. Start with the Input Acceleration Peak to confirm that acceleration has limited explanatory power for isolation displacement.
2. Move to the Input Velocity Peak to confirm that velocity is closer than acceleration to isolation displacement demand.
3. Combine $a(t)$ and $v(t)$ into $P_{\mathrm{in}}(t)=a(t)v(t)$ , converting the seismic input into QSM Power Flow.
4. Observe whether the Power Packet enters the isolation interface and forms $F_{\mathrm{interface}}(t)v_{\mathrm{rel}}(t)$ and interface work.
5. Expand QSM Power Flow into Frequency Groups and observe their contact, conversion, and displacement manifestation with the Effective Isolation Frequency family.

Together, these five steps form the QSM power-potential viewpoint transformation used in this article.

---

# 2. Figure and Data-Reading Framework: From Overall Relations to Individual Mechanisms

The graphical analysis in this article has three layers. The first layer is the overall relation across Case Groups Group1–4, used to observe the overall trends among acceleration, velocity, QSM Power Flow, interface work, and isolation displacement. The second layer is the group-level relation within each Case Group, used to preserve the differences among short-period pulse, medium-period pulse, non-pulse, and spectrally matched records. The third layer is the Diagnosis Figure for each individual record, used to check whether the time waveform, Power Packet, Frequency Group, interface work, and displacement peak can form a traceable mechanism chain.

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Fig01_core_power_viewpoint_transformation.png)

The cross-case-group Figure 1 answers the first question: if the Measured Upper-Lower Isolation Displacement Peak is treated as the response quantity, how much explanatory power is provided by the Input Acceleration Peak, Input Velocity Peak, Input-Side QSM Power Peak, Input-Side 1s QSM Power Packet, Measured Interface Power/Work Packet, and Accumulated Interface Work? The purpose of this figure is not to compress every phenomenon into one score. It shows how the focus of explanation moves from acceleration / velocity indicators toward power / work indicators.

The reading sequence is:

```text
Input Acceleration Peak
→ Input Velocity Peak
→ Input-Side QSM Power Peak
→ Input-Side 1s QSM Power Packet
→ Measured Interface Power/Work Packet
→ Accumulated Interface Work
→ Isolation Displacement
```

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Fig02_qsm_power_frequency_group_contact_combined.png)

The cross-case-group Figure 2 answers the second question: after the input earthquake is converted into QSM Power Flow, how does it unfold in the frequency domain? This figure should be read as a Frequency-Group Contact Map. Each ground-motion record has a set of QSM Power frequency peaks. The same record appears on the figure as multiple points at approximately the same displacement level. The relative relationship between these points and $0.5f_{\mathrm{eff}}$ , $f_{\mathrm{eff}}$ , $2f_{\mathrm{eff}}$ , $3f_{\mathrm{eff}}$ , and $4f_{\mathrm{eff}}$ provides clues about how the power-potential contacts the entry-frequency family of the isolation system. More importantly, the J panel in each individual Diagnosis Figure further shows that the Displacement Response Frequency in many high-displacement cases is not randomly scattered, but is close to the system effective frequency and its harmonic sequence. This allows $f_{\mathrm{eff}}$ to be re-understood as a reference scale for a family of power-potential entries, rather than as a single design parameter.

The analysis of each Case Group preserves group differences instead of mixing all records into one behavior. Short-period pulse, medium-period pulse, non-pulse, and spectrally matched records can all be read through the same QSM framework, but their modes of power-potential entry, interface conversion, and displacement manifestation are not the same. Therefore, in each group-level analysis, this article reads two types of figures together: one is the group-level correlation figure, used to observe the relation among acceleration, velocity, power-potential, work, and displacement; the other is the group-level Frequency-Group Contact Map, used to observe how the power-potential frequencies of that group contact the Effective Isolation Frequency family. The individual Diagnosis Figure then returns to the time series itself and checks whether the event actually exists in the waveform. In that Diagnosis Figure, the J panel is the key panel for reading frequency manifestation: circles represent the QSM Power Frequency Group, squares represent the Interface Frequency Group, and triangles represent the Displacement Response Frequency Group. When the displacement frequencies in high-displacement cases show an orderly sequence close to $f_{\mathrm{eff}}$ , $2f_{\mathrm{eff}}$ , $3f_{\mathrm{eff}}$ , or their lower-order components, the displacement is not a random oscillation; it is a manifestation of the isolation system’s effective-frequency family being driven by the power-potential field.

---

# 3. Overall Evidence across Case Groups Group1–4: From Input Indicators to Interface Work

The cross-case-group Figure 1 gives a direct first result: the Input Acceleration Peak has a weak relationship with the Measured IsoDisp Peak.

- Input Acceleration Peak: Pearson r ≈ 0.051, Spearman ρ ≈ 0.019

This means that, within this experimental dataset, simply looking at the acceleration peak provides almost no ability to judge how large the final displacement of the isolation layer will be. This is consistent with the problem awareness of the original paper: for an isolation system, average spectral acceleration or acceleration peak should not be treated as the only sufficient indicator.

When the analysis moves to the Input Velocity Peak, the data order becomes much clearer:

- Input Velocity Peak: Pearson r ≈ 0.547, Spearman ρ ≈ 0.586

This indicates that isolation displacement is related to whether the seismic wave contains velocity components capable of pushing the isolation layer into sliding. This also echoes the original paper’s emphasis on velocity pulse and pulse period. The isolation layer is not an ordinary fixed member; its core response is relative displacement. To push the isolation layer open, the velocity pulse is naturally closer to the core of the problem than an instantaneous acceleration peak.

The point of QSM, however, is not merely to choose between acceleration and velocity. The actual transformation is to combine the two:

$$
P_{\mathrm{in}}(t)=a(t)v(t)
$$

In this article, this quantity is treated as a proxy for Input-Side QSM Power Flow. It combines the changing capability of acceleration and the transmission direction of velocity, so that the seismic input is no longer only a question of “how large” it is, but also whether it forms a power flow.

The cross-case-group results show:

- Input-Side QSM Power Peak: Pearson r ≈ 0.424, Spearman ρ ≈ 0.466
- Input-Side 1s QSM Power Packet: Pearson r ≈ 0.461, Spearman ρ ≈ 0.448

These two quantities are not the strongest by themselves, but they complete an important shift: seismic input is no longer read only as motion measurement, but as a power event. The strongest result appears at the interface layer:

- Measured Interface Power/Work Packet: Pearson r ≈ 0.729, Spearman ρ ≈ 0.810
- Accumulated Interface Work: Pearson r ≈ 0.595, Spearman ρ ≈ 0.698

This is the most important overall evidence in the article. It shows that isolation displacement is not determined only by input acceleration or velocity. The relationship with displacement becomes clearer after the input power-potential enters the isolation interface and forms actual Interface Power / Work Exchange.

In other words, the input seismic wave must pass through three layers of conversion:

$$
a(t),v(t)
\rightarrow P_{\mathrm{in}}(t)=a(t)v(t)
\rightarrow F_{\mathrm{interface}}(t)v_{\mathrm{rel}}(t)
\rightarrow u_{\mathrm{iso}}(t)
$$

This is the first QSM conclusion drawn from the original experimental data: isolation displacement is the manifestation of power-potential after it passes through the interface, rather than a direct mapping from input acceleration.

---

# 4. Group1: Time Synchronization and Displacement Manifestation in Short-Period Pulse Cases

Group1 contains short-period pulse cases. It is not the group with the largest displacement, but it is very suitable for establishing the QSM time-event viewpoint.

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group1/Group1_Fig01_core_power_viewpoint_transformation.png)

In Group1 Figure 1, the relation between Input Acceleration Peak and IsoDisp Peak is weak and even negative.

- Input Acceleration Peak: Pearson r ≈ -0.217, Spearman ρ ≈ -0.127

After moving to Input Velocity Peak, the relationship becomes very clear.

- Input Velocity Peak: Pearson r ≈ 0.854, Spearman ρ ≈ 0.733

This means that Group1 displacement is not determined by acceleration peak. It is closer to the pushing effect of the velocity pulse. The QSM Power results then show:

- Input-Side QSM Power Peak: Pearson r ≈ 0.757, Spearman ρ ≈ 0.794
- Input-Side 1s QSM Power Packet: Pearson r ≈ 0.840, Spearman ρ ≈ 0.624
- Measured Interface Power/Work Packet: Pearson r ≈ 0.901, Spearman ρ ≈ 0.964
- Accumulated Interface Work: Pearson r ≈ 0.782, Spearman ρ ≈ 0.782

The greatest value of Group1 is that it is not only strong in correlation; it is also strong in time. In many cases, the QSM Power Packet peak and the displacement peak are very close in time. This indicates that the displacement peak is not a slow average accumulation over the whole record. It is formed rapidly when a power packet enters the interface within a key short time window.

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group1/Group1_Fig02_qsm_power_frequency_group_contact_combined.png)

Group1 Figure 2 is important for understanding the short-period pulse group. It shows that the high-displacement cases in Group1 are not concentrated at one single frequency point. Instead, they form multiple contacts near the Effective Isolation Frequency family and its harmonic bands. The upper panel preserves the full QSM Power Frequency Group, showing that the same record expands into multiple frequency points at a fixed IsoDisp level. The lower panel zooms into the region near $0.5f_{\mathrm{eff}}$ , $f_{\mathrm{eff}}$ , $2f_{\mathrm{eff}}$ , $3f_{\mathrm{eff}}$ , and $4f_{\mathrm{eff}}$ . The point of this figure is not to claim that one harmonic alone controls displacement. It shows that a short-period pulse pushes power-potential into a group of frequency entries, which the isolation system then converts into a lower-frequency displacement response.

In the figure, RSN1013 and RSN4847 form the high-displacement rows of Group1, and their QSM Power frequency points contact regions close to $2f_{\mathrm{eff}}$ , $3f_{\mathrm{eff}}$ , and $4f_{\mathrm{eff}}$ at the same time. This means that a short-period pulse, although short in time, is not thin in the power-frequency domain. It enters the system through a Frequency Group. Medium- and low-displacement cases such as RSN148, RSN4102, and RSN4100 also show frequency-group contact, but their displacement levels are lower. This means that frequency contact alone is not a sufficient condition. It still must be read together with Power Packet intensity, interface work exchange, and time synchronization.

Therefore, Group1 Figure 2 should be read after Group1 Figure 1. Figure 1 shows that Group1 displacement is closer to V, QSM Power Packet, and Interface Work. Figure 2 adds the frequency-layer explanation: these power-potential inputs do not enter the isolation layer through one effective frequency only, but form contact through the Effective Isolation Frequency family and harmonic entries. This is exactly what QSM emphasizes: $f_{\mathrm{eff}}$ is not the endpoint; it is the entry coordinate for power-potential entering the isolation system.

## Representative Cases in Group1

### RSN784: Low-Displacement Case

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group1/RSN784_1_0_21_V25_core_diagnosis.png)

The Measured IsoDisp Peak of RSN784 is 73.06 mm, and the peak time is about 11.95 s. Its main values are:

- Input Acceleration Peak: 0.271 g
- Input Velocity Peak: 0.38 m/s
- QSM Power Shock: 0.561 W/kg
- 1s Power Packet: 0.217 J/kg; lag to displacement peak: -0.051 s
- Measured Interface Power/Work Packet: 3.708 kJ; lag to displacement peak: -0.008 s

Its Frequency-Group Closure comparison is:

- QSM Power Frequency Group: 1.749;2.249;2.749;3.873;4.998;0.500;4.498;5.873 Hz
- Interface Frequency Group: 0.250;1.749;2.749;3.873 Hz
- Displacement Response Frequency Group: 0.250;0.625 Hz

This record is a low-displacement response. Its value is that it provides a low-response reference case. It shows that frequency-group contact alone is not sufficient; power-potential magnitude, interface work exchange, and displacement frequency manifestation must all work together to form large displacement.

### RSN1013: Medium-Displacement Case

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group1/RSN1013_1_0_21_V25_core_diagnosis.png)

The Measured IsoDisp Peak of RSN1013 is 150.2 mm, and the peak time is about 3.297 s. Its main values are:

- Input Acceleration Peak: 0.343 g
- Input Velocity Peak: 0.6 m/s
- QSM Power Shock: 1.361 W/kg
- 1s Power Packet: 0.372 J/kg; lag to displacement peak: 2.797 s
- Measured Interface Power/Work Packet: 5.504 kJ; lag to displacement peak: 2.797 s

Its Frequency-Group Closure comparison is:

- QSM Power Frequency Group: 3.109;1.110;2.442;0.666;1.998;1.554;7.105;4.219 Hz
- Interface Frequency Group: 0.666;1.554;2.442 Hz
- Displacement Response Frequency Group: 0.137;0.274;0.411;0.548;0.685;0.822;0.959 Hz

This record is a medium-displacement response. Its value is that it provides a comparison case: even when the QSM Power Frequency Group and Interface Frequency Group exist, displacement will not necessarily reach the highest level if the interface work packet or displacement receiving condition is insufficient.

### RSN4102: Low-Displacement Case

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group1/RSN4102_1_0_21_V25_core_diagnosis.png)

The Measured IsoDisp Peak of RSN4102 is 44.58 mm, and the peak time is about 0.836 s. Its main values are:

- Input Acceleration Peak: 0.461 g
- Input Velocity Peak: 0.393 m/s
- QSM Power Shock: 0.589 W/kg
- 1s Power Packet: 0.204 J/kg; lag to displacement peak: -0.031 s
- Measured Interface Power/Work Packet: 1.708 kJ; lag to displacement peak: 0.012 s

Its Frequency-Group Closure comparison is:

- QSM Power Frequency Group: 1.026;1.437;2.258;2.669;0.616;6.159;3.079;4.311 Hz
- Interface Frequency Group: 2.280;1.866 Hz
- Displacement Response Frequency Group: 1.033;0.620 Hz

This record is a low-displacement response. Its value is that it provides a low-response reference case. It shows that frequency-group contact alone is not sufficient; power-potential magnitude, interface work exchange, and displacement frequency manifestation must all work together to form large displacement.

## Group1 Summary

Group1 shows that, under short-period pulse input, acceleration is not the main explanatory axis. Velocity is a better entry point, while QSM Power Packet and Interface Power / Work Exchange are closer to the displacement event. The most important evidence is time: the QSM peak and the displacement peak are often very close. This indicates that isolation displacement is an instantaneous manifestation event after the power packet enters the interface.

---

# 5. Group2: Power Packets and Large Displacement Amplification in Medium-Period Pulse Cases

Group2 is the medium-period pulse group. It is also the most suitable group for showing the path of “velocity pulse → Power Packet → Interface Exchange → large displacement.” The original paper states that medium $T_p$ pulse-like ground motions produce larger isolation displacement. QSM analysis adds a more mechanism-based explanation: medium-period velocity pulses are more likely to organize the input power-potential into an effective Power Packet and form strong work exchange at the interface.

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group2/Group2_Fig01_core_power_viewpoint_transformation.png)

In Group2 Figure 1, Input Acceleration Peak has almost no explanatory power.

- Input Acceleration Peak: Pearson r ≈ 0.059, Spearman ρ ≈ -0.200

Input Velocity Peak becomes much clearer.

- Input Velocity Peak: Pearson r ≈ 0.777, Spearman ρ ≈ 0.806

Input-Side QSM Power Peak shows only a moderate relationship.

- Input-Side QSM Power Peak: Pearson r ≈ 0.468, Spearman ρ ≈ 0.406

But the Input-Side 1s QSM Power Packet is much better.

- Input-Side 1s QSM Power Packet: Pearson r ≈ 0.704, Spearman ρ ≈ 0.770

This indicates that the key in Group2 is not an instantaneous shock, but a sustainable power packet. The strongest evidence again appears at the interface:

- Measured Interface Power/Work Packet: Pearson r ≈ 0.889, Spearman ρ ≈ 0.794

By comparison, Accumulated Interface Work is:

- Accumulated Interface Work: Pearson r ≈ 0.539, Spearman ρ ≈ 0.527

This difference is important. It means that the large displacement in Group2 is not determined only by total energy accumulation. It is more closely related to the Interface Power/Work Packet within an effective time window. In other words, whether the power-potential concentrates and enters the isolation interface is closer to the formation of displacement peak than the final total accumulated work.

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group2/Group2_Fig02_qsm_power_frequency_group_contact_combined.png)

Group2 Figure 2 shows the core feature of the medium-period pulse group: the overall displacement level is much higher than Group1, and many high-displacement records still preserve QSM Power Frequency Group contact near $2f_{\mathrm{eff}}$ , $3f_{\mathrm{eff}}$ , and $4f_{\mathrm{eff}}$ . This differs from Group1. Group1 is closer to a short-time power event; Group2 shows a longer-period velocity pulse continuously pushing power-potential into the isolation system, forming larger interface work and larger displacement manifestation.

RSN170 is the most prominent high-displacement case in the figure. It maintains high IsoDisp levels across multiple QSM Power frequency peaks, which means the large displacement is not produced by one single frequency point but by a group of power-potential frequencies acting together. RSN1165, RSN802, and RSN983 also fall in the medium- to high-displacement range. This shows that the risk of medium-period pulses is not only that the velocity peak is high, but that their power-frequency groups are more likely to form effective contact with the entry-frequency family of the isolation system.

By contrast, low-displacement cases such as RSN3317, RSN8130, and RSN1085 also show frequency points, but their horizontal displacement levels are much lower. This means Group2 cannot be read only by asking whether there is contact with $f_{\mathrm{eff}}$ or a harmonic. It must also ask whether sufficient Power Packet and Interface Work Packet are formed after the contact. In this sense, the function of Group2 Figure 2 is to move the statement “medium-period pulses cause large displacement” from a simple period description toward a description of how the power-potential Frequency Group enters the isolation interface.

## Representative Cases in Group2

### RSN170: High-Displacement Case

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group2/RSN170_1_0_31_V25_core_diagnosis.png)

The Measured IsoDisp Peak of RSN170 is 588.7 mm, and the peak time is about 4 s. Its main values are:

- Input Acceleration Peak: 0.26 g
- Input Velocity Peak: 0.858 m/s
- QSM Power Shock: 1.508 W/kg
- 1s Power Packet: 0.612 J/kg; lag to displacement peak: -0.809 s
- Measured Interface Power/Work Packet: 28.51 kJ; lag to displacement peak: -0.734 s

Its Frequency-Group Closure comparison is:

- QSM Power Frequency Group: 0.500;1.500;2.250;1.000;2.750;3.750;4.375;6.000 Hz
- Interface Frequency Group: 0.500;1.499;1.000;2.249 Hz
- Displacement Response Frequency Group: 0.125;0.250;0.375;0.500 Hz

The key point of this record is that it shows both a large displacement response and clear interface work exchange. In the J panel, the Displacement Response Frequency Group is not randomly scattered. It is concentrated in a low-frequency sequence and forms a readable relationship with the Effective Isolation Frequency family. Therefore, RSN170 is a representative case of power-potential entering the interface and manifesting as large displacement.

### RSN983: Medium-High-Displacement Case

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group2/RSN983_1_0_22_V25_core_diagnosis.png)

The Measured IsoDisp Peak of RSN983 is 374.4 mm, and the peak time is about 2.133 s. Its main values are:

- Input Acceleration Peak: 0.342 g
- Input Velocity Peak: 0.688 m/s
- QSM Power Shock: 1.685 W/kg
- 1s Power Packet: 0.496 J/kg; lag to displacement peak: 0.93 s
- Measured Interface Power/Work Packet: 13.44 kJ; lag to displacement peak: 0.84 s

Its Frequency-Group Closure comparison is:

- QSM Power Frequency Group: 3.265;0.768;2.881;2.305;1.729;3.649;5.762;4.225 Hz
- Interface Frequency Group: 0.755;1.699;3.210;2.266;2.832;3.587 Hz
- Displacement Response Frequency Group: 0.326 Hz

This record shows that medium-high displacement is not necessarily determined by a single instantaneous peak. Power Packet, Measured Interface Power/Work Packet, and frequency-group conversion must be read together. It is useful as a middle-layer case for showing that the relation among power-potential intensity, interface exchange, and displacement manifestation is not a single linear relation.

### RSN8130: Medium-Displacement Case

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group2/RSN8130_1_0_21_V25_core_diagnosis.png)

The Measured IsoDisp Peak of RSN8130 is 165.0 mm, and the peak time is about 4.938 s. Its main values are:

- Input Acceleration Peak: 0.242 g
- Input Velocity Peak: 0.528 m/s
- QSM Power Shock: 0.645 W/kg
- 1s Power Packet: 0.286 J/kg; lag to displacement peak: -0.699 s
- Measured Interface Power/Work Packet: 7.074 kJ; lag to displacement peak: -0.641 s

Its Frequency-Group Closure comparison is:

- QSM Power Frequency Group: 1.374;0.625;1.874;2.374;3.248;2.874;3.873;6.247 Hz
- Interface Frequency Group: 0.625;1.374;1.874;2.374 Hz
- Displacement Response Frequency Group: 0.250;1.000 Hz

This record is a medium-displacement response. Its value is that it provides a comparison case: even when the QSM Power Frequency Group and Interface Frequency Group exist, displacement will not necessarily reach the highest level if the interface work packet or displacement receiving condition is insufficient.

## Group2 Summary

Group2 provides the clearest medium-period pulse evidence for QSM Power Flow. It shows that medium-period velocity pulses do more than increase the velocity peak; they are more likely to form a Power Packet that can push the isolation layer. When this packet enters the interface and forms strong Interface Power / Work Exchange, the isolation layer is pushed into large displacement.

---

# 6. Group3: Distributed Power-Potential Field and Low-Frequency Displacement Manifestation in Non-Pulse Cases

Group3 is the non-pulse-like group. In a conventional reading, it is easy to treat this group as a control group against pulse-like records. QSM analysis shows that Group3 should not be understood only as “without pulse.” It is closer to a distributed power-potential field: the power-potential does not enter the system through one clear velocity pulse, but through a longer-duration, wider-band, and more distributed way. It can still enter the isolation interface and manifest as large displacement.

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group3/Group3_Fig01_core_power_viewpoint_transformation.png)

In Group3 Figure 1, the relation between Input Acceleration Peak and IsoDisp Peak is not high.

- Input Acceleration Peak: Pearson r ≈ 0.287, Spearman ρ ≈ 0.370

Input Velocity Peak becomes much clearer.

- Input Velocity Peak: Pearson r ≈ 0.559, Spearman ρ ≈ 0.733

QSM Power Peak shows an interesting rank-ordering ability.

- Input-Side QSM Power Peak: Pearson r ≈ 0.486, Spearman ρ ≈ 0.794

The Input-Side 1s QSM Power Packet is:

- Input-Side 1s QSM Power Packet: Pearson r ≈ 0.387, Spearman ρ ≈ 0.733

This means the Power indicators in Group3 do not necessarily produce a clean linear proportion, but they can distinguish displacement levels. This is different from Group2. Group2 is closer to a medium-period pulse directly forming a strong packet; Group3 is closer to distributed power-potential being reorganized through Frequency Groups and the interface.

The interface-side Interface Power/Work Packet is:

- Measured Interface Power/Work Packet: Pearson r ≈ 0.586, Spearman ρ ≈ 0.576

The interface-side Accumulated Interface Work is:

- Accumulated Interface Work: Pearson r ≈ 0.533, Spearman ρ ≈ 0.576

These relationships are not as strong as Group2, but they are reasonable. For non-pulse input, the power-potential is not concentrated in one short time window; it enters the system in a more distributed way. Therefore, Group3 analysis cannot focus only on one peak or one packet. It must read Input-Side Power, Interface Exchange, Frequency Group, and displacement response together.

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group3/Group3_Fig02_qsm_power_frequency_group_contact_combined.png)

Group3 Figure 2 is one of the most easily underestimated and important group-level frequency maps in this article. Because Group3 is classified as non-pulse-like in the original study, it is easy to read it as “without a clear pulse, and therefore less dangerous.” This figure shows that non-pulse does not mean there is no power-potential field. It means the power-potential does not enter through one clear velocity pulse, but through a more distributed, wider-band, and longer-duration form.

In the figure, RSN1164FP and RSN1233FN form very high displacement levels. Their QSM Power Frequency Groups do not only stay near $f_{\mathrm{eff}}$ , but extend into a wider frequency range. This shows that non-pulse ground motions can still interact with the isolation system through a broadband power-potential field and finally manifest as extremely large displacement. This point is important: if the reading is limited to pulse / non-pulse classification, RSN1164FP may look like a control case. Under the QSM reading, it becomes strong evidence that a distributed power-potential field can produce large displacement.

Group3 Figure 2 also shows that most medium- and low-displacement cases have dense contact near 0.5–1.5 Hz while also extending above 2 Hz. This means the displacement of the non-pulse group is not controlled by one clean frequency line. It is jointly determined by the distribution of the power-potential field across multiple frequency entries, interface selection, and low-frequency displacement manifestation. Therefore, Group3 must be read more carefully than Group1 and Group2: it cannot be read only by peak, and it cannot be read only by a one-second packet. Frequency Group and Interface Exchange must be read together.

This figure supports one important inference of the article: what an isolation system faces is not merely whether a given record has a pulse. The deeper issue is whether that seismic wave forms a power-potential field capable of entering the system, passing through the interface, and finally driving displacement.

## Representative Cases in Group3

### RSN175FN: Medium-High-Displacement Case

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group3/RSN175FN_1_0_31_V25_core_diagnosis.png)

The Measured IsoDisp Peak of RSN175FN is 336.6 mm, and the peak time is about 7.113 s. Its main values are:

- Input Acceleration Peak: 0.346 g
- Input Velocity Peak: 0.706 m/s
- QSM Power Shock: 1.718 W/kg
- 1s Power Packet: 0.624 J/kg; lag to displacement peak: 0.934 s
- Measured Interface Power/Work Packet: 10.77 kJ; lag to displacement peak: -5.934 s

Its Frequency-Group Closure comparison is:

- QSM Power Frequency Group: 3.500;2.500;0.875;1.125;1.625;4.375;8.626;6.375 Hz
- Interface Frequency Group: 0.250;1.499;2.249;1.999 Hz
- Displacement Response Frequency Group: 0.125;0.250;0.375;0.500;0.625 Hz

This record shows that medium-high displacement is not necessarily determined by a single instantaneous peak. Power Packet, Measured Interface Power/Work Packet, and frequency-group conversion must be read together. It is useful as a middle-layer case for showing that the relation among power-potential intensity, interface exchange, and displacement manifestation is not a single linear relation.

### RSN878FN: Medium-Displacement Case

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group3/RSN878FN_1_0_31_V25_core_diagnosis.png)

The Measured IsoDisp Peak of RSN878FN is 140.3 mm, and the peak time is about 40.91 s. Its main values are:

- Input Acceleration Peak: 0.275 g
- Input Velocity Peak: 0.37 m/s
- QSM Power Shock: 0.572 W/kg
- 1s Power Packet: 0.144 J/kg; lag to displacement peak: 2.246 s
- Measured Interface Power/Work Packet: 4.392 kJ; lag to displacement peak: 0.945 s

Its Frequency-Group Closure comparison is:

- QSM Power Frequency Group: 0.750;1.249;1.499;2.124;2.624;3.249;1.874;3.623 Hz
- Interface Frequency Group: 0.750;1.125;1.499;2.124 Hz
- Displacement Response Frequency Group: 0.250;0.750 Hz

This record is a medium-displacement response. Its value is that it provides a comparison case: even when the QSM Power Frequency Group and Interface Frequency Group exist, displacement will not necessarily reach the highest level if the interface work packet or displacement receiving condition is insufficient.

### RSN1164FP: High-Displacement Case

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group3/RSN1164FP_1_0_31_V25_core_diagnosis.png)

The Measured IsoDisp Peak of RSN1164FP is 885.3 mm, and the peak time is about 59.37 s. Its main values are:

- Input Acceleration Peak: 0.416 g
- Input Velocity Peak: 0.537 m/s
- QSM Power Shock: 1.339 W/kg
- 1s Power Packet: 0.327 J/kg; lag to displacement peak: 3.715 s
- Measured Interface Power/Work Packet: 10.05 kJ; lag to displacement peak: 5.203 s

Its Frequency-Group Closure comparison is:

- QSM Power Frequency Group: 2.749;4.873;3.124;7.247;1.749;0.875;5.748;1.249 Hz
- Interface Frequency Group: 0.250;0.875;1.249;0.625;2.749;1.749;1.999;2.499 Hz
- Displacement Response Frequency Group: 0.125;0.250;0.375;0.500 Hz

The key point of this record is that it shows both a large displacement response and clear interface work exchange. In the J panel, the Displacement Response Frequency Group is not randomly scattered. It is concentrated in a low-frequency sequence and forms a readable relationship with the Effective Isolation Frequency family. Therefore, RSN1164FP is a representative case of power-potential entering the interface and manifesting as large displacement.

## Group3 Summary

The significance of Group3 is that it extends QSM from pulse cases to non-pulse power-potential fields. Non-pulse ground motions are not without power-potential; the power-potential enters the system in a distributed field form. When these distributed Frequency Groups are converted through the interface into the low-frequency displacement response of the isolation system, they may still produce extremely large displacement.

---

# 7. Group4: Power-Potential Differences in Spectrally Matched Cases

Group4 is the Spectrally Matched Group. It is important for this article because it directly touches a core issue in engineering design: if ground motions have already been adjusted to be similar in the response-spectrum coordinate, should their actual isolation displacement also be similar?

The QSM answer is: not necessarily. Similar response spectra do not guarantee the same QSM Power Flow, Interface Work Exchange, or Frequency-Group Contact.

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group4/Group4_Fig01_core_power_viewpoint_transformation.png)

In Group4 Figure 1, the relationship between Input Acceleration Peak and IsoDisp Peak is still weak.

- Input Acceleration Peak: Pearson r ≈ 0.265, Spearman ρ ≈ 0.127

Input Velocity Peak increases relative to acceleration.

- Input Velocity Peak: Pearson r ≈ 0.496, Spearman ρ ≈ 0.479

The Input-Side QSM Power Peak is:

- Input-Side QSM Power Peak: Pearson r ≈ 0.470, Spearman ρ ≈ 0.442

The Input-Side 1s QSM Power Packet is:

- Input-Side 1s QSM Power Packet: Pearson r ≈ 0.448, Spearman ρ ≈ 0.418

The key quantities are still the Measured Interface Power/Work Packet and Accumulated Interface Work:

- Measured Interface Power/Work Packet: Pearson r ≈ 0.676, Spearman ρ ≈ 0.576
- Accumulated Interface Work: Pearson r ≈ 0.380, Spearman ρ ≈ 0.491

The Measured Interface Power/Work Packet is closer to IsoDisp Peak than acceleration, velocity, or input-side QSM Power. This means the differences in Group4 begin to be amplified at the interface layer. The input side already appears to have been organized through spectral matching, but at the isolation interface, Interface Power / Work Exchange still shows different power-exchange intensities.

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group4/Group4_Fig02_qsm_power_frequency_group_contact_combined.png)

Group4 Figure 2 is the most direct supplementary evidence for spectral matching in this article. These records have been matched in response-spectrum terms, so a conventional reading may expect them to have closer response demands. However, the Frequency-Group Contact Map shows that even after the response spectra are organized, the QSM Power Frequency Group still retains clear differences.

In the figure, RSN802M forms the highest displacement row. RSN803M and RSN1085M are also in the high-displacement layer, while cases such as RSN8130M have lower displacement. These differences cannot be explained by the Input Acceleration Peak in Figure 1 alone, and they do not automatically disappear after spectral matching. Group4 Figure 2 shows that spectrally matched records still have different contact densities and power-potential distributions near $f_{\mathrm{eff}}$ and its harmonics. Some records can effectively bring the QSM Power Frequency Group into the isolation system, while others cannot.

The meaning of this figure is not that spectral matching has no value. It means spectral matching controls the appearance of the response spectrum, but it does not guarantee control of the power-potential path. For an isolation system, the next questions should be: after matching, does the ground motion still form a Power Packet within the time window? Does it form work exchange at the interface? Does it contact the Effective Isolation Frequency family in the frequency-group domain? Does it finally convert into low-frequency displacement manifestation?

Therefore, Group4 Figure 2 should be read as a reminder for engineering design language: similar response spectra do not necessarily mean similar power-potential; similar Frequency Groups do not necessarily mean similar interface work. Isolation displacement must be read from the actual path through which power-potential passes through the interface.

## Representative Cases in Group4

### RSN170M: Medium-High-Displacement Spectrally Matched Case

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group4/RSN170M_1_0_31_V25_core_diagnosis.png)

The Measured IsoDisp Peak of RSN170M is 397.9 mm, and the peak time is about 61.37 s. Its main values are:

- Input Acceleration Peak: 0.209 g
- Input Velocity Peak: 0.53 m/s
- QSM Power Shock: 0.75 W/kg
- 1s Power Packet: 0.275 J/kg; lag to displacement peak: 8.645 s
- Measured Interface Power/Work Packet: 12.85 kJ; lag to displacement peak: 1.785 s

Its Frequency-Group Closure comparison is:

- QSM Power Frequency Group: 1.624;0.500;2.874;1.249;2.374;2.124;3.249;3.623 Hz
- Interface Frequency Group: 0.375;1.499 Hz
- Displacement Response Frequency Group: 0.125;0.250;0.375 Hz

This record shows that medium-high displacement is not necessarily determined by a single instantaneous peak. Power Packet, Measured Interface Power/Work Packet, and frequency-group conversion must be read together. It is useful as a middle-layer case for showing that the relation among power-potential intensity, interface exchange, and displacement manifestation is not a single linear relation.

### RSN802M: High-Displacement Spectrally Matched Case

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group4/RSN802M_1_0_31_V25_core_diagnosis.png)

The Measured IsoDisp Peak of RSN802M is 659.7 mm, and the peak time is about 25.85 s. Its main values are:

- Input Acceleration Peak: 0.39 g
- Input Velocity Peak: 0.661 m/s
- QSM Power Shock: 1.28 W/kg
- 1s Power Packet: 0.503 J/kg; lag to displacement peak: 19.48 s
- Measured Interface Power/Work Packet: 22.15 kJ; lag to displacement peak: -1.176 s

Its Frequency-Group Closure comparison is:

- QSM Power Frequency Group: 2.500;1.125;3.250;1.625;0.625;4.750;3.750;6.375 Hz
- Interface Frequency Group: 0.250;0.750 Hz
- Displacement Response Frequency Group: 0.125;0.250 Hz

The key point of this record is that it shows both a large displacement response and clear interface work exchange. In the J panel, the Displacement Response Frequency Group is not randomly scattered. It is concentrated in a low-frequency sequence and forms a readable relationship with the Effective Isolation Frequency family. Therefore, RSN802M is a representative case of power-potential entering the interface and manifesting as large displacement.

### RSN8130M: Medium-Displacement Spectrally Matched Case

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group4/RSN8130M_1_0_31_V25_core_diagnosis.png)

The Measured IsoDisp Peak of RSN8130M is 118.4 mm, and the peak time is about 34.83 s. Its main values are:

- Input Acceleration Peak: 0.312 g
- Input Velocity Peak: 0.323 m/s
- QSM Power Shock: 0.452 W/kg
- 1s Power Packet: 0.164 J/kg; lag to displacement peak: 19.04 s
- Measured Interface Power/Work Packet: 3.593 kJ; lag to displacement peak: -0.613 s

Its Frequency-Group Closure comparison is:

- QSM Power Frequency Group: 1.999;2.749;3.499;1.499;0.750;6.747;7.497;4.248 Hz
- Interface Frequency Group: 0.750;1.249 Hz
- Displacement Response Frequency Group: 0.375 Hz

This record is a medium-displacement response. Its value is that it provides a comparison case: even when the QSM Power Frequency Group and Interface Frequency Group exist, displacement will not necessarily reach the highest level if the interface work packet or displacement receiving condition is insufficient.

## Group4 Summary

The core contribution of Group4 is that it identifies a blind spot of spectral matching: it aligns the response spectrum, but it does not necessarily align the power-potential channel. It controls the appearance of the input in the design spectrum, but what the structure actually receives is the time packet, velocity push, Power Flow, interface work, and Frequency-Group Contact. This is why the spectrally matched group still shows clear displacement differences.

---

# 8. Conclusion: Seismic Waves as Power-Potential Fields and Isolation Displacement as Interface Manifestation

This article uses real experimental data from a spherical sliding isolation system to conduct the first empirical validation of Quantum Structural Mechanics. This work follows the most important finding of the original study: acceleration alone, or average spectral acceleration alone, cannot sufficiently explain isolation displacement. This article moves forward from that empirical result and attempts to explain how seismic waves pass through velocity, power flow, interface work, and Frequency Groups before manifesting as isolation displacement.

The first conclusion is that the original data do support the statement that acceleration alone is insufficient. The summary figure across Case Groups Group1–4 shows that the Input Acceleration Peak has an extremely low relationship with the Measured IsoDisp Peak. When the analysis moves to Input Velocity Peak, the relationship becomes much clearer. This indicates that isolation displacement is related to velocity pulse, pushing capacity, and time duration. For an isolation system, a seismic wave must push the isolation layer into sliding over a period of time; a single acceleration peak cannot fully describe this process.

The second conclusion is that the QSM viewpoint transformation is reasonable from the data. This article combines $a(t)$ and $v(t)$ into $P_{\mathrm{in}}(t)=a(t)v(t)$ to describe the Input-Side QSM Power Flow. This transformation moves the seismic input from a simple motion time history into an observable power flow. When this power flow is organized as a Power Packet and further enters the isolation interface to form $F_{\mathrm{interface}}(t)v_{\mathrm{rel}}(t)$ as Interface Power / Work Exchange, its relationship with displacement response becomes the clearest. This means the formation of isolation displacement must be read through input-side power-potential, interface exchange, and actual displacement response together.

The third conclusion is that the frequency structure behind isolation displacement cannot be summarized by one effective frequency only. $f_{\mathrm{eff}}$ is important because it provides the entry scale of the isolation system. The data show that the actual response also contains continuous conversion among the QSM Power Frequency Group, Interface Frequency Group, and Displacement Response Frequency Group. The Figure 2 of each Case Group provides group-level evidence: Group1 shows how short-period pulses contact the effective-frequency family as time events; Group2 shows how medium-period pulses form large displacement through stronger Power Packets and harmonic entries; Group3 shows that non-pulse ground motions can still produce large displacement through a distributed broadband power-potential field; Group4 shows that spectrally matched records still preserve different power-potential paths.

The Frequency-Group Closure comparison in individual Diagnosis Figures is one of the most important validation results in this article. In many high-displacement cases, the displacement response frequencies are not randomly scattered. They form an orderly sequence near the original system effective frequency and its harmonics. This means the effective frequency of the isolation system can be understood as a family of power-potential entries. After the QSM Power Frequency Group of the seismic wave enters the system, it is selected and converted through the interface and finally manifests in the Displacement Response Frequency Group. The key point of the J panel is how the power-potential is received and converted along the effective-frequency family, forming an observable displacement response.

Therefore, the core QSM statement of this article can be summarized as follows:

> For a structure, a seismic wave is a power-potential field passing through the system. When the structure cannot convert this field into a stable energy-flow channel, the power-potential forms work exchange at the interface and manifests as isolation displacement.

This is also the main contribution of this article to the original experimental data. The original study has shown that acceleration alone cannot explain isolation displacement. This article further explains that velocity, power flow, interface work, and Frequency Groups together form a more complete path for reading the data. The value of QSM Power Flow is that it moves the seismic input from Input Motion to Power Packet, then to Interface Exchange, and finally to Frequency-Group Manifestation. This path allows us to describe more clearly how seismic power-potential enters the system, passes through the interface, contacts Frequency Groups, and finally becomes displacement.

For engineering application, this means that future isolation-system evaluation should not only ask how large the input earthquake is. It should also ask how the seismic power-potential enters the system. If the isolation system can guide the input power-potential into channels, diversion, or dissipation, the displacement manifestation may be reduced. If the power-potential concentrates at the interface, the isolation layer may be pushed into large displacement.

This article therefore establishes the first real-data validation basis for Quantum Structural Mechanics: seismic waves can be read as power-potential fields, and isolation displacement can be read as the manifestation of power-potential after it passes through the interface.

---

## References and Data Sources

The experimental data used in this article come from the spherical sliding isolation system dataset published on Zenodo by Yang, Lin, Chang, and Huang. The corresponding research paper was published in *Earthquake Spectra* and studies the response of a spherical sliding isolation system subjected to pulse-like ground motions. The original study has shown that, for an isolation system, acceleration or average spectral acceleration alone cannot sufficiently explain the measured isolation displacement; velocity pulse, pulse period, and the effective period of the isolation system should all be included in the analysis.

This article follows the data and problem awareness of that study and further introduces the viewpoint of Quantum Structural Mechanics (QSM): structural response can be read not only as a relationship between stiffness and displacement, but also as a process of energy flow, topological channeling, and interface exchange. Therefore, this article combines input acceleration and velocity into input-side power-potential flow and observes its relationship with interface work, isolation displacement, and Frequency-Group Manifestation.

### References

1. Yang, Y.-H., Huang, Y.-N., Lin, Y.-C., & Chang, C.-C. (2026). *An experimental study of a spherical sliding isolation system subjected to pulse-like ground motions*. **Earthquake Spectra**. https://doi.org/10.1002/esp4.70074

2. Kuo, H.-J. (2026). *Quantum Structural Mechanics: From Stiffness Assets to Value Flow*. ResearchGate. https://doi.org/10.13140/RG.2.2.27121.13928

### Data Source

1. Yang, Y.-H., Lin, Y.-C., Chang, C.-C., & Huang, Y.-N. (2025). *Dataset of an Experimental Study of a Spherical Sliding Isolation System Subjected to Pulse-Like Ground Motions* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.15606761
