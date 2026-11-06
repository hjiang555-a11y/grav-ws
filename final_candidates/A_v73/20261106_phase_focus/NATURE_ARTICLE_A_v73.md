# Optical clocks distinguish neighbouring semidiurnal tides

[Author list, order and affiliation assignments to be confirmed by the authors]

^1^ Hefei National Laboratory, University of Science and Technology of China, Hefei, China

^2^ Shanghai Research Center for Quantum Sciences and CAS Center for Excellence in Quantum Information and Quantum Physics, University of Science and Technology of China, Shanghai, China

^3^ Hefei National Research Center for Physical Sciences at the Microscale and School of Physical Sciences, University of Science and Technology of China, Hefei, China

^4^ Innovation Academy for Precision Measurement Science and Technology, Chinese Academy of Sciences, Wuhan, China

^5^ Jinan Institute of Quantum Technology and CAS Center for Excellence in Quantum Information and Quantum Physics, University of Science and Technology of China, Jinan, China

^6^ Time and Frequency Geodesy Center (TFGC), School of Geodesy and Geomatics, Wuhan University, Wuhan, China

## Abstract

Optical clocks can track changes in Earth's gravitational potential, but tides with similar periods are difficult to distinguish in short comparisons.^1,2,3^ Here we distinguish two semidiurnal responses between coastal Shanghai and inland Wuhan. The principal lunar tide takes about 25 minutes longer per cycle than the principal solar tide. Our 546 hours of observations, spread over 353 days, sample the tides at different relative phases. The measured frequency ratio shows distinct spectral peaks near both principal frequencies. Relative to the combined solid-Earth and ocean-loading prediction, fitted amplitude scales are $1.00\pm0.13$ for the lunar group and $0.93\pm0.36$ for the neighbouring group containing the principal solar tide (one statistical standard error). The changing lunar–solar phase provides a reference for comparing tidal signals across interruptions even when the frequency offsets between observing runs are unknown.

## Main text

Two tides can look similar during a short observation, and interruptions can leave an unknown frequency offset between runs. The principal lunar semidiurnal tide M₂ repeats every 12.42 h and the principal solar tide S₂ every 12 h. Observations at different lunar–solar phases can therefore distinguish their responses without joining the runs at a common frequency level.

We use this phase change in a comparison of a strontium clock in Shanghai and a ytterbium clock in Wuhan. The record contains 545.9 h of accepted observations on 43 UTC dates spread over 353 days. A joint model with an independent constant for every valid segment resolves two semidiurnal groups, M₂+N₂ and S₂+K₂. The observed spectrum also has a local peak near each principal frequency. K₂ contains both lunar and solar forcing; the neighbouring group therefore contains more than the purely solar S₂ tide. The group's internal phases and relative amplitudes follow the astronomical prediction. The approximately daily constituents K₁, O₁, P₁ and Q₁ are estimated together as a third group.

Optical clocks measure potential differences through their relative rates.^1,4^ Clock comparisons have resolved laboratory height-dependent redshifts and enabled remote geodetic measurements.^5,6,7^ Stabilized optical-fibre networks connect clocks without transporting them.^8,9^ Time-dependent measurements must distinguish gravitational responses from changes in the clocks and transfer system. Astronomical tides supply frequencies and phases predicted independently of the clock observations.^2,10,11^

### Observing dates and the coastal–inland baseline

The two clocks are 692 km apart and connected through Hefei by a 1,350-km phase-stabilized fibre link (Fig. 1a).^12^ Between September 2025 and August 2026 they supplied 3,299 ten-minute means in 54 valid segments and eight observing periods (Fig. 1c). Observations occur in eight calendar months, with actual UTC times and all missing intervals retained. The June–August periods contribute 273.9 h and sample different lunar–solar phases; the earlier periods add further phases and operating conditions (Fig. 1d). The placement of observations in the lunar–solar cycle supplies the separation between the nearby signals.

The earlier summer comparison reports a nominal white-frequency-noise trend of $5.4\times10^{-16}/\sqrt{\tau/\mathrm{s}}$, where $\tau$ is averaging time.^12^ This describes the linked-clock system's technical performance, while the present amplitude errors are estimated from the observed record. The individual Sr and Yb systems are described in their clock evaluations.^13,14^ Some summer observations overlap the absolute frequency-ratio measurement of Hou and colleagues; here the measured quantity is the time-dependent tidal response. A positive fractional ratio variation means Wuhan Yb runs faster relative to Shanghai Sr. In the geodetic potential convention, $y=-[\delta W_{\mathrm{Wuhan}}-\delta W_{\mathrm{Shanghai}}]/c^2$.

Tides alter the direct gravitational potential, deform the Earth and move the clocks. Ocean tides add the attraction of redistributed water, the Earth's induced potential and displacement of the clock. The prediction combines an IERS-based solid tide with FES2022 ocean elevations convolved with a kernel containing these three loading contributions (Methods).^15,16,17,18^ Shanghai lies beside the East China Sea and Wuhan inland, making their differential potential sensitive to ocean loading.

For M₂, the predicted solid contribution is $3.43\times10^{-18}$ and the loading contribution $1.42\times10^{-18}$ in fractional clock rate. Their phases differ by 19.8°, giving a combined amplitude of $4.78\times10^{-18}$ (Fig. 1b). After removing segment means, loading's weighted root-mean-square variation is 33.1% of the combined prediction on the sampled record. This model contribution is distinct from an observed loading coefficient. A separate filtered analysis allowing loading its own coefficient reported $0.89\pm0.55$; that coefficient remains unresolved (Methods).

The zero-point choice follows the available experimental records. Of the segment boundaries within the eight periods, 46 have no documented calibrated zero transfer. We therefore allow each of the 54 segments its own constant, retaining the changing tidal signal within each run. Physical responses are estimated jointly from the original ten-minute means with fixed noise weights. No empirical daily sinusoid is removed before this fit, and no fitted values fill the gaps.

### Two semidiurnal responses and two spectral peaks

The joint fit gives $A_L=1.00\pm0.13$ for M₂+N₂ and $A_S=0.93\pm0.36$ for S₂+K₂ (Fig. 2b). One denotes the combined solid-Earth and ocean-loading prediction. Errors are one statistical standard error, taken as the larger of residual-scaled least squares and UTC-day deletion; components and conditional coverage tests are given in Methods. The daily group is estimated in the same model as $A_D=0.58\pm0.54$. Its larger uncertainty is propagated through the joint fit, which still constrains both semidiurnal groups.

The same measured frequency-ratio record shows local spectral peaks at 22.361 and 23.147 µHz, close to the prescribed M₂ and S₂ frequencies of 22.364 and 23.148 µHz (Fig. 2a). The scan uses all 3,299 observed means at their actual UTC times, with 54 segment constants and equal weights. The peak separation exceeds the inverse calendar span, 0.0328 µHz. The left axis gives density in gravitational-potential units and the right the equivalent fractional-frequency density. A fractional variation of $10^{-18}$ corresponds to about $0.09\,\mathrm{m^2/s^2}$ in potential difference.

The observation window also produces sidelobes. Sampling a single tidal line only at the measured times spreads power towards neighbouring frequencies. Passing individual M₂ and S₂ predictions through this same sampling and scan gives 8.03% M₂-to-S₂ cross-power and 8.15% in the reverse direction. These are responses of the sampling window, not random noise generated by missing observations. A conditional scan retains a local feature near each principal frequency after projecting out the sine and cosine at the other (Extended Data Fig. 2).

These checks support assigning the two features to the principal lunar and solar semidiurnal neighbourhoods. The grouped amplitudes come from the simultaneous physical templates, with prescribed internal relationships and Allan-based noise weights; they do not treat N₂ or K₂ as individually resolved spectral lines. The spectrum, including its curve after subtracting the fixed unit prediction, displays the same observations and supplies no independent detection probability.

The phase of the recurring signal is also compatible with the prediction. Adding a lunar component one quarter-cycle from the predicted phase gives in-phase and quadrature responses of $1.00\pm0.13$ and $-0.10\pm0.20$ (Fig. 2c). Figure 3 orders the full record into twelve M₂ phase bins. The observations after subtracting the fixed minor remainder, and the unit lunar prediction, undergo identical projection against the segment constants and other fitted groups. Propagated errors retain nuisance-parameter uncertainty and covariance between phase means. All individual points and each bin's support remain visible, so the folded curve can be traced to the full record.

### Support across observing periods and instrument controls

The lunar response is supported on both sides of summer. With the same segment model it is $1.21\pm0.23$ before summer and $0.77\pm0.18$ in summer. Deleting one observing period at a time gives point estimates from 0.885 to 1.093 (Fig. 4a). These overlapping fits show how each period contributes to the full-record estimate.

As a same-data check, sharing one reference level within each of the eight periods gives a lunar coefficient of $0.987\pm0.123$ and a neighbouring coefficient of $1.129\pm0.288$. Only the intercept grouping changes in this comparison; observations, physical templates and weights are identical. Residual structure and deletion results are retained in Methods and Extended Data Fig. 1. The segment model is selected from the zero-transfer evidence, rather than the proximity of a coefficient to one.

A simultaneous fibre round-trip record tests the monitored transmission channel on 246.6 h of summer observations, from 29 June to 25 August 2026. Clock and monitor means contain matching valid members. Adding the monitor to the otherwise identical fit changes the lunar coefficient by $+0.0061\pm0.0063$ and the neighbouring coefficient by $+0.0059\pm0.0145$ (Fig. 4b). Its coverage is confined to that overlap and transmission route; other local transfer branches and clock effects require their own observations.

Temperature changes and operating schedules motivate checks at 24 h. A separate filtered analysis reports $0.98\pm0.13$ with two-site temperature regressors, whose sampling and supporting measurements are described in Methods. Adding a shared 24-h sine–cosine pair on the present observations gives $1.04\pm0.13$. The weakly constrained physical daily group is not a bound on laboratory disturbance. Freely phased 12-h terms, which compete with the astronomical semidiurnal groups within short runs, are retained only as sensitivity tests in Methods.

The astronomical phase continues across an interruption even when the measured frequency zero is not transferred. This phase reference allows a sparse clock comparison to distinguish nearby tidal responses across a 353-day span. Contemporaneous European clock-network observations by Stahl and colleagues track time-dependent potential on different baselines and with different tidal mixtures.^3^ They complement the grouped semidiurnal measurement on this coastal–inland link. Longer coastal records at lower noise, with phase coverage that distinguishes the solid and loading contributions and calibrated local transfer paths, could allow ocean loading to be tested separately.

\clearpage

## Figure legends

![Figure 1](figures/figure1.png)

**Fig. 1 | Observing geometry and lunar–solar phase coverage.** **a,** Shanghai Sr and Wuhan Yb, 692 km apart, with the 1,350-km fibre connection through Hefei drawn schematically. **b,** Predicted differential M₂ solid and ocean-loading phasors, with the solid component defining phase zero; amplitudes are fractional clock rates in units of $10^{-18}$. **c,** Actual UTC sampling on 43 dates over 353 days, in eight observing periods, with accepted nominal member-hours (545.9 h in total). **d,** The S₂−M₂ astronomical phase at those same samples, including nodal corrections. Summer periods P6–P8 are orange. Geography and phasors describe the prediction; the lower panels describe the observation window.

\clearpage

![Figure 2](figures/figure2.png)

**Fig. 2 | Two semidiurnal spectral peaks and their grouped responses.** **a,** Equal-weight scan of all 3,299 observed means at their true UTC times, with 54 segment constants. Peaks occur at 22.361 and 23.147 µHz, near M₂ and S₂. Blue is the observed scan; orange follows subtraction of the fixed unit total prediction. Gaps are retained. The two axes express the same nominal one-sided projection density per µHz, related by $S_W=c^4S_y$. The actual sampling yields about 8% bidirectional single-line M₂/S₂ cross-power. **b,** Joint physical-group amplitudes with one standard error, defined as the larger of scaled least-squares and UTC-day-jackknife errors. These estimates use the physical templates and Allan-based noise weights. **c,** Lunar in-phase and quadrature responses; the cross marks the unit prediction. Contours have scaled-least-squares covariance radii one and two, not separately calibrated joint confidence levels. The spectral peaks identify principal-frequency neighbourhoods, while **b** estimates prescribed constituent groups. All panels use the same observation rows and are not independent significance tests.

\clearpage

![Figure 3](figures/figure3.png)

**Fig. 3 | The full record ordered by lunar phase.** **a,** Twelve 30° M₂ phase means of all 3,299 observations, after subtracting the fixed minor remainder and projecting against 54 segment constants and the neighbouring semidiurnal and daily groups. Identical weighted projection and averaging are applied to the unit lunar prediction; the fitted curve uses the unbinned primary coefficient. Error bars are one working standard error with the nuisance projection propagated; phase means are correlated. **b,** Every projected observation, with the full observed vertical range. **c,** Number of rows in each bin. Data, weights and templates are the primary segment design throughout. This is a display of the main observations, not an independent experiment.

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

Semidiurnal tides produce approximately two cycles per day. M₂ is the principal lunar constituent; N₂ describes an additional lunar variation associated with orbital ellipticity. S₂ is the principal solar semidiurnal constituent, whereas K₂ contains lunar and solar forcing. The names identify astronomical frequencies, not separate instruments or independent experiments. The diurnal group contains K₁ (lunisolar), O₁ (principal lunar), P₁ (principal solar) and Q₁ (lunar elliptic). Their periods are listed in Extended Data Table 3.^19^ Internal relative amplitudes, phases and nodal modulation are fixed within each physical group. A group response therefore tests that complete specified pattern.

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

with 54 segment intercepts and three physical response coefficients. Weighted least squares uses the frozen Allan-based uncertainties $\sigma_i$, with $W_{ii}=1/\sigma_i^2$. A period noise coefficient $\alpha_p$ is estimated from within-segment overlapping Allan deviations at 256, 512, 1,024, 2,048 and 4,096 s, after removing the fixed unit tide. No Allan window crosses a segment boundary. The bin uncertainty is $\sigma_i=\alpha_{p(i)}/\sqrt{n_i}$, where $n_i$ is its retained member count. This is a working noise model, not stability calculated after joining fit-adjusted levels. Independent QR replay reproduces the eight-period design before changing only its intercept grouping. Sampling, corrections, templates and weights are held fixed.

The inspected interval and correction records contain no documented calibrated zero transfer for the 46 adjacent segment boundaries that share an eight-period intercept. They give valid times, but not a signed boundary transfer with uncertainty or a lock/relock history establishing unchanged reference levels. This motivates the segment design. The eight-period model's weighted residual sum of squares is 3,781.58; the segment model's is 3,713.64, with 46 additional intercept parameters. Their unweighted residual root-mean-square values are 24.114 and $23.934\times10^{-18}$. Reduced residual sums of squares are 1.1501 and 1.1455. The numerical improvement alone does not establish a physical jump at each boundary.

With period constants, weighted segment-mean residuals range from $-6.75$ to $12.00\times10^{-18}$. Adjacent standardized residual correlations, restricted to the same segment and separations of at most 900 s, are −0.127 and −0.148 for the period and segment designs. Deleting a period gives lunar point-estimate ranges 0.877–1.052 and 0.885–1.093, respectively (Extended Data Fig. 1).

### Statistical errors and conditional coverage

For each group the reported standard error is the larger of residual-scaled least squares and leave-one-UTC-day-out jackknife errors. Deletions remove a calendar day, refit all remaining coefficients and drop empty intercept columns. The jackknife variance is $(G-1)G^{-1}\sum_g(\hat A_{(-g)}-\overline A)^2$. Period-deletion errors are recorded separately. Extended Data Table 1 gives all components and the same-data intercept comparisons. Observations are repeated measurements of one clock pair, not thousands of independent experiments.

New conditional simulations apply both designs to the same 3,299-row sampling and heteroscedastic uncertainties. Each of four scenarios has 1,000 realizations: independent Gaussian noise; equal variance contributions from Gaussian white noise and a 6-h Ornstein–Uhlenbeck process within segments; the corresponding 24-h process within periods; and standardized Student-$t_5$ noise. The overall scale is the observed segment-model residual scale; all true physical response coefficients are one. Each realization recomputes both components of the standard-error rule. Seed 2026110617 fixes the simulation. Coverage of $\hat A\pm1.96u$ is 95.1–97.4% for the segment-model lunar coefficient and 95.4–96.8% for its neighbouring coefficient; Monte Carlo standard errors are about 0.4–0.7 percentage points (Extended Data Table 2). These are tests under declared noise laws, not a calibration against every possible disturbance.

The phase-relaxed model adds the lunar quadrature while retaining the prescribed M₂/N₂ relationship. Covariance contours use scaled least squares. Subset and deletion fits refit the same model on their retained rows. No shared-data estimates are averaged, and no half-daily coefficient is converted into a daily upper limit.

### Phase means, spectral density and sampling sidelobes

For the phase plot, $N$ contains segment constants and the two non-lunar groups. We project both $y-r_0$ and the unit lunar prediction with $M_N=I-N(N^TWN)^{-1}N^TW$, and average in twelve fixed M₂ phase bins. If $B$ is weighted bin averaging, the mean covariance is $BM_NC_yM_N^TB^T$, where $C_y$ is the scaled working observation covariance. It retains correlations between means and propagates nuisance estimation. The full unbinned response remains primary.

Figure 2a preserves the independently specified equal-weight, 54-intercept scan of the unchanged observed means, rather than replacing it with the amplitude fit's weights. Every trial sine–cosine pair and the data are projected against the same constants. For a reduction in squared residuals $\Delta\mathrm{RSS}(f)$ with dimensionless $y$, the nominal one-sided projection density is $S_y(f)=600\,\mathrm{s}\,\Delta\mathrm{RSS}(f)$ per Hz, or $10^{-6}$ times that value per µHz. Potential density is $S_W=c^4S_y$; amplitude density is $c^2\sqrt{S_y}$. Uniform-grid checks reproduce the conventional one-sided Fourier density. For interrupted data this normalization is a stated projection density, not a Parseval-calibrated variance over a filled year.^20^

The frequency step is 0.002729 µHz; the inverse calendar span is 0.032752 µHz. Fine plotting steps do not improve physical resolution. M₂-only and S₂-only astronomical injections use the same actual times, nodal factors and equal-weight segment projection. Power at the opposite principal frequency, divided by power at the injected frequency, gives 0.08027 and 0.08149. Conditional scans project out a freely phased sinusoid at the other frequency before scanning the target neighbourhood. Amplitude interference means that such corrections act on sampled waveforms or complex coefficients, not by subtracting scalar power spectra. Gaps alone do not predict the realization of measurement noise. Residual density can describe remaining measurement fluctuations, but includes possible model mismatch and cannot be called a pure instrumental noise floor.

### Instruments, environmental checks and the alternative reduction

The apparatus performance coefficient quoted in the main text describes the gap-concatenated summer record in the earlier frequency-ratio manuscript.^12^ The present noise coefficients are estimated separately using only within-segment Allan windows, as defined above.

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

1. Mehlstäubler, T. E., Grosche, G., Lisdat, C., Schmidt, P. O. & Denker, H. Atomic clocks for geodesy. *Rep. Prog. Phys.* **81**, 064401 (2018). [https://doi.org/10.1088/1361-6633/aab409](https://doi.org/10.1088/1361-6633/aab409)
2. Voigt, C., Denker, H. & Timmen, L. Time-variable gravity potential components for optical clock comparisons and the definition of international time scales. *Metrologia* **53**, 1365–1383 (2016). [https://doi.org/10.1088/0026-1394/53/6/1365](https://doi.org/10.1088/0026-1394/53/6/1365)
3. Stahl, K. et al. Optical clock network tracks tidal variations of the gravity potential. *arXiv*, 2610.39635v1 (2026). [https://arxiv.org/abs/2610.39635v1](https://arxiv.org/abs/2610.39635v1)
4. Ludlow, A. D., Boyd, M. M., Ye, J., Peik, E. & Schmidt, P. O. Optical atomic clocks. *Rev. Mod. Phys.* **87**, 637–701 (2015). [https://doi.org/10.1103/revmodphys.87.637](https://doi.org/10.1103/revmodphys.87.637)
5. Chou, C. W., Hume, D. B., Rosenband, T. & Wineland, D. J. Optical Clocks and Relativity. *Science* **329**, 1630–1633 (2010). [https://doi.org/10.1126/science.1192720](https://doi.org/10.1126/science.1192720)
6. McGrew, W. F. et al. Atomic clock performance enabling geodesy below the centimetre level. *Nature* **564**, 87–90 (2018). [https://doi.org/10.1038/s41586-018-0738-2](https://doi.org/10.1038/s41586-018-0738-2)
7. Grotti, J. et al. Geodesy and metrology with a transportable optical clock. *Nat. Phys.* **14**, 437–441 (2018). [https://doi.org/10.1038/s41567-017-0042-3](https://doi.org/10.1038/s41567-017-0042-3)
8. Lisdat, C. et al. A clock network for geodesy and fundamental science. *Nat. Commun.* **7**, 12443 (2016). [https://doi.org/10.1038/ncomms12443](https://doi.org/10.1038/ncomms12443)
9. Riehle, F. Optical clock networks. *Nat. Photon.* **11**, 25–31 (2017). [https://doi.org/10.1038/nphoton.2016.235](https://doi.org/10.1038/nphoton.2016.235)
10. Denker, H. et al. Geodetic methods to determine the relativistic redshift at the level of $10^{-18}$ in the context of international timescales: a review and practical results. *J. Geod.* **92**, 487–516 (2018). [https://doi.org/10.1007/s00190-017-1075-1](https://doi.org/10.1007/s00190-017-1075-1)
11. Schröder, S., Stellmer, S. & Kusche, J. Potential and scientific requirements of optical clock networks for validating satellite-derived time-variable gravity data. *Geophys. J. Int.* **226**, 764–779 (2021). [https://academic.oup.com/gji/article/226/2/764/6212226](https://academic.oup.com/gji/article/226/2/764/6212226)
12. Hou, L. et al. Yb/Sr optical clock comparison at $2.2\times10^{-18}$ uncertainty over a 1350-km fiber link. *arXiv*, 2610.34250v1 (2026). [https://arxiv.org/abs/2610.34250v1](https://arxiv.org/abs/2610.34250v1)
13. Jia, Z.-P. et al. Improved systematic evaluation of a strontium optical clock with uncertainty below $1\times10^{-18}$. *Metrologia* **63**, 025002 (2026). [https://doi.org/10.1088/1681-7575/ae449e](https://doi.org/10.1088/1681-7575/ae449e)
14. Zhu, Q. et al. Ytterbium lattice clock with systematic uncertainty of $1.3\times 10^{-18}$ and instability at the $10^{-19}$ level. *arXiv*, 2606.10514v2 (2026). [https://arxiv.org/abs/2606.10514v2](https://arxiv.org/abs/2606.10514v2)
15. Petit, G. & Luzum, B. (eds) IERS Conventions (2010). *IERS Technical Note* **36** (2010). [https://iers-conventions.obspm.fr/content/tn36.pdf](https://iers-conventions.obspm.fr/content/tn36.pdf)
16. CNES. FES2022 (Finite Element Solution) Tidal model (Version 2024). CNES [https://doi.org/10.24400/527896/A01-2024.004](https://doi.org/10.24400/527896/A01-2024.004) (2024).
17. Farrell, W. E. Deformation of the Earth by surface loads. *Rev. Geophys.* **10**, 761–797 (1972). [https://doi.org/10.1029/RG010i003p00761](https://doi.org/10.1029/RG010i003p00761)
18. Han, D. & Wahr, J. The viscoelastic relaxation of a realistically stratified earth, and a further analysis of postglacial rebound. *Geophys. J. Int.* **120**, 287–311 (1995). [https://doi.org/10.1111/j.1365-246x.1995.tb01819.x](https://doi.org/10.1111/j.1365-246x.1995.tb01819.x)
19. NOAA. Harmonic constituents. *NOAA Tides and Currents*. [https://tidesandcurrents.noaa.gov/harcon.html?id=8577330](https://tidesandcurrents.noaa.gov/harcon.html?id=8577330) (accessed 6 November 2026).
20. VanderPlas, J. T. Understanding the Lomb–Scargle periodogram. *Astrophys. J. Suppl. Ser.* **236**, 16 (2018). https://doi.org/10.3847/1538-4365/aab766

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
