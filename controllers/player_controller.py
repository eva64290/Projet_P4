from models.player import Player
from views.menu_view import MenuView
from datetime import datetime


class PlayerController:
    def __init__(self):
        self.view = MenuView()

    def create_player(self):
        first_name, last_name, birth_date, chess_id = self.view.get_player_info()
        try:
            birth_date = datetime.strptime(birth_date, "%d-%m-%Y").date().isoformat()
            player = Player(first_name, last_name, birth_date, chess_id)
            player.save()
            print(f"Joueur créé avec l'ID : {player.id}")
        except ValueError:
            print("Format de date invalide. Veuillez utiliser JJ-MM-AAAA.")
            self.create_player()  # Relancer la création du joueur en cas d'erreur

    def display_players(self):
        players = Player.get_all()
        self.view.display_players(players)
