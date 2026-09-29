# NOAA news listing snapshots

These are five distinct news-listing pages captured through a normal browser on September 28, 2026:

- `page-0.html`: https://www.noaa.gov/news
- `page-1.html`: https://www.noaa.gov/news?page=1
- `page-2.html`: https://www.noaa.gov/news?page=2
- `page-3.html`: https://www.noaa.gov/news?page=3
- `page-4.html`: https://www.noaa.gov/news?page=4

Each snapshot contains the rendered page's main news listing (10 articles and its pagination). Blank formatting lines and any script/style elements were removed; this is not a complete styled copy of the website. The source URL and capture date are also recorded in each HTML file.

The NOAA notebook normally requests the live website. If the live site returns a blocked or empty response, students can explicitly set `use_saved_pages = True` in its setup cell and run the notebook again. In that mode, it reads these dated HTML files and prints that it is using saved pages. It does not claim that the articles are current or that a live request succeeded.

All parsing, looping, category/date extraction, and file-writing examples remain the same in either mode.
