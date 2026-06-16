from report_generator import generate_status_report


def main() -> None:
    tasks = [
        {
            "name": "Definisati problem i zahteve agenta",
            "status": "Done",
            "assignee": "Jana",
            "priority": "High",
        },
        {
            "name": "Implementirati analizu napretka projekta",
            "status": "Done",
            "assignee": "Nina",
            "priority": "High",
        },
        {
            "name": "Implementirati identifikaciju blokatora i rizika",
            "status": "Done",
            "assignee": "Nina",
            "priority": "High",
        },
        {
            "name": "Implementirati generisanje status reporta",
            "status": "In Progress",
            "assignee": "Jana",
            "priority": "High",
        },
        {
            "name": "Testirati agenta na 3 primera",
            "status": "To Do",
            "assignee": "",
            "priority": "Medium",
        },
        {
            "name": "Napisati README dokumentaciju",
            "status": "To Do",
            "assignee": "Nina",
            "priority": "Medium",
        },
    ]

    print("Generisanje status reporta...\n")
    report = generate_status_report(tasks)
    print(report)

    with open("status_report.md", "w", encoding="utf-8") as f:
        f.write(report)

    print("\nReport sacuvan u status_report.md")


if __name__ == "__main__":
    main()