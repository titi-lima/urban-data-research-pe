from pathlib import Path
from zipfile import ZipFile

from urban_vulnerability.ibge import read_basic_aggregates


def test_filters_and_parses_decimal_comma(tmp_path: Path) -> None:
    header = ";".join(
        [
            "CD_SETOR",
            "SITUACAO",
            "CD_SIT",
            "CD_TIPO",
            "AREA_KM2",
            "CD_REGIAO",
            "NM_REGIAO",
            "CD_UF",
            "NM_UF",
            "CD_MUN",
            "NM_MUN",
            "CD_DIST",
            "NM_DIST",
            "CD_SUBDIST",
            "NM_SUBDIST",
            "CD_BAIRRO",
            "NM_BAIRRO",
            "CD_NU",
            "NM_NU",
            "CD_FCU",
            "NM_FCU",
            "CD_AGLOM",
            "NM_AGLOM",
            "CD_RGINT",
            "NM_RGINT",
            "CD_RGI",
            "NM_RGI",
            "CD_CONCURB",
            "NM_CONCURB",
            "v0001",
            "v0002",
            "v0003",
            "v0004",
            "v0005",
            "v0006",
            "v0007",
            "v0008",
            "v0009",
        ]
    )
    values = [
        "260290205000001",
        "Urbana",
        "1",
        "0",
        "0,5",
        "2",
        "Nordeste",
        "26",
        "Pernambuco",
        "2602902",
        "Cabo de Santo Agostinho",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "100",
        "40",
        "40",
        "0",
        "2,5",
        "0",
        "38",
        "1",
        "1",
    ]
    archive_path = tmp_path / "sample.zip"
    with ZipFile(archive_path, "w") as archive:
        archive.writestr("sample.csv", header + "\n" + ";".join(values) + "\n")

    result = read_basic_aggregates(archive_path, {"2602902"}, chunksize=1)

    assert len(result) == 1
    assert result.loc[0, "area_km2"] == 0.5
    assert result.loc[0, "mean_household_size"] == 2.5
    assert result.loc[0, "population"] == 100
