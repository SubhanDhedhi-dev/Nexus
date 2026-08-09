from dataclasses import dataclass
from typing import Optional


@dataclass
class Worker:
    """
    Represents an AI worker assigned to a project task.
    """

    id: int
    role: str
    mission: str
    status: str = "Pending"
    result: Optional[str] = None

    def start(self):
        self.status = "Working"

    def complete(self, result: str):
        self.status = "Completed"
        self.result = result

    def fail(self, error: str):
        self.status = "Failed"
        self.result = error