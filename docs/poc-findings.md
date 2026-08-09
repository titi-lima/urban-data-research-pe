# Initial POC findings

Snapshot date: 2026-08-08.

## Census and geometry

- 4,543 unique sectors across Cabo (465), Jaboatão (1,243), and Recife (2,835).
- The source GeoPackage stores Recife sector `261160605180056` as two polygons. The pipeline
  dissolves them into one analysis unit before joining.
- All 4,543 unique mesh sectors matched the current basic aggregate file.
- The within-municipality Queen-contiguity graph contains 13,696 undirected edges.

## Urban-form profile experiment

PCA retains 57.79% and 13.19% of the scaled feature variation in its first two components.
Four-cluster K-means creates groups of 3,026, 59, 1,313, and 145 sectors.

The 59-sector profile is particularly informative as a data-quality/domain-shift clue:
54 of its sectors are in Cabo, and its median occasional-use housing share is 62.3%.
The map places it predominantly along Cabo's coast. This likely distinguishes a coastal/
seasonal housing morphology that a model trained mostly on Recife would barely observe.
That interpretation is a hypothesis to validate with land-use and OSM data, not a finding
about violence.

Median population density also differs substantially: about 7,320 people/km² in Cabo,
11,636 in Jaboatão, and 15,967 in Recife. Cross-city validation is therefore essential.

## Income and street-environment enrichment

The definitive income and surroundings releases add usable data for 4,476 and 4,416 sectors,
respectively. Lower income aligns with worse observed street environments, but the strength
differs sharply: Spearman rho is -0.307 in Cabo, -0.618 in Jaboatão, and -0.759 in Recife.
Bottom-income/top-deficit quintile overlap is 1.30, 2.18, and 2.47 times the independence
expectation. Removing near-universal bus-stop and wheelchair-ramp deficits barely changes the
conclusion.

For the environment target, income changes transfer from marginal to useful: mean cross-city
skill rises from 0.134 with basic urban form to 0.310 with income added. All six enriched
directions have positive test-city R². This is evidence for transferable socioeconomic signal,
not evidence that income causes infrastructure conditions.

The enriched K=4 profile solution is seed-stable but agrees poorly with the original labels
(adjusted Rand index 0.362). This separates computational stability from construct validity:
two broad regimes are robust, while the four-subtype story depends on feature choice.

## MVI outcome experiment

The SDS-PE workbook is much richer temporally than the earlier public-report route suggested:
it has victim rows and exact dates. It is still municipality-only geographically. The useful
next experiment is a separate municipal time-series model or descriptive validation; it is
not legitimate to copy these outcomes onto sectors.

## What this changes

The project now has two linked but distinct analytical scales:

1. intraurban sector representation, currently outcome-independent;
2. municipal MVI time series, suitable for temporal/cross-city context.

They should remain separate until a privacy-safe submunicipal violence source is obtained.
