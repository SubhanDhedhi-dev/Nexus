from app.models.task import Task
from app.core.model_manager import ModelManager


class Planner:
    """
    Responsible for breaking a user request into tasks.
    """

    def __init__(self):
        self.model_manager = ModelManager()

    def plan(self, request: str):

        prompt = f"""
You are an AI Planner.

User Request:
{request}

Break the project into tasks.
"""

        ai_response = self.model_manager.generate(prompt)

        print("\nPlanner AI Response")
        print("-------------------")
        print(ai_response)

        request = request.lower()

        tasks = []

        if "website" in request:

            tasks.append(
                Task(
                    title="HTML",
                    description="Create the HTML structure."
                )
            )

            tasks.append(
                Task(
                    title="CSS",
                    description="Style the website."
                )
            )

            tasks.append(
                Task(
                    title="JavaScript",
                    description="Add interactivity."
                )
            )

        else:

            tasks.append(
                Task(
                    title="General Task",
                    description=request
                )
            )

        return tasks