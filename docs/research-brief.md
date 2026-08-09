# Research brief

## Core idea

Construct a sector-level urban representation for Cabo de Santo Agostinho and compare
three progressively richer representations:

1. tabular socioeconomic and demographic indicators;
2. spatially lagged indicators from neighboring census sectors;
3. graph and network indicators derived first from sector contiguity, then from OSM roads,
   access to services, land use, and Cabo's logistics/industrial corridors.

The strongest technical contribution is not a generic crime predictor. It is the
reproducible construction of a heterogeneous urban feature store and a controlled
ablation study of which data families add information and transfer across cities.

## Candidate questions

1. What urban-form profiles emerge across Cabo, Jaboatão, and Recife?
2. Are sector characteristics spatially autocorrelated enough to justify spatial models?
3. How large is cross-city domain shift, and does a learned model transfer?
4. Is Cabo a distinct urban domain, especially in occasional-use coastal housing?
5. How do MVI rates differ over time, and can public MVI data support sector modeling?

See `research-questions.md` for current empirical answers and limitations.

## Staged model matrix

| Stage | Feature family | Purpose |
|---|---|---|
| A | Census basic + socioeconomic | Transparent baseline |
| B | Neighbor lags + contiguity graph | Test whether local context adds signal |
| C | OSM street graph + accessibility | Measure centrality, connectivity, and isolation |
| D | POIs/equipment + land use | Measure access to services and urban function |
| E | Cross-city evaluation | Quantify generalization and domain shift |

## Outcome strategy

The preferred supervised outcome is geocoded or neighborhood-level CVLI with date. If SDS-PE
only publishes municipality/month counts, it cannot label census sectors. In that case:

- retain the intraurban work as an outcome-independent urban morphology/vulnerability study;
- use municipal time series only for a separate macro validation;
- file a formal access-to-information request for anonymized, spatially coarsened events; or
- adopt a different, legitimately sector-level outcome such as service accessibility.

## Immediate next data families

1. Census 2022 urban-surroundings and income files.
2. OSM road graph and POIs with a cached, timestamped extract.
3. CNES health facilities and INEP schools.
4. MapBiomas land-use proportions.
5. Cabo public works, with locations geocoded only after auditing address quality.
