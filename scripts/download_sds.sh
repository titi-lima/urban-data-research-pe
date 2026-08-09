#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
target_dir="${repo_dir}/data/raw/sds"
output="${target_dir}/MICRODADOS_DE_MVI_JAN_2004_A_JULHO_2026.xlsx"
url="https://www.sds.pe.gov.br/images/indicadores/CVLI/MICRODADOS_DE_MVI_JAN_2004_A_JULHO_2026.xlsx"
expected="8af8eb510db456f43a46bd9c6e6363af244f1cb8ad408efa79720aec348fb276"

mkdir -p "${target_dir}"
if [[ ! -f "${output}" ]]; then
  curl -fL --retry 3 --max-time 300 -o "${output}" "${url}"
fi

actual="$(shasum -a 256 "${output}" | awk '{print $1}')"
if [[ "${actual}" != "${expected}" ]]; then
  echo "Checksum mismatch for ${output}" >&2
  echo "The SDS workbook may have been updated; audit its schema before changing the snapshot." >&2
  echo "expected: ${expected}" >&2
  echo "actual:   ${actual}" >&2
  exit 1
fi

echo "SDS-PE MVI input is present and its checksum matches."

