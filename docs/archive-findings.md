# Archive handoff

Snapshot: 2026-08-08.

## Why this research line closed

The violence-centered line was stopped for two substantive reasons, not because the code
failed:

1. Cabo is a very large MVI outlier, while a central suspected mechanism—gang conflict—is not
   observed in the public data. Adding more census covariates cannot repair a missing causal
   mechanism.
2. The subject is emotionally costly and does not match the researcher's wish to associate
   the work with constructive, visibly beneficial interventions.

This is a useful project-selection result. A technically feasible question can still be a poor
research fit when the outcome is not measurable enough, the intervention is unclear, or the
work is not emotionally sustainable.

## Findings worth preserving

- The SDS-PE workbook provides excellent dates and municipal coverage but no neighborhood,
  coordinates, address, or AIS. It cannot be used to label census sectors.
- Cabo's MVI path is not reproduced well by combinations of other large Pernambuco cities.
  That makes a simple synthetic-control claim weak before any post-treatment result is read.
- Raw employment–MVI associations shrink sharply after common year shocks are removed. In the
  2009–2017 three-city panel, the one-year-lag Spearman correlation changes from -0.595
  (p=0.004) to -0.275 (p=0.227) after year demeaning.
- Sector composition did not improve out-of-year MVI prediction in the small annual panel.
  The best total-employment ridge specification reached MAE 5.56 per 100,000; the best
  sector-composition specification reached 8.64. This is a negative small-sample POC, not a
  universal conclusion.
- A uniform metropolitan spillover story was not supported. Among the target cities and their
  immediate neighbors, 2021–2025 MVI rates had Moran's I 0.118 (p=0.184).
- INEP headquarters data is not a valid local university exposure: multi-campus staff can be
  assigned to the headquarters municipality. Physical in-person course offerings are the
  safer unit.
- Cabo's 2024 higher-education market is segmented. Tuition-free offerings had 2.23
  applications per seat, while paid offerings had 0.26. The actionable question is not simply
  “more seats,” but which public programs, financial support, course mix, and transport access
  are binding constraints.
- The 2014 UACSA/UFRPE and IFPE expansion did not produce a visible aggregate employment jump
  through 2017. It coincided with a much larger industrial/construction downturn, so a citywide
  before/after design cannot isolate the campus effect.
- The census-sector work remains a useful demonstration of denominator discipline, spatially
  blocked evaluation, domain shift, data audits, and the difference between stable clustering
  and a valid social construct.

## What a future user can reuse

- reproducible IBGE sector feature stores and municipal adjacency;
- SDS geography and temporal-coverage audits;
- RAIS/CNAE and Novo CAGED aggregation without retaining person-level records;
- INEP filtering for physical, in-person undergraduate offerings;
- tests that prevent municipal outcomes from being silently copied onto sectors;
- examples of negative results and failed identification checks that belong in honest research.
