from controllers.main_controller import MainController


def main():
    controller = MainController()
    controller.afficher_bienvenue()
    controller.run()


if __name__ == "__main__":
    main()
