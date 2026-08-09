#!/usr/bin/env python3
from __future__ import annotations

import io
import json
import subprocess

import pandas as pd

from urban_vulnerability.config import ProjectPaths
from urban_vulnerability.employment import aggregate_rais_worker_stream, build_sector_composition


def main() -> None:
    paths = ProjectPaths.discover()
    records = json.loads((paths.raw_ibge / "pe_population_2022_sidra.json").read_text())
    municipality_codes = pd.DataFrame(records[1:])["D1C"].dropna().astype(str).tolist()
    archives = sorted((paths.root / "data" / "raw" / "rais").glob("**/PE*.7z"))
    if not archives:
        raise FileNotFoundError("No RAIS PE*.7z archives found under data/raw/rais")

    yearly: list[pd.DataFrame] = []
    for archive in archives:
        year = int(archive.stem[-4:])
        process = subprocess.Popen(["bsdtar", "-xOf", archive], stdout=subprocess.PIPE)
        assert process.stdout is not None
        text = io.TextIOWrapper(process.stdout, encoding="latin-1", errors="replace", newline="")
        yearly.append(aggregate_rais_worker_stream(text, year, municipality_codes))
        text.close()
        if process.wait() != 0:
            raise RuntimeError(f"Could not extract {archive}")

    counts = pd.concat(yearly, ignore_index=True)
    composition = build_sector_composition(counts)
    counts.to_parquet(paths.processed / "rais_city_section.parquet", index=False)
    composition.to_parquet(paths.processed / "rais_sector_composition.parquet", index=False)
    print(f"Aggregated {len(archives)} RAIS archives into {len(composition):,} city-years.")


if __name__ == "__main__":
    main()
