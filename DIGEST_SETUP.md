# Ranked paper digest

The scheduled workflow writes two views:

- `README.md`: the complete high-recall paper feed
- `docs/digests/latest.md`: a shortlist capped at 3 must-read papers and 10
  papers total

## Default mode

No additional setup is required. `rank_papers.py` fetches abstracts for recent
papers, applies deterministic research-track scoring, and creates the digest.
This fallback keeps the workflow useful if an LLM provider is unavailable.

## Optional Chinese LLM summaries

Add the following repository settings under **Settings → Secrets and variables
→ Actions**:

| Type | Name | Required | Default |
|---|---|---:|---|
| Secret | `LLM_API_KEY` | Yes | none |
| Variable | `LLM_BASE_URL` | No | `https://api.deepseek.com` |
| Variable | `LLM_MODEL` | No | `deepseek-chat` |

The endpoint must implement the OpenAI-compatible
`POST /chat/completions` API. The workflow sends only titles, abstracts,
matching topics, and heuristic scores. Never commit an API key to this
repository.

If the request fails, the script logs a warning and publishes the
rule-generated digest instead of failing the paper update.

## Reading policy

- **Must-read**: at most 3 papers per run
- **Skim**: inspect abstract, method figure, and main experiment table
- **Archive**: retained in the full feed for later search

Tune limits in the `digest` section of `config.yaml`.
