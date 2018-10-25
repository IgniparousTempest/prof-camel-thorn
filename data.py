import os
import pickle
from collections import OrderedDict


class Data(object):
    def __init__(self):
        self.data = OrderedDict([
            ("xp", {}),
            ("jogger", {}),
            ("collector", {}),
            ("battle-girl", {})
        ])
        if os.path.isfile("data.pickle"):
            self.data = pickle.load(open("data.pickle", "rb"))

    def update(self, channel: str, user: str, value: int):
        self.data[channel][user] = value
        pickle.dump(self.data, open("data.pickle", "wb"))

    def leaderboard(self, channel, size=10) -> str:
        board = [(k, v) for k, v in self.data[channel].items()]
        sorted(board, key=lambda i: i[1])
        board = board[0:size]
        leader = []
        for i in range(len(board)):
            leader.append("{0}. {1}: {2:,}".format(i + 1, board[i][0], board[i][1]))
        return '\n'.join(leader)
