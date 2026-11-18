# Happy Masks: a fictional web analytics case

Original teaching data for WA Lectures 11 and 12. Happy Masks is a fictional online store that sells masks. All numbers, messages, reviews, and business notes were created for this class. They are not observations about a real business or real customers.

## Files

- `daily_metrics.csv`: 448 rows. Each row is one date × channel × device combination. Two equal windows: September 1–28 and October 1–28, 2026. All days and segments are present.
- `documents.jsonl`: 16 fictional source documents, with stable IDs, dates, types, and source references. These are a small, deliberately selected case packet, not a representative sample of customers.
- `retrieval_checks.json`: six hand-written questions and relevant document IDs. A small classroom check, not a benchmark proving general retrieval quality.
- `generate_metrics.py`: regenerates the exact CSV with Python's standard library and seed 2026. Run `uv run python data/web-analyst/generate_metrics.py` from the `wa` folder.

## Metrics

| Field | Meaning |
| --- | --- |
| date | Calendar date in the fictional store's reporting timezone |
| channel | organic, paid, email, or direct; each session belongs to one channel |
| device | desktop or mobile; each session belongs to one device category |
| sessions | Visits, not unique people |
| orders | Completed purchases; this case assumes at most one purchase per session |
| revenue | USD gross merchandise revenue before refunds, excluding shipping and sales tax |

Conversion rate = total orders / total sessions. Revenue per session = total revenue / total sessions. Average order value = total revenue / total orders. Sum counts first, then calculate rates; do not average row-level rates. A zero denominator is undefined, not zero.

The generator lowers mobile purchase rates in October and expands paid traffic. The documents offer plausible mechanisms and competing hypotheses. Neither the aggregated CSV nor the message packet identifies a causal effect. There are no browser-level observations, customer joins, ad-spend amounts, or profit data.

The notebooks load these files locally from your course repository. Only aggregate tool results and the relevant fictional text excerpts are sent to the LLM API. No live store account is required.
