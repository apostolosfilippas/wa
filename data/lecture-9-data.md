# Lecture 9 visualization data

Both files are local inputs for `scripts/09.2 plotting-with-seaborn.ipynb`. The notebook does not download data or scrape a live table when students run it.

## Mental health in tech survey (2014)

- File: `mental_survey.csv`.
- Source: [the original course CSV on Google Drive](https://drive.google.com/file/d/1JFvtWmu9qV68dZpJEPEethYiNGh_U-uE/view).
- Survey context: [OSMI research](https://osmihelp.org/research).
- Retrieved: October 22, 2026.
- This is the original course file, byte-for-byte unchanged: 1,259 rows and 27 columns.
- SHA-256: `3c4e3e16917f74b5e219ba01caecd09f9dc464c4848becdd018c9442d627abb4`.
- It is a historical, self-selected survey, not a representative estimate of mental-health prevalence or current workplace conditions.
- The notebook keeps an unchanged dataframe, then explicitly filters its working copy to ages 18 through 100. This removes 8 rows, leaving 1,251. It retains raw gender answers and the original treatment answers. `treatment_yes` means reported treatment-seeking, not the presence or absence of a mental-health condition.

## Daily Treasury par yield curve rates (October 2022)

- File: `treasury_yields_2022_10.csv`.
- Source: [US Treasury historical table](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202210).
- Original download: [Treasury CSV](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/all/202210?field_tdr_date_value_month=202210&type=daily_treasury_yield_curve&page&_format=csv).
- Retrieved: October 22, 2026.
- This is a teaching extract of the Date, 1 Mo, 2 Mo, 3 Mo, and 6 Mo columns, sorted by date. Dates are formatted YYYY-MM-DD; numeric yields are unchanged.
- It contains 20 reported business dates, October 3 through October 31, 2022, with no missing values in these five columns. All 80 yield values were checked against the HTML table.
- Yields are annualized percentages: 3.26 means 3.26%, not 326%.
- The period is intentionally fixed so the time-series and correlation examples are reproducible. It is not current market data. Correlations within one month are descriptive; they are not causal estimates or evidence from independent daily observations.
