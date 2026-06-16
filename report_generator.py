import os
from typing import Any
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()


def format_tasks(tasks: list[dict[str, Any]]) -> str:
    lines = []
    for task in tasks:
        lines.append(
            f"- {task['name']} | Status: {task['status']} | "
            f"Zaduzen: {task['assignee']} | Prioritet: {task['priority']}"
        )
    return "\n".join(lines)


def analyze_progress(tasks: list[dict[str, Any]]) -> str:
    total = len(tasks)
    done = len([t for t in tasks if t["status"].lower() == "done"])
    in_progress = len([t for t in tasks if t["status"].lower() == "in progress"])
    to_do = len([t for t in tasks if t["status"].lower() == "to do"])

    percent_done = round((done / total) * 100, 1) if total > 0 else 0

    summary = (
        f"Ukupno taskova: {total}\n"
        f"Zavrseno: {done} ({percent_done}%)\n"
        f"U toku: {in_progress}\n"
        f"Nije zapoceto: {to_do}\n"
    )
    return summary

    def identify_risks(tasks: list[dict[str, Any]]) -> str:
    risks = []

    overdue_to_do = [t for t in tasks if t["status"].lower() == "to do" and t["priority"].lower() == "high"]
    if overdue_to_do:
        risks.append(
            f"Postoji {len(overdue_to_do)} task(ova) visokog prioriteta koji jos nisu zapoceti."
        )

    unassigned = [t for t in tasks if not t.get("assignee") or t["assignee"].lower() == "nepoznato"]
    if unassigned:
        risks.append(
            f"Postoji {len(unassigned)} task(ova) bez dodeljenog zaduzenog lica."
        )

    stuck_in_progress = [t for t in tasks if t["status"].lower() == "in progress"]
    if len(stuck_in_progress) > len(tasks) * 0.5:
        risks.append(
            "Veliki broj taskova je trenutno u toku, sto moze ukazivati na preopterecenost tima."
        )

    if not risks:
        return "Nisu identifikovani znacajni rizici na osnovu trenutnog stanja taskova."

    return "\n".join(f"- {r}" for r in risks)