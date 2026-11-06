# Tidal potential measured on a coastal–inland optical-clock baseline

[Author list, order and affiliation assignments to be confirmed by the authors]

^1^ Hefei National Laboratory, University of Science and Technology of China, Hefei, China

^2^ Shanghai Research Center for Quantum Sciences and CAS Center for Excellence in Quantum Information and Quantum Physics, University of Science and Technology of China, Shanghai, China

^3^ Hefei National Research Center for Physical Sciences at the Microscale and School of Physical Sciences, University of Science and Technology of China, Hefei, China

^4^ Innovation Academy for Precision Measurement Science and Technology, Chinese Academy of Sciences, Wuhan, China

^5^ Jinan Institute of Quantum Technology and CAS Center for Excellence in Quantum Information and Quantum Physics, University of Science and Technology of China, Jinan, China

^6^ Time and Frequency Geodesy Center (TFGC), School of Geodesy and Geomatics, Wuhan University, Wuhan, China

## Abstract

Tides change Earth's gravitational potential and hence the relative rates of distant clocks.^1,2^ Measuring this time dependence connects precision timekeeping to observations of the changing Earth. Here we measure tidal variations of the potential difference between Shanghai and Wuhan with optical clocks and resolve neighbouring semidiurnal signals whose principal frequencies are 0.78 µHz apart. The clocks accumulated 545.9 hours over 353 days. Changing lunar–solar phase links observations across 54 segments with independent frequency offsets. The measured spectrum has local peaks near the principal lunar and solar frequencies. Joint astronomical-template estimates give $1.00\pm0.13$ for M₂+N₂ and $0.93\pm0.36$ for S₂+K₂ relative to the combined solid-Earth and ocean-loading prediction (one statistical standard error). These observations demonstrate optical-clock measurements of tidal potential with high spectral resolution.

## Main text

Earth's gravitational potential varies as the Moon and Sun change position and as water, air and the solid Earth move. Measuring these changes provides a way to study mass redistribution and deformation, and to maintain consistent height and time references.^3,4,5^ Geodetic surveys and satellite gravity observations constrain different aspects of this evolving field.^4,5^ Optical clocks offer a direct measure of potential differences: gravity changes their relative rates, so a frequency comparison between distant clocks contains a geophysical observable.^1,2^ Connecting stable clocks through optical fibres allows repeated observations of the same endpoints across hundreds of kilometres.^6,7^

Laboratory redshift tests and remote optical-clock comparisons have established measurements of static potential differences.^8,9,10^ A time-dependent measurement additionally requires enough precision over the period of the change and sufficiently stable operation of both clocks and their connection. Tides are a well-defined target: celestial motion fixes their frequencies and phases, while deformation and ocean loading determine the signal expected at each station.^3^ Measuring that signal tests whether clock comparisons can follow the changing Earth. It also informs frequency metrology, where the same potential variation enters the redshift correction needed to compare clocks and form common time scales.^11^ Coordinated comparisons already connect optical standards across national borders.^12^

The principal lunar and solar semidiurnal tides are a demanding pair of nearby signals. M₂ repeats every 12.42 h and S₂ every 12 h, giving a frequency separation of only 0.78 µHz. Over a short comparison their variations can look much alike. Their relative phase changes with date, allowing observations distributed over different lunar–solar phases to separate their responses. That astronomical phase remains defined through interruptions, even when the frequency offset between observing runs is unknown.

Here we measure tidal variations of the potential difference between coastal Shanghai and inland Wuhan and resolve their neighbouring semidiurnal responses. Across a 353-day span, 54 valid segments provide 545.9 h of observations. Independent constants represent their reference levels; the tidal phase is retained at every actual observing time. We jointly estimate complete physical templates for the lunar semidiurnal group M₂+N₂, the neighbouring group S₂+K₂ and the approximately daily group K₁+O₁+P₁+Q₁. Internal amplitude ratios and phases remain fixed by the astronomical model, so the fit propagates overlap between the groups. K₂ contains lunar and solar forcing. The spectrum displays local peaks near M₂ and S₂, and both fitted semidiurnal responses agree with the combined solid-Earth and ocean-loading prediction. This coastal–inland measurement resolves tidal components in the changing gravitational potential on a baseline where loading is a sizeable part of the signal.

### A coastal–inland prediction

The strontium clock in Shanghai and ytterbium clock in Wuhan are 692 km apart, joined through Hefei by a 1,350-km phase-stabilized fibre link (Fig. 1a).^13^ The summer observations overlap the absolute frequency-ratio measurement reported by Hou and colleagues; the present observable is the time-dependent tidal response. The two clock systems have published systematic evaluations, which describe their apparatus rather than the uncertainty of the interrupted tidal estimate.^14,15^ We define a positive frequency-ratio variation as Wuhan Yb running faster relative to Shanghai Sr. In the geodetic potential convention used here, the measured fractional variation is $y=-[\delta W_{\mathrm{Wuhan}}-\delta W_{\mathrm{Shanghai}}]/c^2$.

Tides change the direct gravitational potential and deform the Earth, moving the clocks and changing the Earth's own potential. Ocean tides additionally redistribute water. Their contribution includes its attraction, the Earth's deformation and the accompanying displacement of the clock. We combine an IERS-based solid-tide prediction with FES2022 ocean elevations and a loading kernel containing all three loading contributions (Methods).^16,17,18,19^ Shanghai lies by the East China Sea, whereas Wuhan is inland. This geometry makes loading a substantial part of the differential prediction.

The predicted M₂ amplitudes are $3.43\times10^{-18}$ for the solid contribution and $1.42\times10^{-18}$ for loading. Their phases differ by 19.8°, giving a combined amplitude of $4.78\times10^{-18}$ (Fig. 1b). The loading amplitude is about 30% of the combined M₂ amplitude; their vector sum accounts for the phase difference. On the sampled record, after removing segment means, loading has 33.1% of the combined prediction's weighted root-mean-square variation. These amplitude ratios describe the model contribution, making this coastal–inland geometry a useful setting for testing the combined potential. A separately processed analysis allowing loading its own coefficient reported $0.89\pm0.55$, which does not resolve that coefficient (Methods). The observable tested here is the combined potential.

The record spans September 2025 to August 2026, with 54 valid segments in eight observing periods (Fig. 1c). Its 3,299 ten-minute means contain 545.9 h of accepted nominal one-second measurements. Observations occur in eight calendar months; the annual span is not continuous operation. Actual UTC times and all gaps are retained. The June–August observations supply 273.9 h and sample a broad range of relative lunar–solar phase, while the earlier periods add different phases and operating conditions (Fig. 1d). Both the duration and placement of the observations determine what can be separated.

### Jointly resolved semidiurnal responses

Fitting the three physical groups together gives $A_L=1.00\pm0.13$ for M₂+N₂ and $A_S=0.93\pm0.36$ for S₂+K₂. One denotes the specified combined prediction. Each of the 54 segments has its own constant reference level, and the same noise weights are used throughout the amplitude analysis. The coefficients are estimated from the original ten-minute means. No empirical daily sinusoid is subtracted first, and no model values replace missing measurements.

Figure 2 orders the entire record by M₂ phase. The observations, after subtracting the fixed minor tidal remainder, and the unit lunar prediction undergo the same projection against segment constants and the other two fitted groups. Twelve phase bins then reveal the recurring modulation. All individual points and the number supporting each bin are retained. The propagated error bars account for the jointly estimated nuisance terms; the twelve displayed means are a view of the full fit, rather than twelve new independent observations.

Allowing a lunar component one quarter-cycle from the predicted phase gives in-phase and quadrature responses of $1.00\pm0.13$ and $-0.10\pm0.20$ (Fig. 3b). The phase is compatible with the astronomical prediction. The jointly fitted daily group has $A_D=0.58\pm0.54$ (Fig. 3a). Its lower precision is already accounted for through the joint design and covariance; it does not negate the semidiurnal responses. It also does not provide a bound on an unmeasured laboratory daily disturbance.

The reported errors are the larger of residual-scaled least-squares and UTC-day-deletion standard errors. Their components, period-deletion checks and conditional interval coverage are given in Methods. Joint estimation preserves uncertainty from overlap among the physical groups. Improving the daily response calls for longer uninterrupted clock operation and sustained link comparisons with all valid observations retained under data-quality rules fixed independently of the tidal fit. An existing single-bin influence check is described in Methods.

### Spectral separation through the observation window

The spectrum presents the same observations in a complementary, physically intuitive form (Fig. 3c). An equal-weight sinusoidal scan with 54 segment constants has local maxima at 22.361 and 23.147 µHz, close to the predicted M₂ and S₂ frequencies of 22.364 and 23.148 µHz. The prescribed principal frequencies are 0.78 µHz apart, compared with an inverse calendar span of 0.0328 µHz. Resolving this pair is the demonstrated spectral capability; the interrupted observation window determines the accompanying sidelobes. The left axis expresses spectral density in gravitational-potential units and the right in fractional-frequency units. A fractional variation of $10^{-18}$ corresponds to about $0.09\,\mathrm{m^2/s^2}$ of potential difference.

Interruptions shape this spectrum. Sampling a narrow tidal line at the observed times spreads part of its power into sidelobes, including the neighbourhood of the other principal semidiurnal frequency. Single-constituent injections through the actual sampling and scan give 8.03% M₂-to-S₂ cross-power and 8.15% in the reverse direction. These numbers describe the sampling response, not random noise added by the gaps. Conditional scans retain a local feature near each frequency after projecting out the sine and cosine at the other (Extended Data Fig. 2).

The two features and the conditional scans support distinct contributions in the principal lunar and solar semidiurnal neighbourhoods. This attribution does not separately measure N₂ or K₂. The response coefficients instead come from the simultaneous astronomical groups, with their prescribed internal relationships and noise weights. Subtracting the fixed unit physical prediction reduces the spectral structure, as shown by the second curve. That curve is a residual display of the same record, not another significance test. Phase coverage, spectral attribution and grouped estimation answer related but distinct questions.

### Across interruptions and through the fibre

The response is supported by observations on both sides of summer. With the same segment model, the lunar coefficient is $1.21\pm0.23$ before summer and $0.77\pm0.18$ in summer. Deleting each observing period in turn gives point estimates from 0.885 to 1.093 (Fig. 4a). These overlapping fits show the influence of each period; the headline result uses the full record.

The choice of reference levels follows the experimental record. The available interval and correction tables do not establish a calibrated zero transfer across interruptions. We therefore give each valid segment an independent constant. The model with eight period constants reproduces $0.987\pm0.123$ on exactly the same observations, templates and weights. Its lunar result changes little, but its neighbouring-group coefficient becomes $1.129\pm0.288$. Residual structure and deletion results for both designs are retained in Methods and Extended Data Fig. 1. Agreement with one is not used to choose between them.

A simultaneous fibre round-trip record provides a direct instrument control on 246.6 h of summer observations, from 29 June to 25 August 2026. Clock and monitor means are formed from matching valid members. Adding the monitor to the otherwise identical segment model changes the lunar coefficient by $0.0061\pm0.0063$ and the neighbouring coefficient by $0.0059\pm0.0145$ (Fig. 4b). This tests the monitored transmission route on that overlap. Other local transfer branches and clock effects require their own observations.

Daily temperature changes and operating schedules motivate environmental checks. The separately filtered analysis reports a lunar coefficient of $0.98\pm0.13$ with two-site temperature regressors; its distinct sampling and supporting measurements are identified in Methods. On the present observations, adding one shared 24-h sine–cosine pair gives $1.04\pm0.13$. Arbitrary period-specific 12-h terms are retained as sensitivity tests because, over short runs, they compete directly with astronomical semidiurnal variation. They are not assigned an observed laboratory amplitude.

We have measured tidal variations of the gravitational potential between Shanghai and Wuhan and resolved neighbouring semidiurnal responses in an interrupted optical-clock comparison. The jointly estimated amplitudes and the measured spectral peaks connect the observed clock-rate variations to the predicted tidal components. A phase reference supplied by celestial motion preserves the waveform across observing dates, while segment constants accommodate reference levels that have not been transferred between runs. High spectral resolution here is demonstrated by distinguishing the principal lunar and solar semidiurnal neighbourhoods in the actual observation window.

Independent, contemporaneous measurements of tidal potential variations have also been reported with a European optical-clock network.^20^ These parallel observations show that optical clocks can measure changes in the gravitational potential on continental baselines. The coastal–inland geometry in the present experiment makes ocean loading a sizeable part of the combined prediction. Longer coastal records and calibrated local transfer paths could allow the solid and loading responses to be tested separately.

Clock networks connect this geophysical capability to the realization of time itself. International comparisons already link optical standards across countries, and intermittently operated optical clocks have steered continuous time scales.^12,21^ A common time scale requires clock frequencies to be referred to a consistent gravitational potential; Earth monitoring treats changes in that potential as the signal.^4,11^ Once a frequency-transfer link is established, it can repeatedly compare distant endpoints during operation without resurveying the intervening terrain. Such observations complement levelling surveys and the standard monthly gravity products from satellites.^4,5^ The temporal resolution attainable for a particular signal depends on clock stability and simultaneous operation. With improved continuity, calibrated reference levels and colocated height measurements, future networks could extend these differential observations to atmospheric and hydrological mass changes.^5,22^ The measured tidal variations and their spectral separation demonstrate the signal discrimination needed for those applications.

\clearpage

## Figure legends

![Figure 1](figures/figure1.png)

**Fig. 1 | Geometry and changing lunar–solar phase.** **a,** Shanghai Sr and Wuhan Yb, 692 km apart, with the 1,350-km fibre connection through Hefei drawn schematically. **b,** Predicted differential M₂ solid and ocean-loading phasors, with the solid component defining phase zero; amplitudes are fractional clock rates in units of $10^{-18}$. **c,** Actual UTC sampling in eight observing periods, with accepted nominal member-hours. **d,** The S₂−M₂ astronomical phase at those same samples, including nodal corrections. Summer periods P6–P8 are orange. Geography and phasors describe the prediction; the lower panels describe the observation window.

\clearpage

![Figure 2](figures/figure2.png)

**Fig. 2 | The full record ordered by lunar phase.** **a,** Twelve 30° M₂ phase means of all 3,299 observations, after subtracting the fixed minor remainder and projecting against 54 segment constants and the neighbouring semidiurnal and daily groups. Identical weighted projection and averaging are applied to the unit lunar prediction; the fitted curve uses the unbinned primary coefficient. Error bars are one working standard error with the nuisance projection propagated; phase means are correlated. **b,** Every projected observation, with the full observed vertical range. **c,** Number of rows in each bin. Data, weights and templates are the primary segment design throughout. This is a display of the main observations, not an independent experiment.

\clearpage

![Figure 3](figures/figure3.png)

**Fig. 3 | Semidiurnal responses, phase and measured spectral structure.** **a,** Joint group amplitudes with one standard error, defined as the larger of scaled least-squares and UTC-day jackknife errors. **b,** Lunar in-phase and quadrature coefficients; the cross marks the unit prediction. Contours have covariance radii one and two from scaled least squares, not separately calibrated joint confidence levels. **c,** Equal-weight spectral calculation around the principal M₂ and S₂ frequencies, separated by 0.78 µHz: 3,299 real UTC means, 54 segment constants and equal weights. Blue shows the observed scan; orange follows subtraction of the fixed unit total prediction. No gap is filled or compressed. Both axes show the same nominal one-sided projection density per µHz, related by $S_W=c^4S_y$. Sampling sidelobes contribute about 8% bidirectional M₂/S₂ cross-power. Peak locations support the principal-frequency attribution; group coefficients in **a** use the physical templates and Allan-based weights. All panels use the same observation rows.

\clearpage

![Figure 4](figures/figure4.png)

**Fig. 4 | Temporal support and a simultaneous transmission control.** **a,** Lunar estimates from the full record, the pre-summer and summer subsets, and deletion of each observing period. Each fit uses segment constants and the primary noise weights, with errors recalculated on its retained rows. The shaded band is the full-record one-standard-error range. These fits share observations. **b,** Changes caused by including the simultaneous round-trip monitor, with paired UTC-day-jackknife standard errors. Both fits use identical clock/monitor members: 1,482 means representing 246.6 h in P6–P8, between 29 June and 25 August 2026. This control covers the monitored transmission channel on its measured overlap; the principal tide fit retains the entire 545.9-h clock record.

\clearpage

## Methods

### Observations, frequency sign and averaging

The Shanghai and Wuhan coordinates used by the frozen prediction are 31.130° N, 121.570° E and 30.529° N, 114.357° E. The measured ratio is Wuhan Yb/Shanghai Sr. With positive geodetic potential $W$, its tidal fractional variation is $-[\delta W_{\mathrm{Wuhan}}-\delta W_{\mathrm{Shanghai}}]/c^2$. The period-relative beat conversion is $-d_p(f_{\mathrm{beat}}-f_{{\mathrm{ref}},p})/F_{1550}$, where $F_{1550}=1.933992\times10^{14}$ Hz and $d_p=2$ in 2025 and 1 in 2026. Thus a 2026 beat deviation of 1 Hz has fractional magnitude $5.17\times10^{-15}$. The 2025 division factor is applied before forming the small clock-rate variation.

The supplied valid-interval table defines 54 segments in 29 operating groups and eight periods. Counter members are read across midnight before binning. Beijing-time labels are converted to UTC. Summer group corrections follow the decimal-arithmetic frequency-chain calculation; early absolute correction entries remain incomplete. Their constant part is represented by segment intercepts, while any time variation within a segment remains a possible systematic contribution. Fitted intercepts are never applied to join the runs for long-term stability estimation.

The membership audit contains 1,966,908 nominal one-second rows before the minimum-bin-support cut. Three boundary rows reconcile its difference from the printed interval total. Means are formed in nominal 600-s bins separately within each segment and require at least 180 retained members. The 3,299 accepted means contain 1,965,327 members, or 545.924 h. There are 3,291 unique bin centres: eight centres contain separate partial means from different segments, with disjoint members. The 353.39-day span contains observations on 43 UTC dates. The inherited valid mask is retained; this work neither applies an additional triangular filter nor selects points using tidal residuals. Exact raw-file memberships and hashes are retained in the controlled archive.

### What the constituent names mean

Semidiurnal tides produce approximately two cycles per day. M₂ is the principal lunar constituent; N₂ describes an additional lunar variation associated with orbital ellipticity. S₂ is the principal solar semidiurnal constituent, whereas K₂ contains lunar and solar forcing. The names identify astronomical frequencies, not separate instruments or independent experiments. The diurnal group contains K₁ (lunisolar), O₁ (principal lunar), P₁ (principal solar) and Q₁ (lunar elliptic). Their periods are listed in Extended Data Table 3.^23^ Internal relative amplitudes, phases and nodal modulation are fixed within each physical group. A group response therefore tests that complete specified pattern.

### Combined solid and loading potential

The physical target includes the direct astronomical potential, the Earth's induced potential and the effect of clock displacement. The selected frozen solid sequence implements these through the IERS radial displacement $u$ and a fixed effective-potential conversion,

$$y_{\mathrm{solid}}=-\frac{1+k_2-h_2}{h_2}\frac{g(u_{\mathrm{Wuhan}}-u_{\mathrm{Shanghai}})}{c^2},$$

with $h_2=0.6078$, $k_2=0.3010$ and $g=9.794\,\mathrm{m/s^2}$. This is a displacement-based approximation to the combined solid potential, not the alternative frequency-resolved direct-potential implementation. The same conversion also acts on degree-three and frequency-dependent displacement contributions in the supplied sequence. A previous implementation comparison found an approximately 18% K₁ amplitude deficit relative to a potential-weighted reference. The daily response is accordingly not used to infer a Love number. Uncertainty in the solid model remains separate from the quoted statistical errors.

For loading, FES2022 sea-surface elevations $\zeta$ are convolved with the effective-potential kernel

$$\delta W_{\mathrm{load}}=\int \rho_w\zeta(\mathbf{r}',t)G_W(\psi)\,\mathrm{d}A,\qquad
G_W(\psi)=\frac{ga}{M_E}\sum_n(1+k'_n-h'_n)P_n(\cos\psi).$$

The three terms represent direct water attraction, induced potential and clock displacement. PREM load Love numbers are retained through degree 696 with the archived high-degree continuation. Eighteen loading constituents are synthesized with their astronomical nodal corrections. The complex convention is $f\,\mathrm{Re}[C\exp(-i\phi)]$; reversing the exponential sign requires conjugating $C$. The present analysis reads the frozen constituent and time-series tables rather than substituting an older loading sequence.

The eight named constituents are grouped as described above. Minor terms remain once as a fixed remainder $r_0$. On the actual weighted segment-centred sampling, solid, loading and total root-mean-square variations are respectively 2.928, 1.328 and $4.011\times10^{-18}$. Their ratio 0.331 is an amplitude-norm ratio, not an additive fraction of total power. The separately reported $0.89\pm0.55$ loading coefficient belongs to the alternative directly modelled, filtered reduction described below; it has not been recalculated as a separate coefficient of the present estimator.

### Joint estimator and zero-point choice

We fit

$$y_i=c_{s(i)}+A_Ls_{L,i}+A_Ss_{S,i}+A_Ds_{D,i}+r_{0,i}+\epsilon_i,$$

with 54 segment intercepts and three physical response coefficients. Weighted least squares uses the frozen Allan-based uncertainties $\sigma_i$, with $W_{ii}=1/\sigma_i^2$. A period noise coefficient $\alpha_p$ is estimated from within-segment overlapping Allan deviations at 256, 512, 1,024, 2,048 and 4,096 s, after removing the fixed unit tide. No Allan window crosses a segment boundary. The bin uncertainty is $\sigma_i=\alpha_{p(i)}/\sqrt{n_i}$, where $n_i$ is its retained member count. This is a working noise model, not stability calculated after joining fit-adjusted levels. Independent QR replay reproduces the eight-period design on the same rows before changing only its intercept grouping. All comparisons therefore hold sampling, correction values, physical templates and weights fixed.

The inspected interval and correction records contain no documented calibrated zero transfer for the 46 adjacent segment boundaries that share an eight-period intercept. They give valid times, but not a signed boundary transfer with uncertainty or a lock/relock history establishing unchanged reference levels. This motivates the segment design. The eight-period model's weighted residual sum of squares is 3,781.58; the segment model's is 3,713.64, with 46 additional intercept parameters. Their unweighted residual root-mean-square values are 24.114 and $23.934\times10^{-18}$. Reduced residual sums of squares are 1.1501 and 1.1455. The numerical improvement alone does not establish a physical jump at each boundary.

With period constants, weighted segment-mean residuals range from $-6.75$ to $12.00\times10^{-18}$. Adjacent standardized residual correlations, restricted to the same segment and separations of at most 900 s, are −0.127 and −0.148 for the period and segment designs. Deleting a period gives lunar point-estimate ranges 0.877–1.052 and 0.885–1.093, respectively (Extended Data Fig. 1). These checks retain substantial lunar support under either reference-level assumption. They do not supply missing calibration logs. Coefficient proximity to one is not a model-selection rule.

### Statistical errors and conditional coverage

For each group the reported standard error is the larger of residual-scaled least squares and leave-one-UTC-day-out jackknife errors. Deletions remove a calendar day, refit all remaining coefficients and drop empty intercept columns. The jackknife variance is $(G-1)G^{-1}\sum_g(\hat A_{(-g)}-\overline A)^2$. Period-deletion errors are recorded separately. Extended Data Table 1 gives all components and the same-data intercept comparisons. Observations are repeated measurements of one clock pair, not thousands of independent experiments.

New conditional simulations apply both designs to the same 3,299-row sampling and heteroscedastic uncertainties. Each of four scenarios has 1,000 realizations: independent Gaussian noise; equal variance contributions from Gaussian white noise and a 6-h Ornstein–Uhlenbeck process within segments; the corresponding 24-h process within periods; and standardized Student-$t_5$ noise. The overall scale is the observed segment-model residual scale; all true physical response coefficients are one. Each realization recomputes both components of the standard-error rule. Seed 2026110617 fixes the simulation. Coverage of $\hat A\pm1.96u$ is 95.1–97.4% for the segment-model lunar coefficient and 95.4–96.8% for its neighbouring coefficient; Monte Carlo standard errors are about 0.4–0.7 percentage points (Extended Data Table 2). These are tests under declared noise laws, not a calibration against every possible disturbance.

The phase-relaxed model adds the lunar quadrature while retaining the prescribed M₂/N₂ relationship. Covariance contours use scaled least squares. Subset and deletion fits refit the same model on their retained rows. No shared-data estimates are averaged, and no half-daily coefficient is converted into a daily upper limit.

### Phase means, spectral density and sampling sidelobes

For the phase plot, $N$ contains segment constants and the two non-lunar groups. We project both $y-r_0$ and the unit lunar prediction with $M_N=I-N(N^TWN)^{-1}N^TW$, and average in twelve fixed M₂ phase bins. If $B$ is weighted bin averaging, the mean covariance is $BM_NC_yM_N^TB^T$, where $C_y$ is the scaled working observation covariance. It retains correlations between means and propagates nuisance estimation. The full unbinned response remains primary.

Figure 3c preserves the independently specified equal-weight, 54-intercept scan of the unchanged observed means, rather than replacing it with the amplitude fit's weights. Every trial sine–cosine pair and the data are projected against the same constants. For a reduction in squared residuals $\Delta\mathrm{RSS}(f)$ with dimensionless $y$, the nominal one-sided projection density is $S_y(f)=600\,\mathrm{s}\,\Delta\mathrm{RSS}(f)$ per Hz, or $10^{-6}$ times that value per µHz. Potential density is $S_W=c^4S_y$; amplitude density is $c^2\sqrt{S_y}$. Uniform-grid checks reproduce the conventional one-sided Fourier density. For interrupted data this normalization is a stated projection density, not a Parseval-calibrated variance over a filled year.^24^

The frequency step is 0.002729 µHz; the inverse calendar span is 0.032752 µHz. Fine plotting steps do not improve physical resolution. M₂-only and S₂-only astronomical injections use the same actual times, nodal factors and equal-weight segment projection. Power at the opposite principal frequency, divided by power at the injected frequency, gives 0.08027 and 0.08149. Conditional scans project out a freely phased sinusoid at the other frequency before scanning the target neighbourhood. Amplitude interference means that such corrections act on sampled waveforms or complex coefficients, not by subtracting scalar power spectra. Gaps alone do not predict the realization of measurement noise. Residual density can describe remaining measurement fluctuations, but includes possible model mismatch and cannot be called a pure instrumental noise floor.

### Instruments, environmental checks and the alternative reduction

An existing fixed-weight single-bin diagnostic in the eight-period reduction examined the pre-identified extreme mean at 2026-07-07 01:25 Beijing time (segment 46). Omitting that mean changed the daily coefficient from 0.678 to 0.721, a shift of 0.043 compared with its 0.359 standard error. The lunar coefficient changed by 0.039. This archived diagnostic kept the template and weights fixed; it did not recalibrate uncertainty. The point remains in the present 3,299-row sample. Its influence does not explain the weaker daily constraint or justify selecting observations to improve agreement with the tide.

The matched monitor calculation uses 1,482 rows with 887,882 nominal members, or 246.634 h, in P6–P8. Both baseline and augmented fits have identical members, segment labels and weights. Paired day-deletion replicates propagate uncertainty in their difference. The lunar, neighbouring and daily coefficient changes are respectively $0.00606\pm0.00627$, $0.00594\pm0.01453$ and $0.00791\pm0.01388$. The archive does not provide that paired control for the pre-summer periods or every laboratory transfer branch.

The alternative v68 reduction reports $A_L=0.97\pm0.14$ from approximately 544 h in 54 segments, with a 1,200-s triangular filter sampled every 600 s, equal weights, a direct-potential solid model and a continuous-run circular-residual-shift error. It reports $0.98\pm0.13$ with two-site ERA5 temperature regressors and a 474-h round-trip overlap changing lunar and whole-template coefficients by less than 0.005. These are author-reported manuscript results, not the present replay. The stated 98-h Sr chamber record is a distinct thermometer measurement; ERA5 2-m air temperatures are environmental proxies. Exact membership for the 474-h control and temperature-regression support must be supplied for an independent replay. These checks are not combined with the current uncertainty.

On the selected data and model, a common 24-h sine–cosine pair gives $A_L=1.036\pm0.133$; separate 24-h pairs in each period give $1.003\pm0.136$. These are mechanism-motivated daily sensitivity designs, not measurements of an independently observed thermal amplitude. Free 12-h pairs in each period give $0.751\pm0.242$ and a very poorly constrained neighbouring coefficient; the design competes with astronomical semidiurnal variation within short periods. It is retained as a sensitivity boundary, with no assumed laboratory disturbance assigned to it. A sequential residual diagnostic must project its test basis through the same physical-fit operator and propagate uncertainty.

## Data availability

The author review package contains the 3,299 derived means, fixed templates, noise weights, figure source tables and immutable input hashes. The original counters and membership ledger are held in the controlled experimental archive. [Authors to supply an editor-accessible location and confirm the permanent data-access statement and repository identifier before submission.]

## Code availability

The package contains the independent QR replay, same-data design comparison, conditional simulations, spectral calculations, covariance propagation and figure scripts, with software versions and a reproducible entry point. [Authors to confirm the code licence and permanent repository identifier before submission.]

## Author statements

**Author contributions:** [To be completed and approved by all authors.]

**Acknowledgements and funding:** [To be completed by the authors.]

**Competing interests:** [Declaration to be supplied by the authors.]

**Correspondence:** [Corresponding author names and email addresses to be supplied.]

**AI-assisted preparation:** OpenAI Codex assisted English drafting, numerical replay and figure preparation. [Authors to confirm their verification of the analyses, citations and final text, and responsibility for the submitted work.]

\clearpage

## References

1. Ludlow, A. D., Boyd, M. M., Ye, J., Peik, E. & Schmidt, P. O. Optical atomic clocks. *Rev. Mod. Phys.* **87**, 637–701 (2015). [https://doi.org/10.1103/revmodphys.87.637](https://doi.org/10.1103/revmodphys.87.637)
2. Mehlstäubler, T. E., Grosche, G., Lisdat, C., Schmidt, P. O. & Denker, H. Atomic clocks for geodesy. *Rep. Prog. Phys.* **81**, 064401 (2018). [https://doi.org/10.1088/1361-6633/aab409](https://doi.org/10.1088/1361-6633/aab409)
3. Voigt, C., Denker, H. & Timmen, L. Time-variable gravity potential components for optical clock comparisons and the definition of international time scales. *Metrologia* **53**, 1365–1383 (2016). [https://doi.org/10.1088/0026-1394/53/6/1365](https://doi.org/10.1088/0026-1394/53/6/1365)
4. Denker, H. et al. Geodetic methods to determine the relativistic redshift at the level of $10^{-18}$ in the context of international timescales: a review and practical results. *J. Geod.* **92**, 487–516 (2018). [https://doi.org/10.1007/s00190-017-1075-1](https://doi.org/10.1007/s00190-017-1075-1)
5. Schröder, S., Stellmer, S. & Kusche, J. Potential and scientific requirements of optical clock networks for validating satellite-derived time-variable gravity data. *Geophys. J. Int.* **226**, 764–779 (2021). [https://academic.oup.com/gji/article/226/2/764/6212226](https://academic.oup.com/gji/article/226/2/764/6212226)
6. Lisdat, C. et al. A clock network for geodesy and fundamental science. *Nat. Commun.* **7**, 12443 (2016). [https://doi.org/10.1038/ncomms12443](https://doi.org/10.1038/ncomms12443)
7. Riehle, F. Optical clock networks. *Nat. Photon.* **11**, 25–31 (2017). [https://doi.org/10.1038/nphoton.2016.235](https://doi.org/10.1038/nphoton.2016.235)
8. Chou, C. W., Hume, D. B., Rosenband, T. & Wineland, D. J. Optical Clocks and Relativity. *Science* **329**, 1630–1633 (2010). [https://doi.org/10.1126/science.1192720](https://doi.org/10.1126/science.1192720)
9. McGrew, W. F. et al. Atomic clock performance enabling geodesy below the centimetre level. *Nature* **564**, 87–90 (2018). [https://doi.org/10.1038/s41586-018-0738-2](https://doi.org/10.1038/s41586-018-0738-2)
10. Grotti, J. et al. Geodesy and metrology with a transportable optical clock. *Nat. Phys.* **14**, 437–441 (2018). [https://doi.org/10.1038/s41567-017-0042-3](https://doi.org/10.1038/s41567-017-0042-3)
11. Dimarcq, N. et al. Roadmap towards the redefinition of the second. *Metrologia* **61**, 012001 (2024). <https://doi.org/10.1088/1681-7575/ad17d2>
12. Lindvall, T. et al. Coordinated international comparisons between optical clocks connected via fiber and satellite links. *Optica* **12**, 843–852 (2025). <https://doi.org/10.1364/OPTICA.561754>
13. Hou, L. et al. Yb/Sr optical clock comparison at $2.2\times10^{-18}$ uncertainty over a 1350-km fiber link. *arXiv*, 2610.34250v1 (2026). [https://arxiv.org/abs/2610.34250v1](https://arxiv.org/abs/2610.34250v1)
14. Jia, Z.-P. et al. Improved systematic evaluation of a strontium optical clock with uncertainty below $1\times10^{-18}$. *Metrologia* **63**, 025002 (2026). [https://doi.org/10.1088/1681-7575/ae449e](https://doi.org/10.1088/1681-7575/ae449e)
15. Zhu, Q. et al. Ytterbium lattice clock with systematic uncertainty of $1.3\times 10^{-18}$ and instability at the $10^{-19}$ level. *arXiv*, 2606.10514v2 (2026). [https://arxiv.org/abs/2606.10514v2](https://arxiv.org/abs/2606.10514v2)
16. Petit, G. & Luzum, B. (eds) IERS Conventions (2010). *IERS Technical Note* **36** (2010). [https://iers-conventions.obspm.fr/content/tn36.pdf](https://iers-conventions.obspm.fr/content/tn36.pdf)
17. CNES. FES2022 (Finite Element Solution) Tidal model (Version 2024). CNES [https://doi.org/10.24400/527896/A01-2024.004](https://doi.org/10.24400/527896/A01-2024.004) (2024).
18. Farrell, W. E. Deformation of the Earth by surface loads. *Rev. Geophys.* **10**, 761–797 (1972). [https://doi.org/10.1029/RG010i003p00761](https://doi.org/10.1029/RG010i003p00761)
19. Han, D. & Wahr, J. The viscoelastic relaxation of a realistically stratified earth, and a further analysis of postglacial rebound. *Geophys. J. Int.* **120**, 287–311 (1995). [https://doi.org/10.1111/j.1365-246x.1995.tb01819.x](https://doi.org/10.1111/j.1365-246x.1995.tb01819.x)
20. Stahl, K. et al. Optical clock network tracks tidal variations of the gravity potential. *arXiv*, 2610.39635v1 (2026). [https://arxiv.org/abs/2610.39635v1](https://arxiv.org/abs/2610.39635v1)
21. Yao, J. et al. Optical-Clock-Based Time Scale. *Phys. Rev. Applied* **12**, 044069 (2019). <https://doi.org/10.1103/PhysRevApplied.12.044069>
22. Vincent, A. & Müller, J. Detection of time variable gravity signals using terrestrial clock networks. *Adv. Space Res.* **73**, 3312–3320 (2024). <https://doi.org/10.1016/j.asr.2023.07.058>
23. NOAA. Harmonic constituents. *NOAA Tides and Currents*. [https://tidesandcurrents.noaa.gov/harcon.html?id=8577330](https://tidesandcurrents.noaa.gov/harcon.html?id=8577330) (accessed 6 November 2026).
24. VanderPlas, J. T. Understanding the Lomb–Scargle periodogram. *Astrophys. J. Suppl. Ser.* **236**, 16 (2018). <https://doi.org/10.3847/1538-4365/aab766>

\clearpage

## Extended Data

![Extended Data Figure 1](figures/ed_figure1.png)

**Extended Data Fig. 1 | Same-data comparison of reference-level designs.** **a,** Weighted mean residual of each segment after the eight-period joint fit. The additional segment intercepts make these means zero by construction, so a zero line would not demonstrate calibration. **b,** Lunar point estimates after deleting each observing period under eight-period and 54-segment designs. Both use the same frozen observations, physical templates, corrections and noise weights. These diagnostics do not replace lock/relock or zero-transfer records.

![Extended Data Figure 2](figures/ed_figure2.png)

**Extended Data Fig. 2 | Conditional semidiurnal scans.** Equal-weight scans of the same 3,299 observations with 54 segment intercepts. **a,** M₂ neighbourhood before and after projection of a sine–cosine pair at S₂. **b,** S₂ neighbourhood before and after projection at M₂. Dotted lines show the astronomical target frequencies. These are descriptive projections on shared observations, not additional detection probabilities.

\clearpage

**Extended Data Table 1 | Estimator and uncertainty comparison.** All directly replayed designs use the same 3,299 means, physical templates and Allan-based weights. Errors are standard errors. The alternative filtered estimate is separately labelled author-reported.

| Design                | Lunar         | Near_12h      | Diurnal       | Status          |
|:----------------------|:--------------|:--------------|:--------------|:----------------|
| S54                   | 1.000 ± 0.132 | 0.925 ± 0.365 | 0.579 ± 0.538 | Replayed        |
| G29                   | 0.984 ± 0.124 | 1.093 ± 0.298 | 0.759 ± 0.420 | Replayed        |
| P8                    | 0.987 ± 0.123 | 1.129 ± 0.288 | 0.678 ± 0.359 | Replayed        |
| Filtered, 54 segments | 0.97 ± 0.14   | 0.90 ± 0.29   | 0.35 ± 0.51   | Author-reported |

| Group     |   Estimate |   Scaled_LS |   Day_JK |   Period_JK |   Reported_SE |
|:----------|-----------:|------------:|---------:|------------:|--------------:|
| Lunar     |     1.0004 |      0.132  |   0.1218 |      0.147  |        0.132  |
| Near-12 h |     0.9251 |      0.2993 |   0.3649 |      0.3531 |        0.3649 |
| Diurnal   |     0.5792 |      0.3887 |   0.5381 |      0.7735 |        0.5381 |

**Extended Data Table 2 | Conditional 95% interval coverage.** Each scenario has 1,000 simulated realizations per design, with fixed observed sampling and weights. Values are percentages for the larger-of-LS-and-day-jackknife rule, using multiplier 1.96. They assess the specified scenarios, not unknown systematic effects.

| scenario            | design   |   Diurnal |   Lunar |   Near12h |
|:--------------------|:---------|----------:|--------:|----------:|
| 50% OU 24 h, period | P8       |      97.9 |    98   |      97.3 |
| 50% OU 24 h, period | S54      |      96.4 |    95.1 |      95.4 |
| 50% OU 6 h, segment | P8       |      94.7 |    95.7 |      96   |
| 50% OU 6 h, segment | S54      |      95.8 |    95.6 |      96.3 |
| Student t (df 5)    | P8       |      96.8 |    96.3 |      96.2 |
| Student t (df 5)    | S54      |      96.2 |    96.1 |      96.8 |
| Gaussian            | P8       |      95.7 |    96.2 |      95.9 |
| Gaussian            | S54      |      95.5 |    97.4 |      96.7 |

**Extended Data Table 3 | Astronomical constituent guide.** Names specify forcing and frequency; one response coefficient multiplies each complete group with its internal ratios and phases fixed.

| Symbol   |   Period_h | Meaning                     | Group     |
|:---------|-----------:|:----------------------------|:----------|
| M2       |     12.421 | Principal lunar semidiurnal | Lunar     |
| N2       |     12.658 | Lunar elliptic semidiurnal  | Lunar     |
| S2       |     12     | Principal solar semidiurnal | Near-12 h |
| K2       |     11.967 | Lunisolar semidiurnal       | Near-12 h |
| K1       |     23.934 | Lunisolar diurnal           | Diurnal   |
| O1       |     25.819 | Principal lunar diurnal     | Diurnal   |
| P1       |     24.066 | Principal solar diurnal     | Diurnal   |
| Q1       |     26.868 | Lunar elliptic diurnal      | Diurnal   |
