from dataclasses import dataclass


@dataclass
class Worker:
    id: int
    role: str
    task: str
    status: str = "Idle"
    result: str = ""