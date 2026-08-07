from datetime import datetime

from app.models.project import Project
from app.core.planner import Planner
from app.core.worker_manager import WorkerManager
from app.services.workspace import Workspace


class Manager:

    def __init__(self):

        self.current_project = None

        self.planner = Planner()

        self.worker_manager = WorkerManager()

        self.workspace = Workspace()

    def receive_request(self, request):

        print(f"[Manager] Received request: {request}")

        self.current_project = Project(request=request)

        print("[Manager] Project created.")
        print(f"[Manager] Project ID: {self.current_project.id}")

        path = self.workspace.create(self.current_project)

        print(f"[Workspace] Created at: {path}")

    def plan(self):

        print(f"\n[Manager] Planning '{self.current_project.name}'...")

        self.current_project.tasks = self.planner.plan(
            self.current_project.request
        )

        self.current_project.updated_at = datetime.now()

        self.workspace.save(self.current_project)

        print(f"[Manager] Created {len(self.current_project.tasks)} task(s).")

    
    def create_workers(self):

        workers = self.worker_manager.create_workers(
        self.current_project.tasks
    )

        self.current_project.workers = workers

        self.workspace.save(self.current_project)

    def assign_tasks(self):

        self.worker_manager.assign_tasks()

        self.workspace.save(self.current_project)

    def collect_results(self):

        self.worker_manager.collect_results()

        self.workspace.save(self.current_project)

    def finish(self):

        self.current_project.status = "Completed"

        self.current_project.updated_at = datetime.now()

        self.workspace.save(self.current_project)

        print(f"\n[Manager] {self.current_project.name} completed.")