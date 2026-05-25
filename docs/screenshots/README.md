# Screenshot Capture Guide

Screenshots are not committed yet unless they are manually captured. Use this folder as the capture plan for the public README, LinkedIn posts, portfolio landing page, and interview walkthroughs.

Run the dashboard:

```bash
streamlit run src/dashboard/app.py
```

Recommended location for PNG files:

```text
docs/screenshots/images/
```

Why screenshots matter:
- Recruiters can understand the system in seconds.
- Senior engineers can see that the repo produces inspectable runtime artifacts.
- AI platform reviewers can verify that governance, tracing, red-team checks, and approvals are first-class surfaces.

Priority captures:
- `executive-overview.png`
- `tool-governance.png`
- `multi-agent-handoffs.png`
- `red-team-results.png`
- `trace-explorer.png`
- `evaluation-harness.png`
- `approval-workflow.png`
- `flagship-demo.png`
- `scorecards.png`

Capture tips:
- Run `python -m src.pipeline.run_all` before opening the dashboard.
- Use a wide browser window so tables and metrics are readable.
- Capture the top KPI row and one clear evidence table per section.
- Avoid personal browser chrome or unrelated tabs.

