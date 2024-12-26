import os
from controllers.main_controller import MainController
from models.player import Player
from models.tournament import Tournament

def initialize_data():
    if not os.path.exists('data'):
        os.makedirs('data')
    for filename in ['players.json', 'tournaments.json']:
        filepath = os.path.join('data', filename)
        if not os.path.exists(filepath):
            with open(filepath, 'w') as f:
                f.write('[]')
    Player.initialize_last_id()
    Tournament.load_all()

def main():
    print("Bienvenue dans le gestionnaire de tournois d'échecs!")
    initialize_data()
    controller = MainController()
    controller.run()
    print("Merci d'avoir utilisé le gestionnaire de tournois d'échecs. Au revoir!")

if __name__ == "__main__":
    main()
