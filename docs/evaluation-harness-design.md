# Evaluation Harness Design

The evaluation harness compares deterministic runtime outputs against generated task ground truth and runtime evidence.

Metrics include:
- task resolution accuracy
- task routing accuracy
- tool policy precision
- unsafe tool block rate
- prompt attack block rate
- handoff acceptance accuracy
- conflict resolution accuracy
- approval decision accuracy
- red-team detection rate
- decision lineage completeness
- audit record completeness

Outputs are written under `data/evaluations/` and mirrored into `data/scorecards/evaluation_scorecard.*`.

