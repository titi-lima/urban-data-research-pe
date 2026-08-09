# Data layout

- `raw/`: immutable source downloads. Never edit these files.
- `interim/`: extracted or filtered intermediate tables.
- `processed/`: analysis-ready feature stores.

Only this documentation and `.gitkeep` placeholders belong in Git. Use
`../scripts/download_ibge.sh` to reproduce the initial raw inputs.

