from pathlib import Path
from dataclasses import asdict
import json


class Workspace:

    def __init__(self):
        self.projects_folder = Path("projects")
        self.projects_folder.mkdir(exist_ok=True)

    def create(self, project):

        project_path = self.projects_folder / project.id

        project_path.mkdir(exist_ok=True)

        (project_path / "workers").mkdir(exist_ok=True)
        (project_path / "memory").mkdir(exist_ok=True)
        (project_path / "logs").mkdir(exist_ok=True)
        (project_path / "output").mkdir(exist_ok=True)

        self.save(project)

        return project_path

    def save(self, project):

        project_path = self.projects_folder / project.id

        with open(project_path / "project.json", "w") as file:
            json.dump(
                asdict(project),
                file,
                indent=4,
                default=str
            )