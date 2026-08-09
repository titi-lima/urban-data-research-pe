from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

import geopandas as gpd
import pandas as pd
from shapely.geometry import box

from urban_vulnerability.enrichment import (
    enrich_sector_features,
    read_environment_aggregates,
    read_income_aggregates,
)


def _write_zipped_csv(path: Path, name: str, frame: pd.DataFrame) -> None:
    with ZipFile(path, "w", ZIP_DEFLATED) as archive:
        archive.writestr(name, frame.to_csv(index=False, sep=";"))


def test_read_enrichment_and_compute_explicit_deficit_shares(tmp_path: Path) -> None:
    income_path = tmp_path / "income.zip"
    environment_path = tmp_path / "environment.zip"
    sector = "260290205000001"
    _write_zipped_csv(
        income_path,
        "income.csv",
        pd.DataFrame(
            {
                "CD_SETOR": [sector],
                "V06001": [100],
                "V06002": [300],
                "V06004": [1800.0],
                "V06006": [1500.0],
            }
        ),
    )
    environment = {column: [0] for column in [
        "V05000", "V05006", "V05007", "V05009", "V05010", "V05012", "V05013",
        "V05015", "V05016", "V05021", "V05022", "V05024", "V05025", "V05027",
        "V05028", "V05030", "V05031", "V05032", "V05033",
    ]}
    environment.update(
        {
            "CD_setor": [sector],
            "V05000": [100],
            "V05006": [75],
            "V05007": [25],
            "V05009": [50],
            "V05010": [50],
            "V05012": [90],
            "V05013": [10],
            "V05015": [20],
            "V05016": [80],
            "V05021": [60],
            "V05022": [40],
            "V05024": [15],
            "V05025": [45],
            "V05027": [6],
            "V05028": [54],
            "V05030": [30],
            "V05031": [30],
            "V05032": [20],
            "V05033": [20],
        }
    )
    _write_zipped_csv(environment_path, "environment.csv", pd.DataFrame(environment))

    income = read_income_aggregates(income_path, {"2602902"})
    surroundings = read_environment_aggregates(environment_path, {"2602902"})
    sectors = gpd.GeoDataFrame(
        {"CD_SETOR": [sector], "geometry": [box(0, 0, 1, 1)]}, crs=4326
    )
    enriched = enrich_sector_features(sectors, income_path, environment_path)

    assert income["responsible_person_income_median_brl"].item() == 1500
    assert surroundings["unpaved_share"].item() == 0.25
    assert surroundings["no_wheelchair_ramp_share"].item() == 0.9
    assert surroundings["no_trees_share"].item() == 0.3
    assert enriched["has_income_aggregate"].item()
    assert enriched["has_environment_aggregate"].item()
