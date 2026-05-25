# Human Approval Workflow Design

V0.2 extends the V0.1 approval queue with auditable reviewer decisions and SLA reporting.

Approval statuses:
- pending
- approved
- rejected
- requires_more_evidence
- escalated
- expired

Outputs:
- `data/approvals/human_approval_queue.csv`
- `data/approvals/action_escrow.csv`
- `data/approvals/approval_decision_history.csv`
- `data/approvals/approval_sla_report.json`
- `data/approvals/approval_sla_report.csv`

The API supports `POST /submit-approval-decision` for demo-friendly simulated review decisions.

