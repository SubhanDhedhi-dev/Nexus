from pathlib import Path


class ProjectAssembler:
    """
    Combines worker-generated files into the final project output.
    """

    def __init__(self):
        self.base_path = Path("projects")

    def assemble(self, project):
        """
        Collect all worker outputs and place them
        into the project's final output directory.
        """

        print("\n[Assembler] Building final project...")

        project_path = (
            self.base_path
            / str(project.id)
        )

        output_path = project_path / "output"

        output_path.mkdir(
            parents=True,
            exist_ok=True
        )

        # Clear previous output files
        for file in output_path.iterdir():

            if file.is_file():
                file.unlink()

        project.files = []

        for worker in project.workers:

            if not worker.output_file:
                continue

            if worker.output_content is None:
                continue

            destination = (
                output_path
                / worker.output_file
            )

            destination.write_text(
                worker.output_content,
                encoding="utf-8"
            )

            project.files.append(
                str(destination)
            )

            print(
                f"[Assembler] Added: "
                f"{worker.output_file}"
            )

        print(
            f"[Assembler] Final project created at: "
            f"{output_path}"
        )

        return output_path