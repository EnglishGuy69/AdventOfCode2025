from bisect import bisect

class Cafeteria:
    def __init__(self, filepath: str):
        self.fresh_ranges = []
        self.food = []

        self._load_file(filepath)
        self._merge_ranges()

    def _load_file(self, filepath: str):
        '''
        Assumes a file with a set of ranges, followed by a blank line, followed by a list of food IDs, e.g.

        10-20
        15-25
        30-40
                        <- blank line
        1
        12
        28
        35
        45

        Args:
            filepath: The path to the data file to be loaded

        Returns:

        '''
        load_state='RANGES'
        with open(filepath, 'r') as f:
            for line in f.readlines():
                if load_state == 'RANGES':
                    if line.strip() == '':
                        load_state='FOOD'
                    else:
                        (range_start, range_end) = tuple(line.strip().split('-'))
                        self.fresh_ranges.append((int(range_start), int(range_end)))
                else:
                    self.food.append(int(line.strip()))

    def _sort_ranges(self) -> None:
        '''
        Sort the ranges by creating a sort key that consists of the from and to numbers concatenated, but each number
        has to be zero-padded to ensure they are truly in order (e.g. 10|5 vs 10|05 yield different results).

        Returns: None

        '''
        m = len(str(max([n[1] for n in self.fresh_ranges])))  # length of longest number

        self.fresh_ranges = sorted(self.fresh_ranges, key=lambda x: f'{str(x[0]).zfill(m)}|{str(x[1]).zfill(m)})')

    def _merge_ranges(self) -> None:
        '''
        This function works backwards from the highest range to the lowest (after sorting) and merges any ranges
        that overlap. So if range N overlaps range N-1, range N-1 is updated to incorporate the range N, then N
        is removed. This ensures that at the end, the list of ranges is a sorted, non-overlapping list of ranges.

        Returns: None

        '''

        self._sort_ranges()


        for i in reversed(range(0, len(self.fresh_ranges)-1)):  # Reminder, use -1 as end stop to ensure 0 is included
            (r0_min, r0_max) = self.fresh_ranges[i]
            (r1_min, r1_max) = self.fresh_ranges[i+1]

            assert r0_min <= r1_min

            if r1_min <= r0_max+1:  # Must be +1 to merge 10-20 and 21-30
                self.fresh_ranges[i] = (min(r0_min, r1_min), max(r0_max, r1_max))
                self.fresh_ranges = self.fresh_ranges[:i+1] + self.fresh_ranges[i+2:]

    def _is_fresh(self, id: int) -> bool:
        '''
        This function assumes that the ranges are sorted and non-overlapping. The bisect() function will find the
        position just after the range that starts below the food ID. We then check whether that range expands upwards
        to include the id.

        Args:
            n: the ID for the food to check for freshness

        Returns: True if the food is on a range or False otherwise

        '''
        p = bisect([r[0] for r in self.fresh_ranges], id)
        if p == 0:
            return False

        (i0, i1) = self.fresh_ranges[p - 1]

        return i0 <= id <= i1

    @property
    def all_ranges(self):
        return [(x[0], x[1], x[1]-x[0]+1) for x in self.fresh_ranges]

    def answer1(self):
        return sum([1 if self._is_fresh(id) else 0 for id in self.food])

    def answer2(self):
        return sum([r[1]-r[0]+1 for r in self.fresh_ranges])

if __name__ == '__main__':
    test_cafe = Cafeteria('test.txt')
    print(f'Test Answer 1: {test_cafe.answer1()}')
    print(f'Test Answer 2: {test_cafe.answer2()}')

    cafe = Cafeteria('data.txt')
    print(f'Answer 1: {cafe.answer1()}')
    print(f'Answer 2: {cafe.answer2()}')
