f'''
    Author: Guy Pickering
    Date: Dec 2, 2025

    Part 1:
    Count the number of invalid IDs in the ranges that have repeating patterns, e.g. 11, 22, 123123, etc.

    Part 2:
    Count the number of invalid IDs in the ranges that have 2 or more repeating patters, e.g. 121212.
'''
from typing import Set, List, Optional

class GiftShop:
    def __init__(self, filepath: str):
        self.ranges = []
        with open(filepath, 'r') as f:
            self.ranges = [[int(v) for v in x.split('-')] for x in f.readline().strip().split(',')]

    def _generate_equal_length_ranges(self, r, allow_odd: bool) -> List[Optional[List[int,int]]]:
        '''
        This function takes a range (e.g. 10->2050) and generates a series of ranges where the length of the
        start and end are equal

        Args:
            r: range [x,y] when len(y) >= len(x) and y > x
            allow_odd: will generate either odd+event, or only event

        Returns:

        '''
        start = r[0]
        end = r[1]
        len0 = len(str(start))
        len1 = len(str(end))

        l = len0
        ranges = []
        n0 = start
        n1 = min(end, int('9' * l))
        while True:
            if len(str(n1)) % 2 == 0 or allow_odd:
                ranges.append((n0, n1))

            l += 1
            if l > len1:
                break

            n0 = n1 + 1
            n1 = min(end, int('9' * l))

        return ranges

    def _find_invalid_id(self, r0: int, r1: int, split_by: int):
        if split_by > len(str(r0)):
            return set()

        if len(str(r0)) % split_by != 0:
            return set()

        matches = set()
        l = len(str(r0))

        lh = l // split_by

        rr0 = int(str(r0)[:lh])
        rr1 = int(str(r1)[:lh])

        for x in range(rr0, rr1+1):
            xx = int(str(x)*split_by)
            if xx > r1:
                break
            elif xx >= r0:
                matches.add(xx)

        return matches

    def _answer(self, allow_odd: bool, split_by: int):
        matches = set()

        for r in self.ranges:
            possible_ranges = self._generate_equal_length_ranges(r, allow_odd=allow_odd)

            for (r0, r1) in possible_ranges:
                matches |= self._find_invalid_id(r0, r1, split_by=split_by)

        return matches


    def _max_range_length(self):
        return max([len(str(x[1])) for x in self.ranges])

    def answer1(self):
        return sum(self._answer(allow_odd=False, split_by=2))

    def answer2(self):
        max_range_length = self._max_range_length()

        matches = set()
        for l in range(2, max_range_length):
            matches |= self._answer(allow_odd=True, split_by=l)

        return sum(matches)

if __name__ == '__main__':
    gs_test = GiftShop('test.txt')
    print(f'Test Answer 1: {gs_test.answer1()}')
    print(f'Test Answer 2: {gs_test.answer2()}')

    gs1 = GiftShop('data.txt')
    print(f'Answer 1: {gs1.answer1()}')
    print(f'Answer 2: {gs1.answer2()}')
