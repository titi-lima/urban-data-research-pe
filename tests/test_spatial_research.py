import geopandas as gpd
import pandas as pd
from shapely.geometry import box

from urban_vulnerability.enriched_experiments import joint_disadvantage_clusters


def test_joint_disadvantage_cluster_permutation_summary() -> None:
    sectors = gpd.GeoDataFrame(
        {
            "CD_SETOR": [str(i) for i in range(10)],
            "CD_MUN": ["1"] * 10,
            "NM_MUN": ["City"] * 10,
            "responsible_person_income_mean_brl": list(range(1, 11)),
            "environment_deficit_index": list(reversed([i / 10 for i in range(10)])),
            "geometry": [box(i, 0, i + 1, 1) for i in range(10)],
        },
        crs=4326,
    )
    edges = pd.DataFrame(
        {
            "source": [str(i) for i in range(9)],
            "target": [str(i) for i in range(1, 10)],
            "CD_MUN": ["1"] * 9,
        }
    )

    flags, summary = joint_disadvantage_clusters(
        sectors, edges, top_share=0.3, permutations=19, random_state=2
    )

    assert flags["top_joint_disadvantage"].sum() == 3
    assert summary["observed_top_top_edges"].item() == 2
    assert summary["largest_top_component"].item() == 3
