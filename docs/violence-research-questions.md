# Violence-centered research-question slate

Status: **five candidates for the researcher's relevance decision**. Results below are POCs,
not final causal estimates. Questions about rainfall, public works, and school transport are
outside the selected violence scope.

## RQ1 — Do formal-employment shocks alter lethal violence?

**Current answer:** Not demonstrated yet. In the annual 2009–2017 RAIS/SDS panel, changes in
formal jobs per resident correlate negatively with changes in MVI both contemporaneously
(Spearman rho -0.468, p=0.021) and with a one-year lag (-0.595, p=0.004). Once each year's
common three-city shock is removed, the correlations shrink to -0.098 (p=0.648) and -0.275
(p=0.227). In the 2024–2025 monthly Novo CAGED panel, almost all adjusted correlations are
small; only the one-month-lag balance reaches rho -0.243 (p=0.044), without a multiple-testing
correction.

**Interpretation:** The attractive raw association is largely shared macro-time variation.
There is no current basis for saying that job losses caused higher MVI. A defensible causal
version needs a separately identified employment shock, longer Novo CAGED history, city and
time fixed effects, population offsets, and pre-trend/placebo checks.

## RQ2 — Does employment-sector composition predict violence better than total employment?

**Current answer:** No in the current annual POC. With leave-one-year-out evaluation on the
three-city 2009–2017 panel, a ridge model using total formal employment has MAE 7.81 MVI per
100,000. Adding all CNAE section shares raises MAE to 8.64, a 10.6% loss of skill. Across a
regularization sensitivity grid, the best total-employment model reaches MAE 5.56, versus
8.64 for the best sector-composition specification. The 2024–2025 monthly experiment is too
sensitive to regularization to overturn that conclusion.

**Why the question remains substantive:** RAIS confirms very different economic structures.
In 2014, manufacturing was 30.1% of Cabo formal jobs, versus 15.5% in Jaboatão and 4.3% in
Recife. The negative predictive result therefore is not caused by a lack of sector variation;
it is more likely driven by the tiny 27-observation panel and unstable high-dimensional model.

## RQ3 — Are there spatial spillovers of lethal violence between the three cities and neighbors?

**Current answer:** There is no evidence for one uniform adjacency spillover. For the 11-city
system consisting of Cabo, Jaboatão, Recife, and their immediate municipal neighbors, the
2021–2025 average MVI rate has Moran's I 0.118 (999-permutation p=0.184). After removing the
annual Pernambuco-wide rate, Recife co-moves with its neighbors (rho 0.730 contemporaneously;
0.543 with a one-year neighbor lag), Cabo does not (0.220; 0.213), and Jaboatão is negatively
associated contemporaneously (-0.626) but not at one year (-0.183).

**Interpretation:** A single SAR coefficient for the whole metropolitan system would hide
heterogeneity. The next model should distinguish borders/corridors and test direction-specific
lags rather than assume that every touching municipality transmits the same process.

## RQ4 — Did the 2014 public-campus expansion change Cabo's formal economy?

The intervention is the combined start of UACSA/UFRPE and IFPE in Cabo in 2014. This is more
defensible than using university headquarters: the INEP course table locates physical
in-person offerings, while headquarters data can contain statewide staff.

**Current answer:** No aggregate employment boost is visible through 2017. Formal jobs per
100 residents rose from 10.3 in 2009 to 22.5 in 2013, before the campuses, then fell to 22.2,
20.2, 18.3, and 10.5 from 2014 through 2017. A synthetic path with excellent pre-fit (RMSPE
0.315) places Cabo an average 1.69 jobs per 100 residents, or 8.7%, below the synthetic control
after 2014. Education jobs were essentially flat at about 0.50 per 100 residents in 2013–2016.

**Interpretation:** This is not evidence that campuses reduced employment. Their opening
coincided with a large industrial/construction reversal associated with Cabo/Suape, and the
post-period is short. It does show that a campus-impact claim cannot be based on the city's
aggregate job trajectory; effects must be sought in education jobs, graduate retention,
firm formation, wages, and sectors linked to the new engineering programs.

## RQ5 — Did the 2014 public-campus expansion reduce lethal violence in Cabo?

**Current answer:** No detectable break in the descriptive time series. Cabo's MVI trend was
-0.91 per 100,000 per year in 2004–2013 and -0.74 in 2014–2025; neither slope differs reliably
from zero. Relative to the extrapolated pre-period trend, the post-2014 rate averages 4.7 per
100,000 higher, not lower. A simple synthetic-control design is not credible because no convex
combination of large Pernambuco municipalities reproduces Cabo's high and volatile pre-2014
violence path (pre-RMSPE 26.6 per 100,000 in the >=100,000-resident donor pool).

**Interpretation:** The available aggregate evidence does not support a violence-reduction
claim. The question becomes viable only with a better comparison design, a longer mechanism
chain (campus capacity -> local enrollment/completion -> labor-market outcomes -> violence),
and possibly submunicipal CVLI data.

## Decision requested

Mark each question **keep**, **modify**, or **drop**. In particular, decide whether RQ4 and RQ5
capture the university/education impact you wanted, and whether the negative current answers
make them more or less valuable for the final project.
