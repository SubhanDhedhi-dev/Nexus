from datetime import datetime

from app.models.project import Project
from app.core.planner import Planner
from app.core.worker_manager import WorkerManager
from app.core.event_bus import EventBus
from app.services.workspace import Workspace
from app.services.logger import Logger


class Manager:

    def __init__(self):

        self.current_project = None

        self.planner = Planner()
        self.worker_manager = WorkerManager()

        self.event_bus = EventBus()

        self.workspace = Workspace()
        self.logger = Logger()

        self.event_bus.subscribe(
            "PROJECT_CREATED",
            self._on_project_created
        )

        self.event_bus.subscribe(
            "PROJECT_UPDATED",
            self._on_project_updated
        )

    def _on_project_created(self, project):

        path = self.workspace.create(project)

        self.logger.log(f"Project created: {project.id}")

        print(f"[Workspace] Created at: {path}")

    def _on_project_updated(self, project):

        self.workspace.save(project)

        self.logger.log(
            f"Project updated: {project.id} ({project.status})"
        )

    def receive_request(self, request):

        print(f"[Manager] Received request: {request}")

        self.current_project = Project(request=request)

        print("[Manager] Project created.")
        print(f"[Manager] Project ID: {self.current_project.id}")

        self.event_bus.emit(
            "PROJECT_CREATED",
            self.current_project
        )

    def plan(self):

        print(f"\n[Manager] Planning '{self.current_project.name}'...")

        self.current_project.tasks = self.planner.plan(
            self.current_project.request
        )

        self.current_project.updated_at = datetime.now()

        self.event_bus.emit(
            "PROJECT_UPDATED",
            self.current_project
        )

        print(
            f"[Manager] Created {len(self.current_project.tasks)} task(s)."
        )

    def create_workers(self):

        workers = self.worker_manager.create_workers(
            self.current_project.tasks
        )

        self.current_project.workers = workers

        self.event_bus.emit(
            "PROJECT_UPDATED",
            self.current_project
        )

    def assign_tasks(self):

        self.worker_manager.assign_tasks()

        self.event_bus.emit(
            "PROJECT_UPDATED",
            self.current_project
        )

    def collect_results(self):

        self.worker_manager.collect_results()

        self.event_bus.emit(
            "PROJECT_UPDATED",
            self.current_project
        )

    def finish(self):

        self.current_project.status = "Completed"

        self.current_project.updated_at = datetime.now()

        self.event_bus.emit(
            "PROJECT_UPDATED",
            self.current_project
        )

        print(
            f"\n[Manager] {self.current_project.name} completed."
        )