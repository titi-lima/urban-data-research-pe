from pathlib import Path

import pandas as pd

from urban_vulnerability.sds import (
    build_mvi_annual,
    build_mvi_monthly,
    geography_audit,
    read_mvi_events,
)


def test_mvi_filter_and_geography_guardrail(tmp_path: Path) -> None:
    path = tmp_path / "mvi.xlsx"
    source = pd.DataFrame(
        {
            "MUNICIPIO": ["CABO DE SANTO AGOSTINHO", "RECIFE", "OLINDA"],
            "REGIAO_GEOGRAFICA": ["RMR", "CAPITAL", "RMR"],
            "SEXO": ["MASC", "FEM", "MASC"],
            "NATUREZA JURIDICA": ["HOMICIDIO"] * 3,
            "DATA": pd.to_datetime(["2024-01-01", "2024-02-01", "2024-03-01"]),
            "ANO": [2024, 2024, 2024],
            "IDADE": [20, 30, 40],
            "TOTAL DE VITIMAS": [1, 2, 1],
        }
    )
    with pd.ExcelWriter(path) as writer:
        source.to_excel(writer, sheet_name="Plan1", index=False)

    events = read_mvi_events(path)
    annual = build_mvi_annual(events)
    audit = geography_audit(events)

    assert len(events) == 2
    assert int(annual["victims"].sum()) == 3
    assert audit["finest_geography"] == "municipality"
    assert audit["sector_compatible"] is False


def test_build_mvi_monthly_uses_calendar_months() -> None:
    events = pd.DataFrame(
        {
            "CD_MUN": ["1", "1"],
            "municipality": ["Example", "Example"],
            "date": pd.to_datetime(["2025-01-01", "2025-01-31"]),
            "victims": [1, 2],
        }
    )
    monthly = build_mvi_monthly(events)
    assert monthly.iloc[0]["month"] == "2025-01"
    assert monthly.iloc[0]["victims"] == 3
