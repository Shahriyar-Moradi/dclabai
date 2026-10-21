"""First-class research projects and their non-production evidence status."""
import json
from pathlib import Path
from .catalog import ROOT

PROJECTS = {
    "general": {
        "name": "Open tabular lab",
        "summary": "Ten public binary-classification datasets for broad workflow discovery.",
        "datasets": ["adult", "bank_marketing", "breast_cancer", "heart_disease", "credit_default", "german_credit", "mushroom", "spambase", "online_shoppers", "wine_quality"],
        "default_dataset": "bank_marketing",
        "status": "Ready for agentic experiments",
    },
    "telco_churn": {
        "name": "Telco Churn",
        "summary": "Customer churn R&D with a reproducible 15-experiment development-CV benchmark and an agentic follow-up loop.",
        "datasets": ["telco_churn"],
        "default_dataset": "telco_churn",
        "status": "15-experiment campaign available",
    },
}

def _read(path: Path):
    return json.loads(path.read_text()) if path.is_file() else None

def historical_context(project, root=ROOT):
    """Curated context only: old reused holdouts are hypotheses, not live evidence IDs."""
    return []  # no curated history in this edition

def project_catalog(root=ROOT):
    result = []
    for key, value in PROJECTS.items():
        item = {"key": key, **value}
        if key == "telco_churn":
            summary = _read(root / "research/churn-prediction/experiments/churn_exp/results/summary.json")
            item["campaign"] = summary or {"completed": 0, "planned": 15}
            if summary: item["status"] = f"{summary['completed']}-experiment campaign completed"
        result.append(item)
    return result
