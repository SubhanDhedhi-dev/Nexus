from app.agents.manager import Manager


def main():
    request = "Build me a portfolio website"

    manager = Manager()

    manager.run(request)


if __name__ == "__main__":
    main()