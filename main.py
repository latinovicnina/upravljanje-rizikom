from report_generator import generate_status_report


def main() -> None:
    tasks = [
        {
            "name": "Finalize project requirements",
            "status": "To Do",
            "assignee": "",
            "priority": "High",
        },
        {
            "name": "Build core API endpoints",
            "status": "In Progress",
            "assignee": "Stefan",
            "priority": "High",
        },
        {
            "name": "Integrate third-party payment gateway",
            "status": "To Do",
            "assignee": "",
            "priority": "High",
        },
        {
            "name": "Set up CI/CD pipeline",
            "status": "In Progress",
            "assignee": "Stefan",
            "priority": "Medium",
        },
        {
            "name": "Conduct security audit",
            "status": "To Do",
            "assignee": "",
            "priority": "High",
        },
        {
            "name": "Prepare client demo",
            "status": "To Do",
            "assignee": "Stefan",
            "priority": "High",
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