#!/usr/bin/env python3
from __future__ import annotations

import csv
import subprocess
from collections import defaultdict

import pandas as pd

from urban_vulnerability.config import MUNICIPALITIES, ProjectPaths


def main() -> None:
    paths = ProjectPaths.discover()
    wanted = {code[:6] for code in MUNICIPALITIES}
    archives = sorted((paths.root / "data" / "raw" / "caged").glob("**/CAGEDMOV*.7z"))
    if not archives:
        raise FileNotFoundError("No CAGEDMOV*.7z archives found under data/raw/caged")

    counts: defaultdict[tuple[str, str, str], dict[str, int]] = defaultdict(
        lambda: {"admissions": 0, "separations": 0, "balance": 0}
    )
    for archive in archives:
        process = subprocess.Popen(
            ["bsdtar", "-xOf", archive],
            stdout=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        assert process.stdout is not None
        for row in csv.DictReader(process.stdout, delimiter=";"):
            municipality = row["município"]
            if municipality not in wanted:
                continue
            key = (row["competênciamov"], municipality, row["seção"])
            movement = int(row["saldomovimentação"])
            counts[key]["admissions"] += movement == 1
            counts[key]["separations"] += movement == -1
            counts[key]["balance"] += movement
        process.stdout.close()
        if process.wait() != 0:
            raise RuntimeError(f"Could not extract {archive}")

    result = pd.DataFrame(
        [
            {
                "month": month,
                "municipality_6digit": municipality,
                "cnae_section": section,
                **values,
            }
            for (month, municipality, section), values in counts.items()
        ]
    ).sort_values(["month", "municipality_6digit", "cnae_section"])
    result.to_parquet(paths.processed / "novo_caged_city_section.parquet", index=False)
    print(f"Aggregated {len(archives)} Novo CAGED archives into {len(result):,} rows.")


if __name__ == "__main__":
    main()
