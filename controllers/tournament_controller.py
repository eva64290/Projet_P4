from models.tournament import Tournament
from models.player import Player
from views.menu_view import MenuView
from datetime import datetime


class TournamentController:
    def __init__(self):
        self.view = MenuView()

    def create_tournament(self):
        name, location, start_date, end_date, description = self.view.get_tournament_info()
        try:
            start_date = datetime.strptime(start_date, "%d-%m-%Y").date().isoformat()
            end_date = datetime.strptime(end_date, "%d-%m-%Y").date().isoformat()
            tournament = Tournament(name, location, start_date, end_date, description)
            tournament.save()
            print(f"Tournoi créé avec le nom : {tournament.name}")
        except ValueError:
            print("Format de date invalide. Veuillez utiliser JJ-MM-AAAA.")

    def add_player_to_tournament(self):
        tournament_name = input("Nom du tournoi : ")
        tournament = Tournament.get_by_name(tournament_name)
        if not tournament:
            print("Tournoi non trouvé.")
            return

        choice = input("Voulez-vous ajouter les joueurs un par un (1) ou tous d'un coup (2) ? ")
        if choice == '1':
            while True:
                player_id = input("ID du joueur à ajouter (ou 'q' pour terminer) : ")
                if player_id.lower() == 'q':
                    break
                self.add_single_player(tournament, player_id)
        elif choice == '2':
            player_ids = input("Entrez les IDs des joueurs séparés par des virgules : ").split(',')
            for player_id in player_ids:
                self.add_single_player(tournament, player_id.strip())
        else:
            print("Choix invalide.")

        tournament.update()
        print("Ajout des joueurs terminé.")

    def add_single_player(self, tournament, player_id):
        player = Player.get_by_id(player_id)
        if player:
            if player.id not in tournament.players:
                tournament.add_player(player.id)
                print(f"Joueur {player.first_name} {player.last_name} ajouté au tournoi {tournament.name}.")
            else:
                print(f"Le joueur {player.first_name} {player.last_name} est déjà dans le tournoi.")
        else:
            print(f"Joueur avec l'ID {player_id} non trouvé.")

    def display_tournaments(self):
        tournaments = Tournament.get_all()
        self.view.display_tournaments(tournaments)

    def display_tournament_details(self):
        tournament_name = input("Nom du tournoi : ")
        tournament = Tournament.get_by_name(tournament_name)
        if tournament:
            players = [Player.get_by_id(player_id) for player_id in tournament.players]
            self.view.display_tournament_details(tournament, players)
        else:
            print("Tournoi non trouvé.")

    def start_tournament(self):
        tournament_name = input("Nom du tournoi à lancer : ")
        tournament = Tournament.get_by_name(tournament_name)
        if not tournament:
            print("Tournoi non trouvé.")
            return
        if len(tournament.players) < 2:
            print("Il faut au moins 2 joueurs pour commencer le tournoi.")
            return

        num_rounds = tournament.calculate_num_rounds()
        print(f"Le tournoi {tournament.name} va commencer avec {num_rounds} rondes.")

        for round_num in range(1, num_rounds + 1):
            print(f"\nDébut de la ronde {round_num}")
            round = tournament.start_new_round()
            if not round:
                print("Impossible de créer une nouvelle ronde. Le tournoi est peut-être terminé.")
                break
            self.pair_players(tournament, round)
            self.play_round(round)
            tournament.update()
            print(f"Fin de la ronde {round_num}")

        print(f"Le tournoi {tournament.name} est terminé.")
        self.display_final_standings(tournament)

    def pair_players(self, tournament, round):
        players = [Player.get_by_id(player_id) for player_id in tournament.players]
        players.sort(key=lambda x: (x.score, x.chess_id), reverse=True)
        paired = set()

        for i in range(0, len(players), 2):
            if i + 1 < len(players):
                round.add_match(players[i].id, players[i+1].id)
                paired.add(players[i].id)
                paired.add(players[i+1].id)
                print(f"Match: {players[i].last_name} vs {players[i+1].last_name}")

        if len(players) % 2 != 0:
            unpaired_player = next(player for player in players if player.id not in paired)
            print(f"Le joueur {unpaired_player.last_name} est exempté pour cette ronde.")

    def play_round(self, round):
        for match in round.matches:
            player1 = Player.get_by_id(match.player1_id)
            player2 = Player.get_by_id(match.player2_id)
            result = self.view.get_match_result(player1, player2)
            if result == '1':
                match.set_result(player1.id)
                player1.score += 1
            elif result == '2':
                match.set_result(player2.id)
                player2.score += 1
            else:
                player1.score += 0.5
                player2.score += 0.5
            player1.update()
            player2.update()
        round.end_round()

    def display_final_standings(self, tournament):
        players = [Player.get_by_id(player_id) for player_id in tournament.players]
        players.sort(key=lambda x: x.score, reverse=True)
        print("\nClassement final:")
        for i, player in enumerate(players, 1):
            print(f"{i}. {player.first_name} {player.last_name} - Score: {player.score}")
