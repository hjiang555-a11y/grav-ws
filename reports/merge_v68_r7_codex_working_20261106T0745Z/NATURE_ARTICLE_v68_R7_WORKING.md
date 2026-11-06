# Lunar tidal potential measured on a coastal–inland optical-clock baseline

**WORKING DRAFT — v68/R7 synthesis, 6 November 2026.**

Prepared for author evaluation. This is not the unique merged submission manuscript: the round-specific R7 handoff and the matched v68 primary input chain remain outstanding. Both reductions are named wherever their observations or coefficients appear; no combined estimate or final primary estimator is asserted.

[Author list and affiliation assignments to be confirmed.]

## Abstract

Optical clocks probe changing gravitational potentials through their relative rates. The lunar M2 tide has a period of about 12.42 h, whereas S2 is exactly 12 h; their relative phase therefore changes with date. Shanghai–Wuhan observations sample this drift, allowing joint estimation of lunar M2+N2, neighbouring S2+K2 and diurnal responses. Segment- and period-based reductions of the shared record give lunar coefficients of $0.97\pm0.14$ and $0.99\pm0.12$, and neighbouring-band coefficients of $0.90\pm0.29$ and $1.13\pm0.29$, respectively. The reductions are not combined. The diurnal response is less tightly constrained within both joint models. Ocean loading contributes about one third of the combined predicted variation, while its separate coefficient remains unresolved. Full-record phase averaging preserves the identical transformation of observations and prediction. Adding a fibre round-trip monitor on matched 474-h support changes the reported lunar and whole-template scales by less than 0.005.

## Main text

The lunar semidiurnal tide M2 repeats approximately every 12.42 h, while the solar semidiurnal tide S2 repeats every 12 h. Their maxima consequently drift past one another as the date changes. A short observation can confuse these nearby patterns, but measurements distributed over their relative phase can distinguish their responses in one model. Shanghai–Wuhan optical-clock observations exploit this phase diversity to estimate a lunar group, M2+N2, separately from the neighbouring S2+K2 group. K2 contains both lunar and solar forcing; the grouping describes nearby frequencies rather than a division into purely lunar and purely solar causes. Within each group, astronomical phases and relative amplitudes follow the prescribed tidal prediction.^1^

Clock comparisons measure potential differences through the relative rates of atomic transitions.^2,3^ Static chronometric levelling has been demonstrated with laboratory, transportable and fibre-connected clocks.^4,5,6,7,8,9^ Time-varying potentials offer a different observable: a frequency-ratio change with a predicted astronomical phase, superimposed on changes in the clocks and their transfer system.^10,11,12^ On a coastal–inland baseline, redistributed ocean water supplies an appreciable contribution to that prediction. The measurement therefore combines a temporal discriminator—the evolving lunar–solar phase—with a geographical contrast sensitive to loading.

### Stations, potential and phase coverage

The comparison connects a strontium clock in Shanghai (31.130° N, 121.570° E) to a ytterbium clock in Wuhan (30.529° N, 114.357° E). The stations are 692 km apart and joined by a 1,350-km phase-stabilized fibre link through Hefei (Fig. 1).^13^ Evaluations of the two clocks report systematic uncertainties of $9.2\times10^{-19}$ for Sr and $1.3\times10^{-18}$ for Yb.^14,15^ These clock budgets and the uncertainty of a time-dependent tidal coefficient describe different quantities. The observable here is the fractional change of $R=\nu_{\mathrm{Yb,Wuhan}}/\nu_{\mathrm{Sr,Shanghai}}$; positive values mean that Wuhan runs faster relative to Shanghai.

With positive geodetic potential $W$, the predicted change is $y=-[\delta W_{\mathrm{Wuhan}}-\delta W_{\mathrm{Shanghai}}]/c^2$. The effective potential includes direct lunar and solar forcing, the potential induced by Earth's deformation, the clock's vertical displacement, and the complete ocean-loading contribution. In the direct-potential calculation, IERS 2010 terms are combined with a FES2022 ocean-height convolution containing seawater attraction, induced potential and displacement.^1,16,17,18^ The response is to this combined potential at the clock sites, not to the sea height in a nearby ocean grid cell.

In that prediction, the differential M2 solid and loading amplitudes are $3.41\times10^{-18}$ and $1.42\times10^{-18}$, separated by about 20° and adding to $4.77\times10^{-18}$ (Fig. 1b). On the segment-centred sampling, their RMS values are 3.0, 1.35 and $4.1\times10^{-18}$ for solid, loading and combined signals. Loading thus contributes roughly one third of the predicted variation. By contrast, allowing a separate loading coefficient gives $0.89\pm0.55$: the observations do not resolve that coefficient separately. The distinction between a substantial model contribution and an independently measured loading response sets the physical scope of the experiment.

Observations extend from September 2025 to August 2026. The segment-based reduction describes five campaigns, 54 segments and approximately 544 retained hours, including 274 h in summer. The period-based reduction groups the record into eight operating periods and 29 original groups, reporting 546.4 h before ten-minute bin acceptance. Its 3,299 accepted means contain 545.9 sample-hours. These counts reflect different processing and accounting; the bin count multiplied by ten minutes is not exposure. Figure 1 shows the campaign coverage of the segment reduction, while Fig. 2 uses every accepted bin of the period reduction. Both displays identify their own sampling.

The long summer coverage sweeps the lunar pattern through the solar day. This helps separate M2 from S2 even though observing gaps remain. Unknown reference levels are handled by nuisance intercepts, estimated jointly with the physical responses. Such intercepts permit comparisons of within-interval variation without asserting a calibrated absolute level across all interruptions. The choice of which intervals may share a zero point is an experimental assumption that must be supported by the correction record and operating history.

### Joint semidiurnal responses

We consider the lunar group M2+N2, the neighbouring S2+K2 group, and the diurnal group K1+O1+P1+Q1 in the same linear model. A fixed remainder carries the other predicted contributions at unit response. No empirical solar-day sinusoid is subtracted before estimating these physical groups. The segment-based reduction, denoted v68, uses equal weights, a common triangular filter for data and prediction, and 54 intercepts. The period-based reduction, denoted R7, uses ten-minute means, period noise weights and eight intercepts; its solid-potential implementation uses a specified displacement approximation. The definitions and error rules are retained separately throughout this working synthesis.

The reported v68 responses are $(A_L,A_S,A_D)=(0.97\pm0.14,\,0.90\pm0.29,\,0.35\pm0.51)$. The R7 responses, independently replayed from its saved input tables, are $(0.99\pm0.12,\,1.13\pm0.29,\,0.68\pm0.36)$ (Fig. 3a). The lunar–neighbouring-band correlations are −0.32 and −0.36, respectively. The diurnal coefficient remains in each joint design, so its coupling to the semidiurnal coefficients is already included in that design's uncertainty calculation. Its weaker constraint does not supply an additional requirement that the jointly estimated semidiurnal response vanish. These overlapping reductions are compared without averaging their coefficients, errors or significance.

The phase display makes the full-record observation visible without changing the estimator (Fig. 2). After subtracting the fixed remainder, the data and unit lunar template pass through the same nuisance projection and twelve fixed M2 phase intervals. The 3,299 individual R7 means are retained at their full range, and every phase interval contains observations from all eight periods and 31–36 UTC days. Errors on the phase means propagate the projection and averaging under the specified working covariance. The amplitude is estimated before phase averaging; the twelve correlated display means are not twelve independent measurements of it.

A separate phase-relaxed R7 fit yields in-phase and quadrature coefficients of $0.99\pm0.12$ and $-0.18\pm0.14$ (Fig. 3b). The quadrature rotates the prescribed M2+N2 pattern as a whole, retaining the relative constituent phases and amplitudes. It tests a common lunar-band phase response, rather than assigning arbitrary phases to each constituent. Spectral displays of the same observations remain descriptive: interrupted sampling does not separate M2 and S2 into resolved spectral lines, and removing a template fitted to those observations is not another significance test (Extended Data Fig. 1).

### Support across time and the estimator decision

Within R7, the early periods P1–P5 give $A_L=1.10\pm0.21$, and summer P6–P8 gives $0.80\pm0.18$ (Fig. 4a). Omitting each period in turn gives lunar point estimates between 0.88 and 1.05. All reduced designs remain identified. The corresponding v68 subset results are $1.05\pm0.31$ outside summer and $0.87\pm0.18$ in summer. Each subset has its own fit and uncertainty; the full and subset estimates share observations. These comparisons show where the response is supported and expose its sensitivity to temporal selection.

The two reductions assign different projected template support to summer: 61% in the v68 equal-weight segment design, versus 50.2% in the R7 period-weighted design. These are squared-template allocations after removing the other fitted columns, conditional on the chosen weights and intercepts. They are neither exposure fractions nor universal information fractions. Changing an intercept scheme changes the variation available to the tidal fit, even when the observed rows are held fixed.

A controlled bridge on the saved R7 rows and its unchanged physical template isolates part of the discrepancy. Changing eight intercepts to 54 at fixed noise weights moves $A_L$ from 0.9866 to 1.0004. Changing to equal weights while keeping eight intercepts gives 0.9364; using both equal weights and 54 intercepts gives 0.9461. Switching between the saved summer-corrected and period-relative responses changes the weighted eight-intercept lunar coefficient by less than $8\times10^{-5}$. These checks isolate named choices on one common table; they do not reconcile different raw masks, filtering or solid-potential implementations (Extended Data Table 2).

Choosing the final estimator therefore requires more than selecting the smaller quoted uncertainty. Period-level intercepts require evidence that unresolved zero-point changes within each period are negligible for the tidal response. Segment intercepts relax that continuity assumption but remove additional low-frequency variation. Weighting requires support from measured noise, and the quoted interval requires calibration for that same design. The available correction record documents incomplete early absolute-chain calibration and missing correction covariances. A matched raw-support and direct-potential comparison remains necessary before one reduction can be designated primary.

### Environmental and transmission controls

Environmental evidence is strongest when a measured channel or a defined physical mechanism supplies the regressor. In v68, adding temperature covariates for both sites gives $A_L=0.98\pm0.13$ (Fig. 4b). These covariates are derived from ERA5 two-metre air temperatures, not direct measurements of both clock laboratories.^19^ A separate Sr-chamber record averages twenty PT100 sensors over a 98-h overlap; its residual blackbody-shaped coefficient is $0.92\pm0.74$. Both clocks apply real-time blackbody corrections. The temperature proxies and the chamber measurement consequently test different environmental pathways and have different support.

For a laboratory-day mechanism, the first targeted check is a 24-h term whose phase or amplitude is constrained by temperature or operating records. The v68 temperature-phase test gives $0.99\pm0.14$. An unconstrained 12-h term is a different, supplementary sensitivity question: independently resetting that phase in each campaign gives $0.82\pm0.17$. Over a short campaign it competes strongly with physical semidiurnal columns. This conditional fit is not evidence for a measured laboratory disturbance of that period or any assigned amplitude. The diurnal tidal coefficient likewise cannot serve as an upper bound on instrumental disturbance.

The directly recorded fibre round-trip monitor supplies a separate control. In the v68 analysis, the baseline and monitor-augmented regressions use the same 474-h support; adding the monitor changes both the lunar and whole-template amplitude coefficients by less than 0.005 (Fig. 4c). This constrains the portion of the transfer system sampled by that monitor. Clock-specific effects and unmonitored laboratory branches require their own measurements. The matched-support comparison is retained as experimental evidence, with its source reduction identified until the final common design is available.

### Scope and related observations

This comparison tests the combined tidal potential through its lunar and neighbouring semidiurnal responses. A separate loading coefficient and the diurnal response remain less precisely constrained. No diurnal upper limit is inferred from the semidiurnal coefficient: doing so would add a hypothesis that the response is shared across frequency bands. An upper limit derived directly from the diurnal estimator would instead require its own interval calibration.

Hou et al. report the absolute Yb/Sr ratio on this link using overlapping summer observations.^13^ The present question is the separation of physical tidal groups in the extended interrupted record; it neither updates that ratio nor reuses the earlier tidal-correlation significance. Stahl et al. report independent, contemporaneous European clock-network observations on different baselines with a different tidal mixture.^20^ They provide complementary context. Here the coastal–inland loading contrast and the changing lunar–solar phase together motivate the measurement; longer coastal observations and calibrated transfer branches would strengthen a separate test of loading.

\clearpage

## References

1. Petit, G. & Luzum, B. (eds) IERS Conventions (2010). *IERS Technical Note* **36** (2010). [https://iers-conventions.obspm.fr/content/tn36.pdf](https://iers-conventions.obspm.fr/content/tn36.pdf)
2. **Campaign time series.** All five campaigns with matched predictions, retained-segment support and display conventions.
3. **Local-time and blackbody diagnostics.** Local-time folding, chamber-temperature support and the residual blackbody test.
4. **Campaign amplitudes.** Separate five-campaign estimates and their stated error definitions.
5. **Resampling calibration.** Estimator-specific bias, standard deviation and interval coverage, with scenarios, run grouping and seeds.
6. **Separate-reduction comparison.** Primary segment/equal-weight design versus the eight-period reduction; model, sampling, weights and projected-norm definitions identified separately.
7. Grotti, J. et al. Geodesy and metrology with a transportable optical clock. *Nat. Phys.* **14**, 437–441 (2018). [https://doi.org/10.1038/s41567-017-0042-3](https://doi.org/10.1038/s41567-017-0042-3)
8. Lisdat, C. et al. A clock network for geodesy and fundamental science. *Nat. Commun.* **7**, 12443 (2016). [https://doi.org/10.1038/ncomms12443](https://doi.org/10.1038/ncomms12443)
9. Riehle, F. Optical clock networks. *Nat. Photon.* **11**, 25–31 (2017). [https://doi.org/10.1038/nphoton.2016.235](https://doi.org/10.1038/nphoton.2016.235)
10. Voigt, C., Denker, H. & Timmen, L. Time-variable gravity potential components for optical clock comparisons and the definition of international time scales. *Metrologia* **53**, 1365–1383 (2016). [https://doi.org/10.1088/0026-1394/53/6/1365](https://doi.org/10.1088/0026-1394/53/6/1365)
11. Denker, H. et al. Geodetic methods to determine the relativistic redshift at the level of $10^{-18}$ in the context of international timescales: a review and practical results. *J. Geod.* **92**, 487–516 (2018). [https://doi.org/10.1007/s00190-017-1075-1](https://doi.org/10.1007/s00190-017-1075-1)
12. Schröder, S., Stellmer, S. & Kusche, J. Potential and scientific requirements of optical clock networks for validating satellite-derived time-variable gravity data. *Geophys. J. Int.* **226**, 764–779 (2021). [https://academic.oup.com/gji/article/226/2/764/6212226](https://academic.oup.com/gji/article/226/2/764/6212226)
13. Hou, L. et al. Yb/Sr optical clock comparison at $2.2\times10^{-18}$ uncertainty over a 1350-km fiber link. *arXiv*, 2610.34250v1 (2026). [https://arxiv.org/abs/2610.34250v1](https://arxiv.org/abs/2610.34250v1)
14. Jia, Z.-P. et al. Improved systematic evaluation of a strontium optical clock with uncertainty below $1\times10^{-18}$. *Metrologia* **63**, 025002 (2026). [https://doi.org/10.1088/1681-7575/ae449e](https://doi.org/10.1088/1681-7575/ae449e)
15. Zhu, Q. et al. Ytterbium lattice clock with systematic uncertainty of $1.3\times 10^{-18}$ and instability at the $10^{-19}$ level. *arXiv*, 2606.10514v2 (2026). [https://arxiv.org/abs/2606.10514v2](https://arxiv.org/abs/2606.10514v2)
16. CNES. FES2022 (Finite Element Solution) Tidal model (Version 2024). CNES [https://doi.org/10.24400/527896/A01-2024.004](https://doi.org/10.24400/527896/A01-2024.004) (2024).
17. Farrell, W. E. Deformation of the Earth by surface loads. *Rev. Geophys.* **10**, 761–797 (1972). [https://doi.org/10.1029/RG010i003p00761](https://doi.org/10.1029/RG010i003p00761)
18. Han, D. & Wahr, J. The viscoelastic relaxation of a realistically stratified earth, and a further analysis of postglacial rebound. *Geophys. J. Int.* **120**, 287–311 (1995). [https://doi.org/10.1111/j.1365-246x.1995.tb01819.x](https://doi.org/10.1111/j.1365-246x.1995.tb01819.x)
19. Hersbach, H. et al. The ERA5 global reanalysis. *Q. J. R. Meteorol. Soc.* **146**, 1999–2049 (2020). [https://doi.org/10.1002/qj.3803](https://doi.org/10.1002/qj.3803)
20. Stahl, K. et al. Optical clock network tracks tidal variations of the gravity potential. *arXiv*, 2610.39635v1 (2026). [https://arxiv.org/abs/2610.39635v1](https://arxiv.org/abs/2610.39635v1)

\clearpage

## Figure legends

![](figures/figure1.png){width=180mm}

**Fig. 1 | Coastal–inland geometry and lunar–solar phase coverage.** Prediction and sampling panels retained from v68. **a,** Shanghai Sr and Wuhan Yb, their 692-km separation and schematic 1,350-km fibre route through Hefei. Land colour represents predicted M2 clock potential; sea colour represents FES2022 M2 elevation. The inset shows Shanghai loading. **b,** Differential solid and loading phasors of 3.41 and 1.42, separated by approximately 20° and summing to 4.77, in $10^{-18}$ fractional-frequency units. **c,** Five v68 campaigns and their reported integer-hour durations, with an approximately 544-h retained total. **d,** Relative S2–M2 astronomical phase at the v68 filtered samples. These panels describe the specified prediction and sampling, not a hypothesis test. The period-based R7 row support used in Figs. 2–4 is separately identified; phase coverage does not imply calibrated zero-point continuity.

\clearpage

![](figures/figure2.png){width=180mm}

**Fig. 2 | The full-record lunar phase display on the R7 design.** **a,** Twelve fixed 30° phase-bin means after subtracting the fixed remainder and projecting both observations and unit lunar prediction against the same period, near-12-h and diurnal columns. Solid and dashed curves show the identically transformed unit and fitted predictions. Error bars are marginal standard errors from the complete propagated scaled-working covariance, including the nuisance projection; the twelve means are correlated and their covariance has rank eleven. **b,** All 3,299 projected R7 observations, retaining their full ordinate range. **c,** Row counts per phase interval; each interval contains all eight periods and 31–36 UTC days. R7 noise weights, template and sampling are used throughout. The amplitude is fitted to the original rows, not to the phase means. No new rejection, phase adjustment or independent significance test is introduced.

\clearpage

![](figures/figure3.png){width=180mm}

**Fig. 3 | Separate semidiurnal responses and a common lunar phase test.** **a,** Three-group coefficients from the two named reductions of overlapping observations. Open diamonds retain v68 values: the lunar error is its reported residual-resampling standard deviation, while near-12-h and diurnal errors use its scaled-LS/day-jackknife maximum. Filled circles show independently recomputed R7 values, each with its own scaled-LS/day-jackknife maximum. Neither coefficients nor errors are combined. K2 is lunisolar; the neighbouring group is defined by frequency. **b,** The R7 common M2+N2 in-phase/quadrature fit, with marginal errors from that same fit; the cross marks unit in-phase and zero quadrature response. Constituent phases and relative amplitudes remain linked within the lunar group. The bars are not a separately calibrated joint confidence contour. Both panels reuse observations underlying their named fits.

\clearpage

![](figures/figure4.png){width=180mm}

**Fig. 4 | Temporal support and observed-channel controls.** **a,** R7 full-record, early and summer lunar estimates, followed by eight leave-period estimates. Every fit uses its own retained rows and scaled-LS/day-jackknife maximum; these overlapping fits are not independent replications. **b,** Reported v68 base and two-site ERA5-temperature-regression estimates, retaining their respective 0.14 and 0.13 marginal errors. ERA5 is an outdoor-temperature proxy, not direct laboratory thermometry. **c,** Reported v68 bounds on the change induced by adding the round-trip monitor on identical 474-h support. The horizontal intervals indicate $|\Delta A|<0.005$ for each named coefficient; they are neither error bars nor estimates located at zero. Panels b and c have not been recalculated with R7 weights. The monitor constrains its measured transmission channel, with unmonitored branches and clock-specific effects outside its coverage.


\clearpage

## Methods

### Frequency ratio, sign and corrections

The clock apparatus and absolute-ratio experiment are described by Hou et al., with separate Sr and Yb uncertainty evaluations.^13,14,15^ The Sr-referenced optical carrier is transferred from Shanghai and compared with the Yb-referenced comb in Wuhan. The ratio orientation is $R=\nu_{\mathrm{Yb,Wuhan}}/\nu_{\mathrm{Sr,Shanghai}}$. For positive geodetic potential, the differential fractional signal is

$$y(t)=-\frac{\delta W_{\mathrm{eff,Wuhan}}(t)-\delta W_{\mathrm{eff,Shanghai}}(t)}{c^2}.$$

A positive $y$ therefore means that Wuhan runs faster relative to Shanghai. The R7 period-relative beat conversion is $y_{\mathrm{rel}}=-d_p(f_{\mathrm{beat}}-f_{\mathrm{ref},p})/F_{1550}$, with $F_{1550}=1.933992\times10^{14}$ Hz, $d_p=2$ in 2025 and $d_p=1$ in 2026. This corresponds to a 2026 conversion magnitude of approximately $5.17\times10^{-15}$ per hertz; the 2025 divided counter requires restoration of the factor of two. The reference beat is a period-specific level, not the optical frequency.

R7 applies the recorded summer group-resolved Sr and Yb corrections through the frequency-chain equations in 80-digit Decimal arithmetic, before taking a fractional ratio. Early periods retain period-relative scales because their absolute-chain calibration is incomplete. The early 37.2-mHz feedback term can be absorbed by a period intercept only if its sign, magnitude and conversion remain constant within that period. Group-dependent or time-dependent errors are not absorbed by a common intercept. Missing early AC Stark entries and the provisional May Yb entry are recorded as missing or assumed, rather than measured zero. Correction covariances have not been supplied. They are not invented or combined with the statistical errors.

### Selection, support and temporal processing

The v68 specification retains 54 segments in five campaign groupings. It rejects large counter departures and applies a six-robust-standard-deviation transient screen based on local medians, independently of tidal residuals. The reported transient removal is 0.4%, approximately 2.2 h; adding the theoretical tide with factors −1, 1 and 3 leaves the reported mask unchanged. Its data and theoretical samples receive the same 1200-s triangular filter at 600-s steps. Its reported retained duration is approximately 544 h. The final per-row mask, filter membership and matched directly calculated potential series remain required inputs for the common-support replay.

R7 reads the updated 54-segment mask, excludes original group 22 and retains segment 48. Period files are joined before applying intervals, preserving intervals that cross midnight. Beijing-time labels are converted to UTC. Printed-second endpoints retain subsecond timestamp jitter; shared-boundary seconds belong to the preceding segment. Its raw selection has 1,966,908 loaded rows versus 1,966,905 tabulated rows, with the three-row net difference individually reconciled at interval boundaries. Ten-minute means are formed separately by segment on a fixed grid, requiring at least 180 nominal one-second rows. The 3,299 accepted rows contain 545.9242 sample-hours and 43 observed UTC days. Distinct segments may contribute separate partial bins at the same centre without sharing underlying samples. The present R7 replay consumes these saved tables; it does not newly reconstruct their raw selection.

### Physical template and band definitions

The direct-potential formulation used by v68 is

$$\delta W_{\mathrm{solid}}=\sum_m(1+k_{2m})V_{2m}+(1+k_3)V_3-gu_r,$$

with $k_{20}=0.29525$, $k_{22}=0.29801$, $k_3=0.093$, and the IERS resonance prescription for $k_{21}$.^1^ The displacement term follows the associated frequency- and latitude-dependent response. Ocean loading is computed from ocean elevation $\zeta$ and the full effective-potential kernel,

$$\delta W_{\mathrm{load}}=\int\rho_w\zeta(\mathbf r',t)G_W(\psi)\,\mathrm dA,\qquad G_W(\psi)=\frac{ga}{M_E}\sum_n(1+k'_n-h'_n)P_n(\cos\psi).$$

The kernel contains seawater attraction, induced potential and the clock displacement.^16,17,18^ The reported implementation uses water density 1025 kg m$^{-3}$, PREM load Love numbers through degree 696, high-degree continuation and summation to degree 40,000. The $1/30^\circ$ ocean grid is retained near the stations. Ocean means are removed for mass conservation. The complete model configuration and its software versions must accompany the final analysis archive.

R7 instead consumes an IERS-based displacement series converted with $-(1+k_2-h_2)g/(h_2c^2)$, using $h_2=0.6078$, $k_2=0.3010$ and $g=9.794$ m s$^{-2}$. This is a specified approximation, not the same mode-dependent direct-potential implementation. The R7 source documents a K1 amplitude about 18% below its quoted potential-weighted reference; that model discrepancy remains part of the common-template audit. Its loading uses the supplied full-potential phasors. Temporal synthesis uses pyTMD 3.0.9 FES astronomical arguments and nodal corrections.^21^ In the convention $f_k\Re[C_k\exp(-i\phi_k)]$, consistently conjugating the coefficient and reversing the exponential leaves the real series unchanged. The bridge reported here holds this R7 series fixed; it does not certify equivalence to the direct-potential series.

Both reductions group M2+N2, S2+K2 and K1+O1+P1+Q1. Relative amplitudes and phases are fixed within each group. A remaining theoretical contribution enters once at its predicted value. Thus

$$y_i=A_Lb_L(t_i)+A_Sb_S(t_i)+A_Db_D(t_i)+r_0(t_i)+c_{j(i)}+\epsilon_i.$$

The intercept index $j$ is a segment in v68 and a period in R7. The controlled bridge also evaluates original-group intercepts on the same R7 rows. No fitted offsets are used to construct a long-term stability series.

### Statistical errors and controlled bridge

The v68 lunar error is a reported residual-circular-shift standard deviation. Residuals are shifted within continuous filtered runs and added to the unit-response model. The reported lunar values from two sets of 200 realizations are 0.13 and 0.14, with 0.14 retained. Its reported four-scenario study gives 67–68% coverage for $\hat A_L\pm0.14$ and 94.5–95.2% for $\hat A_L\pm1.96(0.14)$. These results remain source-reported until the associated code, seeds and inputs are transferred. They are not calibration of the R7 estimator.

R7 estimates period noise factors from within-segment overlapping Allan deviations after subtracting the fixed unit template and segment constants.^22^ It fits a fixed $\tau^{-1/2}$ slope on 256–4096 nominal one-second samples and uses $\sigma_i=\alpha_{p(i)}/\sqrt{n_i}$. No fitted inter-segment stitching enters this weighting. Scaled least-squares errors use the reduced chi-square; UTC-day jackknife deletes each of 43 observed days and removes empty intercept columns. The reported marginal error is the larger of these two quantities, with period deletion retained separately. For its lunar estimate the three errors are 0.1231, 0.1116 and 0.1314, respectively. The weights are held fixed during deletion (Extended Data Table 1).

The independent bridge uses QR least squares and checks the saved R7 coefficient, covariance and deletion results. It crosses three intercept levels (8 periods, 29 groups, 54 segments), two weight choices (saved noise weights or equal weights) and two saved response representations (summer-corrected or period-relative), giving twelve cases. All use the same 3,299 rows, timestamps, band templates and fixed remainder. This separates those choices from sampling/filtering/template differences that remain untested. A small change on removing saved corrections does not validate missing corrections or establish their constancy in time.

The R7 conditional study holds rows, weights and design fixed. Its independent Gaussian reference and twelve correlation scenarios use $\Sigma=D[(1-\rho)I+\rho K]D$, with exponential correlation times of 1, 6 or 24 h, segment or period clusters, and $\rho=0.1$ or 0.5. These are specified stress scenarios, not estimates of actual laboratory noise. Recounting the saved 10,000 draws per scenario reproduces 95.94% coverage for the reference and 94.16–97.79% across all scenarios for intervals $\hat A_L\pm1.959964u$. The rule is not uniformly conservative (Extended Data Table 3). Estimation of the weights, selection, non-Gaussian excursions and instrumental covariance lie outside that conditional study. The scenario results do not replace the reported standard error.

### Phase display and temporal diagnostics

Let $W=\mathrm{diag}(\sigma_i^{-2})$ and let $N$ contain intercepts and the near-12-h and diurnal columns. The nuisance projector is $M_N=I-N(N^TWN)^{-1}N^TW$. The display uses $z=M_N(y-r_0)$ and $x=M_Nb_L$, with the crest coordinate $[\phi_{M2}-\arg C_{M2}]\bmod 2\pi$. Twelve fixed 30° intervals define inverse-variance averaging operator $B$. The means are $Bz$, $Bx$ and $\hat A_LBx$, using the original unaggregated amplitude fit.

The displayed working covariance is $BM_NC_yM_N^TB^T$, with $C_y=\chi^2_{\mathrm{red}}\mathrm{diag}(\sigma_i^2)$. This propagates the fitted nuisance projection rather than holding nuisance coefficients fixed. It has rank eleven because of the weighted-mean constraint. All points, counts, day/period support and the full covariance are exported. The present independent projection agrees with the saved R7 phase means and marginal errors to numerical precision.

The I/Q diagnostic adds a quadrature obtained by $C_k\rightarrow iC_k$ for both lunar constituents and fits it jointly with the original nuisance columns. The figure shows marginal errors from that fit, not a calibrated joint contour. Early/summer and leave-period fits each recompute their own coefficients and errors on their retained rows. Neither phase averaging, spectra nor deletion of overlapping observations provides independent experimental replication.

### Environmental evidence and limits

The site-temperature regressors in v68 use ERA5 hourly two-metre air temperatures and departures from a 24-h running mean.^19^ The Sr-chamber thermometers provide a separate 98-h direct record. The round-trip counter is normalized by the optical carrier without an additional factor of two, screened and filtered like the ratio; comparisons with and without the regressor use identical 474-h support. These reported controls are retained with their v68 definitions until the final primary design is available for matched recalculation.

A physically motivated 24-h term can test temperature or operating-cycle coupling. An independently phased 12-h term in each campaign is retained only as a supplementary sensitivity variant. A coefficient change under such a model is not an observed disturbance amplitude. Residual diagnostics must propagate the physical fit's projection to both residual data and diagnostic bases. No diurnal upper limit or semidiurnal-to-diurnal extrapolation is reported: each would require an estimator-specific interval or an explicit common-response hypothesis.

### Data availability

The authors will provide the retained counter-row membership, correction ledger, matched physical templates, figure source tables and versioned manifests through [repository and DOI or editor-accessible link to be confirmed]. The current author working package contains the source-bound v68 material and replayable R7 saved-table diagnostics. The matching v68 primary sample/template/resampling package remains to be supplied. Third-party products are identified by their originating citations and access terms.

### Code availability

Versioned selection, frequency conversion, potential generation, fitting, uncertainty and figure code will be deposited at [repository and DOI or review link to be confirmed]. The present bridge and display code is retained with its inputs, hashes, environment and execution logs. The final source archive must also include the direct-potential chain and the accepted estimator decision.

### Author statements

**Authors:** [Author list, order and affiliation assignments to be confirmed.]

Affiliation texts retained from the companion frequency-ratio manuscript, pending author assignments:

^1^ Hefei National Laboratory, University of Science and Technology of China, Hefei, China

^2^ Shanghai Research Center for Quantum Sciences and CAS Center for Excellence in Quantum Information and Quantum Physics, University of Science and Technology of China, Shanghai, China

^3^ Hefei National Research Center for Physical Sciences at the Microscale and School of Physical Sciences, University of Science and Technology of China, Hefei, China

^4^ Innovation Academy for Precision Measurement Science and Technology, Chinese Academy of Sciences, Wuhan, China

^5^ Jinan Institute of Quantum Technology and CAS Center for Excellence in Quantum Information and Quantum Physics, University of Science and Technology of China, Jinan, China

^6^ Time and Frequency Geodesy Center (TFGC), School of Geodesy and Geomatics, Wuhan University, Wuhan, China

**Contributions:** [To be confirmed for this Article.]

**Acknowledgements and funding:** [To be confirmed by the authors.]

**Competing interests:** [Declaration to be provided by all authors.]

**Correspondence:** [Names and contact details to be confirmed.]

**AI-assisted preparation:** OpenAI Codex assisted source comparison, manuscript drafting, numerical replay and figure preparation. [Authors to specify the scope of their verification and responsibility before submission.]


## Methods references

21. Sutterley, T. C., Howard, S. L., Padman, L. & Siegfried, M. R. pyTMD: Python-based tidal prediction software. *J. Open Source Softw.* **10**, 8566 (2025). https://doi.org/10.21105/joss.08566
22. Riley, W. J. & Howe, D. A. Handbook of Frequency Stability Analysis. *NIST Special Publication* **1065** (2008). https://doi.org/10.6028/NIST.SP.1065

\clearpage

## Extended Data

**Extended Data Table 1 | Estimator-specific uncertainty sources.** R7 numbers are independently recomputed on saved input rows. All entries are standard errors of the named coefficient. The reported R7 rule is the marginal maximum of scaled LS and UTC-day jackknife; period deletion is retained as a separate sensitivity. No errors are pooled.

| Reduction and coefficient | Estimate | Scaled LS | Day jackknife | Period jackknife | Reported error |
|---|---:|---:|---:|---:|---:|
| R7 lunar | 0.9866 | 0.1231 | 0.1116 | 0.1314 | 0.1231 |
| R7 near-12 h | 1.1291 | 0.2825 | 0.2878 | 0.3256 | 0.2878 |
| R7 diurnal | 0.6779 | 0.2860 | 0.3586 | 0.4118 | 0.3586 |
| R7 lunar in phase | 0.9910 | 0.1231 | 0.1145 | 0.1416 | 0.1231 |
| R7 lunar quadrature | -0.1792 | 0.1143 | 0.1394 | 0.1681 | 0.1394 |
| R7 early lunar | 1.0986 | 0.1914 | 0.2084 | 0.5183 | 0.2084 |
| R7 summer lunar | 0.7991 | 0.1798 | 0.1674 | 0.0942 | 0.1798 |
| v68 lunar (source reported) | 0.97 | — | — | — | 0.14, residual shift |

R7 full and I/Q fits use 3,299 rows, 43 UTC-day groups and 8 period groups. Early uses 1,651 rows, 20 observed UTC days and 5 periods; summer uses 1,648 rows, 23 observed UTC days and 3 periods. The v68 source reports the maximum of its LS/day-jackknife errors as 0.13 but does not supply those two separate values here. A dash is unavailable, not zero.

\clearpage

**Extended Data Table 2 | Controlled choices on the same R7 rows and physical template.** Saved corrected response, 3,299 observations. P8, G29 and S54 denote 8 period, 29 group and 54 segment intercepts. Quoted errors use each variant's own scaled-LS/day-jackknife maximum. These are bridge calculations, not additional primary results.

| Intercepts | Weights | Lunar | Near-12 h | Diurnal | Lunar–near-12 h correlation |
|---|---|---:|---:|---:|---:|
| P8 | Allan | 0.9866 ± 0.1231 | 1.1291 ± 0.2878 | 0.6779 ± 0.3586 | -0.3572 |
| P8 | equal | 0.9364 ± 0.1323 | 1.1627 ± 0.3071 | 0.5588 ± 0.3626 | -0.3669 |
| G29 | Allan | 0.9841 ± 0.1243 | 1.0930 ± 0.2981 | 0.7587 ± 0.4203 | -0.3496 |
| G29 | equal | 0.9320 ± 0.1337 | 1.1284 ± 0.3241 | 0.5691 ± 0.4482 | -0.3622 |
| S54 | Allan | 1.0004 ± 0.1320 | 0.9251 ± 0.3649 | 0.5792 ± 0.5381 | -0.3003 |
| S54 | equal | 0.9461 ± 0.1407 | 0.9735 ± 0.3753 | 0.4151 ± 0.5711 | -0.3245 |

All twelve corrected/period-relative cases are in the source CSV. The table does not compare the v68 triangular filter, final mask or direct-potential series; those remain missing from the matched replay.

\clearpage

**Extended Data Table 3 | Recount of saved R7 conditional simulations.** Each scenario contains 10,000 saved draws. Coverage refers to nominal 95% intervals $\hat A_L\pm1.959964\max(u_{\mathrm{LS}},u_{\mathrm{day}})$. Rows, design and weights are held fixed. The correlations are specified scenarios, not measured laboratory noise.

| Correlation cluster | Time scale (h) | Correlated fraction | Lunar bias | 95% coverage (%) |
|---|---:|---:|---:|---:|
| Independent Gaussian | — | 0 | +0.0025 | 95.94 |
| segment | 1 | 0.1 | -0.0001 | 94.24 |
| segment | 1 | 0.5 | +0.0025 | 94.16 |
| segment | 6 | 0.1 | +0.0004 | 95.22 |
| segment | 6 | 0.5 | +0.0004 | 95.59 |
| segment | 24 | 0.1 | +0.0008 | 96.00 |
| segment | 24 | 0.5 | +0.0017 | 97.04 |
| period | 1 | 0.1 | -0.0019 | 94.65 |
| period | 1 | 0.5 | +0.0000 | 94.22 |
| period | 6 | 0.1 | -0.0029 | 95.72 |
| period | 6 | 0.5 | +0.0051 | 96.49 |
| period | 24 | 0.1 | +0.0006 | 95.94 |
| period | 24 | 0.5 | -0.0020 | 97.79 |

This recount checks the archived simulations; it does not regenerate the draws or calibrate the v68 estimator. Weight estimation, raw selection and unknown instrumental covariance remain outside this conditional experiment.

\clearpage

![](figures/extended_spectrum.png){width=150mm}

**Extended Data Fig. 1 | Same-record spectral display retained from v68/v29.** Segment-constant-projected sinusoidal power of the v68 record before and after subtraction of the whole template fitted to those observations. The source threshold is the 99% level of the maximum over 5–40 μHz from 200 residual resamples. Markers indicate one and two cycles per solar day. Interrupted sampling does not resolve M2 and S2 as distinct lines here, and fitted-template removal is not independent evidence. This display has not been recomputed on R7 rows; its source and observation identity remain explicit.
