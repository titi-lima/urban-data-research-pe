import geopandas as gpd
from shapely.geometry import box

from urban_vulnerability.spatial import add_spatial_features, sector_adjacency


def test_adjacency_and_neighbor_lag() -> None:
    sectors = gpd.GeoDataFrame(
        {
            "CD_SETOR": ["a", "b", "c"],
            "CD_MUN": ["1", "1", "2"],
            "has_census_aggregate": [True, True, True],
            "population_density_km2": [100.0, 300.0, 900.0],
            "mean_household_size": [2.0, 4.0, 6.0],
            "geometry": [box(0, 0, 1, 1), box(1, 0, 2, 1), box(2, 0, 3, 1)],
        },
        crs=4326,
    )

    edges = sector_adjacency(sectors)
    result = add_spatial_features(sectors, edges).set_index("CD_SETOR")

    assert edges[["source", "target"]].to_records(index=False).tolist() == [("a", "b")]
    assert result.loc["a", "neighbor_count"] == 1
    assert result.loc["a", "neighbor_population_density_mean"] == 300.0
    assert result.loc["c", "neighbor_count"] == 0
