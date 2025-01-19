import uuid
from datetime import datetime
from models.match import Match


class Round:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.start_time = datetime.now().isoformat()
        self.end_time = None
        self.matches = []

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'matches': [match.to_dict() for match in self.matches]
        }

    def add_match(self, player1_id, player2_id):
        match = Match(player1_id, player2_id)
        self.matches.append(match)

    def end_round(self):
        self.end_time = datetime.now().isoformat()

    @staticmethod
    def from_dict(data):
        round = Round(data['name'])
        round.id = data['id']
        round.start_time = data['start_time']
        round.end_time = data['end_time']
        round.matches = [Match.from_dict(match_data) for match_data in data['matches']]
        return round
