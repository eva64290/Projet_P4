import uuid

class Match:
    def __init__(self, player1_id, player2_id):
        self.id = str(uuid.uuid4())
        self.player1_id = player1_id
        self.player2_id = player2_id
        self.winner = None
        self.loser = None

    def to_dict(self):
        return {
            'id': self.id,
            'player1_id': self.player1_id,
            'player2_id': self.player2_id,
            'winner': self.winner,
            'loser': self.loser
        }

    def set_result(self, winner_id):
        self.winner = winner_id
        if winner_id:
            self.loser = self.player2_id if winner_id == self.player1_id else self.player1_id
        else:
            self.loser = None  # Match nul

    @staticmethod
    def from_dict(data):
        match = Match(data['player1_id'], data['player2_id'])
        match.id = data['id']
        match.winner = data['winner']
        match.loser = data['loser']
        return match

