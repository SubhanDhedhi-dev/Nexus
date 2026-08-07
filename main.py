from app.core.manager import Manager


def main():

    manager = Manager()

    manager.receive_request("Build me a portfolio website")

    print("\nCurrent Project")
    print("-" * 40)
    print(manager.current_project)

    manager.plan()

    print("\nTasks")
    print("-" * 40)

    for task in manager.current_project.tasks:
        print(task)

    print()

    manager.create_workers()

    manager.assign_tasks()

    manager.collect_results()

    manager.finish()

    print("\nFinal Project")
    print("-" * 40)
    print(manager.current_project)


if __name__ == "__main__":
    main()