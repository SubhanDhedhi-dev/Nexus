class WorkerEngine:

    def run(self, worker):

        print(f"[Worker Engine] {worker.role} AI started...")

        # Fake AI (temporary)
        response = f"{worker.role} completed."

        print(f"[Worker Engine] {worker.role} AI finished.")

        return response