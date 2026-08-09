import json
from pathlib import Path

import geopandas as gpd
import pandas as pd
from shapely.geometry import box

from urban_vulnerability.experiments import (
    build_mvi_rates,
    build_population_denominators,
    morans_i_by_city,
)


def test_morans_i_detects_positive_neighbor_similarity() -> None:
    sectors = gpd.GeoDataFrame(
        {
            "CD_SETOR": ["a", "b", "c", "d"],
            "CD_MUN": ["1"] * 4,
            "NM_MUN": ["City"] * 4,
            "population_density_km2": [1.0, 2.0, 10.0, 11.0],
            "vacancy_share": [0.1, 0.2, 0.8, 0.9],
            "geometry": [box(i, 0, i + 1, 1) for i in range(4)],
        },
        crs=4326,
    )
    edges = pd.DataFrame({"source": ["a", "c"], "target": ["b", "d"], "CD_MUN": ["1", "1"]})

    result = morans_i_by_city(sectors, edges, permutations=19)

    assert (result["morans_i"] > 0).all()
    assert set(result["variable"]) == {"population_density_km2", "vacancy_share"}


def test_population_denominators_and_rates(tmp_path: Path) -> None:
    header = {"D1C": "Municipality", "D1N": "Name", "D3C": "Year", "V": "Value"}
    estimates = [
        header,
        {"D1C": "1", "D1N": "City", "D3C": "2021", "V": "1000"},
        {"D1C": "1", "D1N": "City", "D3C": "2023", "V": "1200"},
    ]
    census_2010 = [
        header,
        {"D1C": "1", "D1N": "City", "D3C": "2010", "V": "800"},
    ]
    estimate_path = tmp_path / "estimates.json"
    census_path = tmp_path / "census.json"
    estimate_path.write_text(json.dumps(estimates), encoding="utf-8")
    census_path.write_text(json.dumps(census_2010), encoding="utf-8")
    sectors = gpd.GeoDataFrame(
        {
            "CD_MUN": ["1", "1"],
            "NM_MUN": ["City", "City"],
            "population": [500, 600],
            "geometry": [box(0, 0, 1, 1), box(1, 0, 2, 1)],
        },
        crs=4326,
    )

    population = build_population_denominators(
        estimate_path, census_path, sectors, start_year=2021, end_year=2023
    )
    annual = pd.DataFrame(
        {
            "CD_MUN": ["1"] * 3,
            "municipality": ["City"] * 3,
            "year": [2021, 2022, 2023],
            "victims": [10, 11, 12],
            "is_complete_year": [True] * 3,
        }
    )
    rates = build_mvi_rates(annual, population)

    assert population.loc[population["year"] == 2022, "population"].item() == 1100
    assert rates.loc[rates["year"] == 2022, "mvi_rate_100k"].item() == 1000
