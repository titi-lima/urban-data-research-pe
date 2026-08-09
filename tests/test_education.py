import pandas as pd
import pytest

from urban_vulnerability.education import (
    capacity_summary,
    inclusion_funnel,
    price_segment_summary,
)


def _courses() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "CO_MUNICIPIO": ["1", "1"],
            "NO_MUNICIPIO": ["Example", "Example"],
            "CO_IES": ["10", "20"],
            "CO_CURSO": ["100", "200"],
            "IN_GRATUITO": ["1", "0"],
            "QT_VG_TOTAL": [10, 30],
            "QT_INSCRITO_TOTAL": [20, 15],
            "QT_ING": [8, 6],
            "QT_MAT": [25, 15],
            "QT_CONC": [5, 3],
            "QT_ING_PROCESCPUBLICA": [6, 3],
            "QT_MAT_PROCESCPUBLICA": [18, 6],
            "QT_CONC_PROCESCPUBLICA": [3, 1],
            "QT_ING_RESERVA_VAGA": [4, 0],
            "QT_MAT_RESERVA_VAGA": [10, 0],
            "QT_CONC_RESERVA_VAGA": [2, 0],
            "QT_ING_RVPPI": [2, 0],
            "QT_MAT_RVPPI": [5, 0],
            "QT_CONC_RVPPI": [1, 0],
            "QT_ING_APOIO_SOCIAL": [2, 0],
            "QT_MAT_APOIO_SOCIAL": [8, 0],
            "QT_CONC_APOIO_SOCIAL": [1, 0],
        }
    )


def test_capacity_summary_uses_explicit_youth_denominator() -> None:
    youth = pd.DataFrame({"CO_MUNICIPIO": ["1"], "population_20_24": [100]})
    result = capacity_summary(_courses(), youth).iloc[0]
    assert result["vacancies"] == 40
    assert result["applications_per_vacancy"] == pytest.approx(0.875)
    assert result["entrants_per_100_residents_20_24"] == pytest.approx(14)


def test_price_segments_reveal_aggregate_mismatch() -> None:
    result = price_segment_summary(_courses()).set_index("price_segment")
    assert result.loc["tuition_free", "applications_per_vacancy"] == 2
    assert result.loc["paid", "applications_per_vacancy"] == 0.5
    assert result.loc["tuition_free", "enrollment_share"] == pytest.approx(0.625)


def test_inclusion_funnel_is_stage_composition() -> None:
    result = inclusion_funnel(_courses()).set_index("stage")
    assert result.loc["entrant", "public_school_origin_share"] == pytest.approx(9 / 14)
    assert result.loc["graduate", "public_school_origin_share"] == pytest.approx(4 / 8)
    assert result.loc["enrolled", "social_support_share"] == pytest.approx(8 / 40)
