# Replacement captions and Methods text

Prepared for the equivalent-height amplitude update. This file proposes text only; it does not modify the manuscript. Numerical results and panel labels must be checked against the finished figures before incorporation.

## Extended Data captions

**Extended Data Fig. 7 | Amplitude spectra and sampling-response checks.** All panels use the auxiliary non-overlapping reduction, retain the 3,299 recorded bin-centre times and their gaps, and use equal weights and 54 segment constants. Ordinates give fitted equivalent-height peak amplitude in cm on linear scales. **a,** Observed amplitude spectrum and spectrum after subtraction of the fixed unit physical prediction, using the same scans as Fig. 3c. **b,** Spectra before subtraction and after subtraction of the fitted M₂, S₂ or both waveforms. The waveforms come from one simultaneous freely phased fit controlling N₂ and K₂. **c,** Local M₂ scans conditioned on S₂ and S₂ scans conditioned on M₂, with N₂ and K₂ controlled throughout; grey denotes the baseline in b. The response and trial sine–cosine pair undergo the same nuisance projection. **d,** M₂-only, S₂-only and combined fitted-waveform injections through the actual sampling and nuisance projection, compared with the observed spectrum. The amplitude of the combined waveform is obtained from its fitted coefficient vector; individual amplitudes generally do not add. Dotted lines mark N₂, M₂, S₂ and K₂ in ascending frequency. Panel a controls segment offsets only; b–d additionally control N₂ and K₂. No observations are inserted into gaps. Full-range axes retain the large near-nuisance responses; insets labelled “0–6 cm zoom” show the smaller features. At exact controlled frequencies the trial pair is not separately identifiable and its amplitude is undefined. Large nearby amplitudes reflect weak identifiability after nuisance projection and are not interpreted as additional tidal peaks.

**Extended Data Fig. 8 | Amplitude and phase sensitivity to compensation.** **a,c,** Subtracting a scaled M₂ waveform and re-estimating S₂; **b,d,** the reverse. **a,b,** Equivalent-height peak amplitude in cm; **c,d,** phase relative to the common time origin. Solid curves use donor waveforms from the joint fit; dotted curves use single-frequency donor fits. Target-only fits retain segment offsets and free N₂/K₂ pairs. Dashed grey curves additionally retain the donor pair and are invariant by construction. The factor λ = 1 denotes subtraction of the selected fitted waveform. These curves describe deterministic sensitivity conditional on that waveform. Amplitude axes are linear, start at zero and share a scale across the two directions.

**Extended Data Fig. 9 | Harmonic geometry and joint-coefficient correlations on the auxiliary 600-s record.** **a,** Correlations of the M₂ and S₂ cosine and sine design columns after projecting out 54 segment constants and free N₂/K₂ pairs. **b,** Normalized lag correlations of the fitted templates, evaluated on the original timestamps without interpolating missing observations; these describe template similarity, not propagation delay. **c,d,** Correlations between the four coefficients estimated jointly, obtained by normalizing the existing scaled least-squares covariance (c) and UTC-day delete-one jackknife covariance (d). Coefficient order is M₂ cosine, M₂ sine, S₂ cosine and S₂ sine. The three matrices use the same −1 to +1 colour scale. Joint-coefficient covariance describes uncertainty coupling and is distinct from the design-column correlations in a. The 43 UTC days define deletion blocks for the jackknife, not 43 independent measurements. The joint correlations complement the conditional and subtraction evidence for the detected frequency components.

**Extended Data Fig. 10 | Sampling aliases and amplitude response to compensation.** **a,b,** Equivalent-height amplitude spectra of the observations, observations after subtraction of the jointly fitted donor waveform, and that donor alone, using identical timestamps and nuisance projection. Vertical markers retain the three off-centre candidate frequencies selected from local maxima of the original pure-injection least-squares power. They are fixed diagnostic frequencies and need not be maxima of the amplitude spectrum. **c,d,** Observed equivalent-height amplitude at those frequencies as the compensation factor varies. The fitted coefficient vector varies linearly with compensation; its norm gives the square root of a quadratic expression. Agreement with this response checks the processing operator and does not independently establish that an observed feature originates entirely from aliasing. All amplitude axes are linear, start at zero and share scales within rows. Panels a,b retain the full amplitude range and include insets labelled “0–6 cm zoom”. The large responses close to the controlled N₂ and K₂ frequencies arise from weak identifiability of the trial pair and are not interpreted as additional tidal peaks.

## Auxiliary Methods: replace the density-definition paragraph

For a nuisance matrix $N$, we form an orthonormal basis $Q$ and apply $R_N=I-QQ^\mathsf{T}$ to both the observations and each trial cosine–sine pair $X_f$. At each frequency we fit

$$
\hat{\boldsymbol\beta}_f=(R_NX_f)^+R_Ny.
$$

With $y$ expressed numerically in units of $10^{-18}$, the equivalent-height peak amplitude is

$$
A_{h,\mathrm{cm}}(f)=\frac{c^2}{g_0}\,10^{-16}
\sqrt{\hat\beta_{f,\cos}^{\,2}+\hat\beta_{f,\sin}^{\,2}},
$$

where $c=299,792,458\ \mathrm{m\,s^{-1}}$ and $g_0=9.80665\ \mathrm{m\,s^{-2}}$, as in Fig. 3c. This is a fitted sinusoidal peak amplitude, not an amplitude spectral density. Extended Data Fig. 7a uses the Fig. 3c scans with segment constants only. Extended Data Fig. 7b–d additionally control freely phased N₂ and K₂, with conditional scans also controlling the other principal constituent. Phases refer to 6 September 2025, 16:05 UTC, the first stored bin centre.

The projected Gram matrix $G_f=(R_NX_f)^\mathsf{T}(R_NX_f)$ measures the information retained for a unit-amplitude trial pair. Near a frequency already controlled in $N$, the projected pair becomes small, so a modest residual response can require large fitted coefficients. At exact coincidence the target pair lies within the nuisance space and its separate amplitude is undefined; these grid entries are retained in the output with an identifiability flag and are not plotted as numerical amplitudes. Neighbouring, identifiable fits are retained in full-range panels with explicitly labelled 0–6 cm zoom insets. The former least-squares score was $\Delta\mathrm{RSS}=\hat{\boldsymbol\beta}_f^\mathsf{T}G_f\hat{\boldsymbol\beta}_f$, whereas amplitude is proportional to $\|\hat{\boldsymbol\beta}_f\|$. Because $G_f$ depends on frequency and nuisance projection, taking the square root of the former density is not an amplitude conversion.

Keep the following existing paragraph on joint M₂/S₂ waveforms, the ±0.16 μHz conditional windows and covariance estimates. Its reported joint amplitudes are distinct from frequency-scan maxima and do not change in this update.

## Auxiliary Methods: compensation section opening

Compensation tests subtract a fixed fitted donor waveform and re-estimate the target with the same nuisance terms. Extended Data Fig. 8 shows the resulting equivalent-height amplitude and phase. Re-fitting both principal pairs after subtraction provides an algebraic control: the target coefficients are necessarily unchanged. Extended Data Fig. 10 retains candidate sidelobe frequencies selected from the original pure-injection least-squares power and displays their fitted amplitudes. The compensation operator, candidate-selection rule, template correlations and coefficient-correlation matrices are detailed in Supplementary Methods SM7 (Extended Data Figs. 8–10).

## Supplementary Methods SM7: synchronize two passages

In the paragraph defining amplitude and phase, retain the coefficient-norm and phase definitions; replace the sentences beginning “Target-only incremental improvement” through “Density panels” with:

> Equivalent-height amplitudes use the conversion in “Auxiliary frequency-domain analysis”. Extended Data Fig. 8 displays amplitude and phase; the residual-sum-of-squares diagnostic is retained in the analysis files.

Replace the alias-diagnostics paragraph with:

> For alias diagnostics, we scan 20–25 μHz with spacing $1/(12T_{\rm span})$, where $T_{\rm span}$ is the elapsed observation span. For each donor, we retain the three strongest local maxima of the original pure-injection least-squares power at least $2/T_{\rm span}$ from its own frequency. This selection uses the injection response, not a significance threshold on the observations. At each selected frequency, the fitted coefficient vector obeys $\hat b_f(\lambda)=\hat b_f(0)-\lambda\hat b_{f,D}$. The equivalent-height amplitude is $K\|\hat b_f(0)-\lambda\hat b_{f,D}\|$, where $K=(c^2/g_0)10^{-16}\ \mathrm{cm}$ for the numerical coefficient units used here. Its square is quadratic in λ. Agreement with direct refitting verifies the processing operator; because the coefficient relation is a linear identity, this agreement alone does not establish an exclusively aliased origin for an observed peak. The compensation curves describe deterministic sensitivity conditional on the fitted waveforms.

The previous minima at λ = 0.996 and 1.0445 and reductions of 99.56% and 99.39% refer to the original Gram-metric power. Do not attach them to the new amplitude curves. Retain them, if needed, only in the archived power diagnostic description; any amplitude minima or reductions require the actual new coefficient-norm outputs. No new amplitude percentages are supplied here.


## Verified replacement for the two reported lunar sidelobe reductions

The following may replace the old power percentages and minima in SM7 after the updated figures are incorporated:

> At the retained diagnostic frequencies 22.1016 and 22.6283 μHz, subtraction of the jointly fitted lunar waveform reduces the equivalent-height amplitudes from 3.149 to 0.204 cm and from 3.307 to 0.266 cm, respectively, corresponding to reductions of 93.51% and 91.97%. The amplitude minima occur at compensation factors 0.9974 and 1.0490. These are responses at the selected diagnostic frequencies, conditional on the fitted donor waveform.

Source: `figures/alias_amplitude_summary.json`, generated by the figure agent from the stored cosine/sine coefficients. These replace, rather than relabel, the old Gram-power percentages and minima. Keep the values out of the figure caption if brevity is preferred.

## Implementation condition for the new identifiability wording

The exact-frequency entries must actually be flagged undefined in the output and omitted only as non-identifiable numerical coefficients before using the corresponding sentence above. This is a definition/rank issue, not exclusion of observations or removal of large but identifiable nearby estimates. Preserve the original raw numerical solve in a diagnostic field or archived output for traceability. The full-range and 0–6 cm views must both be present as described.
