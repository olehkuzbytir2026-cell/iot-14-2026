from datetime import date
from enum import Enum
from typing import List


class Severity(Enum):
    """Рівні критичності багів."""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


class Status(Enum):
    """Статуси виконання багів."""
    NEW = 1
    IN_PROGRESS = 2
    RESOLVED = 3


class Bug:
    """Клас, що описує окремий баг у системі відстеження."""

    def __init__(self, description: str, severity: Severity, deadline: date, status: Status, assignee: str) -> None:
        if not isinstance(description, str):
            raise TypeError("Description must be a string")
        if not isinstance(severity, Severity):
            raise TypeError("Severity must be an instance of Severity Enum")
        if not isinstance(deadline, date):
            raise TypeError("Deadline must be a date object")
        if not isinstance(status, Status):
            raise TypeError("Status must be an instance of Status Enum")
        if not isinstance(assignee, str):
            raise TypeError("Assignee must be a string")

        self.description: str = description
        self.severity: Severity = severity
        self.deadline: date = deadline
        self._status: Status = status
        self._assignee: str = assignee

    def __del__(self) -> None:
        print(f"Баг '{self.description}' видалено")

    def get_status(self) -> Status:
        """Повертає поточний статус багу."""
        return self._status

    def set_status(self, status: Status) -> None:
        """Встановлює новий статус багу."""
        if not isinstance(status, Status):
            raise TypeError("Status must be an instance of Status Enum")
        self._status = status

    def get_assignee(self) -> str:
        """Повертає виконавця багу."""
        return self._assignee

    def set_assignee(self, assignee: str) -> None:
        """Встановлює нового виконавця багу."""
        if not isinstance(assignee, str):
            raise TypeError("Assignee must be a string")
        self._assignee = assignee

    def show(self) -> None:
        """Виводить інформацію про баг у консоль."""
        print(f"{self.description} | {self.severity.name} | "
              f"{self.deadline} | {self._status.name} | {self._assignee}")


class Backlog:
    """Клас для керування списком багів (беклогом)."""

    def __init__(self) -> None:
        self.bugs: List[Bug] = []

    def __del__(self) -> None:
        print("Беклог видалено")

    def add_bug(self, bug: Bug) -> None:
        """Додає новий баг до беклогу з перевіркою типу."""
        if not isinstance(bug, Bug):
            raise TypeError("Only instances of Bug can be added to Backlog")
        self.bugs.append(bug)

    def get_resolved_by(self, assignee: str) -> List[Bug]:
        """Повертає список вирішених багів конкретного виконавця."""
        return [b for b in self.bugs if b.get_assignee() == assignee
                and b.get_status() == Status.RESOLVED]

    def sort_by_severity(self) -> None:
        """Сортує баги за рівнем критичності у спадному порядку."""
        self.bugs.sort(key=lambda b: b.severity.value, reverse=True)

    def show(self) -> None:
        """Виводить список усіх багів у беклозі."""
        for bug in self.bugs:
            bug.show()


def main() -> None:
    backlog = Backlog()
    backlog.add_bug(Bug("Не працює логін", Severity.CRITICAL,
                        date(2026, 11, 20), Status.RESOLVED, "Oleh"))
    backlog.add_bug(Bug("Колір кнопки", Severity.LOW,
                        date(2026, 12, 1), Status.NEW, "Anna"))
    backlog.add_bug(Bug("Збій збереження", Severity.HIGH,
                        date(2026, 11, 25), Status.RESOLVED, "Oleh"))

    print("Беклог:")
    backlog.show()

    print("\nRESOLVED баги Oleh:")
    for bug in backlog.get_resolved_by("Oleh"):
        bug.show()

    print("\nПісля сортування за severity:")
    backlog.sort_by_severity()
    backlog.show()


if __name__ == "__main__":
    main()
