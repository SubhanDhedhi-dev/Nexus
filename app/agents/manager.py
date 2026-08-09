from datetime import datetime

from app.models.project import Project
from app.agents.planner import Planner
from app.agents.worker_manager import WorkerManager
from app.events.event_bus import EventBus
from app.services.workspace import Workspace
from app.services.logger import Logger
from app.services.project_assembler import ProjectAssembler


class Manager:
    """
    Main controller for the Nexus project pipeline.
    """

    def __init__(self):

        self.current_project = None

        self.planner = Planner()

        self.worker_manager = WorkerManager()

        self.assembler = ProjectAssembler()

        self.event_bus = EventBus()

        self.workspace = Workspace()

        self.logger = Logger()

        # Event subscriptions
        self.event_bus.subscribe(
            "PROJECT_CREATED",
            self._on_project_created
        )

        self.event_bus.subscribe(
            "PROJECT_UPDATED",
            self._on_project_updated
        )

    def _on_project_created(self, project):

        path = self.workspace.create(
            project
        )

        self.logger.log(
            f"Project created: {project.id}"
        )

        print(
            f"[Workspace] Created at: {path}"
        )

    def _on_project_updated(self, project):

        self.workspace.save(
            project
        )

        self.logger.log(
            f"Project updated: "
            f"{project.id} "
            f"({project.status})"
        )

    def receive_request(self, request):

        print(
            f"[Manager] Received request: "
            f"{request}"
        )

        self.current_project = Project(
            request=request
        )

        print(
            "[Manager] Project created."
        )

        print(
            f"[Manager] Project ID: "
            f"{self.current_project.id}"
        )

        self.event_bus.emit(
            "PROJECT_CREATED",
            self.current_project
        )

    def plan(self):

        print(
            f"\n[Manager] Planning "
            f"'{self.current_project.name}'..."
        )

        self.current_project.tasks = (
            self.planner.plan(
                self.current_project.request
            )
        )

        self.current_project.updated_at = (
            datetime.now()
        )

        self.event_bus.emit(
            "PROJECT_UPDATED",
            self.current_project
        )

        print(
            f"[Manager] Created "
            f"{len(self.current_project.tasks)} "
            f"task(s)."
        )

        print("\n## Tasks")

        for task in self.current_project.tasks:

            print(task)

    def create_workers(self):

        self.current_project.workers = (
            self.worker_manager.create_workers(
                self.current_project
            )
        )

        self.current_project.updated_at = (
            datetime.now()
        )

        self.event_bus.emit(
            "PROJECT_UPDATED",
            self.current_project
        )

    def assign_tasks(self):

        self.worker_manager.assign_tasks(
            self.current_project
        )

        self.current_project.updated_at = (
            datetime.now()
        )

        self.event_bus.emit(
            "PROJECT_UPDATED",
            self.current_project
        )

    def collect_results(self):

        self.worker_manager.collect_results()

        self.current_project.updated_at = (
            datetime.now()
        )

        self.event_bus.emit(
            "PROJECT_UPDATED",
            self.current_project
        )

    def assemble(self):

        print(
            "\n[Manager] Assembling project..."
        )

        self.assembler.assemble(
            self.current_project
        )

        self.current_project.updated_at = (
            datetime.now()
        )

        self.event_bus.emit(
            "PROJECT_UPDATED",
            self.current_project
        )

    def finish(self):

        self.current_project.status = (
            "Completed"
        )

        self.current_project.updated_at = (
            datetime.now()
        )

        self.event_bus.emit(
            "PROJECT_UPDATED",
            self.current_project
        )

        print(
            f"\n[Manager] "
            f"{self.current_project.name} "
            f"completed."
        )

    def run(self, request):

        self.receive_request(
            request
        )

        self.plan()

        self.create_workers()

        self.assign_tasks()

        self.collect_results()

        self.assemble()

        self.finish()

        print(
            "\n## Final Project"
        )

        print(
            self.current_project
        )