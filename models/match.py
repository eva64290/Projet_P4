import uuid


class Match:
    def __init__(self, player1_id, player2_id):
        self.id = str(uuid.uuid4())
        self.player1_id = player1_id
        self.player2_id = player2_id
        self.winner_id = None

    def to_dict(self):
        return {
            'id': self.id,
            'player1_id': self.player1_id,
            'player2_id': self.player2_id,
            'winner_id': self.winner_id
        }

    def set_result(self, winner_id):
        self.winner_id = winner_id

    @staticmethod
    def from_dict(data):
        match = Match(data['player1_id'], data['player2_id'])
        match.id = data['id']
        match.winner_id = data['winner_id']
        return match
