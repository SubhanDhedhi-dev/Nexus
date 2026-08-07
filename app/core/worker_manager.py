from app.models.worker import Worker


class WorkerManager:
    """
    Responsible for creating and managing workers.
    """

    def __init__(self):
        self.workers = []

    def create_workers(self, tasks):

        self.workers.clear()

        print("\n[Worker Manager] Creating workers...\n")

        for index, task in enumerate(tasks, start=1):

            worker = Worker(
                id=index,
                role=task.title,
                task=task.description
            )

            self.workers.append(worker)

            print(f"Worker {worker.id} created.")
            print(f"Role   : {worker.role}")
            print(f"Mission: {worker.task}\n")

    def assign_tasks(self):

        print("[Worker Manager] Assigning tasks...\n")

        for worker in self.workers:

            worker.status = "Working"

            print(f"Worker {worker.id} is working...")

            # Fake work (AI will replace this later)
            worker.result = f"{worker.role} completed."

            worker.status = "Completed"

    def collect_results(self):

        print("\n[Worker Manager] Collecting results...\n")

        for worker in self.workers:

            print(f"Worker {worker.id}")
            print(f"Status : {worker.status}")
            print(f"Result : {worker.result}\n")

    def get_workers(self):
        return self.workers