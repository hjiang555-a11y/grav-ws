# Tidal potential measured by optical clocks on a coastal-inland baseline

::: affiliations
[Author list, order and affiliation assignments to be confirmed by the authors]

{{AFFILIATIONS}}
:::

## Abstract

Tides alter the gravitational potential and thereby the relative rates of distant clocks.[@ludlow,mehlstaubler] Here we detect tidal changes using a strontium clock in Shanghai and a ytterbium clock in Wuhan, 692 km apart. The 545.9-hour record spans 353 days in 54 interrupted segments. Reducing data and prediction within each segment retains the astronomical phase without joining their frequency levels. The full tidal prediction has a fitted scale of $0.96\pm0.11$ (one statistical standard error). A joint fit with group-internal amplitude ratios and phases fixed gives $1.00\pm0.13$ for M₂+N₂ and $0.93\pm0.36$ for S₂+K₂. The lunar response is supported by the observed amplitude, phase and spectral structure; the neighbouring group is less precisely constrained. These measurements demonstrate tidal potential sensing on a continental optical-clock baseline during interrupted operation.

## Main text

Earth's gravitational potential changes as the Moon and Sun move and as the oceans, atmosphere and solid Earth respond. Measuring these variations provides information about mass redistribution and deformation, and supports consistent height and time references.[@voigt,denker,schroder] Optical clocks make potential differences observable through their relative rates: clocks at different gravitational potentials accumulate time differently.[@ludlow,mehlstaubler] Fibre links connect clocks across hundreds of kilometres and allow repeated measurements between the same endpoints.[@lisdat,riehle]

Laboratory redshift tests and remote clock comparisons have established measurements of static potential differences.[@chou,mcgrew,grotti,takano] Published chronometric-levelling experiments have also calculated the tidal perturbation expected during a comparison.[@takano] Treating that perturbation as the measured signal tests a further capability: can distant clocks detect the Earth's changing potential on hourly timescales? The answer matters both for geophysical measurements and for the time-dependent redshift corrections used in coordinated clock comparisons.[@voigt,dimarcq,lindvall]

Here we address this question with the strontium–ytterbium comparison between coastal Shanghai and inland Wuhan. The observations are interrupted, so the frequency level established during one run need not be known in the next. The astronomical phase, however, remains defined at every actual observation time. We combine the changes recorded within separate segments to estimate the response to a complete tidal prediction. We then ask how much of that response can be assigned to neighbouring semidiurnal groups. The principal lunar tide M₂ repeats every 12.42 h, whereas the principal solar tide S₂ repeats every 12 h. Their changing relative phase makes observations on different dates informative about their separate contributions.

### A coastal–inland clock baseline

The Shanghai and Wuhan clocks are 692 km apart and connected through Hefei by a 1,350-km phase-stabilized fibre link (Fig. 1a). The apparatus and frequency-comparison chain are described by Hou and colleagues.[@hou] Evaluations of the two clock systems and the field-deployed transmission architecture provide the experimental basis for the comparison.[@jia,zhu,chenlink] We take a positive fractional-rate variation to mean Wuhan Yb running faster relative to Shanghai Sr. For displaying the measurements, the equivalent potential is $U=c^2y=-[\delta W_{\mathrm{Wuhan}}-\delta W_{\mathrm{Shanghai}}]$.

The coastal–inland geometry gives the two stations different responses to ocean mass redistribution. The combined prediction contains the direct astronomical forcing, the Earth's induced potential and clock displacement, together with ocean-loading effects. We use the frozen IERS-based solid prediction and FES2022 ocean elevations convolved with a kernel that includes water attraction, induced potential and clock displacement (Methods).[@iers,fes,farrell,han]

For M₂, the predicted solid and loading amplitudes are $3.43\times10^{-18}$ and $1.42\times10^{-18}$ in fractional rate. Their 19.8° phase difference gives a combined amplitude of $4.78\times10^{-18}$, equivalent to approximately $0.43\,\mathrm{m^2/s^2}$ (Fig. 1b). Loading is about 30% of the combined M₂ phasor amplitude. Its weighted root-mean-square variation is 33.1% of the combined prediction on the sampled, segment-centred record. These are model contributions; the experiment measures the combined potential.

The record spans September 2025 to August 2026. Its 3,299 accepted ten-minute means contain 545.9 nominal member-hours in 54 segments and eight observing periods (Fig. 1c). The observations fall in eight calendar months and on 43 UTC dates. Summer contributes 273.9 h, while the earlier periods add different lunar–solar phases (Fig. 1d). The analysis retains every accepted sample at its actual time.

### Detecting the tidal variation

Each segment is reduced about its own measured reference level. We subtract the weighted mean separately from the observed rates and from every prediction column. No fitted tidal amplitude enters this operation. The remaining within-segment variations are then combined in one estimate. The frequency levels are left independent across interruptions, while the predicted phase fixes which part of the tidal cycle each observation samples.

A single scale multiplying the complete tidal prediction gives $A_T=0.96\pm0.11$. The reported uncertainty follows the day-deletion rule in Methods. Removing the tidal scale increases the weighted residual sum of squares by 110.35. An eight-period restricted residual sign-flip diagnostic gives $P=0.0078$, at its finite-pattern resolution limit (Methods).

The full record also reveals recurring modulation when ordered by M₂ phase (Fig. 2a). To display the lunar response, the observations and unit lunar prediction undergo the same projection against segment constants and the non-lunar groups. The displayed uncertainties propagate that operation, and the support of each phase bin is retained.

Figure 2b,c returns to actual UTC observations. The displayed segment is selected solely by its largest accepted member count: 42.5 h during 10–12 August 2026. Fixed UTC three-hour averages improve readability, with the same averaging applied to the prediction. The complete ten-minute measurements retain their full range below. The statistical estimates use the original means from all 54 segments, rather than the display averages or this selected interval.

Allowing the lunar response to deviate from the predicted phase gives in-phase and quadrature coefficients of $1.00\pm0.13$ and $-0.10\pm0.20$ (Fig. 3b). The astronomical phase is compatible with the observed response. The phase fold, phase-relaxed fit and spectrum describe the same record and contribute amplitude, phase and frequency information.

### Constraining neighbouring semidiurnal responses

We jointly estimate the lunar group M₂+N₂, the neighbouring group S₂+K₂ and an auxiliary daily group. Relative amplitudes and phases are fixed within each physical group. M₂ and N₂ are lunar constituents; S₂ is the principal solar semidiurnal tide, while K₂ contains lunar and solar forcing. Each semidiurnal group has its own coefficient in this common model. The approximately daily constituents are retained to propagate their covariance with the target responses.

The estimates are $A_L=1.00\pm0.13$ and $A_S=0.93\pm0.36$, relative to the combined solid-Earth and loading prediction (Fig. 3a). Their scaled least-squares correlation is −0.30. The weaker neighbouring coefficient provides a less precise constraint, whose interpretation depends more strongly on same-frequency disturbances. Conditional joint regions and the targeted weak-group test are reported in Extended Data Fig. 4 and Methods.

The observed semidiurnal spectrum has local maxima at 22.361 and 23.147 µHz (Fig. 3c). These lie near the known principal frequencies of M₂ and S₂, whose astronomical spacing is approximately 0.78 µHz. The two reported local maxima are 0.786 µHz apart. Spectra before and after subtracting the fixed unit prediction retain the original gaps and use the same segment projection. The potential-density axis is related to the fractional-frequency density by $S_W=c^4S_y$.

Single-line injections on the actual observation window produce about 8% cross-power at the other principal frequency. Conditional scans remove the competing principal sinusoid before examining each neighbourhood (Extended Data Fig. 1). These calculations explain sampling sidelobes and the remaining competition near S₂. The spectrum displays frequency structure; the physical group amplitudes come from the simultaneous template fit.

### Consistency and experimental controls

Both early and summer observations support the lunar response. Their separate coefficients are $1.21\pm0.23$ and $0.77\pm0.18$. Deleting each period in turn leaves lunar coefficients between 0.885 and 1.093 and neighbouring coefficients between 0.750 and 1.229 (Fig. 4a,b). Changing the zero-point hierarchy gives the same-data comparisons in Fig. 4c,d; documented calibrated transfers across the relevant interruptions are absent, motivating the segment treatment.

A shared 24-h sine–cosine pair, motivated by daily operating schedules and environmental variation, gives a lunar coefficient of $1.04\pm0.13$. A freely phased 12-h pair in every period instead gives lunar $0.75\pm0.24$ and neighbouring $-5.10\pm15.01$. The latter interval is very broad because a freely phased 12-h term competes directly with the semidiurnal template. Shared and period-wise results for both groups, including working intervals, are listed in Extended Data Table 4. These are sensitivity scenarios, not measurements of an independently established laboratory disturbance.

The matched round-trip transmission monitor covers 246.6 member-hours in the summer periods. Including it on identical support changes the lunar coefficient by $0.0061\pm0.0063$ and the neighbouring coefficient by $0.00594\pm0.01453$ (Extended Data Fig. 3). This recorded control constrains the monitored route during that overlap. The 12-h sensitivity and transmission monitor address different questions: same-frequency attribution and the measured transfer path, respectively.

The full-record tidal response and the lunar amplitude–phase agreement support detection of changing potential. The additional neighbouring coefficient has weaker evidence under period-wise residual resampling, with a restricted wild sign-flip diagnostic of $P=0.0625$. It is therefore reported as a component constraint within the specified physical model.

The measurement extends a fixed-endpoint optical-clock comparison from a static potential difference to its tidal variation. The segment-based reduction uses the changes measured during each run and combines them at their known astronomical phases. It provides a way to retain this information through interruptions while keeping uncertain frequency levels separate.

The substantial loading contribution makes this coastal–inland baseline a useful test of the combined potential prediction. Separating loading from the solid response will require observations that distinguish their amplitude and phase more strongly. More continuous operation and independent records of instrumental variation near 12 h would also strengthen attribution of the neighbouring response. Related results have been reported independently by a European optical-clock network in a contemporaneous arXiv preprint.[@stahl]

\clearpage

## References

{{MAIN_REFERENCES}}

\clearpage

## Figure legends

![Figure 1](figures/figure1.png)

**Fig. 1 | A coastal–inland baseline and its tidal prediction.** **a,** Shanghai Sr and Wuhan Yb connected by the fibre route through Hefei. The dashed line marks the 692-km baseline. Land shading and contours illustrate the model M₂ clock-rate response in $10^{-18}$; sea contours show M₂ ocean-tide height in centimetres. These are different physical quantities. **b,** Differential solid, loading and combined M₂ phasors from the frozen numerical prediction, with equal data-axis scales; the combined $4.78\times10^{-18}$ corresponds to about $0.43\,\mathrm{m^2/s^2}$. **c,** Actual UTC sampling and accepted member-hours in eight periods. **d,** S₂−M₂ phase at those same observations, including nodal corrections. P6–P8 are summer. The map fields and phasors are predictions; the lower panels describe the measured observation window.

\clearpage

![Figure 2](figures/figure2.png)

**Fig. 2 | Tidal variation in the measured clock rates.** **a,** Twelve M₂-phase means of all 3,299 ten-minute observations. The fixed minor remainder is removed, and data and unit lunar prediction undergo identical weighted projection against segment levels and the other physical groups. Error bars are one working standard error with nuisance propagation; means are correlated. Row counts appear beneath the phase labels. **b,** The segment with the largest accepted member count, shown at real UTC. Points are fixed-UTC three-hour means after independent weighted centring of data and prediction. Squares apply the same averaging to the unit combined prediction; the line evaluates it at the observed ten-minute times. Error bars propagate centring. **c,** Every original ten-minute mean in that segment, with its complete vertical range. No empirical daily sinusoid or fit-dependent offset is removed. Left axes use $U=c^2y=-\Delta W$; right axes give fractional rate. Panels are views of the same measurements, and display averaging does not change the primary sample or inference.

\clearpage

![Figure 3](figures/figure3.png)

**Fig. 3 | Amplitude, phase and frequency of the tidal response.** **a,** The single complete-template response, followed by the jointly fitted lunar and neighbouring semidiurnal coefficients. Error bars are one statistical standard error, the larger of scaled LS and UTC-day-deletion jackknife errors. The estimates share the same observations and weights. **b,** Lunar in-phase and quadrature fit; the cross marks $(1,0)$. Contours have covariance radii one and two under scaled LS, not independently calibrated joint confidence levels. **c,** The measured 21–24.5 µHz spectrum and the spectrum after subtracting the fixed unit physical prediction. The scan retains all 3,299 original UTC rows and gaps, with equal weights and 54 segment constants. Vertical markers are the prescribed M₂ and S₂ frequencies. Left and right density axes obey $S_W=c^4S_y$. Peaks, phase and amplitudes use the same record and do not add independent detection significance. Sampling cross-power and conditional scans are given in Extended Data Fig. 1; joint group regions appear in Extended Data Fig. 4.

\clearpage

![Figure 4](figures/figure4.png)

**Fig. 4 | Period support and reference-level sensitivity.** **a,b,** Lunar and neighbouring coefficients for the full record, before summer, summer, and deletion of each of the eight periods. Every retained row is reduced within its segment and all remaining coefficients are refitted. **c,d,** The same observations, physical templates and weights with 54 segment, 29 group or eight period reference levels. The 54-segment design is primary; the other groupings are sensitivity comparisons. Error bars throughout are one statistical standard error, the larger of scaled least squares and UTC-day-deletion jackknife errors. Dashed lines mark unit response. Subset, deletion and grouping estimates share observations and are not pooled.

\clearpage

## Methods

### Observations, frequency sign and averaging

The Shanghai and Wuhan coordinates used by the frozen prediction are 31.130° N, 121.570° E and 30.529° N, 114.357° E. The measured ratio is Wuhan Yb/Shanghai Sr. With positive geodetic potential $W$, its tidal fractional variation is $-[\delta W_{\mathrm{Wuhan}}-\delta W_{\mathrm{Shanghai}}]/c^2$. The period-relative beat conversion is $-d_p(f_{\mathrm{beat}}-f_{{\mathrm{ref}},p})/F_{1550}$, where $F_{1550}=1.933992\times10^{14}$ Hz and $d_p=2$ in 2025 and 1 in 2026. Thus a 2026 beat deviation of 1 Hz has fractional magnitude $5.17\times10^{-15}$. The 2025 division factor is applied before forming the small clock-rate variation.

The supplied valid-interval table defines 54 segments in 29 operating groups and eight periods. Counter members are read across midnight before binning. Beijing-time labels are converted to UTC. Summer group corrections follow the decimal-arithmetic frequency-chain calculation; early absolute correction entries remain incomplete. Their constant part is represented by segment intercepts, while any time variation within a segment remains a possible systematic contribution. Fitted intercepts are never applied to join the runs for long-term stability estimation.

The membership audit contains 1,966,908 nominal one-second rows before the minimum-bin-support cut. Three boundary rows reconcile its difference from the printed interval total. Means are formed in nominal 600-s bins separately within each segment and require at least 180 retained members. The 3,299 accepted means contain 1,965,327 members, or 545.924 h. There are 3,291 unique bin centres: eight centres contain separate partial means from different segments, with disjoint members. The 353.39-day span contains observations on 43 UTC dates. The inherited valid mask is retained; this work neither applies an additional triangular filter nor selects points using tidal residuals. Exact raw-file memberships and hashes are retained in the controlled archive.

### What the constituent names mean

Semidiurnal tides produce approximately two cycles per day. M₂ is the principal lunar constituent; N₂ describes an additional lunar variation associated with orbital ellipticity. S₂ is the principal solar semidiurnal constituent, whereas K₂ contains lunar and solar forcing. The names identify astronomical frequencies, not separate instruments or independent experiments. The diurnal group contains K₁ (lunisolar), O₁ (principal lunar), P₁ (principal solar) and Q₁ (lunar elliptic). Their periods are listed in Extended Data Table 1.[@noaa] Internal relative amplitudes, phases and nodal modulation are fixed within each physical group. A group response therefore tests that complete specified pattern.

### Combined solid and loading potential

The physical target includes the direct astronomical potential, the Earth's induced potential and the effect of clock displacement. The selected frozen solid sequence implements these through the IERS radial displacement $u$ and a fixed effective-potential conversion,

$$y_{\mathrm{solid}}=-\frac{1+k_2-h_2}{h_2}\frac{g(u_{\mathrm{Wuhan}}-u_{\mathrm{Shanghai}})}{c^2},$$

with $h_2=0.6078$, $k_2=0.3010$ and $g=9.794\,\mathrm{m/s^2}$. This is a displacement-based approximation to the combined solid potential. The same conversion also acts on degree-three and frequency-dependent displacement contributions in the supplied sequence. A previous implementation comparison found an approximately 18% K₁ amplitude deficit relative to a potential-weighted reference. The daily response is accordingly not used to infer a Love number. Uncertainty in the solid model remains separate from the quoted statistical errors.

For loading, FES2022 sea-surface elevations $\zeta$ are convolved with the effective-potential kernel

$$\delta W_{\mathrm{load}}=\int \rho_w\zeta(\mathbf{r}',t)G_W(\psi)\,\mathrm{d}A,\qquad
G_W(\psi)=\frac{ga}{M_E}\sum_n(1+k'_n-h'_n)P_n(\cos\psi).$$

The three terms represent direct water attraction, induced potential and clock displacement. PREM load Love numbers are retained through degree 696 with the archived high-degree continuation. Eighteen loading constituents are synthesized with their astronomical nodal corrections. The complex convention is $f\,\mathrm{Re}[C\exp(-i\phi)]$; reversing the exponential sign requires conjugating $C$. The present analysis reads the frozen constituent and time-series tables rather than substituting an older loading sequence.

The eight named constituents form the three physical groups. Minor terms remain once as a fixed remainder $r_0$. On the actual weighted segment-centred sampling, solid, loading and total root-mean-square variations are respectively 2.928, 1.328 and $4.011\times10^{-18}$. Their ratio 0.331 is an amplitude-norm ratio, not an additive fraction of total power. A separate loading coefficient is not estimated here; the measured group responses test the combined prediction.

### Segment reduction and the two estimands

Let $W_s$ be the original diagonal weight matrix in segment $s$, and define $\langle v\rangle_s=(\mathbf{1}^TW_sv)/(\mathbf{1}^TW_s\mathbf{1})$. For each observation vector and each prediction column we form $\widetilde v_s=v_s-\mathbf{1}\langle v\rangle_s$. This operation uses sample times and weights but no fitted tidal amplitude. For a physical design matrix $T_s$, the common coefficients solve

$$\widehat{\boldsymbol A}=\left(\sum_s\widetilde T_s^TW_s\widetilde T_s\right)^{-1}\sum_s\widetilde T_s^TW_s\widetilde y_s.$$

The stored segment matrices and vectors are sufficient statistics for this estimate. All 54 segments enter the same fit; separately fitted segment amplitudes are not averaged. An independent full-design QR fit with 54 intercepts reproduces the three coefficients to within $3\times10^{-15}$. Recomputing the segment means after every deletion also reproduces the original standard errors. No segment level is transferred to create a continuous, calibrated long-term record.

For the full-response estimate, $y$ is the observed fractional rate and $T=s_L+s_S+s_D+r_0$ is the complete frozen prediction. A single coefficient $A_T$ multiplies that entire column. The comparison is between 54 segment constants alone and the same constants plus this one template. For component estimation, we instead subtract the fixed minor remainder once and fit

$$y_i-r_{0,i}=c_{s(i)}+A_Ls_{L,i}+A_Ss_{S,i}+A_Ds_{D,i}+\epsilon_i.$$

These estimands share the observations but answer different questions. Both use $W_{ii}=1/\sigma_i^2$ with the frozen Allan-based weights. The period noise coefficients are estimated from within-segment overlapping Allan deviations at 256–4,096 s after removal of the fixed unit tide. No Allan window crosses a segment boundary. This does not use stability calculated after joining fit-adjusted segment levels.

The daily group is an auxiliary physical component; its coefficient remains $0.58\pm0.54$ (Extended Data Table 2). The interval and correction records do not establish calibrated zero transfer at the 46 boundaries where an eight-period intercept would be shared. They document valid observing times but not signed boundary transfers with uncertainties. The segment convention follows that experimental information.

### Statistical errors and conditional coverage

For each group the reported standard error is the larger of residual-scaled least squares and leave-one-UTC-day-out jackknife errors. Deletions remove a calendar day, refit all remaining coefficients and drop empty intercept columns. The jackknife variance is $(G-1)G^{-1}\sum_g(\hat A_{(-g)}-\overline A)^2$. Period-deletion errors are recorded separately. Extended Data Table 2 gives all components and the same-data intercept comparisons. Observations are repeated measurements of one clock pair, not thousands of independent experiments.

Conditional simulations apply both designs to the same 3,299-row sampling and heteroscedastic uncertainties. Each of four scenarios has 1,000 realizations: independent Gaussian noise; equal variance contributions from Gaussian white noise and a 6-h Ornstein–Uhlenbeck process within segments; the corresponding 24-h process within periods; and standardized Student-$t_5$ noise. The overall scale is the observed segment-model residual scale; all true physical response coefficients are one. Each realization recomputes both components of the standard-error rule. Seed 2026110617 fixes the simulation. Coverage of $\hat A\pm1.96u$ is 95.1–97.4% for the segment-model lunar coefficient and 95.4–96.8% for its neighbouring coefficient; Monte Carlo standard errors are about 0.4–0.7 percentage points (Extended Data Table 3). These are tests under declared noise laws, not a calibration against every possible disturbance.

The new full-template coefficient uses the same standard-error rule. Its scaled-LS, day-deletion, day-cluster CR1 and period-deletion standard errors are respectively 0.0973, 0.1082, 0.1033 and 0.1216. The CR1 sandwich uses 43 UTC-day clusters and the finite-sample factor $[G/(G-1)][(n-1)/(n-K)]$, with $K=55$. The working interval $\widehat A_T\pm1.96u$ is 0.743–1.167. This is an explicitly labelled working interval, rather than a confidence statement valid for every possible noise process.

For targeted zero-response tests, we compare the weighted RSS of nested models on the unchanged rows. The full-template test adds one entire prediction to segment constants. The neighbouring-group test adds one S₂+K₂ coefficient while retaining the lunar and daily groups and the constants. Noise is generated on the true window with the original heteroscedastic uncertainties and the observed full-model residual scale. Each of the four declared noise scenarios has 20,000 realizations; seeds 2026110711 and 2026110709 fix the full-template and neighbouring-group simulations. The exact residualized-template projection computes the RSS improvement, and direct restricted/full refits check that calculation. The full-template statistic is 110.353; none of the 20,000 draws in any scenario reaches it. The plus-one tail estimate is $1/20,001$ in each scenario, not zero. For the neighbouring statistic 10.943, the corresponding tail estimates are 0.00185, 0.12559, 0.01435 and 0.00205 in the listed noise-scenario order.

Restricted period-wise residual sign flips enumerate all $2^8=256$ patterns, preserving each period's internal structure. The diagnostic tail fractions are 2/256 for the full response and 16/256 for the added neighbouring group. They rely on period independence and symmetry and are not exact experimental randomization tests. The two-sided resolution is 2/256. No Gaussian sigma value is inferred from either finite enumeration.

The noise scenarios are conditional stress tests, not measured noise laws. In separate 2,000-draw diagnostics per law, the observed within-segment lag-one residual correlation is −0.148. The simulated 95% ranges are −0.054–0.015 for Gaussian noise, 0.216–0.347 for the 6-h mixture, 0.072–0.202 for the 24-h mixture and −0.051–0.017 for $t_5$. Thus the positively correlated mixtures do not describe the observed short-lag structure; neither do the other two laws fully reproduce it. No scenario is selected because of its tidal tail probability. No simulated record is added to the observations.

Extended Data Fig. 4 gives conditional two-group regions: the first 10,000 draws estimate error covariance and the empirical 95% Mahalanobis threshold; the other 10,000 assess coverage. Held-out joint coverage is 94.3–94.8%, with binomial Monte Carlo standard errors of about 0.22 percentage points and additional calibration uncertainty. These nominal regions describe the specified laws and do not replace the reported marginal working errors with a universally calibrated joint confidence region.

The phase-relaxed model adds the lunar quadrature while retaining the prescribed M₂/N₂ relationship. Covariance contours use scaled least squares. Subset and deletion fits refit the same model on their retained rows. Shared-data estimates are not averaged. The simulation coverage refers to two-sided intervals; the reported $\pm$ values are standard errors.

### Phase means, spectral density and sampling sidelobes

For the phase plot, $N$ contains segment constants and the two non-lunar groups. We project both $y-r_0$ and the unit lunar prediction with $M_N=I-N(N^TWN)^{-1}N^TW$, and average in twelve fixed M₂ phase bins. If $B$ is weighted bin averaging, the mean covariance is $BM_NC_yM_N^TB^T$, where $C_y$ is the scaled working observation covariance. It retains correlations between means and propagates nuisance estimation. The full unbinned response remains primary.

For the actual-time display, the representative segment maximizes accepted nominal member count, with segment ID breaking ties. Segment 51 contains 255 ten-minute means and 153,000 members. Its 42.5 member-hours extend from 10 August 2026 21:35 UTC to 12 August 15:55 UTC. Three-hour display bins follow fixed UTC boundaries and remain inside the segment. All 255 means are assigned; none is removed to improve the display. Weighted averaging is identical for observed and unit-predicted centred values. If a display bin has total weight $w_b$ and its segment has total weight $w_s$, the centred-observation variance is $\widehat\sigma^2(1/w_b-1/w_s)$. This propagates the segment-mean operation and creates correlations between display means. The curve at ten-minute timestamps is a sampled physical prediction, not gap filling. The potential display uses $U=c^2y$ and the right axis retains the fractional rate.

Figure 3c preserves the independently specified equal-weight, 54-intercept scan of the unchanged observed means, rather than replacing it with the amplitude fit's weights. Every trial sine–cosine pair and the data are projected against the same constants. For a reduction in squared residuals $\Delta\mathrm{RSS}(f)$ with dimensionless $y$, the nominal one-sided projection density is $S_y(f)=600\,\mathrm{s}\,\Delta\mathrm{RSS}(f)$ per Hz, or $10^{-6}$ times that value per µHz. Potential density is $S_W=c^4S_y$; amplitude density is $c^2\sqrt{S_y}$. Uniform-grid checks reproduce the conventional one-sided Fourier density. For interrupted data this normalization is a stated projection density, not a Parseval-calibrated variance over a filled year.[@vanderplas]

The frequency step is 0.002729 µHz; the inverse calendar span is 0.032752 µHz. Fine plotting steps do not improve physical resolution. The listed peak positions are scan maxima; no constituent-frequency fit or frequency-confidence interval is reported. M₂-only and S₂-only astronomical injections use the same actual times, nodal factors and equal-weight segment projection. Power at the opposite principal frequency, divided by power at the injected frequency, gives 0.08027 and 0.08149. Conditional scans project out a freely phased sinusoid at the other frequency before scanning the target neighbourhood. Amplitude interference means that such corrections act on sampled waveforms or complex coefficients, not by subtracting scalar power spectra. Gaps alone do not predict the realization of measurement noise. Residual density can describe remaining measurement fluctuations, but includes possible model mismatch and cannot be called a pure instrumental noise floor.

### Instrument and daily-response checks

The matched monitor calculation uses 1,482 rows with 887,882 nominal members, or 246.634 h, in P6–P8. Both baseline and augmented fits have identical members, segment labels and weights. Paired day-deletion replicates propagate uncertainty in their difference. Extended Data Fig. 3 reports the response changes and dates. This comparison concerns the monitored transmission route during the measured overlap.

On the selected data and model, a common 24-h sine–cosine pair gives $A_L=1.036\pm0.133$; separate 24-h pairs in each period give $1.003\pm0.136$. These daily sensitivity designs address a periodicity motivated by temperature and operating schedules, without assigning an independently measured thermal amplitude. A shared 12-h pair gives lunar $0.994\pm0.132$ and neighbouring $2.931\pm1.011$. Separate pairs in each period give $0.751\pm0.242$ and $-5.100\pm15.008$. The normalized design condition number grows from 2.37 to 6.90 and 122.54, respectively; all designs retain full numerical rank. These terms test same-frequency identifiability and are not independently measured disturbances. Extended Data Table 4 reports both groups and their 1.96-SE working intervals.

### AI-assisted preparation

OpenAI Codex assisted English drafting, numerical replay and figure preparation. [Authors to confirm their verification of the analyses, citations and final text, and responsibility for the submitted work.]

## Data availability

The author review package contains the 3,299 derived means, fixed templates, noise weights, figure source tables and immutable input hashes. The original counters and membership ledger are held in the controlled experimental archive. [Authors to supply an editor-accessible location and confirm the permanent data-access statement and repository identifier before submission.]

## Code availability

The package contains the independent QR replay, same-data design comparison, conditional simulations, spectral calculations, covariance propagation and figure scripts, with software versions and a reproducible entry point. [Authors to confirm the code licence and permanent repository identifier before submission.]

## Methods references

{{METHOD_REFERENCES}}

\clearpage

## Acknowledgements

[To be completed by the authors.]

## Funding statement

[Funding sources and grant identifiers to be completed by the authors.]

## Author contributions

[To be completed and approved by all authors.]

## Competing interests

[Declaration to be supplied by the authors.]

## Additional information

**Correspondence:** [Corresponding author names and email addresses to be supplied; mark them with an asterisk in the author list.]

\clearpage

## Extended Data

![Extended Data Figure 1](figures/ed_figure2.png)

**Extended Data Fig. 1 | Conditional semidiurnal scans.** Equal-weight scans of the same 3,299 observations with 54 segment intercepts. **a,** M₂ neighbourhood before and after projection of a sine–cosine pair at S₂. **b,** S₂ neighbourhood before and after projection at M₂. Dotted lines show the astronomical target frequencies. These are descriptive projections on shared observations, not additional detection probabilities.

\clearpage

![Extended Data Figure 2](figures/ed_figure1.png)

**Extended Data Fig. 2 | Same-data comparison of reference-level designs.** **a,** Weighted segment-mean residuals after the eight-period joint fit, ranging from $-6.75$ to $12.00\times10^{-18}$. Segment constants make these means zero by construction. **b,** Lunar point estimates after period deletion, spanning 0.877–1.052 with eight period constants and 0.885–1.093 with 54 segment constants. The weighted residual sums of squares are 3,781.58 and 3,713.64; the latter has 46 additional intercept parameters. Unweighted residual root-mean-square values are 24.114 and $23.934\times10^{-18}$, and reduced residual sums of squares are {{REDUCED_RSS}}. Adjacent standardized residual correlations are −0.127 and −0.148, using pairs within the same segment and separated by at most 900 s. All comparisons retain identical observations, templates, corrections and noise weights. These are residual diagnostics, not measurements of physical jumps or zero-transfer calibration.

\clearpage

![Extended Data Figure 3](figures/ed_figure3.png)

**Extended Data Fig. 3 | Simultaneous summer transmission control.** Changes caused by adding the fibre round-trip monitor to the joint model, with paired UTC-day-jackknife standard errors. Baseline and augmented fits use identical clock/monitor members, labels and weights: 1,482 means containing 887,882 nominal one-second members, or 246.634 h in P6–P8, from 29 June to 25 August 2026. The lunar, neighbouring and daily shifts are respectively $0.00606\pm0.00627$, $0.00594\pm0.01453$ and $0.00791\pm0.01388$. The paired monitor constrains the measured transmission route on this summer overlap. The main tidal estimate uses the entire 545.9-h clock record. The prior transmission-architecture demonstration over 2,067 km is a separate experiment.[@chenlink]

\clearpage

![Extended Data Figure 4](figures/extended4.png)

**Extended Data Fig. 4 | Conditional uncertainty of the neighbouring response.** **a,** Nominal 95% joint regions for $(A_L,A_S)$ under four declared noise laws on the original 3,299-row design. The point is the observed estimate and the cross is $(1,1)$. Each region uses 10,000 calibration and 10,000 validation simulations; held-out coverage is 94.3–94.8%. The regions are conditional on the specified laws, none of which fully matches the measured short-lag residual structure. **b,** Null tail curves for the added S₂+K₂ coefficient from 20,000 simulations per law. The vertical line marks the observed weighted-RSS improvement; the dotted horizontal line is 0.05. Simulations are separate from the measured data. The declared scenarios provide sensitivity information, not four additional experiments or an independently validated laboratory-noise model.

\clearpage

**Extended Data Table 1 | Astronomical constituent guide.** Names specify forcing and frequency; one response coefficient multiplies each complete group with its internal ratios and phases fixed.

{{TIDE_TABLE}}

\clearpage

**Extended Data Table 2 | Estimator and uncertainty comparison.** All directly replayed designs use the same 3,299 means, physical templates and Allan-based weights. Errors are standard errors.

{{DESIGN_TABLE}}

{{ERROR_TABLE}}

\clearpage

**Extended Data Table 3 | Conditional 95% interval coverage.** Each scenario has 1,000 simulated realizations per design, with fixed observed sampling and weights. Values are percentages for the larger-of-LS-and-day-jackknife rule, using multiplier 1.96. They assess the specified scenarios, not unknown systematic effects.

{{COVERAGE_TABLE}}

\clearpage

**Extended Data Table 4 | Same-data 12-h sensitivity.** Each row retains the original 3,299 means, 54 segment levels, astronomical group templates and Allan weights. Errors are the larger of scaled LS and day-deletion jackknife standard errors. Working intervals are estimate ±1.96 standard errors; they are not calibrated for all correlated-noise or deterministic-disturbance models. A common 12-h sine–cosine pair has one phase across the record; the period-wise design gives each of eight periods its own pair. These fits assess degeneracy, not the independently established magnitude of an instrumental effect.

| Model           | Lunar coefficient   | Lunar working interval   | Neighbouring coefficient   | Neighbouring working interval   |
|:----------------|:--------------------|:-------------------------|:---------------------------|:--------------------------------|
| Primary         | 1.000 ± 0.132       | [0.742, 1.259]           | 0.925 ± 0.365              | [0.210, 1.640]                  |
| Shared 12 h     | 0.994 ± 0.132       | [0.735, 1.252]           | 2.931 ± 1.011              | [0.950, 4.913]                  |
| 12 h per period | 0.751 ± 0.242       | [0.277, 1.224]           | -5.100 ± 15.008            | [-34.515, 24.316]               |
