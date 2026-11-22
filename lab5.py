"""Лабораторна робота 5. Варіант 12: Bug і Backlog."""

from datetime import date
from enum import Enum

 
class Severity(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


class Status(Enum):
    NEW = 1
    IN_PROGRESS = 2
    RESOLVED = 3


class Bug:
    def __init__(self, description, severity, deadline, status, assignee):
        self.description = description
        self.severity = severity
        self.deadline = deadline
        self._status = status
        self._assignee = assignee

    def __del__(self):
        print(f"Баг '{self.description}' видалено")

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    def get_assignee(self):
        return self._assignee

    def set_assignee(self, assignee):
        self._assignee = assignee

    def show(self):
        print(f"{self.description} | {self.severity.name} | "
              f"{self.deadline} | {self._status.name} | {self._assignee}")


class Backlog:
    def __init__(self):
        self.bugs = []

    def __del__(self):
        print("Беклог видалено")

    def add_bug(self, bug):
        self.bugs.append(bug)

    def get_resolved_by(self, assignee):
        return [b for b in self.bugs if b.get_assignee() == assignee
                and b.get_status() == Status.RESOLVED]

    def sort_by_severity(self):
        self.bugs.sort(key=lambda b: b.severity.value, reverse=True)

    def show(self):
        for bug in self.bugs:
            bug.show()


def main():
    backlog = Backlog()
    backlog.add_bug(Bug("Не працює логін", Severity.CRITICAL,
                        date(2026, 11, 20), Status.RESOLVED, "Oleh"))
    backlog.add_bug(Bug("Колір кнопки", Severity.LOW,
                        date(2026, 12, 1), Status.NEW, "Anna"))
    backlog.add_bug(Bug("Збій збереження", Severity.HIGH,
                        date(2026, 11, 25), Status.RESOLVED, "Oleh"))
    print(backlog.bugs[0].severity)
    print("Беклог:")
    backlog.show()
    for bug in backlog.bugs:
        print(bug.severity)

    print("\nRESOLVED баги Oleh:")
    for bug in backlog.get_resolved_by("Oleh"):
        print(bug.severity)

    print("\nПісля сортування за severity:")
    backlog.sort_by_severity()
    backlog.show()


if __name__ == "__main__":
    main()