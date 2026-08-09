from io import StringIO

from urban_vulnerability.employment import (
    aggregate_rais_worker_stream,
    build_sector_composition,
    cnae_section,
)


def test_cnae_divisions_map_to_official_sections() -> None:
    assert cnae_section("10716") == "C"
    assert cnae_section("47113") == "G"
    assert cnae_section("85414") == "P"
    assert cnae_section("invalid") == "unknown"


def test_rais_stream_keeps_active_target_city_jobs_only() -> None:
    text = StringIO(
        "Vínculo Ativo 31/12;CNAE 2.0 Classe;Mun Trab\n"
        "1;10716;260290\n"
        "0;10716;260290\n"
        "1;47113;260290\n"
        "1;47113;999999\n"
    )
    counts = aggregate_rais_worker_stream(text, 2014, ["2602902"])
    wide = build_sector_composition(counts).iloc[0]
    assert wide["formal_jobs_total"] == 2
    assert wide["jobs_C"] == 1
    assert wide["jobs_G"] == 1
    assert wide["share_C"] == 0.5
