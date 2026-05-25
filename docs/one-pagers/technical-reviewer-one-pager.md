# Technical Reviewer One-Pager

## Design Choices

- Deterministic runtime by default for reproducible tests.
- Optional live-agent adapter is advisory and disabled by default.
- Policy engine remains authoritative.
- Tools are simulated to avoid external dependencies and unsafe actions.
- Runtime artifacts are written as CSV/JSON/Markdown and loaded into DuckDB.

## What Is Evaluated

- task routing accuracy
- tool policy precision
- unsafe tool block rate
- prompt attack block rate
- handoff accuracy
- conflict resolution accuracy
- approval decision accuracy
- lineage completeness
- audit completeness

## What Is Traced

- task received
- route selected
- agent evaluated
- tool requested
- policy checked
- tool simulated
- handoff created
- conflict detected
- guardrail triggered
- approval required
- final decision created

## Limitations

Synthetic data only, deterministic agents by default, local DuckDB, simulated tools, no auth, no cloud deployment, and no real approval system yet.

