from dataclasses import dataclass, field
from datetime import datetime
import uuid


@dataclass
class Project:
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    name: str = "Untitled Project"
    request: str = ""
    status: str = "Planning"

    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    tasks: list = field(default_factory=list)
    workers: list = field(default_factory=list)

    files: list = field(default_factory=list)
    logs: list = field(default_factory=list)
    memory: dict = field(default_factory=dict)