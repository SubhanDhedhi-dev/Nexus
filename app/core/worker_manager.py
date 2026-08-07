from app.models.worker import Worker
from app.services.worker_workspace import WorkerWorkspace
from app.engines.worker_engine import WorkerEngine


class WorkerManager:

    def __init__(self):

        self.workers = []
        self.workspace = WorkerWorkspace()
        self.engine = WorkerEngine()

    def create_workers(self, project):

        print("\n[Worker Manager] Creating workers...")

        self.workers = []

        for index, task in enumerate(project.tasks, start=1):

            worker = Worker(
                id=index,
                role=task.title,
                mission=task.description
            )

            self.workers.append(worker)

            self.workspace.create(
                project.id,
                worker
            )

            print(f"\nWorker {worker.id} created.")
            print(f"Role   : {worker.role}")
            print(f"Mission: {worker.mission}")

        return self.workers

    def assign_tasks(self):

        print("\n[Worker Manager] Assigning tasks...")

        for worker in self.workers:

            print(f"\nWorker {worker.id} is working...")

            worker.status = "Working"

            worker.result = self.engine.run(worker)

            worker.status = "Completed"

    def collect_results(self):

        print("\n[Worker Manager] Collecting results...")

        for worker in self.workers:

            print(f"\nWorker {worker.id}")
            print(f"Status : {worker.status}")
            print(f"Result : {worker.result}")