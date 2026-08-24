# Ranked paper digest

The scheduled workflow writes two views:

- `README.md`: the complete high-recall paper feed
- `docs/digests/index.md`: dated daily shortlists with 10 papers each

## Default mode

No additional setup is required. `rank_papers.py` fetches abstracts for recent
papers, checks author affiliations for a bounded major-company bonus, applies
deterministic research-track scoring, and creates the digest. A company name
never bypasses the content relevance score.

## Cursor full-paper summaries

Add the following repository settings under **Settings → Secrets and variables
→ Actions**:

- Repository secret `CURSOR_API_KEY`: a Cursor user API key
- Repository variable `CURSOR_MODEL`: optional; defaults to `gpt-5.6-luna`

The workflow extracts text from the selected 10 PDFs, excluding references
where possible and limiting each paper to 100,000 characters. Cursor reads the
full extracted text, translates the abstract, and writes a Chinese summary,
contributions, relevance, and supported limitations.

Never commit the API key. If the key, quota, PDF, or model call fails, the
workflow keeps the rule-generated digest instead of losing the daily update.

## Reading policy

- **Must-read**: the highest-scoring 3 papers
- **Skim**: the remaining 7 papers in the model reading budget
- **Archive**: retained in the full feed for later search

The workflow runs once every 24 hours. Each day is stored as
`docs/digests/YYYY-MM-DD.md`; previous days are retained.
