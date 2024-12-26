class MenuView:
    def display_main_menu(self):
        print("\n--- Menu Principal ---")
        print("1. Créer un nouveau joueur")
        print("2. Créer un nouveau tournoi")
        print("3. Ajouter un joueur à un tournoi")
        print("4. Afficher tous les joueurs")
        print("5. Afficher tous les tournois")
        print("6. Afficher les détails d'un tournoi")
        print("7. Lancer un tournoi")
        print("8. Modifier un joueur")
        print("9. Modifier un tournoi")
        print("10. Quitter")
        return input("Choisissez une option : ")

    def get_player_info(self):
        while True:
            first_name = input("Prénom du joueur : ").strip()
            if first_name:
                break
            print("Le prénom ne peut pas être vide.")
        
        while True:
            last_name = input("Nom du joueur : ").strip()
            if last_name:
                break
            print("Le nom ne peut pas être vide.")
        
        birth_date = input("Date de naissance (JJ-MM-AAAA) : ")
        chess_id = input("Numéro d'inscription (6 éléments) : ")
        return first_name, last_name, birth_date, chess_id

    def get_tournament_info(self):
        name = input("Nom du tournoi : ")
        location = input("Lieu du tournoi : ")
        start_date = input("Date de début (JJ-MM-AAAA) : ")
        end_date = input("Date de fin (JJ-MM-AAAA) : ")
        description = input("Description du tournoi : ")
        return name, location, start_date, end_date, description

    def display_players(self, players):
        for player in players:
            print(f"ID: {player.id}, Nom: {player.last_name}, Prénom: {player.first_name}, Date de naissance: {player.birth_date}, N° Dossier: {player.chess_id}")

    def display_tournaments(self, tournaments):
        for tournament in tournaments:
            print(f"Nom: {tournament.name}, Lieu: {tournament.location}")

    def display_tournament_details(self, tournament, players):
        print(f"Nom: {tournament.name}")
        print(f"Lieu: {tournament.location}")
        print(f"Date de début: {tournament.start_date}")
        print(f"Date de fin: {tournament.end_date}")
        print(f"Description: {tournament.description}")
        print(f"Nombre de rounds: {tournament.calculate_num_rounds()}")
        print(f"Round actuel: {tournament.current_round}")
        print("Joueurs:")
        for player_id in tournament.players:
            player = next((p for p in players if p.id == player_id), None)
            if player:
                print(f" - {player.first_name} {player.last_name}")
        print("Rounds:")
        for round in tournament.rounds:
            print(f" - {round.name}")
            for match in round.matches:
                player1 = next((p for p in players if p.id == match.player1_id), None)
                player2 = next((p for p in players if p.id == match.player2_id), None)
                if player1 and player2:
                    print(f"   {player1.last_name} vs {player2.last_name}")

    def get_match_result(self, player1, player2):
        print(f"Match: {player1.last_name} vs {player2.last_name}")
        result = input("Entrez le résultat (1 pour joueur 1, 2 pour joueur 2, 0 pour match nul): ")
        return result
