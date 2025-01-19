class MenuView:
    def display_main_menu(self):
        print("\n--- Menu Principal ---")
        print("1. Créer un joueur")
        print("2. Créer un tournoi")
        print("3. Ajouter des joueurs à un tournoi")
        print("4. Afficher tous les joueurs")
        print("5. Afficher tous les tournois")
        print("6. Afficher les détails d'un tournoi")
        print("7. Lancer un tournoi")
        print("8. Quitter")
        return input("Choisissez une option : ")

    def get_player_info(self):
        print("\n--- Création d'un joueur ---")
        while True:
            first_name = input("Prénom : ").strip()
            if first_name:
                break
            print("Le prénom ne peut pas être vide. Veuillez réessayer.")

        while True:
            last_name = input("Nom : ").strip()
            if last_name:
                break
            print("Le nom ne peut pas être vide. Veuillez réessayer.")

        while True:
            birth_date = input("Date de naissance (JJ-MM-AAAA) : ").strip()
            if birth_date:
                break
            print("La date de naissance ne peut pas être vide. Veuillez réessayer.")

        while True:
            chess_id = input("Identifiant national d'échecs : ").strip()
            if chess_id:
                break
            print("L'identifiant national d'échecs ne peut pas être vide. Veuillez réessayer.")

        return first_name, last_name, birth_date, chess_id

    def get_tournament_info(self):
        print("\n--- Création d'un tournoi ---")
        name = input("Nom du tournoi : ")
        location = input("Lieu : ")
        start_date = input("Date de début (JJ-MM-AAAA) : ")
        end_date = input("Date de fin (JJ-MM-AAAA) : ")
        description = input("Description : ")
        return name, location, start_date, end_date, description

    def display_players(self, players):
        print("\n--- Liste des joueurs ---")
        for player in players:
            print(f"ID: {player.id}, Nom: {player.last_name}, Prénom: {player.first_name}, Date de naissance: {player.birth_date}")

    def display_tournaments(self, tournaments):
        print("\n--- Liste des tournois ---")
        for tournament in tournaments:
            print(f"Nom: {tournament.name}, Lieu: {tournament.location}, Date de début: {tournament.start_date}, Date de fin: {tournament.end_date}")

    def display_tournament_details(self, tournament, players):
        print(f"\n--- Détails du tournoi : {tournament.name} ---")
        print(f"Lieu: {tournament.location}")
        print(f"Date de début: {tournament.start_date}")
        print(f"Date de fin: {tournament.end_date}")
        print(f"Description: {tournament.description}")
        print("\nJoueurs inscrits:")
        for player in players:
            print(f"- {player.first_name} {player.last_name}")
        print(f"\nNombre de rondes: {len(tournament.rounds)}")
        print(f"Ronde actuelle: {tournament.current_round}")

    def get_match_result(self, player1, player2):
        print(f"\nMatch : {player1.last_name} vs {player2.last_name}")
        while True:
            result = input("Entrez le résultat (1 pour joueur 1, 2 pour joueur 2, 0 pour match nul) : ")
            if result in ['0', '1', '2']:
                return result
            print("Entrée invalide. Veuillez réessayer.")
