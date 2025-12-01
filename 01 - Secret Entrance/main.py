'''
    Author: Guy Pickering
    Date: Dec 1, 2025

    Part 1:
    Given a safe with numbers 0-99 and initially pointing to 50, run through the instructions (e.g. L10, R1005, etc.)
    and determine how many times the number '0' is passed or landed on.

    Part 2:
    Refine part 1 by tracking the total number of times '0' is passed or landed on when the turn is >100 (e.g. 1,000
    passes '0' ten times.
'''

from math import floor
from typing import Tuple, List

class SecretEntrance:
    SAFE_COMBINATIONS=100
    INITIAL_NUMBER=50
    DIRECTION={'L':-1, 'R':1}

    def __init__(self, filepath: str):
        '''
        Load the instruction file (e.g. L10, R1005) to prepare for the calculation.

        :param filepath: path of the instruction file
        '''
        self.instructions: List[Tuple[str, int]] = []

        with open(filepath, 'r') as f:
            self.instructions.extend([(line[0], int(line.strip()[1:]))
                                      for line in f.readlines() if len(line.strip()) > 0])


    def calc_part1(self):
        n = SecretEntrance.INITIAL_NUMBER
        cnt = 0
        for (direction, amount) in self.instructions:
            m = SecretEntrance.DIRECTION[direction]
            n = (n + (m*amount)) % SecretEntrance.SAFE_COMBINATIONS
            if n == 0:
               cnt += 1

        return cnt

    @staticmethod
    def _calc_count_v2(n: int, direction: str, amount: int) -> int:
        if direction == 'R':
            return floor((n + amount) // SecretEntrance.SAFE_COMBINATIONS)
        else:
            return floor(((SecretEntrance.SAFE_COMBINATIONS - n) % SecretEntrance.SAFE_COMBINATIONS + amount) // SecretEntrance.SAFE_COMBINATIONS)

    def calc_part2(self):
        n = SecretEntrance.INITIAL_NUMBER

        cnt = 0
        for (direction, amount) in self.instructions:
            cnt += SecretEntrance._calc_count_v2(n=n, direction=direction, amount=amount)

            n = (n + (SecretEntrance.DIRECTION[direction]*amount)) % SecretEntrance.SAFE_COMBINATIONS
        return cnt

    def display_results(self):
        print(f'Answer 1: {self. calc_part1()}')
        print(f'Answer 2: {self. calc_part2()}')