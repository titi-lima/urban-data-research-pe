import geopandas as gpd
import pytest
from shapely.geometry import box

from urban_vulnerability.enriched_experiments import deprivation_overlap


def test_deprivation_overlap_detects_concentration() -> None:
    sectors = gpd.GeoDataFrame(
        {
            "NM_MUN": ["City"] * 10,
            "responsible_person_income_mean_brl": list(range(1, 11)),
            "environment_deficit_index": [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1],
            "geometry": [box(i, 0, i + 1, 1) for i in range(10)],
        },
        crs=4326,
    )

    result = deprivation_overlap(sectors)

    assert result["joint_share"].item() == 0.2
    assert result["overlap_lift_vs_independence"].item() == pytest.approx(5.0)
    assert result["spearman_income_vs_environment_deficit"].item() == pytest.approx(-1.0)
