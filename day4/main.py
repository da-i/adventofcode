import pdb

from dataclasses import dataclass, field
from typing import List
import numpy as np


def read_input(file_path="day4/input/input.txt"):
    with open(file_path, "r") as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]

    return lines



@dataclass
class BingoCard:
    scorecard: np.array
    matchcard: np.array = field(init=False)

    def __post_init__(self):
        self.matchcard = np.zeros(self.scorecard.shape)

    def update_matchcard(self, score):
        self.matchcard[self.scorecard == score] = 1

    def check_valid_matchcard(self):
        valid = False
        result_vert = np.all(self.matchcard == 1, axis=1)
        result_hori = np.all(self.matchcard == 1, axis=0)

        if True in result_hori or True in result_vert:
            valid = True
        return valid

    def get_sum_unmatched(self):
        self.scorecard_masked = self.scorecard
        self.scorecard_masked[self.matchcard == 1] = 0
        return np.sum(self.scorecard_masked)

    def get_win_statistics(self, scores: List[int]):

        for i, score in enumerate(scores):
            self.update_matchcard(score)
            if self.check_valid_matchcard():
                break
        unmatched_score = self.get_sum_unmatched()
        self.win_rounds = i
        self.win_score = score
        self.win_unmatched_score = unmatched_score
        return i, score, unmatched_score


def create_draws(line):
    draws = line.split(",")
    draws = [int(x) for x in draws]
    return draws

def create_bingo_cards(lines):
    bingo_cards = []
    current_card = []

    for i in lines:
        if i == "":
            bingo_cards.append(BingoCard(np.array(current_card)))
            current_card = []
            continue
        else:
            current_card.append([int(x) for x in i.split()])
            
    return bingo_cards

def main():
    input = read_input()

    draws = create_draws(input[0])
    # [7,4,9,5,11,17,23,2,0,14,21,24,10]

    cards = create_bingo_cards(input[2:])
    
    win_stats = [x.get_win_statistics(draws) for x in cards]
    # sort gives card with lowest turns required 
    win_stats.sort()
    print("solution 1:")
    print(win_stats[0][1]*win_stats[0][2])
    # Got super lucky with choosing a deterministic approach! just pick the last item in the sorted list!
    print("solution 2:")
    print(win_stats[-1][1]*win_stats[-1][2])
    

if __name__ == "__main__":
    main()
