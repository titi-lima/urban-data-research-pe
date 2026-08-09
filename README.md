# Urban Data Research PE

An archived collection of reproducible urban-data proofs of concept for Cabo de Santo
Agostinho, Jaboatão dos Guararapes, Recife, and their metropolitan context.

## Archive status

The violence-centered research line was intentionally closed. Cabo is an extreme municipal
outlier, important mechanisms are not measured in the public datasets,
and the topic was not a good fit for the researcher's desired social contribution. The code
and negative findings remain public-facing material and may help a future researcher
avoid overstating what these sources can identify.

This is an archive, not an abandoned claim of causal results. See
[`docs/archive-findings.md`](docs/archive-findings.md) for the handoff and
[`docs/violence-research-questions.md`](docs/violence-research-questions.md) for the POCs.

## Repository map

- `src/urban_vulnerability/`: census, spatial, education, employment, and SDS processing.
- `scripts/`: source downloads and privacy-preserving RAIS/Novo CAGED aggregation.
- `tests/`: unit tests for joins, denominators, geography guardrails, and experiments.
- `docs/`: data audit, POC findings, question history, and archive handoff.
- `data/`: ignored raw/intermediate/processed data, with tracked placeholders only.
- `artifacts/`: ignored generated reports and figures, with a tracked placeholder only.

Raw administrative records and generated outputs are deliberately excluded from Git. The
repository publishes transformations and checks—not person-level records or local downloads.

The repository contains the following proofs of concept:

1. **Census feature store** — filters the definitive 2022 IBGE census-sector mesh and
   basic aggregates to the three study cities and creates one analysis-ready GeoParquet.
2. **Spatial neighborhood graph** — builds Queen-contiguity neighbors and adds lagged
   neighborhood features, testing the basic graph representation before OSM is added.
3. **Urban-form profiles** — runs an unsupervised PCA + clustering exploration over
   population density, household size, vacancy, occasional use, and occupancy. This is
   an exploratory morphology profile, **not** a crime or danger score.
4. **MVI outcome audit** — ingests the official SDS-PE victim-level workbook and produces
   a municipal time series while programmatically rejecting it as a census-sector label.
5. **Income + street-environment enrichment** — adds the definitive 2022 responsible-person
   income and urban-surroundings aggregates, with explicit denominators and coverage flags.
6. **Research-question experiments** — measures deprivation overlap, cross-city transfer,
   profile sensitivity, spatial autocorrelation, and municipal MVI divergence.
7. **Higher-education capacity audit** — separates physical in-person offerings from
   institution headquarters and distinguishes scarce tuition-free capacity from underused
   paid capacity.
8. **Employment panels** — aggregates RAIS by municipality/CNAE and Novo CAGED by
   municipality/month, with the former violence join retained as an archived experiment.

## Quick start

Requirements: Python 3.11+ and [`uv`](https://docs.astral.sh/uv/).

```bash
uv sync --extra dev
./scripts/download_ibge.sh
./scripts/download_sds.sh
uv run urban-research run-pocs
uv run urban-research run-research
uv run pytest
```

The combined command writes:

- `data/processed/census_sectors.parquet`
- `data/processed/spatial_features.parquet`
- `data/processed/enriched_features.parquet`
- `data/processed/urban_profiles.parquet`
- `data/processed/mvi_events.parquet`
- `data/processed/mvi_annual.parquet`
- `artifacts/urban_profiles.geojson`
- `artifacts/urban_profiles.png`
- `artifacts/mvi_annual_counts.png`
- `artifacts/poc_report.json`
- `artifacts/research_questions_report.json`
- `artifacts/rq_profile_composition.png`
- `artifacts/rq_domain_separability.png`
- `artifacts/rq_transfer_matrix.png`
- `artifacts/rq_mvi_rates.png`
- `artifacts/rq_income_environment_overlap.png`
- `artifacts/rq_environment_transfer.png`
- `artifacts/rq_profile_sensitivity.png`

Run `uv run urban-research --help` for individual stages.

## Research guardrails

- The current profiles are descriptive and unsupervised. They must not be described as
  predicting crime, dangerousness, or individual behavior.
- Crime data must be audited for geographic coverage, reporting bias, temporal alignment,
  and privacy before it becomes an outcome.
- Evaluation must use spatially blocked and cross-city splits; random row splits would
  leak nearby spatial context.
- Keep raw downloads out of Git. Source URLs and expected checksums live in the download
  script so the dataset remains reproducible.

The exploratory question slates are retained as methodological history.
