# Tidal potential measured on a coastal–inland optical-clock baseline

[Author list and affiliation assignments to be completed by the authors]

^1^ Hefei National Laboratory, University of Science and Technology of China, Hefei, China

^2^ Shanghai Research Center for Quantum Sciences and CAS Center for Excellence in Quantum Information and Quantum Physics, University of Science and Technology of China, Shanghai, China

^3^ Hefei National Research Center for Physical Sciences at the Microscale and School of Physical Sciences, University of Science and Technology of China, Hefei, China

^4^ Innovation Academy for Precision Measurement Science and Technology, Chinese Academy of Sciences, Wuhan, China

^5^ Jinan Institute of Quantum Technology and CAS Center for Excellence in Quantum Information and Quantum Physics, University of Science and Technology of China, Jinan, China

^6^ Time and Frequency Geodesy Center (TFGC), School of Geodesy and Geomatics, Wuhan University, Wuhan, China

## Abstract

Optical clocks can sense Earth's changing gravitational potential through their relative rates. The principal lunar tide repeats every 12.42 hours, whereas the principal solar tide repeats every 12 hours. Their changing relative phase offers a way to distinguish two nearby signals. We compare clocks in coastal Shanghai and inland Wuhan, connected by a 1,350-km fibre link, using 545.9 hours of observations distributed across a year. Jointly estimated responses are $0.99\pm0.12$ for the lunar semidiurnal group and $1.13\pm0.29$ for the neighbouring semidiurnal group, relative to the combined solid-Earth and ocean-loading prediction. Loading contributes about one third of the predicted variation. The approximately daily response is less precisely determined. The lunar response persists across observing periods and changes little when a simultaneous fibre monitor is included on its summer overlap.

## Main text

Optical clocks turn a comparison of time into a measurement of gravitational potential: clocks at different potentials run at different rates.^1,2^ Fibre networks now connect clocks in separate laboratories while preserving the stability needed to compare them.^3,4^ This has extended chronometric levelling from laboratory height differences to geographically separated and transportable clocks.^5,6,7,8^ A network can also follow a potential that changes with time. Doing so requires identifying a common physical variation amid changes in the clocks and their connections. Tides provide a particularly well-specified signal, because their frequencies and phases follow the motion of the Moon and Sun.^9,10,11^

Two strong tidal rhythms are close but different. The principal lunar semidiurnal tide, M₂, repeats in about 12.42 h; the principal solar semidiurnal tide, S₂, repeats in exactly 12 h. The corresponding lunar maximum arrives about 50 min later on successive solar days. Over several weeks, the lunar tide therefore moves through the daily laboratory cycle. A comparison that samples different dates can use this phase change to distinguish neighbouring half-daily responses. The relevant baseline is not simply the number of accumulated hours: it is also where those hours fall in the relative lunar–solar cycle.

Here we use that phase coverage in a comparison between coastal Shanghai and inland Wuhan. We estimate a lunar group, M₂+N₂, and a neighbouring group, S₂+K₂, together in one model. N₂ adds a lunar component associated with the Moon's elliptical orbit; K₂ includes both lunar and solar forcing. Within each group, astronomical phases and relative amplitudes remain fixed by the prediction. A third group contains the approximately daily tides. This construction asks how strongly the observed clock-rate variation follows each prescribed pattern, without first removing an empirical daily oscillation.

### A baseline sensitive to ocean loading

The experiment compares a strontium clock in Shanghai with a ytterbium clock in Wuhan. The stations are 692 km apart and connected through Hefei by a 1,350-km phase-stabilized fibre link (Fig. 1a).^12^ Evaluations of the clock systems report systematic uncertainties below $10^{-18}$ for Sr and $1.3\times10^{-18}$ for Yb.^13,14^ These evaluations characterize the clock apparatus; the statistical errors of the tidal responses are obtained from the interrupted comparison itself. The measured variation is that of the Wuhan-Yb/Shanghai-Sr frequency ratio. A positive variation means that Wuhan runs faster relative to Shanghai.

The Moon and Sun affect this ratio in several ways. Their gravitational field changes, the solid Earth deforms and the clocks move with it. Ocean tides redistribute water, adding its attraction and the response of the underlying Earth. We combine a solid-tide prediction based on IERS 2010 with ocean loading derived from FES2022 elevations and a full effective-potential loading kernel (Methods).^15,16,17,18^ Shanghai's proximity to the East China Sea makes the ocean contribution appreciable relative to inland Wuhan. The clocks therefore test a potential difference in which the ocean is a substantial part of the physical prediction.

For M₂, the differential solid and loading amplitudes are respectively $3.43\times10^{-18}$ and $1.42\times10^{-18}$ in fractional clock rate. Their phases differ by 19.8°, producing a combined amplitude of $4.78\times10^{-18}$ (Fig. 1b). The components must be added as vectors, because their maxima do not occur together. On the actual weighted observations, after removing period constants, loading has 33.7% of the combined prediction's root-mean-square variation. This is a measure of the model contribution, rather than a separately measured loading coefficient. The response coefficients reported below multiply the combined potential.

Eight observing periods extend from September 2025 to August 2026 (Fig. 1c). The retained 3,299 ten-minute observations contain 545.9 h of nominal one-second measurements in 54 valid segments. Interruptions remain absent from the record: we neither fill them with predictions nor compress calendar time for estimation. The earlier periods and the June–August observations sample different lunar–solar phases (Fig. 1d). Summer supplies about half the operating time and a broad range of relative phase; the earlier observations add another part of the year to the comparison.

### Two semidiurnal responses in one measurement

The joint fit gives a lunar response $A_L=0.99\pm0.12$ and a neighbouring semidiurnal response $A_S=1.13\pm0.29$. A coefficient of one means agreement with the predicted potential variation. Both groups are estimated simultaneously with the daily group and eight period constants, using weights derived from the observed frequency noise. Their correlation is −0.36. The quoted uncertainties are standard errors obtained by the stated scaled least-squares and day-deletion rule; conditional coverage checks and the separate period-deletion errors are given in Methods and Extended Data Table 1.

Figure 2 shows the full record ordered by M₂ phase. Before averaging, the observations and the unit lunar prediction undergo the same removal of period constants and the other physical groups. This is essential: changing the data alone would change the shape being compared. Twelve phase intervals show the recurring modulation, while the underlying 3,299 points and their support counts remain visible. The uncertainty of the removed terms is propagated into the phase means. The amplitude is estimated from the original observation rows, rather than by fitting the twelve displayed means.

The phase is also tested by allowing the lunar pattern a component one quarter-cycle away from the predicted phase. Its in-phase and quadrature coefficients are $0.99\pm0.12$ and $-0.18\pm0.14$, respectively. The result is close to the predicted phase and does not require a freely moving tidal waveform. The daily group gives $A_D=0.68\pm0.36$ (Fig. 3a,b). It is less precisely determined, but it is already present in the same joint model: uncertainty in that group and its correlation with the half-daily groups are included in their estimation.

The semidiurnal spectrum provides a direct view of the measured variation in physical units (Fig. 3c). A prominent feature lies near M₂, with further structure in the neighbouring 12-h band. The left axis expresses power density as gravitational-potential variation; the right gives the same density in fractional-frequency units. For scale, a fractional clock-rate variation of $10^{-18}$ corresponds to about $0.09\,\mathrm{m^2/s^2}$ of potential difference. Removing the fitted physical tides substantially reduces the semidiurnal structure.

The smaller spectral peaks also carry the imprint of the observing schedule. Interruptions distribute a narrow oscillation into a central feature and neighbouring sidelobes, whose positions and heights depend on the sampling and weights. In this record, the largest local maximum in the 12-h neighbourhood need not coincide exactly with S₂. We therefore identify the two semidiurnal groups by their simultaneous astronomical templates and date-dependent phase coverage, rather than assigning every spectral maximum to a separate tide. The phase display and spectrum are views of these same observations, not additional independent measurements.

### Support across the year and a transmission control

The lunar coefficient is $1.10\pm0.21$ before summer and $0.80\pm0.18$ in summer. Removing each observing period in turn leaves point estimates between 0.88 and 1.05 (Fig. 4a). These overlapping analyses show where the full-record response is supported. They do not turn the eight observing periods into eight independent experiments, and they are not averaged to obtain another headline estimate. The main fit continues to use all eight periods across the full annual span.

Unknown reference levels are represented by period constants, fitted jointly with the tidal coefficients. This describes changes within the observed periods without constructing a calibrated absolute frequency level across the year. Tests that give the original groups or all 54 segments their own constants are reported in Methods. With the same observations, physical templates and noise weights, the lunar coefficients remain close to one. This provides a direct check that the lunar response is not created by the chosen number of static reference levels; it does not establish that every interruption preserved an absolute calibration.

The fibre round-trip record supplies a targeted control of the monitored transmission channel. Its successfully matched overlap contains 246.6 h in the three summer periods, from 29 June to 25 August 2026. Adding this recorded signal to the fit changes the lunar coefficient by $0.0064\pm0.0061$ and the neighbouring semidiurnal coefficient by $0.0040\pm0.0125$ (Fig. 4b). Each difference compares identical clock observations with and without the monitor; the error accounts for that pairing. This short-overlap control addresses transmission coupling where it was recorded. It neither reduces the main fit to summer nor supplies a control for unobserved clock effects and laboratory branches.

Environmental variation is approached through recorded channels and physical mechanisms. Heating and operating schedules motivate examination of 24-h structure, whereas a free 12-h term can compete directly with the astronomical semidiurnal groups over a short period. We keep the astronomical estimate as the primary result and treat such terms as residual diagnostics or explicit sensitivity models. Residual tests account for the projection introduced by the physical fit. The observation model, the scope of the available environmental records and the limits of the solid-tide approximation are specified in Methods.

### Measuring a changing potential with a clock network

The geographical contrast and the temporal coverage contribute different information. The coastal–inland baseline makes ocean loading important to the predicted potential. Observations at different lunar–solar phases permit two nearby half-daily responses to be estimated within one physical model. Together they extend the clock comparison from a static rate difference to a measurement of prescribed time-dependent potential components. The present result concerns the combined solid and loading response; the substantial predicted loading contribution motivates a future measurement that separates those contributions themselves.

Hou et al. report an absolute Yb/Sr frequency ratio on the same link, with summer observations overlapping this study.^12^ Here the scientific question is the separation of tidal components in an extended interrupted record; the absolute ratio and the earlier tidal-correlation significance are not re-reported. Independent, contemporaneous European clock-network observations by Stahl et al. use different baselines and mixtures of daily and half-daily tides.^19^ The geographical and temporal comparisons are complementary. Longer coastal records, accompanied by calibrated transfer branches, could make optical-clock networks probes of the ocean-loading contribution as well as of the combined tidal potential.

\clearpage

## Methods

### What the tidal names mean

A tidal constituent is one predictable rhythm in the changing gravitational field, not an extra wave discovered by fitting the clock data. The names are conventional astronomical labels. A subscript 2 denotes a roughly twice-daily rhythm and a subscript 1 a roughly once-daily rhythm; the periods need not divide the 24-h solar day exactly.^20^

M₂ is the principal lunar semidiurnal tide, with period 12.42 h. S₂ is the principal solar semidiurnal tide, with period 12.00 h. Their slowly changing relative phase produces the familiar spring–neap modulation. N₂, at 12.66 h, describes part of the modulation associated with the Moon's elliptical orbit. K₂, at 11.97 h, contains both lunar and solar forcing. Thus our neighbouring S₂+K₂ group is not a purely solar measurement. The approximately daily group contains the lunisolar K₁ (23.93 h), lunar O₁ (25.82 h), solar P₁ (24.07 h) and lunar elliptic Q₁ (26.87 h) constituents. Their names, periods and grouping are collected in Extended Data Table 2. Grouping fixes each member's relative amplitude and phase to the physical prediction; it does not assign a separate fitted response to every member.

The clocks sense gravitational potential, rather than water height. Each astronomical rhythm contributes through the tide-generating field, the deformation of the Earth and the associated redistribution of ocean water. The solid and ocean responses can differ in phase, which is why the combined clock prediction is assembled before comparison with observations.

### Frequency ratio, time and retained observations

The frequency-transfer apparatus and absolute-ratio measurement are described by Hou et al.; the clock evaluations provide their systematic budgets.^12,13,14^ We define $R=\nu_{\mathrm{Yb,Wuhan}}/\nu_{\mathrm{Sr,Shanghai}}$. With positive geodetic potential $W$, the varying signal is

$$y(t)=-\frac{\delta W_{\mathrm{Wuhan}}(t)-\delta W_{\mathrm{Shanghai}}(t)}{c^2}.$$

The period-relative beat conversion is $y_{\mathrm{rel}}=-d_p(f_{\mathrm{beat}}-f_{\mathrm{ref},p})/F_{1550}$, with $F_{1550}=1.933992\times10^{14}$ Hz. The recorded counter division gives $d_p=2$ in 2025 and $d_p=1$ in 2026, corresponding to a 2026 conversion magnitude of approximately $5.17\times10^{-15}$ per hertz. Summer group-resolved clock corrections are evaluated through the frequency chain in decimal arithmetic before taking the small ratio difference. Early periods retain relative levels where the absolute correction ledger is incomplete. Missing entries are not interpreted as measured zero. A static missing correction can be absorbed by a constant only over the interval in which that correction is actually constant.

The supplied 54 valid intervals identify the retained segments. Source counter files are read before forming bins, so intervals spanning midnight remain intact. Beijing-time labels are converted to UTC; nominal second indices and small timestamp jitter are retained in the membership audit. The interval selection contains 1,966,908 nominal one-second rows. The three-row difference from the printed interval total was reconciled at boundary seconds. Ten-minute means are formed separately in each segment, requiring at least 180 retained members. The accepted 3,299 means contain 1,965,327 members, equivalent to 545.924 h at nominal one-second sampling. Underfilled bins are excluded; no missing observation is replaced with a fitted value. Original group 22 is outside the supplied mask, and segment 48 is retained.

The data span 353.39 calendar days and 43 UTC dates with observations. Eight shared bin centres arise when different segments contribute separate partial bins; these remain separate observations with disjoint members. Their times are not collapsed into a continuous series. Substituting mean member times for bin centres changes the lunar coefficient from 0.9866 to 0.9872. The final row selection is inherited and audited; this manuscript does not assert that the selection was prospectively registered. In particular, the separate six-robust-standard-deviation selection and triangular filter used in another reduction are not silently applied here.

### Physical prediction and its approximation

The effective solid-tide potential can be written as the direct astronomical contribution plus the induced potential, minus the potential change due to clock displacement. The present implementation uses the IERS 2010 radial displacement sequence and the fixed conversion

$$y_{\mathrm{solid}}=-\frac{1+k_2-h_2}{h_2}\frac{g(u_{\mathrm{Wuhan}}-u_{\mathrm{Shanghai}})}{c^2},$$

with $h_2=0.6078$, $k_2=0.3010$ and $g=9.794\,\mathrm{m/s^2}$. This is an effective-potential approximation, not a degree- and frequency-resolved direct-potential reconstruction. The radial sequence includes degree-three and frequency-dependent displacement contributions, to which the same conversion is applied. The approximation is particularly relevant in the daily band: a prior model comparison found a K₁ amplitude deficit of about 18% relative to a potential-weighted reference. We therefore report the daily coefficient without interpreting it as a separate test of the Earth's daily response.

A bounded check changes only the semidiurnal potential coefficient from $k_2=0.3010$ to $k_{22}=0.29801$, holding $h_2$, the fixed remainder, sampling and loading unchanged. The solid semidiurnal multiplier changes by −0.43%, and the lunar fitted coefficient changes by +0.0030. This measures sensitivity to that one response factor. It neither reconstructs the full direct-potential model nor calibrates all template uncertainty. The model approximation and the statistical standard errors are kept separate.

Ocean loading is calculated from the FES2022 height field with the effective-potential kernel

$$\delta W_{\mathrm{load}}=\int\rho_w\zeta(\mathbf r',t)G_W(\psi)\,\mathrm dA,\qquad G_W(\psi)=\frac{ga}{M_E}\sum_n(1+k'_n-h'_n)P_n(\cos\psi).$$

The terms include seawater attraction, induced potential and clock displacement.^16,17,18^ The station phasors use PREM load Love numbers through degree 696 and the documented high-degree continuation. Eighteen loading constituents are synthesized with the declared complex-phase convention and astronomical nodal factors. For a coefficient $C$, the waveform is $f\,\mathrm{Re}[C\exp(-i\phi)]$. Conjugating $C$ requires reversing the exponential sign to preserve the waveform. The complete phasor inventory and convention accompany the figure source data.

The solid and loading predictions are sampled on the same observation times. Fixed astronomical harmonic coefficients form the eight named constituents; minor contributions are retained once as a fixed remainder. The weighted period-centred root-mean-square values of the solid, loading and total predictions are 3.278, 1.509 and $4.482\times10^{-18}$, respectively. Their ratio, $1.509/4.482=0.337$, is not the fraction of total power: the components have nonzero covariance. The loading coefficient is tied to the corresponding solid component in the primary grouped fit.

### Joint model, weights and reference levels

The fitted model is

$$y_i=c_{p(i)}+A_Ls_{M_2+N_2,i}+A_Ss_{S_2+K_2,i}+A_Ds_{K_1+O_1+P_1+Q_1,i}+r_{0,i}+\epsilon_i.$$

It has three response coefficients and eight period constants. The astronomical phase and relative component amplitudes are fixed within each group. Weighted least squares uses $1/\sigma_i^2$, with $\sigma_i$ derived from the within-run Allan-based noise estimates stored with the observations. No empirical daily term is removed before this estimation, and no filtered state estimate is substituted for an observation. This does not produce a long-term stability record: the fitted constants are nuisance parameters, not measured corrections with which to join separate runs.

One constant per period assumes that the retained segments in that period share a reference level. Experimental continuity across all interruptions has not been established from the available logs. The same-weight, same-template checks use 29 group constants and 54 segment constants, giving lunar coefficients $0.984\pm0.124$ and $1.000\pm0.132$, respectively. The corresponding neighbouring-group coefficients are $1.093\pm0.298$ and $0.925\pm0.365$. Equal weighting with 54 segment constants gives $0.946\pm0.141$ for the lunar group. These tests separate reference-level and weighting choices; they are not independent experiments or estimates to average.

### Uncertainty and support checks

For each response coefficient we report the larger of the residual-scaled least-squares error and a leave-one-UTC-day-out jackknife error. For the lunar coefficient these are 0.1231 and 0.1116; for the neighbouring coefficient, 0.2825 and 0.2878; and for the daily coefficient, 0.2860 and 0.3586. The separate leave-period errors are 0.1314, 0.3256 and 0.4118. Extended Data Table 1 retains these sources separately. Taking a maximum of marginal errors does not construct a new joint confidence region.

Archived simulations test this lunar uncertainty rule conditionally on the specified sample, weights and noise scenarios. Thirteen scenarios, with 10,000 realizations each, include white noise and specified correlated components on one-, six- and 24-h timescales, grouped within segments or periods. Recounting the saved realizations gives 94.16–97.79% coverage of nominal 95% intervals. This checks the lunar estimator under those scenarios; it is not a distribution-free calibration of every coefficient or of model uncertainty. We do not convert the response divided by its error into a universal detection probability.

Subset and deletion fits retain the same physical definitions and recalculate their coefficients and errors on the retained rows. The phase-relaxed fit adds the lunar quadrature template while preserving the M₂–N₂ phase relation. The joint ellipse in Fig. 3b uses the scaled least-squares covariance and radii one and two. Those contours show covariance geometry, rather than separately calibrated joint confidence levels.

### Phase display and frequency-domain view

Let $N$ contain the period constants and the two non-lunar groups, and $W$ contain the observation weights. The nuisance residual operator is $M_N=I-N(N^TWN)^{-1}N^TW$. We apply it both to $y-r_0$ and to the unit lunar template. The M₂ crest phase defines twelve fixed 30° bins. If $B$ performs weighted bin averaging, the phase-mean covariance is $BM_NC_yM_N^TB^T$, with the full scaled working observation covariance $C_y$. It has rank eleven because the projected means are correlated. All 3,299 projected rows are displayed, with each bin's row count; the primary amplitude is never estimated from the phase bins.

For the spectra, each trial sine–cosine pair and the observations are projected against the same eight period constants. Relative weights are normalized to mean one. The reduction in weighted squared residuals is $\Delta\mathrm{RSS}_w(f)$. We define the nominal one-sided projection density as $S_y(f)=600\,\mathrm{s}\,\Delta\mathrm{RSS}_w(f)$ when the response is expressed as a dimensionless fractional frequency. A density per microhertz is $10^{-6}$ times the density per hertz. The potential axes follow $S_W=c^4S_y$, and amplitude densities follow $\sqrt{S_W}=c^2\sqrt{S_y}$. The use of microhertz on both axes therefore changes the density's numerical value as well as its label.

This weighted sinusoidal scan is evaluated at the real UTC times, with no gap filling or compression. Its fine grid samples the spectral shape but does not improve physical resolving power. The spectra before and after subtraction use the same rows and normalization; the latter subtracts the three physical groups fitted to those observations. The displayed ranges are 21–24.5 µHz and, in Extended Data Fig. 1, 9.5–12.5 µHz. At the actual sampling and weights, the maximum phase-dependent projection of a sinusoid at M₂ into S₂, or vice versa, is 11.8% in squared norm. Window sidelobes and interference can shift local maxima, so their frequencies do not alone identify individual constituents.

Extended Data Fig. 2 expresses the same spectra as amplitude density. This is a description of measurement residuals, which may include remaining tidal mismatch, clock noise, transfer noise and environmental effects. It is not a pure instrumental noise floor or a minimum detectable potential. Under uniform sampling and stationary noise, a sinusoidal quadrature error can scale as $\sqrt{S_W/T_{\mathrm{obs}}}$. For this interrupted weighted record the applicable calculation is instead $KC_yK^T$, where $K$ is the projected regression operator. The annual span controls the available phase separation; observing time, noise and sampling together determine precision.

### Recorded controls and daily residuals

The located round-trip monitor is paired to the same valid nominal seconds as the clock data before aggregation. The matched fit contains 1,482 rows and 887,882 members, or 246.634 h, confined to P6–P8. Its intervals do not cover the earlier periods. Baseline and monitor-augmented fits use identical observations and weights. Paired day-deletion replicates propagate the covariance of their coefficient difference. The resulting changes are $0.006408\pm0.006086$ for the lunar group, $0.003985\pm0.012514$ for the neighbouring group and $0.001522\pm0.010732$ for the daily group. The monitored route is the scope of this control; the complete 545.9-h clock record remains the input to the principal fit.

Outdoor weather and direct clock thermometry are distinct measurements. Meteorological records are environmental proxies rather than measurements of the clocks' thermal enclosures. A mechanism-based 24-h diagnostic should use a declared temperature or operating-time relationship. If performed after the physical fit, the same residual operator must be applied to the daily basis as to the observations, with uncertainty propagated. Free 12-h regressors are sensitivity models because they can be nearly degenerate with astronomical semidiurnal components in short periods; they do not establish the presence or amplitude of an actual laboratory disturbance.

### Data availability

Derived observation tables, fixed templates, weights, figure source tables and their input hashes are assembled in the author review package. The raw-counter membership audit and original files remain in the controlled research archive. [Authors to confirm the editorial-access link, raw-data access terms and permanent repository identifier before submission.]

### Code availability

The author review package includes the independent primary-estimator replay, covariance propagation, spectral calculations and figure-generation scripts. It reproduces the supplied derived-input analysis; raw selection and spatial model generation have separate archived dependencies. [Authors to confirm the public release, software licence and permanent code identifier before submission.]

### AI-assisted preparation

OpenAI Codex assisted English drafting, source reconciliation, independent numerical checks and figure preparation. [Authors to confirm and describe their scientific verification and responsibility for the final manuscript.]

## Author statements

**Author affiliations:** The institutional list will follow the verified frequency-ratio manuscript; author-to-affiliation assignments remain to be confirmed.

**Author contributions:** [To be completed by the authors.]

**Acknowledgements and funding:** [To be completed by the authors.]

**Competing interests:** [Declaration to be supplied by the authors.]

**Correspondence:** [Names and email addresses to be supplied.]

\clearpage

## References

1. Ludlow, A. D., Boyd, M. M., Ye, J., Peik, E. & Schmidt, P. O. Optical atomic clocks. *Rev. Mod. Phys.* **87**, 637–701 (2015). [https://doi.org/10.1103/revmodphys.87.637](https://doi.org/10.1103/revmodphys.87.637)
2. Mehlstäubler, T. E., Grosche, G., Lisdat, C., Schmidt, P. O. & Denker, H. Atomic clocks for geodesy. *Rep. Prog. Phys.* **81**, 064401 (2018). [https://doi.org/10.1088/1361-6633/aab409](https://doi.org/10.1088/1361-6633/aab409)
3. Lisdat, C. et al. A clock network for geodesy and fundamental science. *Nat. Commun.* **7**, 12443 (2016). [https://doi.org/10.1038/ncomms12443](https://doi.org/10.1038/ncomms12443)
4. Riehle, F. Optical clock networks. *Nat. Photon.* **11**, 25–31 (2017). [https://doi.org/10.1038/nphoton.2016.235](https://doi.org/10.1038/nphoton.2016.235)
5. Chou, C. W., Hume, D. B., Rosenband, T. & Wineland, D. J. Optical Clocks and Relativity. *Science* **329**, 1630–1633 (2010). [https://doi.org/10.1126/science.1192720](https://doi.org/10.1126/science.1192720)
6. McGrew, W. F. et al. Atomic clock performance enabling geodesy below the centimetre level. *Nature* **564**, 87–90 (2018). [https://doi.org/10.1038/s41586-018-0738-2](https://doi.org/10.1038/s41586-018-0738-2)
7. Bothwell, T. et al. Resolving the gravitational redshift across a millimetre-scale atomic sample. *Nature* **602**, 420–424 (2022). [https://doi.org/10.1038/s41586-021-04349-7](https://doi.org/10.1038/s41586-021-04349-7)
8. Grotti, J. et al. Geodesy and metrology with a transportable optical clock. *Nat. Phys.* **14**, 437–441 (2018). [https://doi.org/10.1038/s41567-017-0042-3](https://doi.org/10.1038/s41567-017-0042-3)
9. Voigt, C., Denker, H. & Timmen, L. Time-variable gravity potential components for optical clock comparisons and the definition of international time scales. *Metrologia* **53**, 1365–1383 (2016). [https://doi.org/10.1088/0026-1394/53/6/1365](https://doi.org/10.1088/0026-1394/53/6/1365)
10. Denker, H. et al. Geodetic methods to determine the relativistic redshift at the level of $10^{-18}$ in the context of international timescales: a review and practical results. *J. Geod.* **92**, 487–516 (2018). [https://doi.org/10.1007/s00190-017-1075-1](https://doi.org/10.1007/s00190-017-1075-1)
11. Schröder, S., Stellmer, S. & Kusche, J. Potential and scientific requirements of optical clock networks for validating satellite-derived time-variable gravity data. *Geophys. J. Int.* **226**, 764–779 (2021). [https://academic.oup.com/gji/article/226/2/764/6212226](https://academic.oup.com/gji/article/226/2/764/6212226)
12. Hou, L. et al. Yb/Sr optical clock comparison at $2.2\times10^{-18}$ uncertainty over a 1350-km fiber link. *arXiv*, 2610.34250v1 (2026). [https://arxiv.org/abs/2610.34250v1](https://arxiv.org/abs/2610.34250v1)
13. Jia, Z.-P. et al. Improved systematic evaluation of a strontium optical clock with uncertainty below $1\times10^{-18}$. *Metrologia* **63**, 025002 (2026). [https://doi.org/10.1088/1681-7575/ae449e](https://doi.org/10.1088/1681-7575/ae449e)
14. Zhu, Q. et al. Ytterbium lattice clock with systematic uncertainty of $1.3\times 10^{-18}$ and instability at the $10^{-19}$ level. *arXiv*, 2606.10514v2 (2026). [https://arxiv.org/abs/2606.10514v2](https://arxiv.org/abs/2606.10514v2)
15. Petit, G. & Luzum, B. (eds) IERS Conventions (2010). *IERS Technical Note* **36** (2010). [https://iers-conventions.obspm.fr/content/tn36.pdf](https://iers-conventions.obspm.fr/content/tn36.pdf)
16. CNES. FES2022 (Finite Element Solution) Tidal model (Version 2024). CNES [https://doi.org/10.24400/527896/A01-2024.004](https://doi.org/10.24400/527896/A01-2024.004) (2024).
17. Farrell, W. E. Deformation of the Earth by surface loads. *Rev. Geophys.* **10**, 761–797 (1972). [https://doi.org/10.1029/RG010i003p00761](https://doi.org/10.1029/RG010i003p00761)
18. Han, D. & Wahr, J. The viscoelastic relaxation of a realistically stratified earth, and a further analysis of postglacial rebound. *Geophys. J. Int.* **120**, 287–311 (1995). [https://doi.org/10.1111/j.1365-246x.1995.tb01819.x](https://doi.org/10.1111/j.1365-246x.1995.tb01819.x)
19. Stahl, K. et al. Optical clock network tracks tidal variations of the gravity potential. *arXiv*, 2610.39635v1 (2026). [https://arxiv.org/abs/2610.39635v1](https://arxiv.org/abs/2610.39635v1)
20. NOAA. Harmonic constituents. *NOAA Tides and Currents*. [https://tidesandcurrents.noaa.gov/harcon.html?id=8577330](https://tidesandcurrents.noaa.gov/harcon.html?id=8577330) (accessed 6 November 2026).

\clearpage

## Figure legends

![](figures/figure1.png){width=180mm}

**Fig. 1 | Geometry and phase coverage of the clock comparison.** **a,** Coastal Shanghai Sr and inland Wuhan Yb, with the 1,350-km fibre route schematically drawn through Hefei. Geographic separation is 692 km. Neutral land and sea colours indicate geography, not a calculated potential field. **b,** Model M₂ phasors in fractional-frequency units, with the solid component as phase zero: solid 3.43, loading 1.42 and their sum 4.78, in $10^{-18}$. The phase difference is 19.8°. **c,** Actual observation dates and accepted nominal one-second sample-hours in eight periods. The 545.9-h total is distributed over 353.39 calendar days, with no observations inserted in gaps. **d,** S₂–M₂ astronomical phase, including nodal phase corrections, at the same 3,299 observation rows. Each period retains its own row membership. Panels a and b describe the geography and prediction; c and d show sampling, not statistical tests.

\clearpage

![](figures/figure2.png){width=180mm}

**Fig. 2 | The lunar modulation across the full observed record.** **a,** Twelve 30° phase-bin means after subtracting the fixed remainder and projecting observations and unit lunar prediction against identical period, neighbouring-semidiurnal and daily columns. Solid grey and dashed orange lines show the identically transformed unit and fitted predictions. Error bars are marginal standard errors from the propagated scaled working covariance, including nuisance estimation; the twelve means are correlated, with covariance rank eleven. **b,** All 3,299 projected observations from all eight periods, including their full ordinate range. **c,** Row counts in each phase interval. These are repeated observations of one clock comparison, not independent experimental replicates. The coefficient is fitted to the original rows using the noise weights, not to the displayed phase-bin means. The fold is a representation of those observations and supplies no independent significance test.

\clearpage

![](figures/figure3.png){width=180mm}

**Fig. 3 | Joint semidiurnal responses and their frequency-domain signature.** **a,** The three simultaneous response coefficients on all 3,299 rows. Error bars show the larger of scaled least-squares and UTC-day jackknife standard errors. The dashed line marks unit response. **b,** Lunar and neighbouring-semidiurnal coefficients with scaled least-squares covariance contours of radii one and two; the cross marks the unit prediction. The contours show covariance geometry, not calibrated joint confidence regions. **c,** Nominal weighted projection power density of the same observations after the fixed remainder and period constants are removed, before and after subtraction of their fitted three-group tide. Both traces use the same weights and normalization, retain real UTC gaps and include all spectral values in the displayed band. Left and right axes obey $S_W=c^4S_y$. Dotted lines mark astronomical M₂ and S₂ frequencies, not fitted peak positions. Sampling sidelobes and overlapping responses shape nearby maxima; individual peaks cannot be identified solely from proximity to a tidal frequency. The spectrum and phase display reuse the amplitude-fit observations.

\clearpage

![](figures/figure4.png){width=180mm}

**Fig. 4 | Support across observing periods and a matched transmission control.** **a,** Lunar coefficients from the full record, the pre-summer and summer subsets, and eight leave-period fits. Every point uses the same physical definitions, period-constant model and noise weights on its retained observations. Bars use that fit's scaled-LS/day-jackknife maximum; the pale band is the full-record standard error. The subset and deletion fits share observations. **b,** Coefficient changes when the recorded fibre monitor is added to identical paired clock observations: 1,482 rows, 887,882 nominal seconds and 246.6 h in summer P6–P8, from 29 June to 25 August 2026. Bars are paired day-jackknife standard errors. This panel tests the monitored transmission path on its available overlap; the principal tidal fit in a uses the full 545.9-h record across the year.

\clearpage

## Extended Data

![](figures/ed_figure1.png){width=180mm}

**Extended Data Fig. 1 | Daily-band structure on the principal observation design.** Nominal weighted projection densities before and after subtraction of the physical groups fitted to the same 3,299 rows. The weighting, eight period constants, UTC sampling and density normalization are those of Fig. 3c. Dotted lines mark the named astronomical daily constituents. Changes after subtraction include interference with the sampled semidiurnal contributions; they do not independently identify each daily constituent or set an upper bound on laboratory daily disturbances.

\clearpage

![](figures/ed_figure2.png){width=180mm}

**Extended Data Fig. 2 | Equivalent-potential amplitude densities.** **a,** Daily and **b,** semidiurnal bands from the same weighted scans, expressed as the square root of nominal power density. The right axis is the corresponding fractional-frequency density, with $\sqrt{S_W}=c^2\sqrt{S_y}$. Every trace retains the actual observation gaps. The residual follows a fitted subtraction on the same data, and includes remaining model mismatch and all measured noise channels. It is not an independently calibrated sensitivity or a pure clock or fibre noise floor; amplitude-estimation errors require the observation covariance and projected design described in Methods.

\clearpage

**Extended Data Table 1 | Statistical errors and reference-level sensitivity.** All entries below use the selected physical template and actual retained rows. The main rule is the larger of scaled LS and day jackknife; period jackknife is shown separately. These are standard errors, not added systematic corrections.

| Group     |   Estimate |   Scaled_LS |   Day_jackknife |   Period_jackknife |   Reported_SE |
|:----------|-----------:|------------:|----------------:|-------------------:|--------------:|
| Lunar     |     0.9866 |      0.1231 |          0.1116 |             0.1314 |        0.1231 |
| Near-12 h |     1.1291 |      0.2825 |          0.2878 |             0.3256 |        0.2878 |
| Diurnal   |     0.6779 |      0.286  |          0.3586 |             0.4118 |        0.3586 |

| Constants   | Lunar         | Near_12h      | Diurnal       |
|:------------|:--------------|:--------------|:--------------|
| 8 periods   | 0.987 ± 0.123 | 1.129 ± 0.288 | 0.678 ± 0.359 |
| 29 groups   | 0.984 ± 0.124 | 1.093 ± 0.298 | 0.759 ± 0.420 |
| 54 segments | 1.000 ± 0.132 | 0.925 ± 0.365 | 0.579 ± 0.538 |

**Extended Data Table 2 | Astronomical rhythms used in the three physical groups.** Periods are calculated from the constituent frequencies used in the template. The symbols denote astronomical components, not fitted empirical daily disturbances. K₂ contains lunar and solar forcing. The predicted relative amplitude and phase of members within each group are retained when fitting one group response.

| Symbol   |   Period_h | Meaning                     | Fit_group   |
|:---------|-----------:|:----------------------------|:------------|
| M2       |      12.42 | Principal lunar semidiurnal | Lunar       |
| N2       |      12.66 | Lunar elliptic semidiurnal  | Lunar       |
| S2       |      12    | Principal solar semidiurnal | Near-12 h   |
| K2       |      11.97 | Lunisolar semidiurnal       | Near-12 h   |
| K1       |      23.93 | Lunisolar diurnal           | Diurnal     |
| O1       |      25.82 | Principal lunar diurnal     | Diurnal     |
| P1       |      24.07 | Principal solar diurnal     | Diurnal     |
| Q1       |      26.87 | Lunar elliptic diurnal      | Diurnal     |

**Extended Data Table 3 | Conditional calibration of the lunar error rule.** Each stored scenario contains 10,000 simulated realizations. The table recounts coverage of the estimator-specific nominal 95% interval; it does not calibrate template errors, every other parameter, or arbitrary experimental noise. The scenario names preserve the archived one-, six- and 24-h correlation settings and their segment or period scope.

| scenario             |     n |   Coverage_95_percent |    Bias |
|:---------------------|------:|----------------------:|--------:|
| G0                   | 10000 |                 95.94 |  0.0025 |
| segment_tau1h_rho10  | 10000 |                 94.24 | -0.0001 |
| segment_tau1h_rho50  | 10000 |                 94.16 |  0.0025 |
| segment_tau6h_rho10  | 10000 |                 95.22 |  0.0004 |
| segment_tau6h_rho50  | 10000 |                 95.59 |  0.0004 |
| segment_tau24h_rho10 | 10000 |                 96    |  0.0008 |
| segment_tau24h_rho50 | 10000 |                 97.04 |  0.0017 |
| period_tau1h_rho10   | 10000 |                 94.65 | -0.0019 |
| period_tau1h_rho50   | 10000 |                 94.22 |  0      |
| period_tau6h_rho10   | 10000 |                 95.72 | -0.0029 |
| period_tau6h_rho50   | 10000 |                 96.49 |  0.0051 |
| period_tau24h_rho10  | 10000 |                 95.94 |  0.0006 |
| period_tau24h_rho50  | 10000 |                 97.79 | -0.002  |
