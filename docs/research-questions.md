# Answered research-question slate

## RQ1 — What urban-form profiles emerge across Cabo, Jaboatão, and Recife?

**Current answer:** The data strongly supports two broad regimes, while a four-profile
solution provides stable and more interpretable subtypes. The two-cluster silhouette is
0.8497, compared with 0.4246 for four clusters. However, the four-cluster solution is highly
stable across repeated initializations (mean adjusted Rand index 0.9857), and it exposes a
small seasonal/coastal subtype that the two-cluster solution obscures. The first two PCA
dimensions explain 70.98% of the scaled variation.

**Finding:** Treat two profiles as the strongest coarse statistical partition and four as an
exploratory, fine-grained typology. Neither is a vulnerability or danger classification.

**Main limitation:** Results depend on the chosen feature set and scaling. RQ8 confirms that
income and surroundings materially change the four-profile assignment.

## RQ2 — Are sector characteristics spatially autocorrelated enough to justify spatial models?

**Current answer:** Yes. All six city-variable tests are significant under 999 permutations
(empirical p=0.001). Moran's I for log population density is 0.662 in Cabo, 0.550 in Jaboatão,
and 0.346 in Recife. Vacancy-share Moran's I is 0.331, 0.202, and 0.138 respectively.

**Finding:** A model that assumes independent sectors discards real structure, especially in
Cabo. Spatial lags, blocked evaluation, and graph representations are empirically justified.

**Main limitation:** Global Moran's I establishes clustering but does not locate hot/cold
spots or show that spatial features improve a specific downstream outcome.

## RQ3 — How large is cross-city domain shift, and does a learned model transfer?

**Current answer:** The domains are measurably different. A spatial-blocked linear classifier
distinguishes Cabo from Recife with mean ROC AUC 0.876, Cabo from Jaboatão with 0.738, and
Jaboatão from Recife with 0.715. Neighbor density is the strongest Cabo–Recife discriminator.

The initial vacancy-share regression does **not** transfer reliably: mean skill across the six
cross-city directions is -0.079 relative to simply predicting the training-city median. The
worst direction is Jaboatão → Cabo (skill -0.249; R² -0.539). Only Recife → Jaboatão beats that
naive median (skill +0.123), while still having negative R² against the test-city mean.

**Finding:** Domain shift exists, but the current vacancy model is also weak inside each city.
We cannot yet attribute transfer failure solely to domain shift; richer features and a more
substantive target are required.

**Main limitation:** Vacancy share is a methodological proxy, not the final social outcome.

## RQ4 — Is Cabo a distinct urban domain, especially in occasional-use coastal housing?

**Current answer:** Yes, within the current representation. Profile-composition divergence
between Cabo and Recife is 0.110 bits, more than three times the Jaboatão–Recife divergence
of 0.0335 bits. The most seasonal profile has a median occasional-use share of 62.26% and
contains 11.61% of Cabo sectors, versus 0.32% of Jaboatão and 0.04% of Recife sectors.

**Finding:** Cabo contains a sizable urban subtype that is almost absent elsewhere, consistent
with the mapped coastal sectors. This is a concrete reason to expect Recife-trained models to
miss part of Cabo's urban structure.

**Main limitation:** “Coastal” is currently inferred from the map and housing signature.
Distance to coastline, Suape, BR-101, PE-60, and land-use data must test that interpretation.

## RQ5 — How do MVI rates differ over time, and can public MVI data support sector modeling?

**Current answer:** Cabo has improved much less than the comparison cities. From 2004 to
2025, its MVI rate declined 16.7%, versus 62.2% in Jaboatão and 46.3% in Recife. Its mean
2021–2025 rate is 73.64 victims per 100,000 residents, compared with 42.33 and 36.97.
In 2025 Cabo's rate is 65.12, versus 36.33 in Recife and 34.93 in Jaboatão.
That is 1.79 times Recife's rate (approximate 95% CI 1.49–2.15) and 1.86 times Jaboatão's
(1.51–2.29), using a Poisson rate-ratio approximation.

The official SDS microdata has exact dates but only municipality and region fields. It has no
neighborhood, address, coordinates, or AIS, so it cannot label Census sectors.

**Finding:** The municipal MVI divergence is a strong motivation and a valid macro outcome,
but it cannot answer where within Cabo violence concentrates. A sector-level violence model
requires a new privacy-safe data source or a different sector-level outcome.

**Main limitation:** Rates use official estimates plus Census 2010/2022 counts; 2007 and 2023
denominators are linearly interpolated. MVI is not identical to the older CVLI definition.

## RQ6 candidate — Do lower-income sectors overlap with worse street environments?

**Current answer:** Yes, but far more strongly in Recife and Jaboatão than in Cabo. Within
each municipality, the bottom-income and top-environment-deficit quintiles overlap 1.30 times
more often than independence would predict in Cabo, 2.18 times in Jaboatão, and 2.47 times in
Recife. Spearman correlations between mean responsible-person income and the exploratory
environment index are -0.307, -0.618, and -0.759 respectively.

The result survives removing the two dimensions with the strongest ceiling effects (no bus
stop and no wheelchair ramp): overlap lifts become 1.36, 2.30, and 2.48, while correlations
are -0.327, -0.623, and -0.752.

**Finding:** Socioeconomic and street-environment disadvantage are tightly coupled in Recife
and Jaboatão, but only moderately coupled in Cabo. Cabo likely needs extra explanatory
dimensions rather than a Recife-derived deprivation rule.

**Main limitation:** This is a cross-sectional ecological association. The income measure is
the mean monthly income of responsible persons with income, and the equal-weight environment
index is descriptive; neither supports individual or causal claims.

## RQ7 candidate — Does income make street-environment models transferable across cities?

**Current answer:** Materially. With only basic urban-form predictors, mean skill over the six
cross-city directions is 0.134 relative to the training-city median. Adding mean responsible-
person income raises mean skill to 0.310. Every enriched transfer direction has positive
out-of-city R² (minimum 0.164), whereas five of six basic-feature directions have negative R².

The stricter five-dimension environment index gives the same result: mean cross-city skill
rises from 0.162 to 0.330, and every enriched direction remains positive in R² (minimum 0.211).

**Finding:** Income supplies transferable signal that basic morphology misses. This is the
first POC in the project where cross-city generalization works consistently, although the
target is observed infrastructure—not violence.

**Main limitation:** Income and surroundings come from the same 2022 Census context, so this
is contemporaneous prediction and ablation, not forecasting or causal inference.

## RQ8 candidate — Are the original profiles robust to income and environment enrichment?

**Current answer:** No, not as a substantive four-class typology. The enriched K=4 solution
is extremely stable across random seeds (mean ARI 0.998), but agreement with the original K=4
labels is only ARI 0.362. In both the basic and enriched specifications, K=2 remains the clear
silhouette winner (0.850 and 0.851); K=4 falls from 0.425 to 0.377 after enrichment.

**Finding:** The optimization is reproducible, but the four-profile interpretation is
construct-sensitive. The two broad regimes are defensible; finer labels should be treated as
feature-dependent exploratory views rather than a fixed urban taxonomy.

**Main limitation:** This sensitivity test still uses PCA + K-means and two added summary
features. Alternative representations and external validation could support other typologies.
