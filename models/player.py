from tinydb import TinyDB, Query
import random

class Player:
    db = TinyDB('data/players.json')
    last_id = 0

    @classmethod
    def get_next_id(cls):
        cls.last_id += 1
        return f"P{cls.last_id:04d}"

    @staticmethod
    def chess_id_exists(chess_id):
        return bool(Player.db.search(Query().chess_id == chess_id))

    def __init__(self, first_name, last_name, birth_date, chess_id=None):
        self.id = self.get_next_id()
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        if chess_id:
            if self.chess_id_exists(chess_id):
                raise ValueError("Ce numéro d'inscription existe déjà.")
            self.chess_id = chess_id
        else:
            self.chess_id = self.generate_unique_chess_id()
        self.score = 0

    def generate_unique_chess_id(self):
        while True:
            chess_id = f"C{random.randint(100000, 999999)}"
            if not self.chess_id_exists(chess_id):
                return chess_id

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': self.birth_date,
            'chess_id': self.chess_id,
            'score': self.score
        }

    def save(self):
        Player.db.insert(self.to_dict())

    def update(self):
        Player.db.update(self.to_dict(), Query().id == self.id)

    @staticmethod
    def get_all():
        return [Player.from_dict(player) for player in Player.db.all()]

    @staticmethod
    def get_by_id(player_id):
        result = Player.db.search(Query().id == player_id)
        return Player.from_dict(result[0]) if result else None

    @staticmethod
    def from_dict(data):
        player = Player(data['first_name'], data['last_name'], data['birth_date'], data['chess_id'])
        player.id = data['id']
        player.score = data.get('score', 0)
        return player

    @classmethod
    def initialize_last_id(cls):
        players = cls.get_all()
        if players:
            last_id = max(int(p.id[1:]) for p in players if p.id.startswith('P'))
            cls.last_id = last_id
        else:
            cls.last_id = 0
