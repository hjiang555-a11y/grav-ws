# Resolving lunar and solar tidal responses with an optical clock baseline

::: affiliations
[Author list, order and affiliation assignments to be confirmed by the authors]

^1^ Hefei National Laboratory, University of Science and Technology of China, Hefei, China

^2^ Shanghai Research Center for Quantum Sciences and CAS Center for Excellence in Quantum Information and Quantum Physics, University of Science and Technology of China, Shanghai, China

^3^ Hefei National Research Center for Physical Sciences at the Microscale and School of Physical Sciences, University of Science and Technology of China, Hefei, China

^4^ Innovation Academy for Precision Measurement Science and Technology, Chinese Academy of Sciences, Wuhan, China

^5^ Jinan Institute of Quantum Technology and CAS Center for Excellence in Quantum Information and Quantum Physics, University of Science and Technology of China, Jinan, China

^6^ Time and Frequency Geodesy Center (TFGC), School of Geodesy and Geomatics, Wuhan University, Wuhan, China
:::

**Optical clocks measure tides through changes in their relative rates, but neighbouring tidal components are difficult to separate when observations are interrupted and frequency reference levels differ between segments.^1,2^ Here we use the changing astronomical phase between lunar and solar tides as an external reference to resolve neighbouring semidiurnal responses. Clocks in coastal Shanghai and inland Wuhan accumulated 545.9 hours over 353 days. Their measured spectrum has local peaks near the principal lunar and solar frequencies, 0.78 µHz apart. Joint physical-template estimates give $1.00\pm0.13$ for the lunar group M₂+N₂ and $0.93\pm0.36$ for the neighbouring group S₂+K₂ relative to the combined solid-Earth and ocean-loading prediction (one statistical standard error). Astronomical phase thus allows neighbouring tidal responses to be distinguished across interruptions without requiring a calibrated frequency reference level shared by all observing segments.**

\clearpage


Earth's gravitational potential varies as the Moon and Sun change position and as water, air and the solid Earth move. Measuring these changes provides a way to study mass redistribution and deformation, and to maintain consistent height and time references.^3,4,5^ Geodetic surveys and satellite gravity observations constrain different aspects of this evolving field.^4,5^ Optical clocks offer a direct measure of potential differences: gravity changes their relative rates, so a frequency comparison between distant clocks contains a geophysical observable.^1,2^ Connecting stable clocks through optical fibres allows repeated observations of the same endpoints across hundreds of kilometres.^6,7^

Laboratory redshift tests and remote optical-clock comparisons have established measurements of static potential differences.^8,9,10^ A time-dependent measurement additionally requires enough precision over the period of the change and sufficiently stable operation of both clocks and their connection. Tides are a well-defined target: celestial motion fixes their frequencies and phases, while deformation and ocean loading determine the signal expected at each station.^3^ Measuring that signal tests whether clock comparisons can follow the changing Earth. The same variation enters the redshift correction needed to compare clocks and form common time scales.^11^ Coordinated comparisons already connect optical standards across national borders.^12^

The principal lunar and solar semidiurnal tides are a demanding pair of nearby signals. M₂ repeats every 12.42 h and S₂ every 12 h, giving a frequency separation of only 0.78 µHz. Over a short comparison their variations can look much alike. The lunar peaks arrive about 50 minutes later in solar time each day, so the relative phase of the two tides changes with the observing date. Measurements on different dates therefore sample different combinations of the two signals.

An interruption can leave the frequency reference level of a new observing segment unknown, while its astronomical phase remains determined by the actual observation time. Each segment still records the changes within it. Combining these changes at their known lunar–solar phases supplies separate constraints on the two responses without first aligning the segments to a common frequency level. This physical reference motivates retaining the actual UTC times, assigning each segment an independent constant and estimating the astronomical templates together.

Here we measure tidal variations of the potential difference between coastal Shanghai and inland Wuhan and separate neighbouring semidiurnal responses. Across a 353-day span, 54 valid segments provide 545.9 h of observations. The two target responses are represented by complete physical templates for the lunar semidiurnal group M₂+N₂ and the neighbouring group S₂+K₂. The joint model also retains the approximately daily tides as an auxiliary physical component. Internal amplitude ratios and phases remain fixed by the astronomical model. K₂ contains lunar and solar forcing. The measured spectrum has local peaks near M₂ and S₂, and the joint estimates are consistent with the combined solid-Earth and ocean-loading prediction.

### A coastal–inland prediction

The strontium clock in Shanghai and ytterbium clock in Wuhan are 692 km apart, joined through Hefei by a 1,350-km phase-stabilized fibre link (Fig. 1a).^13^ The summer observations overlap the absolute frequency-ratio measurement reported by Hou and colleagues; the present observable is the time-dependent tidal response. The clock systems and their performance are described in their published evaluations.^14,15^ The link extends a transmission architecture previously demonstrated over 2,067 km of field-deployed fibre.^16^ We define a positive frequency-ratio variation as Wuhan Yb running faster relative to Shanghai Sr. In the geodetic potential convention used here, the measured fractional variation is $y=-[\delta W_{\mathrm{Wuhan}}-\delta W_{\mathrm{Shanghai}}]/c^2$.

Ocean mass redistribution produces different gravitational responses at coastal Shanghai and inland Wuhan. Their differential tidal signal therefore includes an appreciable loading contribution alongside the solid-Earth tide. The solid response combines the direct astronomical potential, the Earth's induced potential and displacement of the clocks. Ocean loading likewise includes water attraction, induced potential and clock displacement. We combine an IERS-based solid-tide prediction with FES2022 ocean elevations and a loading kernel containing all three loading contributions (Methods).^17,18,19,20^

The predicted M₂ amplitudes are $3.43\times10^{-18}$ for the solid contribution and $1.42\times10^{-18}$ for loading. Their phases differ by 19.8°, giving a combined amplitude of $4.78\times10^{-18}$ (Fig. 1b). Loading is about 30% of the combined M₂ amplitude. On the sampled record, after removing segment means, its weighted root-mean-square variation is 33.1% of the combined prediction. These ratios describe the model contribution; the measurement tests the combined potential.

The record spans September 2025 to August 2026, with 54 valid segments in eight observing periods (Fig. 1c). Its 3,299 ten-minute means contain 545.9 h of accepted nominal one-second measurements. Observations occur in eight calendar months; the annual span is not continuous operation. Actual UTC times and all gaps are retained. The June–August observations supply 273.9 h and sample a broad range of relative lunar–solar phase, while the earlier periods add different phases and operating conditions (Fig. 1d). Both the duration and placement of the observations determine what can be separated.

### Jointly resolved semidiurnal responses

The reference levels of the 54 observing segments are left independent. The analysis retains the variation within each segment and uses its actual UTC times to place that variation at the correct astronomical phase. All segments can therefore constrain common physical responses without an artificial joining of their frequency levels. The constants represent unknown reference levels, not measured frequency jumps. The full record reveals recurring modulation when ordered by M₂ phase (Fig. 2).

Joint estimation gives $A_L=1.00\pm0.13$ for M₂+N₂ and $A_S=0.93\pm0.36$ for S₂+K₂ (Fig. 3a). Each semidiurnal group has its own response coefficient within the same physical model. One denotes the specified combined prediction. The coefficients are estimated from the original ten-minute means using the same noise weights throughout. The reported errors are the larger of residual-scaled least-squares and UTC-day-deletion standard errors; their components and conditional interval coverage are given in Methods. No empirical daily sinusoid is subtracted before this joint estimate.

After subtracting the fixed minor tidal remainder, the observations and unit lunar prediction undergo the same projection against segment constants and the other two groups. Twelve phase bins reveal the recurring modulation, with the uncertainty of the jointly estimated nuisance terms propagated into the error bars. The complete set of individual observations and the support of each bin are shown below the phase means.

Allowing a lunar component one quarter-cycle from the predicted phase gives in-phase and quadrature responses of $1.00\pm0.13$ and $-0.10\pm0.20$ (Fig. 3b), consistent with the astronomical phase.

### Spectral separation through the observation window

The measured spectrum provides a direct view of the two principal semidiurnal neighbourhoods (Fig. 3c). An equal-weight sinusoidal scan with 54 segment constants has local maxima at 22.361 and 23.147 µHz, close to the predicted M₂ and S₂ frequencies of 22.364 and 23.148 µHz. The prescribed principal frequencies are 0.78 µHz apart. The left axis expresses spectral density in gravitational-potential units and the right in fractional-frequency units; a fractional variation of $10^{-18}$ corresponds to about $0.09\,\mathrm{m^2/s^2}$ of potential difference.

The observation gaps produce sidelobes around a sampled tidal line. Single-constituent injections through the actual sampling and scan give 8.03% M₂-to-S₂ cross-power and 8.15% in the reverse direction. Conditional scans retain a local feature near each frequency after projecting out the sine and cosine at the other (Extended Data Fig. 1). Together with the joint physical-template estimates, these features identify distinct responses in the neighbouring semidiurnal groups. The two groups' prescribed internal structure and the sampling-window response are treated explicitly in Methods.

### Consistency across observing periods

Observations before and during summer both contribute to the lunar response. With the same segment model, the coefficient is $1.21\pm0.23$ before summer and $0.77\pm0.18$ in summer. Deleting each observing period in turn gives point estimates from 0.885 to 1.093 (Fig. 4a). These overlapping fits show each period's influence on the full-record estimate.

Changing only the grouping of the reference levels gives similar lunar coefficients (Fig. 4b). The available interval and correction records do not establish a calibrated transfer of zero across interruptions, motivating the separate segment constants used here. The eight-period design gives $0.987\pm0.123$ on the same observations, physical templates and weights. Its residual structure and the full comparison of group coefficients are given in Methods and Extended Data Fig. 2.

Daily temperature changes and operating schedules motivate a 24-h sensitivity check. Adding one shared 24-h sine–cosine pair to the present model gives $A_L=1.04\pm0.13$. The matched summer round-trip monitor also leaves the lunar estimate essentially unchanged, with a paired shift of $0.0061\pm0.0063$ over 246.6 h. The measurement support and full results of that control are shown in Extended Data Fig. 3. Free 12-h terms are confined to the sensitivity analysis in Methods.

The Shanghai–Wuhan comparison measures tidal variations of the gravitational potential and separates neighbouring semidiurnal responses across an interrupted record. The two semidiurnal groups have separately estimated response coefficients, supported by local peaks near M₂ and S₂ and by the conditional scans. Together they resolve neighbouring lunar and solar-driven tidal responses within the specified physical grouping. The phase plot, spectrum and group estimates describe the same observations from their time, frequency and physical-model perspectives.

Astronomical phase provides the reference that persists between observing segments. Independent constants accommodate unknown frequency levels, while the changing lunar–solar phase lets observations at different dates constrain the neighbouring responses. The result here concerns separation of neighbouring responses when observations are interrupted and a common frequency zero has not been transferred between segments.

This distinction matters for clock networks whose stations cannot operate continuously. Measurements can retain a common physical phase reference even when their frequency levels are established separately on each run. The achievable separation depends on the distribution of observing dates as well as the accumulated measurement time. Celestial phase therefore provides a practical reference for resolving adjacent tidal variations of the gravitational potential in interrupted optical-clock comparisons. Independent, contemporaneous European clock-network observations have tracked the overall tidal potential on different baselines.^21^

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
16. Chen, F.-X. et al. 10⁻²¹-level optical frequency dissemination over 2067 km of noise-loaded field-deployed fiber network. *Light Sci. Appl.* **15**, 276 (2026). <https://doi.org/10.1038/s41377-026-02299-1>
17. Petit, G. & Luzum, B. (eds) IERS Conventions (2010). *IERS Technical Note* **36** (2010). [https://iers-conventions.obspm.fr/content/tn36.pdf](https://iers-conventions.obspm.fr/content/tn36.pdf)
18. CNES. FES2022 (Finite Element Solution) Tidal model (Version 2024). CNES [https://doi.org/10.24400/527896/A01-2024.004](https://doi.org/10.24400/527896/A01-2024.004) (2024).
19. Farrell, W. E. Deformation of the Earth by surface loads. *Rev. Geophys.* **10**, 761–797 (1972). [https://doi.org/10.1029/RG010i003p00761](https://doi.org/10.1029/RG010i003p00761)
20. Han, D. & Wahr, J. The viscoelastic relaxation of a realistically stratified earth, and a further analysis of postglacial rebound. *Geophys. J. Int.* **120**, 287–311 (1995). [https://doi.org/10.1111/j.1365-246x.1995.tb01819.x](https://doi.org/10.1111/j.1365-246x.1995.tb01819.x)
21. Stahl, K. et al. Optical clock network tracks tidal variations of the gravity potential. *arXiv*, 2610.39635v1 (2026). [https://arxiv.org/abs/2610.39635v1](https://arxiv.org/abs/2610.39635v1)

\clearpage

## Figure legends

![Figure 1](figures/figure1.png)

**Fig. 1 | Geometry and changing lunar–solar phase.** **a,** Shanghai Sr and Wuhan Yb, 692 km apart, with the 1,350-km fibre connection through Hefei drawn schematically. **b,** Predicted differential M₂ solid and ocean-loading phasors, with the solid component defining phase zero; amplitudes are fractional clock rates in units of $10^{-18}$. **c,** Actual UTC sampling in eight observing periods, with accepted nominal member-hours. **d,** The S₂−M₂ astronomical phase at those same samples, including nodal corrections. Summer periods P6–P8 are orange. Geography and phasors describe the prediction; the lower panels describe the observation window.

\clearpage

![Figure 2](figures/figure2.png)

**Fig. 2 | The full record ordered by lunar phase.** **a,** Twelve 30° M₂ phase means of all 3,299 observations, after subtracting the fixed minor remainder and projecting against 54 segment constants and the neighbouring semidiurnal and daily groups. Identical weighted projection and averaging are applied to the unit lunar prediction; the fitted curve uses the unbinned primary coefficient. Error bars are one working standard error with the nuisance projection propagated; phase means are correlated. **b,** Every projected observation, with the full observed vertical range. **c,** Number of rows in each bin. Data, weights and templates are the primary segment design throughout. This is a display of the main observations, not an independent experiment.

\clearpage

![Figure 3](figures/figure3.png)

**Fig. 3 | Semidiurnal responses, phase and measured spectral structure.** **a,** The two semidiurnal coefficients from the three-group joint model, using all 3,299 means. Error bars are one standard error, defined as the larger of scaled least-squares and UTC-day jackknife errors. The daily group remains in the fit and is reported in Methods and Extended Data Table 2. **b,** Lunar in-phase and quadrature coefficients; the cross marks the unit prediction. Contours have covariance radii one and two from scaled least squares, not separately calibrated joint confidence levels. **c,** Equal-weight spectral calculation around the principal M₂ and S₂ frequencies, separated by 0.78 µHz: 3,299 real UTC means, 54 segment constants and equal weights. Blue shows the observed scan; orange follows subtraction of the fixed unit total prediction. No gap is filled or compressed. Both axes show the same nominal one-sided projection density per µHz, related by $S_W=c^4S_y$. Sampling sidelobes contribute about 8% bidirectional M₂/S₂ cross-power. Peak locations support the principal-frequency attribution; group coefficients in **a** use the physical templates and Allan-based weights. All panels use the same observation rows.

\clearpage

![Figure 4](figures/figure4.png)

**Fig. 4 | Consistency across observing periods and reference-level designs.** **a,** Lunar estimates from the full record, the pre-summer and summer subsets, and deletion of each observing period. Each fit uses segment constants and the primary noise weights, with errors recalculated on its retained rows. The full, pre-summer and summer fits contain 3,299, 1,651 and 1,648 means. Deleting P1–P8 retains 3,136, 3,096, 2,890, 2,852, 2,870, 2,698, 2,704, 2,847 means, respectively. **b,** Lunar response with 54 segment, 29 operating-group or eight period constants. Only the intercept grouping changes; all designs use the same 3,299 observations, physical templates, corrections and noise weights. Error bars are one standard error using the same larger-of-scaled-least-squares-and-day-jackknife rule. Shading marks the full-record segment estimate and its standard error. The estimates share observations; reference-level choice follows the available calibration records.

\clearpage

## Methods

### Observations, frequency sign and averaging

The Shanghai and Wuhan coordinates used by the frozen prediction are 31.130° N, 121.570° E and 30.529° N, 114.357° E. The measured ratio is Wuhan Yb/Shanghai Sr. With positive geodetic potential $W$, its tidal fractional variation is $-[\delta W_{\mathrm{Wuhan}}-\delta W_{\mathrm{Shanghai}}]/c^2$. The period-relative beat conversion is $-d_p(f_{\mathrm{beat}}-f_{{\mathrm{ref}},p})/F_{1550}$, where $F_{1550}=1.933992\times10^{14}$ Hz and $d_p=2$ in 2025 and 1 in 2026. Thus a 2026 beat deviation of 1 Hz has fractional magnitude $5.17\times10^{-15}$. The 2025 division factor is applied before forming the small clock-rate variation.

The supplied valid-interval table defines 54 segments in 29 operating groups and eight periods. Counter members are read across midnight before binning. Beijing-time labels are converted to UTC. Summer group corrections follow the decimal-arithmetic frequency-chain calculation; early absolute correction entries remain incomplete. Their constant part is represented by segment intercepts, while any time variation within a segment remains a possible systematic contribution. Fitted intercepts are never applied to join the runs for long-term stability estimation.

The membership audit contains 1,966,908 nominal one-second rows before the minimum-bin-support cut. Three boundary rows reconcile its difference from the printed interval total. Means are formed in nominal 600-s bins separately within each segment and require at least 180 retained members. The 3,299 accepted means contain 1,965,327 members, or 545.924 h. There are 3,291 unique bin centres: eight centres contain separate partial means from different segments, with disjoint members. The 353.39-day span contains observations on 43 UTC dates. The inherited valid mask is retained; this work neither applies an additional triangular filter nor selects points using tidal residuals. Exact raw-file memberships and hashes are retained in the controlled archive.

### What the constituent names mean

Semidiurnal tides produce approximately two cycles per day. M₂ is the principal lunar constituent; N₂ describes an additional lunar variation associated with orbital ellipticity. S₂ is the principal solar semidiurnal constituent, whereas K₂ contains lunar and solar forcing. The names identify astronomical frequencies, not separate instruments or independent experiments. The diurnal group contains K₁ (lunisolar), O₁ (principal lunar), P₁ (principal solar) and Q₁ (lunar elliptic). Their periods are listed in Extended Data Table 1.^22^ Internal relative amplitudes, phases and nodal modulation are fixed within each physical group. A group response therefore tests that complete specified pattern.

### Combined solid and loading potential

The physical target includes the direct astronomical potential, the Earth's induced potential and the effect of clock displacement. The selected frozen solid sequence implements these through the IERS radial displacement $u$ and a fixed effective-potential conversion,

$$y_{\mathrm{solid}}=-\frac{1+k_2-h_2}{h_2}\frac{g(u_{\mathrm{Wuhan}}-u_{\mathrm{Shanghai}})}{c^2},$$

with $h_2=0.6078$, $k_2=0.3010$ and $g=9.794\,\mathrm{m/s^2}$. This is a displacement-based approximation to the combined solid potential, not the alternative frequency-resolved direct-potential implementation. The same conversion also acts on degree-three and frequency-dependent displacement contributions in the supplied sequence. A previous implementation comparison found an approximately 18% K₁ amplitude deficit relative to a potential-weighted reference. The daily response is accordingly not used to infer a Love number. Uncertainty in the solid model remains separate from the quoted statistical errors.

For loading, FES2022 sea-surface elevations $\zeta$ are convolved with the effective-potential kernel

$$\delta W_{\mathrm{load}}=\int \rho_w\zeta(\mathbf{r}',t)G_W(\psi)\,\mathrm{d}A,\qquad
G_W(\psi)=\frac{ga}{M_E}\sum_n(1+k'_n-h'_n)P_n(\cos\psi).$$

The three terms represent direct water attraction, induced potential and clock displacement. PREM load Love numbers are retained through degree 696 with the archived high-degree continuation. Eighteen loading constituents are synthesized with their astronomical nodal corrections. The complex convention is $f\,\mathrm{Re}[C\exp(-i\phi)]$; reversing the exponential sign requires conjugating $C$. The present analysis reads the frozen constituent and time-series tables rather than substituting an older loading sequence.

The eight named constituents form the three physical groups. Minor terms remain once as a fixed remainder $r_0$. On the actual weighted segment-centred sampling, solid, loading and total root-mean-square variations are respectively 2.928, 1.328 and $4.011\times10^{-18}$. Their ratio 0.331 is an amplitude-norm ratio, not an additive fraction of total power. The separately reported $0.89\pm0.55$ loading coefficient belongs to the alternative directly modelled, filtered reduction. It is unresolved and has not been recalculated as a separate coefficient of the present estimator.

### Joint estimator and zero-point choice

We fit

$$y_i=c_{s(i)}+A_Ls_{L,i}+A_Ss_{S,i}+A_Ds_{D,i}+r_{0,i}+\epsilon_i,$$

with 54 segment intercepts and three physical response coefficients. Weighted least squares uses the frozen Allan-based uncertainties $\sigma_i$, with $W_{ii}=1/\sigma_i^2$. A period noise coefficient $\alpha_p$ is estimated from within-segment overlapping Allan deviations at 256, 512, 1,024, 2,048 and 4,096 s, after removing the fixed unit tide. No Allan window crosses a segment boundary. The bin uncertainty is $\sigma_i=\alpha_{p(i)}/\sqrt{n_i}$, where $n_i$ is its retained member count. This is a working noise model, not stability calculated after joining fit-adjusted levels. Independent QR replay reproduces the eight-period design on the same rows before changing only its intercept grouping. All comparisons therefore hold sampling, correction values, physical templates and weights fixed.

The daily group is an auxiliary physical component, fitted simultaneously to propagate its covariance with the semidiurnal responses. Its coefficient is $A_D=0.58\pm0.54$ (Extended Data Table 2). Its predicted variation is smaller on this baseline, and its longer period supplies fewer cycles within short segments, increasing overlap with segment reference levels and slow variations. This auxiliary estimate is not a separate measurement objective.

The inspected interval and correction records contain no documented calibrated zero transfer for the 46 adjacent segment boundaries that share an eight-period intercept. They give valid times, but not a signed boundary transfer with uncertainty or a lock/relock history establishing unchanged reference levels. This motivates separate segment constants. The same-data residual and deletion diagnostics are reported in Extended Data Fig. 2 and Table 2. Coefficient proximity to one is not a model-selection rule.

### Statistical errors and conditional coverage

For each group the reported standard error is the larger of residual-scaled least squares and leave-one-UTC-day-out jackknife errors. Deletions remove a calendar day, refit all remaining coefficients and drop empty intercept columns. The jackknife variance is $(G-1)G^{-1}\sum_g(\hat A_{(-g)}-\overline A)^2$. Period-deletion errors are recorded separately. Extended Data Table 2 gives all components and the same-data intercept comparisons. Observations are repeated measurements of one clock pair, not thousands of independent experiments.

Conditional simulations apply both designs to the same 3,299-row sampling and heteroscedastic uncertainties. Each of four scenarios has 1,000 realizations: independent Gaussian noise; equal variance contributions from Gaussian white noise and a 6-h Ornstein–Uhlenbeck process within segments; the corresponding 24-h process within periods; and standardized Student-$t_5$ noise. The overall scale is the observed segment-model residual scale; all true physical response coefficients are one. Each realization recomputes both components of the standard-error rule. Seed 2026110617 fixes the simulation. Coverage of $\hat A\pm1.96u$ is 95.1–97.4% for the segment-model lunar coefficient and 95.4–96.8% for its neighbouring coefficient; Monte Carlo standard errors are about 0.4–0.7 percentage points (Extended Data Table 3). These are tests under declared noise laws, not a calibration against every possible disturbance.

The phase-relaxed model adds the lunar quadrature while retaining the prescribed M₂/N₂ relationship. Covariance contours use scaled least squares. Subset and deletion fits refit the same model on their retained rows. Shared-data estimates are not averaged. The simulation coverage refers to two-sided intervals; the reported $\pm$ values are standard errors.

### Phase means, spectral density and sampling sidelobes

For the phase plot, $N$ contains segment constants and the two non-lunar groups. We project both $y-r_0$ and the unit lunar prediction with $M_N=I-N(N^TWN)^{-1}N^TW$, and average in twelve fixed M₂ phase bins. If $B$ is weighted bin averaging, the mean covariance is $BM_NC_yM_N^TB^T$, where $C_y$ is the scaled working observation covariance. It retains correlations between means and propagates nuisance estimation. The full unbinned response remains primary.

Figure 3c preserves the independently specified equal-weight, 54-intercept scan of the unchanged observed means, rather than replacing it with the amplitude fit's weights. Every trial sine–cosine pair and the data are projected against the same constants. For a reduction in squared residuals $\Delta\mathrm{RSS}(f)$ with dimensionless $y$, the nominal one-sided projection density is $S_y(f)=600\,\mathrm{s}\,\Delta\mathrm{RSS}(f)$ per Hz, or $10^{-6}$ times that value per µHz. Potential density is $S_W=c^4S_y$; amplitude density is $c^2\sqrt{S_y}$. Uniform-grid checks reproduce the conventional one-sided Fourier density. For interrupted data this normalization is a stated projection density, not a Parseval-calibrated variance over a filled year.^23^

The frequency step is 0.002729 µHz; the inverse calendar span is 0.032752 µHz. Fine plotting steps do not improve physical resolution. M₂-only and S₂-only astronomical injections use the same actual times, nodal factors and equal-weight segment projection. Power at the opposite principal frequency, divided by power at the injected frequency, gives 0.08027 and 0.08149. Conditional scans project out a freely phased sinusoid at the other frequency before scanning the target neighbourhood. Amplitude interference means that such corrections act on sampled waveforms or complex coefficients, not by subtracting scalar power spectra. Gaps alone do not predict the realization of measurement noise. Residual density can describe remaining measurement fluctuations, but includes possible model mismatch and cannot be called a pure instrumental noise floor.

### Instrument and daily-response checks

The matched monitor calculation uses 1,482 rows with 887,882 nominal members, or 246.634 h, in P6–P8. Both baseline and augmented fits have identical members, segment labels and weights. Paired day-deletion replicates propagate uncertainty in their difference. Extended Data Fig. 3 reports the response changes and dates. This comparison concerns the monitored transmission route during the measured overlap.

On the selected data and model, a common 24-h sine–cosine pair gives $A_L=1.036\pm0.133$; separate 24-h pairs in each period give $1.003\pm0.136$. These daily sensitivity designs address a periodicity motivated by temperature and operating schedules, without assigning an independently measured thermal amplitude. Free 12-h pairs in each period give $0.751\pm0.242$ and a very poorly constrained neighbouring coefficient because they compete with astronomical semidiurnal variation within short periods. That fit is retained as a sensitivity boundary.

The archived single-bin diagnostic and separately filtered reduction are documented in Extended Data Table 4. The latter uses different filtering, weighting, a direct-potential solid model and a residual-shift uncertainty; its manuscript-reported results are distinguished from the present replay. Its ERA5 air-temperature regressors are environmental proxies, distinct from the stated chamber-thermometer record.

### AI-assisted preparation

OpenAI Codex assisted English drafting, numerical replay and figure preparation. [Authors to confirm their verification of the analyses, citations and final text, and responsibility for the submitted work.]

## Data availability

The author review package contains the 3,299 derived means, fixed templates, noise weights, figure source tables and immutable input hashes. The original counters and membership ledger are held in the controlled experimental archive. [Authors to supply an editor-accessible location and confirm the permanent data-access statement and repository identifier before submission.]

## Code availability

The package contains the independent QR replay, same-data design comparison, conditional simulations, spectral calculations, covariance propagation and figure scripts, with software versions and a reproducible entry point. [Authors to confirm the code licence and permanent repository identifier before submission.]

## Methods references

22. NOAA. Harmonic constituents. *NOAA Tides and Currents*. [https://tidesandcurrents.noaa.gov/harcon.html?id=8577330](https://tidesandcurrents.noaa.gov/harcon.html?id=8577330) (accessed 6 November 2026).
23. VanderPlas, J. T. Understanding the Lomb–Scargle periodogram. *Astrophys. J. Suppl. Ser.* **236**, 16 (2018). <https://doi.org/10.3847/1538-4365/aab766>

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

**Extended Data Fig. 2 | Same-data comparison of reference-level designs.** **a,** Weighted segment-mean residuals after the eight-period joint fit, ranging from $-6.75$ to $12.00\times10^{-18}$. Segment constants make these means zero by construction. **b,** Lunar point estimates after period deletion, spanning 0.877–1.052 with eight period constants and 0.885–1.093 with 54 segment constants. The weighted residual sums of squares are 3,781.58 and 3,713.64; the latter has 46 additional intercept parameters. Unweighted residual root-mean-square values are 24.114 and $23.934\times10^{-18}$, and reduced residual sums of squares are 1.1501 and 1.1455. Adjacent standardized residual correlations are −0.127 and −0.148, using pairs within the same segment and separated by at most 900 s. All comparisons retain identical observations, templates, corrections and noise weights. These are residual diagnostics, not measurements of physical jumps or zero-transfer calibration.

\clearpage

![Extended Data Figure 3](figures/ed_figure3.png)

**Extended Data Fig. 3 | Simultaneous summer transmission control.** Changes caused by adding the fibre round-trip monitor to the joint model, with paired UTC-day-jackknife standard errors. Baseline and augmented fits use identical clock/monitor members, labels and weights: 1,482 means containing 887,882 nominal one-second members, or 246.634 h in P6–P8, from 29 June to 25 August 2026. The lunar, neighbouring and daily shifts are respectively $0.00606\pm0.00627$, $0.00594\pm0.01453$ and $0.00791\pm0.01388$. The paired monitor constrains the measured transmission route on this summer overlap. The main tidal estimate uses the entire 545.9-h clock record. The prior transmission-architecture demonstration over 2,067 km is a separate experiment.^16^

\clearpage

**Extended Data Table 1 | Astronomical constituent guide.** Names specify forcing and frequency; one response coefficient multiplies each complete group with its internal ratios and phases fixed.

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

\clearpage

**Extended Data Table 2 | Estimator and uncertainty comparison.** All directly replayed designs use the same 3,299 means, physical templates and Allan-based weights. Errors are standard errors. The alternative filtered estimate is separately labelled author-reported.

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

\clearpage

**Extended Data Table 3 | Conditional 95% interval coverage.** Each scenario has 1,000 simulated realizations per design, with fixed observed sampling and weights. Values are percentages for the larger-of-LS-and-day-jackknife rule, using multiplier 1.96. They assess the specified scenarios, not unknown systematic effects.

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

\clearpage

**Extended Data Table 4 | Archived influence diagnostic and alternative reduction.** These rows identify the observation support and estimator of each result. The single-bin diagnostic retains its original eight-period design. The filtered reduction is reported in the alternative manuscript (v68); its measurements overlap the present data and its results are not pooled with the primary estimates.

| Check | Observation support and design | Result and status |
|---|---|---|
| Pre-identified extreme mean | 2026-07-07 01:25 Beijing time, segment 46; archived eight-period model, fixed templates and weights | Omitting the mean changes the daily coefficient from 0.678 to 0.721: +0.043 versus its original 0.359 standard error. The lunar change is +0.039. Uncertainty was not recalibrated. The mean remains in the present 3,299 rows. |
| Filtered lunar response | Approximately 544 h, 54 segments; 1,200-s triangular filter every 600 s; equal weights, direct-potential solid model; continuous-run circular-residual-shift error | $0.97\pm0.14$, author-reported. The other grouped results are in Extended Data Table 2. |
| Separate loading coefficient | Same alternative filtered reduction; loading assigned a separate coefficient | $0.89\pm0.55$, author-reported and unresolved. This is not a separate loading estimate from the primary design. |
| Temperature regressors | Two-site ERA5 2-m air-temperature proxies in the alternative reduction; distinct from its stated 98-h Sr chamber-thermometer record | Lunar $0.98\pm0.13$, author-reported. Exact regression membership is needed for independent replay. |
| Alternative round-trip control | Reported 474-h overlap in the filtered reduction | Lunar and whole-template coefficient changes less than 0.005, author-reported. Exact matching memberships are needed for independent replay; the directly replayed 246.634-h control is shown in Extended Data Fig. 3. |

The archived influence diagnostic is retained for provenance; the current observation membership is unchanged.
