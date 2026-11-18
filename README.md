# Predicting Family Food Security

A DATA 1030 project at Brown by Liza Whitmire, Prasanna Nagarajan, and Declan Treacy.

We're trying to predict how food secure a family is using the kind of information a health
survey already collects — who's in the household, their socioeconomic situation, where they
live, and their health. The motivation is pretty direct: in 2024 the USDA found that 13.7%
of US households (about 18.3 million) were food insecure at some point in the year, and food
insecurity is tied to a long list of worse physical and mental health outcomes. SES is the
obvious predictor, but plenty of other factors matter too, so we wanted to see what a model
can learn about who's most at risk.

## The problem

Our target is `FSSTATDET` — a family's food security status on the USDA 30-day food
security scale. The scale scores a household 0–10 based on how many food-hardship questions
they answer yes to, and that score gets binned into four ordered categories:

| Status | Scale score | People in our data |
|--------|-------------|--------------------|
| High food security | 0 | 34,447 |
| Marginal | 1–2 | 2,753 |
| Low | 3–5 | 2,165 |
| Very low | 6–10 | 1,565 |

(59 people have an unknown status.) So this is an **ordinal classification** problem, and a
heavily imbalanced one — the vast majority of families are fully food secure, which is
something we'll have to deal with when we model it.

## The data

Everything comes from the 2024 **IPUMS NHIS** — the CDC's National Health Interview Survey,
pulled through IPUMS (Health Surveys, Version 8.2). The full survey is 40,989 people (32,629
adults and 8,360 children) across 791 columns covering demographics, SES, health conditions,
insurance, behaviors, and more, with a mix of continuous, categorical, and ordinal variables.
We're not using all 791 — the plan is to drop columns that just restate another question,
don't apply to everyone, or are mostly missing.


## How the repo is laid out

```
├── data/        the IPUMS files (.dat.gz + .xml), the processed parquet, and variable lists
├── figures/     EDA figures (.png)
├── results/     predictions, saved models, anything the code outputs
├── report/      the midterm report PDF and, later, the final slides
├── src/         all the code — notebooks and .py files
├── .gitignore
├── LICENSE
├── environment.yml
├── requirements.txt
└── README.md
```

Inside `src/`:

- `extraction.ipynb` pulls the IPUMS extract and writes it to `data/nhis_data.parquet`.
- `eda_famkidno.ipynb`, `eda_gotstampfam.ipynb`, and `eda_urbrrl.ipynb` are the per-variable EDA.
- `visualization.ipynb` has some extra plots.
- `set_fig_theme.py` sets a shared matplotlib style so everyone's figures match.
- `api.py`, `main.py`, and `test.py` are small helpers around the IPUMS API client.

## Setup

We developed everything on Python 3.14.6. The main packages and the versions we used:

| Package | Version |
|---------|---------|
| pandas | 3.0.3 |
| matplotlib | 3.11.0 |
| numpy | 2.4.6 |
| pyarrow | 26.0.0 |
| ipumspy | 0.9.0 |
| python-dotenv | 1.2.3 |

Easiest way to match that is conda:

```bash
conda env create -f environment.yml
conda activate data1030
```

Or with pip:

```bash
pip install -r requirements.txt
```

## Running it

Run the notebooks from inside `src/` — the data paths (`../data/nhis_data.parquet`) are
relative to that folder, so launching from somewhere else will break them.

The processed dataset is already in `data/nhis_data.parquet`, so you can open any EDA
notebook and run it straight through; each one loads that file and saves its figures into
`figures/`. To rebuild the data from scratch instead, run `extraction.ipynb` — that's the
only step that talks to IPUMS and needs an API key.

### Getting an API key

`extraction.ipynb` and `api.py` read your IPUMS key from an environment variable, so it
never has to live in the code. Make a `.env` file in the project root with:

```
IPUMS_API_KEY=your_key_here
```

The `.env` file is gitignored on purpose — don't commit it. You can get a free key from your
IPUMS NHIS account.

## A note on the data

The NHIS files are small enough that we just keep them in `data/`. IPUMS has its own terms of
use, so if you build on this, please cite IPUMS NHIS (Blewett et al., 2026, DOI
10.18128/D070.V8.2).

## License

MIT — see [LICENSE](LICENSE).
