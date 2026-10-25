# DATA 1030 Project — Predicting Family Food Security

A project for DATA 1030 at Brown University. We use the **2024 IPUMS NHIS** (National
Health Interview Survey) to predict a family's **food security status** from
demographic, household, and socioeconomic characteristics.

- **Dataset:** IPUMS NHIS, 2024 sample — 40,989 individual responses (32,629 adults and
  8,360 children).
- **Prediction target:** `FSSTATDET` — detailed family-level food security status on the
  USDA 30-day scale (high / marginal / low / very low food security).
- **Example predictors explored so far:** `FAMKIDNO` (number of family members under 18),
  `GOTSTAMPFAM` (family received food stamps/SNAP), and `URBRRL` (urban–rural county
  classification).

## Repository structure

```
├── data/        # raw + preprocessed data (IPUMS .dat.gz, DDI .xml, nhis_data.parquet, variable lists)
├── figures/     # generated EDA figures (.png)
├── results/     # predictions, saved models, and other outputs
├── report/      # PDF midterm report and final presentation slides
├── src/         # all source code (Jupyter notebooks + Python files)
├── .gitignore
├── LICENSE
├── environment.yml
├── requirements.txt
└── README.md
```

### What's in `src/`
- `extraction.ipynb` — downloads the IPUMS extract and saves it to `data/nhis_data.parquet`.
- `eda_famkidno.ipynb`, `eda_gotstampfam.ipynb`, `eda_urbrrl.ipynb` — exploratory analysis of individual variables.
- `visualization.ipynb` — additional visualizations.
- `set_fig_theme.py` — shared matplotlib theme so all figures look consistent.
- `api.py`, `main.py`, `test.py` — helper/scaffolding code for the IPUMS API client.

## Environment and versions

Developed with **Python 3.14.6**. Key package versions:

| Package | Version |
|---------|---------|
| pandas | 3.0.3 |
| matplotlib | 3.11.0 |
| numpy | 2.4.6 |
| pyarrow | 26.0.0 |
| ipumspy | 0.9.0 |
| python-dotenv | 1.2.3 |

### Setup (conda, recommended)

```bash
conda env create -f environment.yml
conda activate data1030
```

### Setup (pip)

```bash
pip install -r requirements.txt
```

## Reproducing the work

The notebooks are meant to be run **from inside the `src/` folder** (paths like
`../data/nhis_data.parquet` are relative to it).

1. **Get the data.** The processed dataset is already included at `data/nhis_data.parquet`,
   so you can skip straight to the EDA. To regenerate it from scratch, run
   `src/extraction.ipynb` — this requires a free IPUMS API key (see below).
2. **Run the EDA notebooks** (`eda_famkidno.ipynb`, `eda_gotstampfam.ipynb`,
   `eda_urbrrl.ipynb`). They each load `../data/nhis_data.parquet` and produce the figures
   saved in `figures/`.

### IPUMS API key

`extraction.ipynb` and `api.py` read your IPUMS API key from an environment variable.
Create a file named `.env` in the project root (it is gitignored and must never be
committed) containing:

```
IPUMS_API_KEY=your_key_here
```

You can request a free key from your IPUMS NHIS account.

## Data access

The IPUMS NHIS files in `data/` are small enough to live in the repo. Use of IPUMS data is
subject to IPUMS's terms; please cite IPUMS NHIS appropriately if you reuse this work.

## License

Released under the MIT License — see [LICENSE](LICENSE).
