from tinydb import TinyDB, Query


class Player:
    db = TinyDB('data/players.json')
    last_id = 0

    def __init__(self, first_name, last_name, birth_date, chess_id):
        self.id = self.generate_unique_id()
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.chess_id = chess_id
        self.score = 0

    @classmethod
    def generate_unique_id(cls):
        cls.last_id += 1
        return str(cls.last_id)

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
        players = [Player.from_dict(player) for player in Player.db.all()]
        Player.last_id = max(int(player.id) for player in players) if players else 0
        return players

    @staticmethod
    def get_by_id(player_id):
        result = Player.db.search(Query().id == player_id)
        return Player.from_dict(result[0]) if result else None

    @staticmethod
    def from_dict(data):
        player = Player(
            data['first_name'],
            data['last_name'],
            data['birth_date'],
            data['chess_id']
        )
        player.id = data['id']
        player.score = data['score']
        return player
