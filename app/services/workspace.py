from pathlib import Path
import json
from dataclasses import asdict
from datetime import datetime


class Workspace:

    def __init__(self):

        self.projects_folder = Path("projects")
        self.projects_folder.mkdir(exist_ok=True)

    def create_project(self, project):

        project_folder = self.projects_folder / project.id

        project_folder.mkdir(exist_ok=True)

        (project_folder / "workers").mkdir(exist_ok=True)
        (project_folder / "memory").mkdir(exist_ok=True)
        (project_folder / "logs").mkdir(exist_ok=True)
        (project_folder / "final").mkdir(exist_ok=True)

        data = asdict(project)

        data["created_at"] = project.created_at.isoformat()
        data["updated_at"] = project.updated_at.isoformat()

        with open(project_folder / "project.json", "w", encoding="utf-8") as file:

            json.dump(data, file, indent=4)

        print(f"[Workspace] Project created at: {project_folder}")

        return project_folder