from pathlib import Path
import json


class WorkerWorkspace:

    def create(self, project_id, worker):

        worker_path = Path("projects") / project_id / f"worker_{worker.id:03}"

        worker_path.mkdir(exist_ok=True)

        (worker_path / "output").mkdir(exist_ok=True)

        with open(worker_path / "prompt.txt", "w") as f:
            f.write("")

        with open(worker_path / "response.txt", "w") as f:
            f.write("")

        with open(worker_path / "memory.json", "w") as f:
            json.dump({}, f, indent=4)

        with open(worker_path / "status.json", "w") as f:
            json.dump(
                {
                    "status": worker.status,
                    "role": worker.role
                },
                f,
                indent=4
            )

        return worker_path