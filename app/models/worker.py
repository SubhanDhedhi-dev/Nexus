from dataclasses import dataclass


@dataclass
class Worker:

    id: int

    role: str

    mission: str

    status: str = "Idle"

    result: str = ""