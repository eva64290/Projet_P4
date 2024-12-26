from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from views.menu_view import MenuView

class MainController:
    def __init__(self):
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()
        self.menu_view = MenuView()

    def run(self):
        while True:
            choice = self.menu_view.display_main_menu()
            if choice == '1':
                self.player_controller.create_player()
            elif choice == '2':
                self.tournament_controller.create_tournament()
            elif choice == '3':
                self.tournament_controller.add_player_to_tournament()
            elif choice == '4':
                self.player_controller.display_players()
            elif choice == '5':
                self.tournament_controller.display_tournaments()
            elif choice == '6':
                self.tournament_controller.display_tournament_details()
            elif choice == '7':
                self.tournament_controller.start_tournament()
            elif choice == '8':
                break
            else:
                print("Choix invalide. Veuillez réessayer.")
