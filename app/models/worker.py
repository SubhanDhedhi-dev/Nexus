class Worker:
    """
    Represents a worker responsible for completing one task.
    """

    def __init__(
        self,
        id: int,
        role: str,
        mission: str,
        status: str = "Pending",
        result: str = ""
    ):
        self.id = id
        self.role = role
        self.mission = mission
        self.status = status
        self.result = result

        self.output_file = None
        self.output_content = None

    def __repr__(self):

        return (
            f"Worker("
            f"id={self.id}, "
            f"role='{self.role}', "
            f"mission='{self.mission}', "
            f"status='{self.status}', "
            f"result='{self.result}'"
            f")"
        )