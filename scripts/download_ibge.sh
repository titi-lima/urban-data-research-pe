#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
target_dir="${repo_dir}/data/raw/ibge"
mkdir -p "${target_dir}"

download() {
  local url="$1"
  local output="$2"
  local expected="$3"

  if [[ ! -f "${output}" ]]; then
    curl -fL --retry 3 --max-time 300 -o "${output}" "${url}"
  fi

  local actual
  actual="$(shasum -a 256 "${output}" | awk '{print $1}')"
  if [[ "${actual}" != "${expected}" ]]; then
    echo "Checksum mismatch for ${output}" >&2
    echo "expected: ${expected}" >&2
    echo "actual:   ${actual}" >&2
    exit 1
  fi
}

download \
  "https://ftp.ibge.gov.br/Censos/Censo_Demografico_2022/Agregados_por_Setores_Censitarios/Agregados_por_Setor_csv/Agregados_por_setores_basico_BR_20260520.zip" \
  "${target_dir}/Agregados_por_setores_basico_BR_20260520.zip" \
  "ec04624286233d699ebe69c7b9625744a1cfdfc8352126f30245bdef5e9bdc63"

download \
  "https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_de_setores_censitarios__divisoes_intramunicipais/censo_2022/setores/gpkg/UF/PE/PE_setores_CD2022.gpkg" \
  "${target_dir}/PE_setores_CD2022.gpkg" \
  "d26cb665fe4546104500e2295af95785cbbf92b8b8f201fceac73fb37d23edc8"

download \
  "https://ftp.ibge.gov.br/Censos/Censo_Demografico_2022/Agregados_por_Setores_Censitarios/dicionario_de_dados_agregados_por_setores_censitarios_20260520.xlsx" \
  "${target_dir}/dicionario_de_dados_agregados_por_setores_censitarios_20260520.xlsx" \
  "0b8aedece57f6125d785b6aa2234cfd587e92dfb6ce5ca6ace8c67f140831344"

download \
  "https://ftp.ibge.gov.br/Censos/Censo_Demografico_2022/Agregados_por_Setores_Censitarios_Rendimento_do_Responsavel/Agregados_por_setores_renda_responsavel_BR_20260508_csv.zip" \
  "${target_dir}/Agregados_por_setores_renda_responsavel_BR_20260508_csv.zip" \
  "141c83e7635674e7e2c941e55f98811e538fcbf2e1e1125b0aa7892c260f4a23"

download \
  "https://ftp.ibge.gov.br/Censos/Censo_Demografico_2022/Agregados_por_Setores_Censitarios_Rendimento_do_Responsavel/dicionario_de_dados_renda_responsavel_20260508.xlsx" \
  "${target_dir}/dicionario_de_dados_renda_responsavel_20260508.xlsx" \
  "fea6e2b2439eeb167c6fa9c136ed7cb13ebcb06f4c875d634e3e2578c668a48d"

download \
  "https://ftp.ibge.gov.br/Censos/Censo_Demografico_2022/Agregados_por_Setores_Censitarios_Caracteristicas_urbanisticas_do_entorno_dos_domicilios/Agregados_por_Setor_csv/Agregados_por_setores_entorno_domic%C3%ADlios_BR.zip" \
  "${target_dir}/Agregados_por_setores_entorno_domicilios_BR.zip" \
  "945ad03f2cca535c51b8956188ed9a7e3e017caa5ae2a79449e2202d359ffa60"

download \
  "https://ftp.ibge.gov.br/Censos/Censo_Demografico_2022/Agregados_por_Setores_Censitarios_Caracteristicas_urbanisticas_do_entorno_dos_domicilios/dicionarios_de_dados_entorno.zip" \
  "${target_dir}/dicionarios_de_dados_entorno.zip" \
  "eda4e2c9968e753fa2c158380ae537c284ccbddde5b74a6d5fec0b3c2250d1b4"

download \
  "https://apisidra.ibge.gov.br/values/t/6579/n6/2602902,2607901,2611606/v/9324/p/all?formato=json" \
  "${target_dir}/population_estimates_sidra.json" \
  "274437981a8fb63abf8fc52162741d43700faac0a33cf195f6282bb5337ec279"

download \
  "https://apisidra.ibge.gov.br/values/t/202/n6/2602902,2607901,2611606/v/93/p/2010?formato=json" \
  "${target_dir}/population_2010_sidra.json" \
  "1f56cd1b4759a242364b6ed641ee197a26d6afe51a145e1aec18d3e62939c445"

echo "IBGE inputs are present and checksums match."
