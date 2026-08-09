import geopandas as gpd
from shapely.geometry import Point

from urban_vulnerability.profiles import PROFILE_FEATURES, build_urban_profiles


def test_profiles_exclude_sectors_without_aggregates() -> None:
    rows = 9
    data = {
        "CD_SETOR": [str(i) for i in range(rows)],
        "NM_MUN": ["Test city"] * rows,
        "has_census_aggregate": [True] * 8 + [False],
        "geometry": [Point(i, 0) for i in range(rows)],
    }
    for offset, feature in enumerate(PROFILE_FEATURES):
        data[feature] = [float(i + offset) for i in range(rows)]
    sectors = gpd.GeoDataFrame(data, crs=4326)

    profiles, report = build_urban_profiles(sectors, n_clusters=2)

    assert len(profiles) == 8
    assert report["rows"] == 8
    assert set(profiles["profile_cluster"]) == {0, 1}
