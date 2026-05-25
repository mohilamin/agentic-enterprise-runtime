# Flagship Demo Guide

Run:

```bash
python -m src.demo.run_flagship_demo
```

Scenario: `support_refund_with_fraud_and_prompt_injection`

Five-minute demo flow:
1. Support refund task arrives.
2. Support agent proposes a refund.
3. Fraud signal triggers handoff to fraud agent.
4. Fraud agent recommends shadow freeze or step-up authentication.
5. A prompt injection attempt is detected by the security agent.
6. Governance agent reviews policy.
7. Conflict arbitration chooses the safe path.
8. Direct freeze is blocked and staged for approval.
9. Executive briefing is generated.
10. Trace, audit, and scorecard evidence is written.

Artifacts:
- `data/demo/flagship_demo_trace.json`
- `data/demo/flagship_demo_summary.json`
- `data/demo/flagship_demo_decision_path.csv`
- `data/demo/flagship_demo_briefing.md`

