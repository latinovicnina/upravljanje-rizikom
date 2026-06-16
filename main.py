from report_generator import generate_status_report


def main() -> None:
    tasks = [
        {
            "name": "Setup development environment",
            "status": "Done",
            "assignee": "Marko",
            "priority": "High",
        },
        {
            "name": "Design database schema",
            "status": "Done",
            "assignee": "Ana",
            "priority": "High",
        },
        {
            "name": "Implement user authentication",
            "status": "Done",
            "assignee": "Marko",
            "priority": "High",
        },
        {
            "name": "Implement payment integration",
            "status": "Done",
            "assignee": "Ana",
            "priority": "Medium",
        },
        {
            "name": "Write unit tests",
            "status": "In Progress",
            "assignee": "Marko",
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