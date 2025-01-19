from tinydb import TinyDB, Query
import uuid
from models.round import Round
import math


class Tournament:
    db = TinyDB('data/tournaments.json')

    def __init__(self, name, location, start_date, end_date, description=""):
        self.id = str(uuid.uuid4())
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.players = []
        self.rounds = []
        self.current_round = 0

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'description': self.description,
            'players': self.players,
            'rounds': [round.to_dict() for round in self.rounds],
            'current_round': self.current_round
        }

    def save(self):
        Tournament.db.insert(self.to_dict())

    def update(self):
        Tournament.db.update(self.to_dict(), Query().id == self.id)

    def add_player(self, player_id):
        if player_id not in self.players:
            self.players.append(player_id)
            self.update()

    def calculate_num_rounds(self):
        num_players = len(self.players)
        if num_players <= 1:
            return 0
        elif num_players == 2:
            return 1
        else:
            return math.ceil(math.log2(num_players))

    def start_new_round(self):
        num_rounds = self.calculate_num_rounds()
        if self.current_round < num_rounds:
            self.current_round += 1
            new_round = Round(f"Round {self.current_round}")
            self.rounds.append(new_round)
            self.update()
            return new_round
        return None

    @staticmethod
    def get_all():
        return [Tournament.from_dict(tournament) for tournament in Tournament.db.all()]

    @staticmethod
    def get_by_name(tournament_name):
        result = Tournament.db.search(Query().name == tournament_name)
        return Tournament.from_dict(result[0]) if result else None

    @staticmethod
    def from_dict(data):
        tournament = Tournament(
            data['name'],
            data['location'],
            data['start_date'],
            data['end_date'],
            data['description']
        )
        tournament.id = data['id']
        tournament.players = data['players']
        tournament.rounds = [Round.from_dict(round_data) for round_data in data['rounds']]
        tournament.current_round = data['current_round']
        return tournament
