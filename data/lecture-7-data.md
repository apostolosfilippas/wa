# Lecture 7 data

## Auto MPG

`auto-mpg.data-original` is the original, unmodified whitespace-delimited Auto MPG file from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/9/auto+mpg).

- Source file: [auto-mpg.data-original](https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data-original)
- Citation: Quinlan, R. (1993). Auto MPG [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5859H
- License: [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/)
- Retrieved: October 13, 2026.
- This original file has 406 rows, including missing values. The commonly used 398-row version excludes eight rows whose MPG is unknown; we retain the original file used in the lesson.
- The notebook supplies the column names and reads spaces as separators. The column labeled `model_year` is a model year, not a model identifier.

Both Lecture 7 notebooks use this local copy, so the pandas and linear-model lessons run without a live download.

## Fictional employee reviews

`employee_reviews.csv` is a purpose-built **synthetic teaching sample** for `scripts/07.1 pandas.ipynb`. It was created for this course update, not scraped or collected from employees. It describes no real company or people; it must not be presented as actual Amazon reviews or used to make real workplace claims.

- Grain: one fictional review per row.
- 60 rows and 14 columns; no repeated complete rows.
- 12 job roles, four job types, and nine departments.
- Dates span January through June 2025. Monthly counts are 8, 12, 6, 14, 9, and 11 so ordering and counting have visible results.
- Ratings are whole numbers from 1 to 5.
- `Role` contains a job title, not a person's name.
- Three reviews omit `Place` to practice missing-value checks. All other fields are populated.
- Text and ratings are invented examples. Repeated phrases are intentional; they are not evidence of copied real reviews.

This replaces the [previous Amazon employee-review exercise file](https://drive.google.com/file/d/10hKwrxftkO8g73HrQiXHcDbA9B9skTbO/view?usp=sharing). The file reviewed on October 13, 2026 contained 9,990 rows but only 10 distinct complete rows, each repeated 999 times; all job types were Full Time and all dates were in August 2023. The original file is not modified or redistributed here.

The notebook saves its CSV round-trip example to `temp/mpg_df.csv`, not to the input data files.
