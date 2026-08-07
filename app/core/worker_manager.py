from app.models.worker import Worker


class WorkerManager:

    def __init__(self):

        self.workers = []

    def create_workers(self, tasks):

        print("\n[Worker Manager] Creating workers...")

        self.workers = []

        for index, task in enumerate(tasks, start=1):

            worker = Worker(
                id=index,
                role=task.title,
                mission=task.description
            )

            self.workers.append(worker)

            print(f"\nWorker {worker.id} created.")
            print(f"Role   : {worker.role}")
            print(f"Mission: {worker.mission}")

        return self.workers

    def assign_tasks(self):

        print("\n[Worker Manager] Assigning tasks...")

        for worker in self.workers:

            print(f"\nWorker {worker.id} is working...")

            worker.status = "Working"

            worker.result = f"{worker.role} completed."

            worker.status = "Completed"

    def collect_results(self):

        print("\n[Worker Manager] Collecting results...")

        for worker in self.workers:

            print(f"\nWorker {worker.id}")
            print(f"Status : {worker.status}")
            print(f"Result : {worker.result}")