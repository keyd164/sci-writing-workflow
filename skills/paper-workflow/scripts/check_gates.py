"""Read-only workflow report. Requires PyYAML. Does not grant approval."""
import argparse
import json
import os
from pathlib import Path
import yaml

def locate(explicit):
    selected = explicit or os.environ.get("PAPER_PROJECT_ROOT")
    if selected:
        root = Path(selected).resolve()
        if not (root / ".paper/workflow.yml").is_file():
            raise ValueError("Selected project has no .paper/workflow.yml")
        return root
    for root in [Path.cwd(), *Path.cwd().parents]:
        if (root / ".paper/workflow.yml").is_file():
            return root
    raise ValueError("Project not found")

def report(root):
    data = yaml.safe_load((root / ".paper/workflow.yml").read_text(encoding="utf-8"))
    stages, gates = data["stages"], data["gates"]
    if not isinstance(stages, list) or not isinstance(gates, list):
        raise ValueError("Invalid workflow lists")
    gate_map = {g["id"]: g for g in gates}
    stage_map = {s["id"]: s for s in stages}
    if len(gate_map) != len(gates) or len(stage_map) != len(stages):
        raise ValueError("Duplicate stage or gate id")
    known_status = {"not_started", "pending_approval", "in_progress", "completed", "blocked", "approved"}
    for stage in stages:
        if stage["status"] not in known_status:
            raise ValueError("Unknown stage status: " + str(stage["status"]))
        if stage.get("gate_id") and stage["gate_id"] not in gate_map:
            raise ValueError("Unknown stage gate")
        for dep in stage.get("blocked_by", []):
            if dep not in gate_map and dep not in stage_map:
                raise ValueError("Unknown dependency: " + dep)
    pending = [s for s in stages if s["status"] != "completed"]
    current = pending[0] if pending else None
    unresolved = [g["id"] for g in gates if g["status"] != "approved"]
    return {
        "project": str(root),
        "first_unfinished_stage": current,
        "unapproved_gates": unresolved,
        "preparation_allowed": "Read-only checks and approval materials; no downstream drafting or release without required approvals.",
        "note": "Report only; an exit code of zero is not gate approval or a scientific audit pass."
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("project", nargs="?")
    args = parser.parse_args()
    try:
        print(json.dumps(report(locate(args.project)), ensure_ascii=False, indent=2, default=str))
    except (OSError, ValueError, KeyError, TypeError, yaml.YAMLError) as error:
        parser.exit(2, "Workflow report failed: " + str(error) + "\n")

