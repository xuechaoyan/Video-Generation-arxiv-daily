# Ranked paper digest

The scheduled workflow writes two views:

- `README.md`: the complete high-recall paper feed
- `docs/digests/latest.md`: a shortlist capped at 3 must-read papers and 10
  papers total

## Default mode

No additional setup is required. `rank_papers.py` fetches abstracts for recent
papers, applies deterministic research-track scoring, and creates the digest.
This fallback keeps the workflow useful if an LLM provider is unavailable.

## Cursor full-paper summaries

The workflow ranks papers with rules first, then Cursor reads the 3 must-read
PDFs. Add these repository settings under **Settings → Secrets and variables
→ Actions**:

| Type | Name | Required | Default |
|---|---|---:|---|
| Secret | `PAPER_READING` | Yes | none |
| Variable | `CURSOR_MODEL` | No | `gpt-5.6-luna` |

Never commit the API key. If the key, quota, PDF, or model call fails, the
workflow keeps the rule-generated digest instead of losing the daily update.

## Reading policy

- **Must-read**: at most 3 papers per run; Cursor reads these in full
- **Skim**: inspect abstract, method figure, and main experiment table
- **Archive**: retained in the full feed for later search

Tune limits in the `digest` section of `config.yaml`.
