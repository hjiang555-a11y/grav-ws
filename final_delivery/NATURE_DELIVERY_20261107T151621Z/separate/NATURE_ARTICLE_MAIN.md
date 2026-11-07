# Tidal potential measured with distant optical clocks

::: authors
Lei Hou^1,2^, Xiang Zhang^1,2,3^, Qiang Zhu^4^, Xiang-Pei Liu^1,3^, Fa-Xi Chen^1,5^, Wen-Xuan Song^1,2,3^, Zhuan-Xian Xiong^1,4^, Jian-Yu Guan^1,2^, Yu-Chen Zhang^1,2,3^, De-Quan Kong^1,2,3^, Jia-Hao Zhang^1,2,3^, Long-Fei Liao^1,2,3^, Shao-Mao Wang^1,2^, Bing Wang^4^, De-Zhi Xiong^1,4^, Xing-Yang Cui^1,2^, Ping Xu^1,2,3^, Peng Liu^1,2^, Jie Li^2,3^, Xiao Jiang^1,2,3^, Hua-Qing Zhang^1,5^, Ling-Xiang He^1,4^, Li-Bo Li^5^, Qi Shen^1,2,3^, Youchao Xie^6^, Lei Wang^6^, Sheng-Kai Liao^1,2,3^, Juan Yin^1,2,3^, Cheng-Zhi Peng^1,2,3^, Wen-Bin Shen^6^, Baolong Lyu^1,4^, Han-Ning Dai^1,2,3^, Qiang Zhang^1,2,3,5^, Yu-Ao Chen^1,2,3^, Hai-Feng Jiang^1,2,3^, Jian-Wei Pan^1,2,3^

^1^ Hefei National Laboratory, University of Science and Technology of China, Hefei, China

^2^ Shanghai Research Center for Quantum Sciences and CAS Center for Excellence in Quantum Information and Quantum Physics, University of Science and Technology of China, Shanghai, China

^3^ Hefei National Research Center for Physical Sciences at the Microscale and School of Physical Sciences, University of Science and Technology of China, Hefei, China

^4^ Innovation Academy for Precision Measurement Science and Technology, Chinese Academy of Sciences, Wuhan, China

^5^ Jinan Institute of Quantum Technology and CAS Center for Excellence in Quantum Information and Quantum Physics, University of Science and Technology of China, Jinan, China

^6^ Time and Frequency Geodesy Center (TFGC), School of Geodesy and Geomatics, Wuhan University, Wuhan, China

:::

**The Moon and the Sun alter Earth’s gravitational potential through their tidal fields and the responses of the solid Earth and oceans. Changes in the tidal potential modify the relative ticking rates of clocks at different locations. Advances in optical clocks and fiber-optic network technologies have made clocks precise probes of spacetime, providing an experimental foundation for the long-term vision of monitoring Earth’s gravitational potential with a global clock network. In this work, we use strontium and ytterbium clocks separated by 692 km to detect tidal variations in the potential difference between the coastal region of Shanghai and the inland region of Wuhan. Based on 545.9 hours of observations spanning 353 days, the measured variation agrees with the combined solid-Earth and ocean-loading prediction, with a response coefficient of 0.96 ± 0.11. Using spectral analysis, we separate the principal lunar semidiurnal tidal constituent M₂ and the principal solar semidiurnal tidal constituent S₂. The equivalent-height amplitude spectrum has peaks of 4.87 and 2.87 cm at 22.361 and 23.148 μHz, respectively. These measurements demonstrate the use of distant optical clocks to resolve tidal potential changes and identify components for subtraction from future records.**

## Introduction

In the weak-field limit of general relativity, a potential difference $\Delta U$ produces a fractional frequency shift $\Delta\nu/\nu\simeq\Delta U/c^2$, where $c$ is the speed of light.^1^ Optical clocks have become precise probes of spacetime, and their evaluated fractional systematic uncertainties now approach $10^{-19}$.^2^ Fibre networks and free-space frequency transfer now connect distant optical clocks,^3–5^ while proposed quantum clock networks^6^ have advanced to an elementary demonstration using entangled clocks.^7^ Near Earth's surface, fractional shifts of $10^{-18}$, $10^{-19}$ and $10^{-20}$ correspond to equivalent heights of approximately 1 cm, 1 mm and 0.1 mm, respectively.^8,9^ Clock measurements complement conventional levelling and satellite gravity observations,^10,11^ and have resolved gravitational redshift within a millimetre-sized atomic sample.^9^ Precision clock comparisons also support searches for ultralight dark matter and the development of future gravitational-wave detectors.^12,13^

Earth's dynamic environment offers both signals to measure and backgrounds to understand. Mass redistribution and deformation accompany volcanic activity,^14^ ocean and atmospheric disturbances generate tsunamis,^15^ and changing water storage records climate variability.^16^ Monitoring these processes is important for understanding the environment and its hazards. Their contributions to gravitational potential also overlap in a clock record, so a signal of interest in one measurement can become a background in another. Extracting weaker signals therefore requires identifying the sources of measured variations and assessing how accurately each can be removed. Tides provide a predictable signal with which to develop this capability. The Moon and Sun alter the potential directly and through deformation of the solid Earth and movement of ocean water. Their contributions must be distinguished from one another and from laboratory variations synchronized to the solar day. Observational gaps further distribute spectral power into neighbouring frequencies. Separating the tidal components and their sampling sidelobes is therefore important for subtracting the tidal background and identifying weaker signals in the residual record.

Here we measure tidal changes in the potential difference between a strontium clock in coastal Shanghai^17^ and a ytterbium clock in inland Wuhan,^18^ separated by 692 km and connected by a 1,350-km fibre link.^19^ From 545.9 hours of observations spanning 353 days, we measure the combined solid-Earth and ocean-loading tide and separately detect the principal lunar semidiurnal contribution (M₂) and the contribution at the principal solar semidiurnal frequency (S₂). The two contributions evolve differently in phase and produce neighbouring spectral peaks. Each remains identifiable after the other contribution is removed. These measurements test how individual tidal contributions can be identified and removed before weaker potential variations are sought.


## Results

### Measuring a coastal–inland potential difference

The Shanghai Sr clock and Wuhan Yb clock measure tidal changes in potential difference along a 692-km baseline (Fig. 1a). A 1,350-km phase-stabilized fibre link connects them through Hefei.^19^ The comparison instability is about $5.4\times10^{-16}/\sqrt{\tau/\mathrm{s}}$, where $\tau$ is the averaging time, and is dominated by the clocks. Changes in their frequency ratio track the changing potential, while a fitted offset for each observing segment absorbs the static contribution.

Ocean loading contributes appreciably along the coastal–inland baseline. The solid-Earth calculation follows the IERS conventions.^20^ The FES2022 loading calculation^21,22^ includes water attraction, induced Earth potential and clock displacement.^23^ For the principal lunar semidiurnal tide, M₂, the differential solid-tide and loading amplitudes are $3.41\times10^{-18}$ and $1.42\times10^{-18}$ in fractional frequency. Their 20° phase difference gives a combined amplitude of $4.77\times10^{-18}$ (Fig. 1b).

The record spans 353 days, five campaigns and 54 observing segments (Fig. 1c). The primary triangular-filter reduction retains approximately 544 h after transient screening and applies a 1,200-s filter at 600-s steps identically to observations and model. The auxiliary reduction used in Fig. 3 contains 3,299 non-overlapping 600-s means formed from 545.924 h of retained samples. It supports the frequency-domain checks without the triangular filter. The reductions have distinct selections, weights and physical-template realizations, with segment offsets in both (Methods).

### Tidal amplitude, phase and observation coverage

The auxiliary full-template response is $0.96\pm0.11$, consistent with the combined potential prediction (Fig. 3a). Its error is the larger of scaled least squares and UTC-day jackknife, with observations weighted by each period's noise. A response of one denotes agreement with the predicted frequency-ratio change. To separate the semidiurnal contributions, we group M₂ with the larger lunar elliptic semidiurnal tide, N₂, associated with the Moon's elliptical orbit. The neighbouring group combines the principal solar semidiurnal tide, S₂, with the lunisolar semidiurnal tide, K₂, associated with lunar and solar declination. Within each group, relative amplitudes and phases follow the physical model.

The primary reduction gives lunar and neighbouring responses of $0.97\pm0.14$ and $0.90\pm0.29$ (Fig. 2 and Extended Data Fig. 11). Residual resampling calibrates the lunar uncertainty. The neighbouring-group error is the larger of scaled least squares and day-by-day jackknife. A free-phase lunar fit gives amplitude $0.98\pm0.11$ and phase offset $-6°\pm8°$, with segment-bootstrap uncertainties. The auxiliary phase fit also agrees with the predicted timing (Fig. 3b; Methods). The primary grouped estimate contains no empirical daily terms. Additional fits test their influence.

The lunar and solar semidiurnal periods are approximately 12.42 h and 12 h. Their changing relative phase lets the summer observations distinguish them: the two-month campaign covers the full relative phase cycle, whereas shorter campaigns cover narrower intervals (Fig. 1d). The five campaign estimates are mutually consistent (Extended Data Fig. 3 and Table 3). Figure 2 shows the summer time series and its lunar-phase dependence after removal of fitted offsets and non-lunar groups. The lunar model is folded using the same sampling. Gaps are compressed and marked on the time axis; Extended Data Fig. 4 retains calendar time. The phase and amplitude results agree with the predicted tidal variation.

### Amplitude spectrum and separate semidiurnal detections

The equivalent-height amplitude spectrum has lunar and solar-frequency peaks of 4.87 and 2.87 cm at 22.361 and 23.148 μHz (Fig. 3c). These are sinusoidal peak amplitudes from separate frequency scans with equal weights and 54 segment offsets. Subtracting the fixed unit-amplitude complete physical prediction reduces the amplitudes at these frequencies to 0.71 and 1.02 cm. The calendar span sets the nominal frequency scale; the actual gaps and offset projection shape the spectral response (Methods). The plotted heights express the same measured potential variation through the gravitational redshift relation.

Each principal frequency retains structure when the other is controlled with a freely phased sinusoid (Extended Data Fig. 7). These conditional scans also control N₂ and K₂. Joint fitting gives M₂ and S₂ amplitudes of $4.50\times10^{-18}$ and $1.92\times10^{-18}$, with coefficient uncertainties in Extended Data Table 4. They differ from the scan peaks because neighbouring frequencies are fitted simultaneously. Unlike the physical groups above, the individual sinusoidal contributions have independent phases. The conditional spectra therefore support two contributions without imposing their astronomical phase relation.

### Reliability of the separated signals

Reciprocal subtraction tests their coupling on the recorded sampling (Extended Data Fig. 8). Removing the jointly fitted lunar waveform changes the solar-frequency amplitude from $2.918\times10^{-18}$ to $1.921\times10^{-18}$; removing the solar-frequency waveform changes the lunar amplitude from $4.857\times10^{-18}$ to $4.505\times10^{-18}$. Both remain identifiable. The maximum canonical correlation, measuring the strongest overlap between linear combinations of the projected sine–cosine pairs, is 0.290 (Extended Data Fig. 9). Together, the conditional spectra, reciprocal subtraction and correlation analysis support separation while quantifying the coupling introduced by the sampling.

The primary lunar estimate also remains consistent under explicit daily-disturbance models (Fig. 4). A $10^{-18}$ fractional-frequency sinusoid at 24 h or 12 h changes the response by at most 0.020 when its phase is fixed across the record. Allowing independent campaign phases increases these bounds to 0.032 and 0.12, respectively. These limits apply to the specified amplitudes and phase assumptions. Both clocks correct blackbody shifts in real time; temperature regressions and the chamber-temperature record provide further checks (Methods and Extended Data Fig. 2).

Adding the fibre-link monitor on matching samples changes the lunar and full-template responses by less than 0.005. Retaining excluded transients likewise leaves the lunar result consistent. Fits improve predictions for most withheld observation periods (Methods). Coastal-model sensitivity is larger: extending the ocean mask near Shanghai by 0.3° or 0.6° changes the response by about −0.06 or −0.07. These model shifts are reported separately from statistical uncertainty. Thus the checks distinguish small instrumental and processing effects from the appreciable sensitivity to coastal loading representation.

### Ocean loading and diurnal response

The primary triangular-filter record constrains separate ocean loading and the once-daily tidal band less precisely. The loading coefficient is $0.89\pm0.55$ (Methods). A joint diurnal–semidiurnal fit gives a diurnal response of $0.36\pm0.50$, using the larger scaled-least-squares or day-jackknife error (Extended Data Fig. 3b). This is a physical tidal response, distinct from the empirical 24-h disturbances tested above. The combined potential agrees with the observations, while the separate contributions remain more weakly constrained; refining coastal loading would sharpen this comparison.^24^

## Discussion

The precision of each tidal component depends on signal strength, noise and phase coverage. Sampling interval, continuous observation length and total span affect different parts of the measurement. For uniformly sampled, band-limited signals, the Nyquist condition requires sampling faster than twice the highest signal frequency. Within short observing segments, a slowly varying tide can be absorbed into the fitted offset. Continuous runs of at least two days would cover successive diurnal cycles. Maintaining phase lock preserves the phase connection throughout these runs (Methods, “Fibre-link phase locking and monitoring”). Shorter runs provide less information about slow signals per unit exposure. A longer calendar span separates neighbouring frequencies, while gaps create sidelobes. Their response to lunar-waveform subtraction identifies features associated with the sampling window (Extended Data Fig. 10; Supplementary Methods SM7).

For a specified estimator, the amplitude signal-to-noise ratio scales locally as

$$
\rho_i(T)\simeq\rho_i(T_0)
\frac{\eta_i(T)}{\eta_i(T_0)}
\left(\frac{T}{T_0}\right)^{a_i-b_i}.\tag{1}
$$

Here $T$ is retained exposure, defined consistently at $T_0$, and $\rho_i=S/R$. The exponents $a_i$ and $b_i$ describe accumulation of the unnormalized, phase-aligned signal and noise standard deviation. The factor $\eta_i$ accounts for the sampling window, weights and parameter coupling. For a coherent signal and independent white noise, $a_i=1$ and $b_i=1/2$, giving $\rho_i\propto\sqrt{T}$ at fixed $\eta_i$. The white-noise calculation uses the measured amplitudes and actual sampling, with covariance propagation described in Methods.

::: display
**Table 1 | Calculated and measured signal-to-noise ratios.**

| Evaluation | Lunar M₂ | Solar S₂ | Diurnal group | Ocean loading |
|:--|--:|--:|--:|--:|
| $S/R$ (white noise) | 7.17 | 2.78 | 1.55 | 1.17 |
| $S/R$ (measured) | 7.02 | 1.96 | 1.08 | 0.89 |

Here $S=|\hat A|$ is the measured amplitude or template-response magnitude, $R=u(\hat A)$ is its standard error, and $S/R=\rho$. The white-noise row uses the common noise coefficient and actual sampling; the measured row uses UTC-day-jackknife covariance. All entries use the auxiliary non-overlapping reduction. M₂ and S₂ use their joint sine–cosine fit, the diurnal group uses the three-group fit, and ocean loading uses the complete solid-Earth/loading fit (Methods).
:::

The lunar precision closely matches the white-noise estimate, whereas the solar-frequency contribution has a larger empirical uncertainty (Table 1). Measurements at this frequency may also be affected by the 12-h harmonic of daily laboratory activity. The diurnal group and separate ocean-loading response have signal-to-noise ratios near unity. Short segments constrain diurnal cycles poorly after offset removal, while ocean loading has a smaller predicted amplitude and overlaps the solid-Earth waveform. Unmodelled changes in loading amplitude or phase may further weaken accumulation against a fixed template.^22^ The present estimates do not quantify such coherence loss. The calculated sensitivities account for much of the difference in precision between components under the same assumed time exponents.

Sustained network operation would improve phase coverage and separation, while better clock stability would increase sensitivity within a given observing time. Stable endpoints, local environmental records and additional sites would help identify weaker changes after subtraction of the tidal background. These measurements extend demonstrated sub-centimetre-equivalent clock performance^8^ towards time-varying geophysical observations, alongside applications to ultralight-dark-matter searches^12^ and future clock-based gravitational-wave detectors.^13^

## Summary

We measured tidal potential differences between Shanghai and Wuhan optical clocks and separately detected lunar and solar-frequency semidiurnal contributions, with equivalent-height amplitude-spectrum peaks of 4.87 and 2.87 cm. Conditional spectra, reciprocal subtraction and correlation analysis support their separation. We also developed a sensitivity estimate based on signal strength, noise and sampling that broadly agrees with the precision achieved in the measurements. Sustained observations at more sites would extend this capability to weaker potential changes and their spatial structure.

The 274-h summer record was also used in the absolute-frequency-ratio study by Hou et al.; Extended Data Table 5 relates those estimates to the present tidal analysis.^25^ An independent study has also reported tidal potential variations in a European optical-clock network.^26^


## Methods

### Clocks, frequency transfer and sampling

The Sr optical lattice clock is located in Shanghai (31.130° N, 121.570° E, height approximately 5 m) and the Yb optical lattice clock in Wuhan (30.529° N, 114.357° E, approximately 30 m). The tidal model is insensitive to the absolute heights: changing the Shanghai height by 5 m changes the differential model by $4\times10^{-23}$. The geopotential difference between the clocks, $280.042\pm0.085\ \mathrm{m^2\,s^{-2}}$, was determined by first-order levelling ^25^. It enters the static frequency ratio and is absorbed by the fitted offsets. The clocks, fibre link and frequency chain are described in ref. ^25^. The evaluated systematic uncertainties of the Sr and Yb clocks are $9.2\times10^{-19}$ and $1.3\times10^{-18}$, respectively ^17,18^; optical frequency dissemination over field fibres of comparable length has also been demonstrated ^19,27^.

A 1,550-nm carrier referenced to the Sr clock through a frequency comb in Shanghai is transmitted to Wuhan, where its beat against the Yb-referenced comb is recorded at 1-s intervals. In the 2026 campaigns, the beat frequency is 33.6 MHz and a deviation of 1 Hz corresponds to $5.17\times10^{-15}$ in Yb/Sr. In 2025, the counter recorded the beat after division by two; these deviations are therefore multiplied by two. Fitting the September–October 2025 campaign alone gives $A=1.28\pm0.31$, consistent with this scale and sign. The white-frequency-noise level of the tide-corrected ratio, $\sigma_y\sqrt{\tau}$, obtained from the overlapping Allan deviation ^28^ at averaging times of 256–4,096 s, is $7.9\times10^{-16}$ in September–October 2025 and $4.2$–$5.3\times10^{-16}$ in the 2026 campaigns.

The record contains five campaigns: September–October 2025, January 2026, April 2026, May 2026 and June–August 2026. The 54 segments were defined by the experiment team; the summer segments are those used in ref. ^25^. There are 38 segments and 270 h before June and 16 segments and 274 h in June–August, giving 544 h, or approximately 23 days, of retained data. The analysis distinguishes these five campaigns from eight observation periods and 29 operating groups. Campaigns define the seasonal subsets and campaign-specific daily terms; observation periods are the units of held-out prediction; operating groups are the units of group bootstrap resampling; segments carry the offsets in the primary fit. These levels are not treated as interchangeable independent samples.

### Data selection

The same selection procedure is applied to every segment. The time axis of each data file is reconstructed from its first time stamp and the sample index. Samples more than 10 Hz from the segment median are removed, the longest uninterrupted run is retained, and leading and trailing samples deviating from the median by more than 1% of the peak-to-peak range are trimmed. The 10-Hz threshold corresponds to approximately $5\times10^{-14}$ in Yb/Sr. To identify smaller transient excursions, the retained 1-s data are averaged over 300 s and compared with a running median over ±30 min. Averages deviating by more than six robust standard deviations of these differences within the segment are removed together with their neighbours. This step removes 0.4% of the samples, or 2.2 h, including an excursion of approximately $-2\times10^{-16}$ lasting about 20 min on 7 July 2026.

The transient criterion uses no tidal model. Its invariance to tidal additions and sensitivity to screening choices are documented in Supplementary Methods SM2. Injection simulations use the selected data because the tested additions leave selection unchanged and the subsequent filter is linear.

Durations refer to retained 1-s samples; exposure measured from the filtered data at 600-s steps, used for temperature overlap, is slightly shorter. The last April segment ends at 18:00 on 19 April. Time stamps are in local time (UTC+8). Endpoint and timing checks are given in Supplementary Methods SM2. Long-period tides are outside the analysis.

### Solid Earth tide and ocean loading

The solid Earth contribution at each clock is computed directly as

$$
\delta W=\sum_m(1+k_{2m})V_{2m}+(1+k_3)V_3-g u_r.
$$

Here $V_{2m}$ are the degree-2 tide-generating potentials of the Moon and Sun separated by order $m$, $V_3$ is the lunar degree-3 potential, and $u_r$ is radial displacement. The IERS algorithm supplies displacement and frequency-dependent Love numbers ^20^; their values and constituent definitions are given in Supplementary Methods SM1.

The ocean-loading potential is computed by grid convolution:

$$
\delta W_{\rm ocean}(t)=\sum_{\rm ocean}\rho_w\zeta(\mathbf r',t)G_W(\psi)\,\mathrm dA,
\qquad
G_W(\psi)=\frac{ga}{M_E}\sum_n(1+k'_n-h'_n)P_n(\cos\psi).
$$

The ocean elevation $\zeta$ is taken from FES2022 on a $1/30^\circ$ grid ^21,22^, with $\rho_w=1,025\ \mathrm{kg\,m^{-3}}$. Here $a$ and $M_E$ are Earth's radius and mass, and $\psi$ is angular distance. The Green's function ^23^ uses PREM load Love numbers ^29,30^. We remove the ocean mean and synthesize eight constituents with astronomical arguments and nodal corrections. Numerical implementation and displacement validation are given in Supplementary Methods SM1.

Coastal-mask changes shift the fitted response by 0.06–0.07, approximately half the lunar statistical uncertainty. These are physical-model sensitivity tests, not independent Gaussian errors or an exhaustive loading uncertainty (Supplementary Methods SM1).

### Tidal fits and uncertainty

The 1-s observations and model are filtered identically using a 1,200-s triangular window stepped by 600 s. The whole-template model is fitted by least squares as $y(t)=c_i+A s(t)$, with an offset $c_i$ for segment $i$. The diurnal constituents are the lunisolar diurnal tide, K₁, the principal lunar diurnal tide, O₁, the principal solar diurnal tide, P₁, and the larger lunar elliptic diurnal tide, Q₁. For the band analysis, the eight-constituent model is divided either into semidiurnal (M₂, S₂, N₂, K₂) and diurnal (K₁, O₁, P₁, Q₁) bands, or into lunar (M₂, N₂), near-12-h (S₂, K₂) and diurnal groups with separate amplitudes. The primary grouped fit contains no empirical daily terms. If the full physical model is correct, fitting the solid Earth tide alone on the actual sampling is expected to give $A=1.32$, because loading adds to the solid tide with an M₂ phase difference of approximately 20°.

Where indicated, uncertainty is the larger of the scaled least-squares standard error^31^ and the day-by-day jackknife error. For the full template, semidiurnal band and lunar group, uncertainty is calibrated by residual resampling. The fitted residuals are shifted circularly within each continuous run of the filtered record and added to the model with $A=1$; the standard deviation of the refitted amplitude over 200 realizations supplies the calibrated error. These shifts retain the within-run residual structure under circular wrapping. Calibration uses two independent sets of 200 realizations for the lunar group; disturbance coverage is checked with 5,000 realizations per scenario (Supplementary Methods SM3).

Calibrated errors are used for the whole-template and semidiurnal responses of individual campaigns and of the full record. For the diurnal and near-12-h groups, fits containing empirical daily terms, and fitted daily amplitudes, the larger of the scaled least-squares and jackknife errors is used. In the resampled data, these errors differ from the calibrated uncertainty by factors of 0.8–1.3. Unless otherwise specified, quoted ± uncertainties denote one standard deviation or one standard error as defined by the applicable procedure.

Group-bootstrap intervals are obtained by drawing the 29 operating groups with replacement and refitting 1,000 times; the segment bootstrap instead draws the 54 segments. These procedures permit correlations within each resampling unit but assume independence between units. In the phase test, each tidal band has in-phase and quadrature templates, the latter formed by shifting every constituent by 90°; uncertainty uses segment bootstrap resampling (Supplementary Methods SM3).

The phase-folded summer display is formed after subtracting the fitted segment offsets and non-lunar groups and then averaging in 30° M₂-phase bins; the M₂+N₂ model is folded with the same sampling. Its day-by-day jackknife error bars hold the fitted non-lunar terms fixed. They are conditional display uncertainties and do not propagate uncertainty in those fitted terms; they are distinct from the uncertainty of the joint lunar-amplitude estimate. The summer time-series display uses 3-h averages. Gaps longer than 6 h are removed from the horizontal axis and their locations are marked.

The eight constituents explain 99.84% of model variance; the remaining component, with an r.m.s. of $0.18\times10^{-18}$, is held at its predicted value. Remainder and loading checks are given in Supplementary Methods SM1.

### Daily disturbances and validation

Daily sensitivity fits add terms $a_1\cos\omega t+b_1\sin\omega t+a_2\cos2\omega t+b_2\sin2\omega t$, where $\omega=2\pi/(1\ \mathrm{day})$ and $t$ is local time. Common coefficients and campaign-specific coefficients are examined. A physically constrained alternative uses a free-amplitude 24-h term in each campaign with the phase of the 24-h harmonic of hourly ERA5 2-m air temperature at the two sites ^32^, averaged over that campaign. Another alternative includes the air-temperature anomalies at both sites relative to a 24-h running mean as two regressors. Within a short campaign, a 24-h term is partly degenerate with diurnal tides and segment offsets.

The sensitivity of the lunar estimate to $B\cos(\omega t-\varphi)$ is evaluated using the lunar row $h$ of the operator $H$ defined below, evaluated for the primary fit. For a common phase, the maximum amplitude change is

$$
B\sqrt{(h\cdot\cos\omega t)^2+(h\cdot\sin\omega t)^2}.
$$

For phases independent between campaigns, the maximum is the sum of the corresponding campaign norms. These bounds describe the specified sinusoidal disturbances and phase assumptions; they do not exclude arbitrary time-varying daily effects.

Injection tests use circularly shifted residuals of the full-template fit, adding either the full tidal model ($A=1$) or the model without its lunar group ($A=0$). Four daily-disturbance scenarios are considered: no added daily disturbance; campaign-specific 24-h terms with air-temperature phases and amplitudes fitted to the observations; common 24-h and 12-h terms with fitted amplitudes and phases; and the fitted summer 24-h and 12-h terms. We use 300 realizations per scenario and injected amplitude; biases and coverage, conditional on these residual and disturbance models, are reported in Supplementary Methods SM3.

Campaign information shares are calculated by projecting the lunar template onto the complement of the near-12-h and diurnal templates and segment offsets, then summing its squared projected values within each campaign.

Held-out prediction estimates the amplitude from the other observation periods and applies it to the excluded period, fitting that period's segment offsets. Results are given in Supplementary Methods SM4.

### Primary spectral diagnostics

The full-record and April spectra show sinusoidal power, defined as squared sinusoidal amplitude divided by two, after projection of segment offsets and before and after subtraction of the fitted whole template (Extended Data Figs. 4 and 11). Its 99% threshold is the quantile of the maximum over 5–40 μHz in 200 resampled residual series. For the April record, pointwise 99% thresholds and the 99% threshold of the maximum over 15–50 μHz are obtained from 1,000 resampled residual series. No frequency exceeds the latter threshold after tidal correction; the largest residual feature, near 39 μHz, is away from the tidal frequencies. The four-day April record combines neighbouring constituents into broad diurnal and semidiurnal bands. Spectral displays use a linear vertical scale. A decrease in spectral power after fitted-template subtraction is a consistency check, not an independent detection statistic.

Segment-wise and independent ten-day-baseline processing are cross-checks on shared observations, not independent measurements (Extended Data Table 5; Supplementary Methods SM5).

### Fibre-link phase locking and monitoring

The 1,350-km link extends the earlier 2,067-km dissemination system, which uses bias-free noise compensation based on digital radio-frequency phase recording ^19,25^. Frequency counter B continuously monitors the out-of-loop round-trip signal, and the optical phase-locked loops in the frequency chain are monitored to assess the operating state ^25^. Maintaining lock preserves the phase connection needed for coherent accumulation. Lock continuity refers to the phase-locked loops remaining locked; it is distinct from the sampling intervals and gaps in the clock record.

The round-trip beat of the fibre link is recorded at the Shanghai end near 10 MHz with 1-s resolution. Its deviations are normalized by the optical carrier frequency without division by two and filtered in the same way as the clock ratio. Samples more than 10 Hz from the median are excluded. Monitor excursions reaching $10^{-12}$ leave the recorded ratio unchanged. Excluding 300-s monitor blocks deviating by more than $5\times10^{-16}$ changes the regression result by less than 0.005. The monitor covers 474 h of the analysed data. On that overlap, the lunar and whole-template amplitudes are 0.93 and 0.80; including the monitor as an additional regressor changes each by less than 0.005.

### Environmental analysis

The Sr vacuum-chamber temperature is the mean of 20 PT100 sensors sampled every 20 s, available from 28 June to 7 July 2026 and overlapping 98 h of the filtered summer record. The blackbody sensitivity is $6.26\times10^{-17}\ \mathrm{K^{-1}}$ at 294.3 K; a temperature increase raises Yb/Sr. The daily temperature profile is obtained after subtracting a 24-h running mean and excluding the chamber-temperature transient on 30 June. Both clocks apply blackbody corrections in real time, so the recorded ratio already includes them. The regression therefore tests correction errors proportional to chamber temperature; its expected coefficient is zero.

Temperature-regression results and disturbance checks are given in Supplementary Methods SM4.

The triangular-filter analysis reports a separately fitted loading coefficient of $0.89\pm0.55$ (Supplementary Methods SM4). It is distinct from the auxiliary complete-template loading fit described below.




### Auxiliary grouped-response and phase estimates

Figure 3 uses the non-overlapping reduction, with 3,299 means, 1,965,327 nominal one-second members and 54 segment constants. The 545.924 member-hours span 353.39 days. This reduction retains its existing valid-interval selection and does not apply the primary analysis's triangular filter or additional transient screening. The template realization is also distinct from the direct-potential primary model. Its solid-Earth sequence converts the IERS radial displacements into fractional frequency as

$$
y_{\rm solid}=-\frac{1+k_2-h_2}{h_2}\frac{g(u_{\rm Wuhan}-u_{\rm Shanghai})}{c^2},
$$

with $h_2=0.6078$, $k_2=0.3010$ and $g=9.794\ \mathrm{m/s^2}$. Its ocean-loading sequence uses the effective-potential convolution with direct water attraction, induced potential and clock displacement, synthesizing 18 loading constituents. Eight named constituents form the lunar, neighbouring semidiurnal and diurnal groups; the remaining terms form a fixed remainder $r_0$.

For the complete-template estimate, a single coefficient multiplies the full prediction, $y_i=c_{s(i)}+A_T(s_{L,i}+s_{S,i}+s_{D,i}+r_{0,i})+\epsilon_i$. For the grouped estimate, the remainder is subtracted once and the three groups are fitted jointly, $y_i-r_{0,i}=c_{s(i)}+A_Ls_{L,i}+A_Ss_{S,i}+A_Ds_{D,i}+\epsilon_i$. The phase-relaxed model adds a quarter-cycle-shifted lunar template while retaining the prescribed internal M₂/N₂ relationship. All models retain the same segment constants. They do not average amplitudes fitted separately to individual segments.

The amplitude fits use $W_{ii}=1/\sigma_i^2$, where $\sigma_i=\alpha_{p(i)}/\sqrt{\Delta t_i}$ and $\Delta t_i=n_i\delta t$ is the retained exposure in bin $i$, with $n_i$ one-second members and $\delta t=1\,\mathrm{s}$. The coefficient $\alpha_p$ describes white frequency noise in observing period $p$ and has units $\sqrt{\mathrm{s}}$. The coefficients are derived from overlapping Allan deviations at 256–4,096 s within acquisition segments. The reported marginal errors are the larger of the residual-scaled least-squares and UTC-day-deletion jackknife standard errors; each deletion refits the coefficients. Grouped and phase-relaxed responses are summarized in Fig. 3 and Supplementary Methods SM6. The contours in Fig. 3b instead use the scaled-least-squares covariance at radii one and two; its quadrature marginal standard error is 0.1273. These contours are covariance summaries, not independently calibrated joint confidence regions.

### Signal-to-noise ratios for the retained sampling

We use $S/R=\rho_i=|\hat A_i|/u(\hat A_i)$, where $S$ is the fitted amplitude or template-response magnitude and $R$ is its standard error. To evaluate the coherent-white-noise case of equation (1), we retain the fitted design matrix $X$, weights $W$ and exposures $\Delta t_k=n_k\delta t$. The operator $H=(X^{\mathsf T}WX)^{-1}X^{\mathsf T}W$ maps observations to fitted coefficients. For white frequency noise with $\alpha=5.4\times10^{-16}\sqrt{\mathrm{s}}$, the bin variance is $\alpha^2/\Delta t_k$, giving

$$
u_{i,\mathrm{white}}^2=\alpha^2\sum_k\frac{H_{ik}^2}{\Delta t_k},
\qquad
\rho_{i,\mathrm{white}}=\frac{|\hat A_i|}{u_{i,\mathrm{white}}}.\tag{2}
$$

The retained exposure is $T=\sum_k\Delta t_k=1,965,327\,\mathrm{s}$. For template $s_i(t_k)$ per unit response at bin-centre time $t_k$, define $s_{i,\mathrm{rms}}^2=\sum_k\Delta t_k\,s_i(t_k)^2/T$ and $\eta_i=\alpha/(s_{i,\mathrm{rms}}\sqrt{T}\,u_{i,\mathrm{white}})$. Then

$$
\rho_{i,\mathrm{white}}=
\frac{|\hat A_i|s_{i,\mathrm{rms}}}{\alpha}\,\eta_i\sqrt{T}.\tag{3}
$$

All retained samples contribute to $T$. The sampling window, fitted offsets, template coupling and chosen weights enter $\eta_i$. No two-day minimum is applied to this record. Equation (3) gives the $a_i=1$, $b_i=1/2$ sensitivity at the measured amplitude; the time exponents are not fitted.

The first four rows of Extended Data Table 6 use the existing non-overlapping full-template or three-group fits and their larger scaled-least-squares or UTC-day-jackknife errors. To quantify separate loading sensitivity on the same record, we fit the complete solid-Earth and loading templates with two free coefficients and 54 segment offsets, using equal weights. Their sum equals the complete prediction, so no fixed remainder is added separately. This auxiliary fit gives $A_{\rm solid}=1.08\pm0.32$ and $A_{\rm loading}=0.49\pm0.54$. Errors are from deleting each of the 43 UTC days and refitting both coefficients and all remaining offsets. This is distinct from the triangular-filter loading estimate reported above.

For Table 1, the individual M₂ and S₂ estimates retain the equal-weight joint fit of M₂, S₂, N₂ and K₂ sine–cosine pairs and 54 segment offsets. For each target pair, $\hat A=(\beta_c^2+\beta_s^2)^{1/2}$ and $J=(\beta_c,\beta_s)/\hat A$. We propagate the full fitted coefficient covariance and take the target block $C_i$, giving $u^2(\hat A)=JC_iJ^{\mathsf T}$. For the white-noise row, $C_\beta=H\Sigma H^{\mathsf T}$ with $\Sigma_{kk}=\alpha^2/\Delta t_k$. The measured row of Table 1 propagates the coefficient covariance from 43 UTC-day deletion fits through the same gradient. These are local scalar amplitude-to-error ratios, rather than calibrated Gaussian detection significances. The measured amplitudes and propagated errors are listed in Supplementary Methods SM6.

The diurnal and loading columns of Table 1 use their original template estimators; the loading column refers to the auxiliary complete-template fit. Within each column, the estimator, amplitude and physical target are unchanged between the white-noise calculation and measured uncertainty (Supplementary Methods SM6).

### Local amplitude spectrum in Figure 3

Figure 3c uses the original fractional-frequency means of the auxiliary reduction, equal row weights and their stored UTC bin-centre times. At each trial frequency, we fit a freely phased sinusoid and the same 54 segment constants:

$$
y_i=c_{s(i)}+a_f\cos[2\pi f(t_i-t_0)]+b_f\sin[2\pi f(t_i-t_0)]+\epsilon_i.
$$

The plotted scalar is the sinusoidal peak amplitude $A_y(f)=\sqrt{a_f^2+b_f^2}$. For the residual curve, the fixed unit-amplitude complete physical prediction is first subtracted from the time series, and the sinusoidal fit is then repeated. The response coefficients of Fig. 3a are not applied in this subtraction.

The left axis gives equivalent-height peak amplitude $A_{h,\mathrm{cm}}=100c^2A_y/g_0$ in cm, with conventional standard gravity $g_0=9.80665\ \mathrm{m/s^2}$ and $c=299,792,458\ \mathrm{m/s}$. The right axis gives the same amplitude in fractional-frequency units. Both axes are linear and start at zero. This conversion expresses a potential difference as an equivalent height without changing the physical model's gravity value. It is neither a root-mean-square amplitude nor an amplitude spectral density.

The plotted band is 21–24.5 μHz. The elapsed span $T_{\rm span}=353.3889$ d gives the nominal Rayleigh frequency scale $1/T_{\rm span}=0.03275$ μHz. The basic scan spacing is $1/(12T_{\rm span})=0.002729$ μHz, with the prescribed astronomical frequencies also included. The grid oversamples the Rayleigh scale; the actual sampling window and offset projection determine the peak shapes and coupling. Scan peaks are selected as local amplitude maxima within one Rayleigh scale of each prescribed frequency. These fits control segment offsets only; the joint constituent estimates below also control neighbouring frequencies.

### Auxiliary frequency-domain analysis

The analyses in Extended Data Figs. 7–10 use the same non-overlapping observations and UTC bin-centre convention as Fig. 3c. Fractional-frequency values are expressed numerically in units of 10⁻¹⁸. Spectral fits use equal weights; the physical-template estimates in Fig. 3a,b use the period-dependent noise weights.

For a nuisance matrix N, we form its orthonormal basis Q and apply R = I − QQᵀ to both the observation vector and each trial cosine–sine pair. The spectral score ΔRSS is the reduction in residual sum of squares when the projected pair is fitted. We use the nominal-600-s normalization, D(f) = 600 × 10⁻⁴² ΔRSS per µHz. This convention provides a common scale for comparisons on these gapped observations; integrating it is not asserted to recover the time-domain variance. Extended Data Fig. 7a uses segment constants only. Extended Data Fig. 7b–d add freely phased N₂ and K₂ terms. All sinusoidal phases refer to 6 September 2025, 16:05 UTC, the first stored bin centre.

The M₂ and S₂ subtraction waveforms come from a simultaneous four-coefficient fit after the same nuisance projection. Conditional scans add the other principal pair to N and scan within ±0.16 µHz of the target. No physical amplitude ratio or phase constraint links the two principal components. As a nuisance sensitivity check, their joint amplitudes without N₂/K₂ control are 4.63 and 1.82 × 10⁻¹⁸. Scaled least-squares and UTC-day-deletion covariances quantify the joint coefficient uncertainties (Extended Data Table 4 and Extended Data Fig. 9). Synthetic injection curves contain only the fitted principal sinusoidal waveform evaluated at the measured times, with no added random noise.

### Compensation sensitivity and template correlation

Compensation tests subtract a fixed fitted donor waveform and re-estimate the target with the same nuisance terms. Re-fitting both principal pairs after subtraction is an algebraic control: the target is necessarily unchanged. Pure-injection peaks define the candidate sidelobes. The compensation operator, selection rule, template correlations and coefficient-correlation matrices are detailed in Supplementary Methods SM7 (Extended Data Figs. 8–10).

Identification of the S₂-frequency contribution does not by itself assign its entire amplitude to the astronomical tide: a laboratory variation at exactly 12 h occupies the same frequency. Environmental and daily-term checks are described above.


## Author contributions

Jian-Wei Pan planned and directed the study and contributed to manuscript writing. Hai-Feng Jiang designed and coordinated the optical-clock comparison and organized its implementation. Qiang Zhang designed and coordinated the comparison experiment. Lei Hou coordinated the remote frequency comparison and was responsible for the optical frequency combs at both stations. Xiang-Pei Liu designed and coordinated the Sr-clock comparison and evaluated its gravitational redshift. Qi Shen designed the optical-frequency-comb and clock-comparison experimental schemes. Sheng-Kai Liao, Juan Yin and Cheng-Zhi Peng contributed to discussions of the experimental design and planning.

Han-Ning Dai was responsible for the overall Sr-clock design. Xiang Zhang operated and maintained Sr1 and analysed the Sr-clock data. Jia-Hao Zhang and Long-Fei Liao operated and maintained the Sr clock. Xiao Jiang and Yu-Ao Chen were responsible for the Sr-clock system. Yu-Chen Zhang was responsible for the link between the Sr1 ultrastable laser and the frequency comb and for height measurements in Shanghai. De-Quan Kong maintained the U1 ultrastable laser. Xing-Yang Cui constructed and maintained the Sr-clock laser servo systems; Ping Xu constructed and maintained its ultrastable clock-laser system; Peng Liu constructed and maintained the atomic-physics system; and Jie Li constructed and maintained its electronics. Hua-Qing Zhang optimized and modified the Sr-clock laser output.

Zhuan-Xian Xiong and Baolong Lyu were responsible for the overall Yb-clock system. Qiang Zhu constructed the Yb-clock optical system, designed its electronics and analysed data. Bing Wang constructed the optical system and operated and maintained the Yb clock; Ling-Xiang He operated and maintained the Yb clock. De-Zhi Xiong performed simulations and analysis of the Yb-clock blackbody-radiation shift and ultrastable-cavity vibrations. Baolong Lyu also performed theoretical analysis and data processing for the AC Stark-shift uncertainty.

Fa-Xi Chen was responsible for the fibre link, and Li-Bo Li maintained it. Wen-Xuan Song operated the Shanghai optical frequency comb and acquired and processed data. Jian-Yu Guan was responsible for the optical frequency combs and comparison-data acquisition and processing. Shao-Mao Wang was responsible for the 1,550-nm ultrastable laser used for frequency transfer in the local frequency-comb system. Youchao Xie, Lei Wang and Wen-Bin Shen evaluated the gravitational potentials in Wuhan and Shanghai. Yu-Ao Chen also processed data.

Lei Hou, Wen-Xuan Song, Jian-Yu Guan, Han-Ning Dai, Qiang Zhang, Yu-Ao Chen, Hai-Feng Jiang and Jian-Wei Pan contributed to manuscript writing.


## References

1. Chou, C. W., Hume, D. B., Rosenband, T. & Wineland, D. J. Optical clocks and relativity. *Science* **329**, 1630–1633 (2010). <https://doi.org/10.1126/science.1192720>
2. Arnold, K. J. et al. Lu$^+$ optical frequency references with accuracy verified at the 19th digit. *Nature* **658**, 60–64 (2026). <https://doi.org/10.1038/s41586-026-11072-8>
3. Lisdat, C. et al. A clock network for geodesy and fundamental science. *Nat. Commun.* **7**, 12443 (2016). <https://doi.org/10.1038/ncomms12443>
4. Shen, Q. et al. Free-space dissemination of time and frequency with $10^{-19}$ instability over 113 km. *Nature* **610**, 661–666 (2022). <https://doi.org/10.1038/s41586-022-05228-5>
5. Caldwell, E. D. et al. Quantum-limited optical time transfer for future geosynchronous links. *Nature* **618**, 721–726 (2023). <https://doi.org/10.1038/s41586-023-06032-5>
6. Kómár, P. et al. A quantum network of clocks. *Nat. Phys.* **10**, 582–587 (2014). <https://doi.org/10.1038/nphys3000>
7. Nichol, B. C. et al. An elementary quantum network of entangled optical atomic clocks. *Nature* **609**, 689–694 (2022). <https://doi.org/10.1038/s41586-022-05088-z>
8. McGrew, W. F. et al. Atomic clock performance enabling geodesy below the centimetre level. *Nature* **564**, 87–90 (2018). <https://doi.org/10.1038/s41586-018-0738-2>
9. Bothwell, T. et al. Resolving the gravitational redshift across a millimetre-scale atomic sample. *Nature* **602**, 420–424 (2022). <https://doi.org/10.1038/s41586-021-04349-7>
10. Grotti, J. et al. Geodesy and metrology with a transportable optical clock. *Nat. Phys.* **14**, 437–441 (2018). <https://doi.org/10.1038/s41567-017-0042-3>
11. Tapley, B. D., Bettadpur, S., Ries, J. C., Thompson, P. F. & Watkins, M. M. GRACE measurements of mass variability in the Earth system. *Science* **305**, 503–505 (2004). <https://doi.org/10.1126/science.1099192>
12. Boulder Atomic Clock Optical Network (BACON) Collaboration. Frequency ratio measurements at 18-digit accuracy using an optical clock network. *Nature* **591**, 564–569 (2021). <https://doi.org/10.1038/s41586-021-03253-4>
13. Zheng, X., Dolde, J., Lochab, V., Merriman, B. N., Li, H. & Kolkowitz, S. Differential clock comparisons with a multiplexed optical lattice clock. *Nature* **602**, 425–430 (2022). <https://doi.org/10.1038/s41586-021-04344-y>
14. Rymer, H. & Brown, G. Gravity changes as a precursor to volcanic eruption at Poás volcano, Costa Rica. *Nature* **342**, 902–905 (1989). <https://doi.org/10.1038/342902a0>
15. Lynett, P. et al. Diverse tsunamigenesis triggered by the Hunga Tonga-Hunga Ha’apai eruption. *Nature* **609**, 728–733 (2022). <https://doi.org/10.1038/s41586-022-05170-6>
16. Rodell, M. et al. Emerging trends in global freshwater availability. *Nature* **557**, 651–659 (2018). <https://doi.org/10.1038/s41586-018-0123-1>
17. Jia, Z.-P. et al. Improved systematic evaluation of a strontium optical clock with uncertainty below $1\times10^{-18}$. *Metrologia* **63**, 025002 (2026). <https://doi.org/10.1088/1681-7575/ae449e>
18. Zhu, Q. et al. Ytterbium lattice clock with systematic uncertainty of $1.3\times10^{-18}$ and instability at the $10^{-19}$ level. *Metrologia* **63**, 065002 (2026). <https://doi.org/10.1088/1681-7575/aeb809>
19. Chen, F.-X. et al. $10^{-21}$-Level optical frequency dissemination over 2067 km of noise-loaded field-deployed fiber network. *Light Sci. Appl.* **15**, 276 (2026). <https://doi.org/10.1038/s41377-026-02299-1>
20. Petit, G. & Luzum, B. (eds) *IERS Conventions (2010)*. IERS Technical Note **36** (2010). <https://iers-conventions.obspm.fr/content/tn36.pdf>
21. Lyard, F. H., Allain, D. J., Cancet, M., Carrère, L. & Picot, N. FES2014 global ocean tide atlas: design and performance. *Ocean Sci.* **17**, 615–649 (2021). <https://doi.org/10.5194/os-17-615-2021>
22. CNES. *FES2022 (Finite Element Solution) Tidal model (Version 2024)* [Data set] (2024). <https://doi.org/10.24400/527896/A01-2024.004>
23. Farrell, W. E. Deformation of the Earth by surface loads. *Rev. Geophys.* **10**, 761–797 (1972). <https://doi.org/10.1029/RG010i003p00761>
24. Schröder, S., Stellmer, S. & Kusche, J. Potential and scientific requirements of optical clock networks for validating satellite-derived time-variable gravity data. *Geophys. J. Int.* **226**, 764–779 (2021). <https://doi.org/10.1093/gji/ggab132>
25. Hou, L. et al. Yb/Sr optical clock comparison at $2.2\times10^{-18}$ uncertainty over a 1350-km fiber link. Preprint at <https://arxiv.org/abs/2610.34250v1> (2026).
26. Stahl, K. et al. Optical clock network tracks tidal variations of the gravity potential. Preprint at <https://arxiv.org/abs/2610.39635v1> (2026).
27. Schioppo, M. et al. Comparing ultrastable lasers at $7\times10^{-17}$ fractional frequency instability through a 2220 km optical fibre network. *Nat. Commun.* **13**, 212 (2022). <https://doi.org/10.1038/s41467-021-27884-3>
28. Riley, W. J. *Handbook of Frequency Stability Analysis*. NIST Special Publication **1065** (2008). <https://doi.org/10.6028/NIST.SP.1065>
29. Han, D. & Wahr, J. The viscoelastic relaxation of a realistically stratified earth, and a further analysis of postglacial rebound. *Geophys. J. Int.* **120**, 287–311 (1995). <https://doi.org/10.1111/j.1365-246x.1995.tb01819.x>
30. Sutterley, T. C. *gravity-toolkit: Python tools for working with time-variable gravity fields*. <https://github.com/polargeodesy/gravity-toolkit>.
31. Birge, R. T. The calculation of errors by the method of least squares. *Phys. Rev.* **40**, 207–227 (1932). <https://doi.org/10.1103/PhysRev.40.207>
32. Hersbach, H. et al. The ERA5 global reanalysis. *Q. J. R. Meteorol. Soc.* **146**, 1999–2049 (2020). <https://doi.org/10.1002/qj.3803>



\clearpage

![Figure 1](figures/figure1.png){width=100%}

**Fig. 1 | The predicted tide on a coastal–inland baseline.** **a,** The Sr clock in Shanghai, the Yb clock in Wuhan and the fibre link through Hefei. The dashed line marks the 692-km distance between the clocks. Land colours show the predicted M₂ tidal potential sensed by a clock, including the solid Earth tide and ocean loading, expressed as fractional frequency. The inset shows the ocean-loading contribution around Shanghai; sea colours show the FES2022 M₂ ocean-tide amplitude. **b,** Predicted differential M₂ phasors of the solid Earth tide, the ocean-loading potential and their sum, referenced to the solid Earth tide. **c,** Filtered samples and observation hours in the five campaigns from September 2025 to August 2026. **d,** Relative astronomical phase of S₂ and M₂, including the nodal correction, at the same samples. The short campaigns cover limited relative phases, whereas the summer campaign covers the full cycle as the lunar tide moves through the solar day.

\clearpage

![Figure 2](figures/figure2.png){width=100%}

**Fig. 2 | The lunar tide in the summer record.** **a,** Three-hour averages of the June–August 2026 frequency ratio after subtracting fitted segment offsets and the fitted near-12-h and diurnal tidal groups (blue), with the lunar model (red). The measurement-time axis compresses gaps longer than 6 h; grey lines mark their removal. White frequency noise alone corresponds to a scatter of approximately 5 × 10⁻¹⁸ for a 3-h average. **b,** The same data folded at the model M₂ phase in 30° bins, with the lunar model (M₂ and N₂) folded using identical sampling. Error bars are day-by-day jackknife uncertainties conditional on the fitted non-lunar terms, which are held fixed during resampling. No empirical daily terms are fitted. Extended Data Fig. 4 provides a complementary view with the actual calendar-time axis.

\clearpage

![Figure 3](figures/amplitude/figure3.png){width=100%}

**Fig. 3 | Amplitude, phase and frequency of the tidal response.** All panels use the auxiliary reduction into 3,299 non-overlapping 600-s means, retaining 54 segment constants. **a,** Complete-template response and jointly fitted lunar (M₂, N₂) and neighbouring semidiurnal (S₂, K₂) responses, using the period-dependent noise weights. Error bars are one statistical standard error, the larger of scaled least squares and UTC-day-deletion jackknife errors. The complete-template and grouped coefficients come from separate fits to the same observations. **b,** Lunar in-phase and quadrature coefficients; the cross marks $(1,0)$. Contours have radii one and two in the scaled-least-squares covariance. The marginal working errors are 0.13 and 0.20; the scaled-least-squares quadrature error is 0.127. **c,** Equivalent-height sinusoidal peak-amplitude spectra over 21–24.5 μHz, before and after subtracting the fixed unit-amplitude physical prediction from the observations. The scan uses equal weights and projects both data and trial sinusoids against the segment constants. Both vertical axes are linear and start at zero. Equivalent-height amplitude on the left and fractional-frequency amplitude on the right obey $A_{h,\mathrm{cm}}=100c^2A_y/g_0$, with $g_0=9.80665\ \mathrm{m/s^2}$. Markers indicate the prescribed M₂ and S₂ frequencies. The nominal Rayleigh scale is 0.03275 μHz and the basic grid step is 0.002729 μHz; both are annotated. Sampling and conditional scans are shown in Extended Data Fig. 7. The primary triangular-filter results are presented with their methods in Extended Data Fig. 11.

\clearpage

![Figure 4](figures/figure4.png){width=100%}

**Fig. 4 | Robustness of the lunar amplitude.** **a,** Lunar amplitude for the main fit (filled diamond and shaded uncertainty band), alternative offset definitions, daily terms represented by air-temperature measurements or fitted 24-h and 12-h sinusoids, the summer campaign alone, omission of each campaign, and retention of segment ends or transient excursions. The thin bar below the main result is the 95% interval from resampling operating groups. These estimates share observations. The grey interval obtained without the summer campaign shows the loss of information that separates the tidal groups. **b,** Change in the lunar amplitude caused by a 24-h or 12-h sinusoid of fractional-frequency amplitude 10⁻¹⁸, either with one phase common to all campaigns or with the combination of independent campaign phases that produces the largest change. The dashed line marks the uncertainty of the main estimate. The vertical axis is linear.



\clearpage

![Extended Data Figure 1](figures/ed1.png){width=100%}

**Extended Data Fig. 1 | Tidal records in all campaigns.** Three-hour averages of the filtered frequency ratio after subtraction of fitted segment offsets (blue), with the tidal model (red). Measurement-time axes compress gaps longer than 6 h, marked by vertical lines; gaps longer than 5 days are labelled. The vertical range is ±15 × 10⁻¹⁸, and triangles mark values outside this range. The actual calendar-time axis is retained for the April campaign in Extended Data Fig. 4a.

\clearpage

![Extended Data Figure 2](figures/ed2.png){width=100%}

**Extended Data Fig. 2 | Folds by tidal phase and local time.** **a,** All observations folded at the M₂ phase after subtracting fitted segment offsets and all tidal constituents except M₂ from the full-model fit. Points are means in 30° bins with day-by-day jackknife uncertainties; the curve is the M₂ model. These phase-bin uncertainties are conditional on the fitted terms removed before folding, which are held fixed. **b,** Tidally corrected residuals folded by local time in 2-h bins for summer, May (light symbols), the other three campaigns, and summer observations overlapping the temperature record from 28 June to 7 July (open circles). Error bars are day-by-day jackknife uncertainties; bins covering fewer than three days are omitted. The dashed curve is the mean daily blackbody-radiation shift computed from the Sr chamber temperature from 28 June to 7 July 2026 after removing a 24-h running mean and excluding the temperature transient on 30 June. The real-time correction removes this chamber-temperature shift from the recorded frequency ratio.

\clearpage

![Extended Data Figure 3](figures/ed3.png){width=100%}

**Extended Data Fig. 3 | Campaign-resolved tidal amplitudes.** **a,** Full-model and semidiurnal amplitude factors for each campaign and the combined observations, fitted with segment offsets. Combined-data estimates also include the lunar group and the solid Earth tide alone. Short campaigns constrain the semidiurnal band as a whole; the joint fit separates the lunar group. **b,** Diurnal amplitude fitted jointly with the semidiurnal band in a two-band fit; the combined estimate is 0.36 ± 0.50. The arrow marks an uncertainty extending beyond the plotted range. Error bars represent one standard deviation, calibrated by residual resampling for the full model, semidiurnal band and lunar group; for the diurnal band and solid Earth tide alone they are the larger of the scaled least-squares and day-by-day jackknife uncertainties. Thin lines in the combined-data rows show 95% intervals from resampling operating groups, or segments for the lunar group.

\clearpage

![Extended Data Figure 4](figures/ed4.png){width=100%}

**Extended Data Fig. 4 | April campaign in calendar time and frequency.** **a,** Frequency-ratio observations after the 1,200-s triangular filter and removal of fitted segment offsets, their 3-h averages, and predictions with and without ocean loading. The horizontal axis retains actual calendar dates and gaps (local time, UTC+8). **b,** Sinusoidal power before and after subtracting the model, expressed as amplitude squared divided by two on a linear vertical axis, in units of 10⁻³⁶. The dashed curve is the 99% level at each frequency; the dotted line is the 99% level for the maximum over 15–50 μHz, both obtained from 1,000 resampled residual series. The four-day record combines K₁, P₁ and O₁ into a diurnal band and M₂, S₂ and N₂ into a semidiurnal band. Power below 8 μHz exceeds the displayed range.

\clearpage

![Extended Data Figure 5](figures/ed5.png){width=100%}

**Extended Data Fig. 5 | Transient excursions and sample exclusion.** **a,** Sixty-second averages around the excursion on 7 July 2026; red points indicate the 1-s samples excluded by the criterion in Methods. **b,** Distribution of deviations of 300-s means from a running median over ±30 min, divided by the robust standard deviation within each segment. The dashed line marks the threshold of six. The count axis is logarithmic. **c,** Observation time excluded in each campaign.

\clearpage

![Extended Data Figure 6](figures/ed6.png){width=100%}

**Extended Data Fig. 6 | Radial-displacement validation of the loading convolution.** **a,b,** Amplitude ratios (**a**) and phase differences (**b**) between radial displacements calculated with the loading Green's function and the FES2022 load-tide grid in the centre-of-mass frame, at Shanghai and Wuhan, for eight constituents. Methods discusses the S₂ discrepancy.

\clearpage

![Extended Data Figure 7](figures/ed7.png){width=100%}

**Extended Data Fig. 7 | Local spectra and sampling-response checks on the auxiliary 600-s non-overlapping reduction.** All panels retain 3,299 recorded bin-centre times and the gaps between them, use equal weights and 54 segment constants, and share a linear ordinate and identical density normalization. **a,** The existing observed spectrum, reproduced from the frozen observations, and the stored spectrum after subtraction of the fixed unit physical prediction. **b,** Spectra before subtraction, after subtracting the fitted M₂ waveform, after subtracting the fitted S₂ waveform, and after subtracting both. The two waveforms are obtained from one simultaneous freely phased fit with N₂ and K₂ controlled by their own sine–cosine pairs. **c,** Local scans around M₂ conditioned on S₂, and around S₂ conditioned on M₂; N₂ and K₂ remain controlled. Both the response and the scanned sine–cosine pair undergo the same nuisance projection. The grey curve is the baseline from b. **d,** Deterministic M₂-only, S₂-only and combined fitted-waveform injections through the same sampling and projection operator, compared with the observed spectrum. Individual injected powers need not sum to the combined power because of interference. Dotted vertical lines mark N₂, M₂, S₂ and K₂, in ascending frequency. The ordinate is the nominal-600-s least-squares density defined in Methods, not the amplitude²/2 power in the main triangular-filter analysis. No observations are added in gaps, and these auxiliary estimates do not replace the main lunar-group response.


\clearpage

![Extended Data Figure 8](figures/ed8.png){width=100%}

**Extended Data Fig. 8 | Compensation sensitivity on the auxiliary 600-s record.** a,c,e, Subtracting a scaled M₂ waveform and re-estimating S₂; b,d,f, the reverse. a,b, Target amplitude; c,d, absolute phase; e,f, nominal 600-s least-squares density. Solid curves use donor waveforms from the joint fit; dotted curves use single-frequency donor fits. All target-only fits retain segment offsets and free N₂/K₂ pairs. Dashed grey curves also control the donor pair and are invariant by construction. The power improvement for these curves is conditional on the donor and therefore has a different baseline from the target-only curves. λ = 1 denotes subtraction of the selected estimated waveform. Curves describe deterministic sensitivity conditional on the fitted waveforms. Amplitude and density panels share their respective vertical scales across directions, and density axes are linear with zero baselines.


\clearpage

![Extended Data Figure 9](figures/ed9.png){width=100%}

**Extended Data Fig. 9 | Harmonic geometry and joint-coefficient correlations on the auxiliary 600-s record.** a, Correlations of the M₂ and S₂ cosine and sine design columns after projecting out 54 segment constants and free N₂/K₂ pairs. b, Normalized lag correlations of the fitted templates, evaluated on the original timestamps without interpolating missing observations; these describe template similarity, not propagation delay. c,d, Correlations between the four coefficients estimated jointly, obtained by normalizing the existing scaled least-squares covariance (c) and UTC-day delete-one jackknife covariance (d). Coefficient order is M₂ cosine, M₂ sine, S₂ cosine and S₂ sine. The three matrices use the same −1 to +1 colour scale. Joint-coefficient covariance describes uncertainty coupling and is distinct from the design-column correlations in a. The 43 UTC days define deletion blocks for the jackknife, not 43 independent measurements. The joint correlations complement the conditional and subtraction evidence for the detected frequency components.

\clearpage

![Extended Data Figure 10](figures/ed10.png){width=100%}

**Extended Data Fig. 10 | Sampling aliases and compensation response.** a,b, Observed spectra, spectra after subtraction of a joint-fit donor, and spectra of that donor alone on the identical timestamps and nuisance projection. Vertical markers identify three off-centre local maxima selected from the injection. c,d, Observed power at those fixed candidate frequencies as the compensation factor varies. The curves equal the quadratic responses predicted from the complex coefficient subtraction; this agreement is an operator check rather than an independent alias attribution. All density axes are linear and share scales within rows.

\clearpage

![Extended Data Figure 11](figures/primary_response_methods.png){width=100%}

**Extended Data Fig. 11 | Primary grouped responses and full-record harmonic power.** **a,** Amplitude factors for the full model and the semidiurnal band, each fitted with one amplitude, and for the lunar (M₂, N₂), near-12-h (S₂, K₂) and diurnal groups fitted jointly. All fits include segment offsets and omit empirical daily terms. Error bars are one standard deviation, calibrated by residual resampling for the full model, semidiurnal band and lunar group; for the near-12-h and diurnal groups, the larger of the scaled least-squares and day-by-day jackknife uncertainties is used. The dashed line denotes the prediction, *A* = 1. **b,** Joint covariance contours at radii one and two for the lunar and near-12-h amplitudes, using the least-squares correlation and scaling the covariance to the quoted marginal uncertainties. These radii do not denote joint 68% and 95% confidence regions. The cross denotes the model prediction. **c,** Sinusoidal power of the full record after projection of segment offsets, before and after subtracting the fitted full model. Power is the squared sinusoidal amplitude divided by two, plotted on a linear vertical axis in units of 10⁻³⁶; it is not a power spectral density per unit frequency. The dotted line is the 99% quantile of the maximum power over 5–40 μHz from 200 resampled residual series.

\clearpage

\clearpage

**Extended Data Table 1 | Noise-model simulations of the alternative processing.** Bias and coverage of nominal 95% intervals based on the largest of the least-squares, delete-day and delete-period standard errors. *T* denotes the full template without daily terms, and *L* the lunar group with daily terms, using the ten-day calendar-baseline design in Extended Data Table 5 and the actual observation times. Gaussian scenarios contain 1,024 simulations; Student-*t* and moving-average scenarios contain 4,096. OU denotes Ornstein–Uhlenbeck noise and MA(1) a first-order moving-average process.

| Noise model | Bias (*T*) | Coverage (*T*), % | Bias (*L*) | Coverage (*L*), % |
|:--|--:|--:|--:|--:|
| White | −0.000 | 96.7 | −0.001 | 98.3 |
| White + OU, 1 h | −0.007 | 94.5 | −0.002 | 96.9 |
| White + OU, 12 h | −0.002 | 96.1 | +0.031 | 98.8 |
| White + OU, 3 d | +0.003 | 95.9 | +0.004 | 99.8 |
| White + period constants | +0.001 | 96.0 | +0.004 | 98.3 |
| Student-*t*₇ MA(1) | +0.002 | 98.3 | +0.004 | 98.2 |
| Student-*t*₅ MA(1) | +0.001 | 98.9 | +0.003 | 98.3 |
| Student-*t*₇ MA(1) + OU | +0.001 | 97.2 | +0.005 | 98.5 |

\clearpage

**Extended Data Table 2 | Injection tests of the main estimator.** Lunar amplitudes fitted with segment offsets and no empirical daily terms to resampled residuals plus either the full tidal model (*A*true = 1) or the model without the lunar group (*A*true = 0). The four daily-disturbance scenarios are defined in Methods, with 300 realizations per row. Bias and standard deviation describe the fitted amplitude. The median standard error is that computed within each realization, before the final residual-based calibration. Coverage is the fraction of intervals containing the injected amplitude; the accompanying 95% binomial interval refers to one-standard-error coverage. The last column gives the fraction with *A* > 3σ.

| Disturbance | *A*true | Bias | s.d. | Median error | 1σ coverage | 95% binomial interval | 1.96σ coverage | *A* > 3σ |
|:--|--:|--:|--:|--:|--:|:--|--:|--:|
| None | 0 | −0.026 | 0.134 | 0.135 | 0.70 | 0.645–0.751 | 0.94 | 0.003 |
| None | 1 | −0.003 | 0.135 | 0.137 | 0.71 | 0.659–0.764 | 0.94 | 1.000 |
| 24 h, air-temperature phase | 0 | −0.013 | 0.141 | 0.136 | 0.61 | 0.549–0.662 | 0.93 | 0.000 |
| 24 h, air-temperature phase | 1 | −0.007 | 0.145 | 0.138 | 0.64 | 0.579–0.691 | 0.94 | 1.000 |
| Common 24 h + 12 h | 0 | −0.013 | 0.148 | 0.140 | 0.63 | 0.573–0.685 | 0.90 | 0.000 |
| Common 24 h + 12 h | 1 | −0.024 | 0.148 | 0.139 | 0.60 | 0.546–0.659 | 0.92 | 1.000 |
| Summer 24 h + 12 h | 0 | −0.021 | 0.138 | 0.140 | 0.67 | 0.610–0.720 | 0.95 | 0.000 |
| Summer 24 h + 12 h | 1 | −0.016 | 0.150 | 0.137 | 0.59 | 0.529–0.643 | 0.92 | 1.000 |

\clearpage

**Extended Data Table 3 | Daily terms and campaign-specific tidal amplitudes.** Amplitude and local time of maximum of the 24-h term, and amplitude of the 12-h term, fitted jointly with the full tidal model within each campaign. Daily amplitudes are expressed in 10⁻¹⁸. Their uncertainties are the larger of the scaled least-squares and day-by-day jackknife values; uncertainties in the time of maximum are jackknife estimates. Weak sinusoidal amplitudes are biased positive. The full-template amplitude *A*, fitted without daily terms, and its residual-calibrated uncertainty are those in Extended Data Fig. 3a. The last column gives the lunar amplitude fitted independently to each campaign with the main estimator.

| Campaign | Days | 24-h amplitude | 24-h maximum, h | 12-h amplitude | *A* | *A*lunar |
|:--|--:|:--|:--|:--|:--|:--|
| Sep–Oct 2025 | 4 | 5.1 ± 2.7 | 20.7 ± 5.6 | 5.0 ± 9.7 | 1.28 ± 0.31 | 0.04 ± 0.74 |
| Jan 2026 | 4 | 2.1 ± 3.0 | 17.2 ± 3.9 | 4.1 ± 1.8 | 1.27 ± 0.30 | 1.36 ± 0.37 |
| Apr 2026 | 5 | 2.9 ± 2.2 | 1.9 ± 1.4 | 1.0 ± 3.9 | 0.91 ± 0.13 | 0.66 ± 0.42 |
| May 2026 | 4 | 5.2 ± 3.3 | 3.8 ± 2.4 | 3.1 ± 2.6 | 0.97 ± 0.18 | 0.28 ± 0.68 |
| Jun–Aug 2026 | 22 | 2.8 ± 1.3 | 15.8 ± 1.5 | 0.6 ± 0.7 | 0.67 ± 0.18 | 0.87 ± 0.18 |


\clearpage

**Extended Data Table 4 | Free sinusoidal coefficients in the auxiliary reduction.** Joint M₂ and S₂ cosine–sine coefficients, after controlling 54 segment constants and freely phased N₂ and K₂ terms. Coefficients and standard errors are in units of $10^{-18}$. Phases refer to 6 September 2025, 16:05 UTC. Scaled least-squares errors use the residual variance; UTC-day jackknife errors delete each of the 43 observed dates and refit all coefficients. The full covariance matrices are retained with the analysis. These errors describe this auxiliary harmonic model and are not substituted for the primary lunar-group uncertainty.

| Coefficient | Estimate | Scaled LS standard error | UTC-day jackknife standard error |
|:--|--:|--:|--:|
| M₂ cosine | -1.667 | 0.688 | 0.880 |
| M₂ sine | -4.185 | 0.679 | 0.635 |
| S₂ cosine | -0.460 | 0.738 | 0.701 |
| S₂ sine | -1.866 | 0.750 | 1.043 |


\clearpage

**Extended Data Table 5 | Related tidal estimates.** These estimates share observations and are not combined. The last column specifies each uncertainty definition. Applying the segment-wise estimator of Hou et al.^25^ to the summer record with the tidal model used here gives 0.78 ± 0.19.

| Analysis | Data and model | Amplitude factor *A* | Uncertainty |
|:--|:--|:--|:--|
| Hou et al.^25^ | Summer; 16 segments; their tidal model and segment-wise correlation | 0.87(15) | Reported weighted statistical error |
| Main analysis | 54 segments; lunar group; segment offsets; astronomical ephemerides | 0.97 ± 0.14 | Calibrated by residual resampling |
| Full-template analysis | Same observations; full template; segment offsets | 0.90 ± 0.12 | Calibrated by residual resampling |
| Alternative processing | 2026 observations; 600-s means; ten-day calendar baselines; full template | 0.88 ± 0.10 | Largest of least-squares, delete-day and delete-period standard errors |
| Alternative processing | Same observations and baselines; lunar group; daily terms in each ten-day block | 0.89 ± 0.28 | Largest of least-squares, delete-day and delete-period standard errors |


\clearpage

**Extended Data Table 6 | Template-response signal-to-noise ratios.** The first four rows use the non-overlapping full-template or three-group fits; their empirical errors are the larger of scaled-least-squares and UTC-day-jackknife errors. The final two rows use the equal-weight complete solid-Earth/loading fit with UTC-day-jackknife errors. The common-white-noise calculation retains each estimator and uses $\alpha=5.4\times10^{-16}\sqrt{\mathrm{s}}$. The dimensionless factor $\eta_i$ is defined in Methods.

| Fit and coefficient | $\hat A_i\pm u_i$ | $\rho_i$ | $\rho_{i,\mathrm{white}}$ | $\eta_i$ |
|:--|:--|--:|--:|--:|
| Full tide, one template | $0.955\pm0.108$ | 8.83 | 9.79 | 0.865 |
| Lunar group, three-group fit | $1.000\pm0.132$ | 7.58 | 7.50 | 0.840 |
| Near-12-h group (S₂, K₂) | $0.925\pm0.365$ | 2.54 | 3.14 | 0.856 |
| Diurnal group, three-group fit | $0.579\pm0.538$ | 1.08 | 1.55 | 0.740 |
| Solid Earth, two-template fit | $1.082\pm0.322$ | 3.36 | 5.81 | 0.611 |
| Ocean loading, two-template fit | $0.486\pm0.544$ | 0.89 | 1.17 | 0.612 |
