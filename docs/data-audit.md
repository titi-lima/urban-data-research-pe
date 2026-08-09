# Data audit

## Confirmed and used in the POCs

| Source | Grain | Status | Notes |
|---|---|---|---|
| IBGE 2022 definitive sector mesh, Pernambuco | Census sector | Working | 19,578 PE sectors; GeoPackage |
| IBGE 2022 basic sector aggregates | Census sector | Working | Population and household indicators; Brazil CSV |
| IBGE 2022 responsible-person income aggregates | Census sector | Working | Mean/median nominal monthly income and denominator counts |
| IBGE 2022 urban surroundings, occupied households | Census sector | Working | Pavement, drainage, lighting, transit, sidewalk, ramp, and trees |
| SDS-PE MVI microdata, Jan 2004–Jul 2026 | Victim/date/municipality | Working | Exact date, age, sex, legal category; no submunicipal location |
| RAIS worker microdata, 2009–2017 POC | Job/municipality/CNAE/year | Working | Active jobs aggregated immediately; person rows are not retained |
| Novo CAGED movement microdata, 2024–2025 POC | Movement/municipality/CNAE/month | Working | Movement file only; exclusions/late declarations still need integration |
| INEP Higher Education Census, 2024 | Physical course offering | Working POC | In-person undergraduate offerings; headquarters totals rejected as local exposure |
| IBGE 2024 municipal mesh | Municipality | Working | Used to construct contiguity among target cities and neighbors |

The first filtered build contains the sectors in municipality codes `2602902` (Cabo),
`2607901` (Jaboatão), and `2611606` (Recife). The code asserts join coverage and reports
any geometry/data mismatch rather than silently dropping sectors.

Of 4,543 sectors, 4,476 have a nonmissing income aggregate, 4,416 have an observed
street-environment denominator, and 4,415 support the exploratory environment index. Coverage
is lowest in Cabo (96.8% income; 89.9% environment) and is recorded explicitly in the feature
store. Binary environment shares exclude “not declared” or “skipped” cases from their
denominators rather than counting them as absence.

## Validated as available, not yet integrated

| Source | Likely grain | Role | Main risk |
|---|---|---|---|
| OpenStreetMap | Network/point/polygon | Streets, centrality, POIs | Completeness varies by place/category |
| CNES | Facility | Health access | Active-date and duplicate-facility handling |
| INEP school census | School | Education access | Year alignment and geocoding quality |
| MapBiomas | Raster | Land use/cover | Resolution and zonal-statistics choices |
| Cabo transparency/public works | Project/address | Public investment | Unstructured or incomplete locations |

## Violence-data audit result

SDS-PE publishes an official 87,182-row MVI workbook (87,186 victims), covering 2004-01-01
through 2026-07-31. It contains `MUNICIPIO`, `REGIAO_GEOGRAFICA`, `SEXO`, legal category,
exact `DATA`, `ANO`, `IDADE`, and victim count. It does **not** contain neighborhood,
address, coordinates, AIS, or any other submunicipal field. Therefore it supports municipal
time-series and cross-city work but cannot label census sectors. Do not infer intraurban
labels from municipal totals.

For the three study cities, the workbook contains 3,478 victims in Cabo, 8,449 in Jaboatão,
and 15,745 in Recife over the available period. The 2026 data is partial through July and is
excluded from annual comparison plots.

Before supervised modeling, record:

- finest stable geography (coordinates, address, neighborhood, AIS, or municipality);
- event date resolution and years covered;
- whether counts refer to incidents or victims;
- retroactive revisions and category-definition changes;
- suppression/privacy rules;
- reporting and policing intensity biases.

## Reproducibility

`scripts/download_ibge.sh` contains exact source URLs and SHA-256 checksums for the snapshot
used on 2026-08-08. Raw files and generated artifacts are ignored by Git.
