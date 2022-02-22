from copy import deepcopy


class GameState():
    def __init__(self):
        self.board = [
            ["wL", "wN", "wS", "wG", "wK", "wG", "wS", "wN", "wL"],
            ["--", "wR", "--", "--", "--", "--", "--", "wB", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "bB", "--", "--", "--", "--", "--", "bR", "--"],
            ["bL", "bN", "bS", "bG", "bK", "bG", "bS", "bN", "bL"]]