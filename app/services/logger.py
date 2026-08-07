from pathlib import Path
from datetime import datetime


class Logger:

    def __init__(self):

        self.logs_folder = Path("logs")
        self.logs_folder.mkdir(exist_ok=True)

    def log(self, message):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        line = f"[{timestamp}] {message}\n"

        with open(self.logs_folder / "nexus.log", "a") as file:
            file.write(line)

        print(f"[Logger] {message}")