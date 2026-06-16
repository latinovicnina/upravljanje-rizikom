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