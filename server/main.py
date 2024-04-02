from util.app.constructor import AppConstructor


if __name__ == "__main__":
    from container.constructor import ContainerConstructor

    ContainerConstructor()

    app_creator: AppConstructor = AppConstructor()
    app_creator.run_app(
        app=app_creator.create_app()
    )