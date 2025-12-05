
class PrintingDepartmentMap:
    PAPER_ROLL='@'
    SPACE='.'
    MAX_ALLOWED_ROLLS = 4

    def __init__(self, filepath: str):
        super().__init__()

        with open(filepath, 'r') as f:
            self.map = [l.strip() for l in f.readlines() if l.strip() != '']

        self.width = len(self.map[0])
        self.height = len(self.map)

    def _can_move_paper_roll(self, x: int, y: int) -> bool:
        '''
        The problem states that only roles that have <4 rolls in the 8 squares
        around them can be moved. This looks at the (up to) 8 squares and counts
        the rolls and returns True if the count <4.

        Args:
            x: Position of the roll on the map
            y: Position of the roll on the map

        Returns: True if there is a roll and it has <4 rolls around it

        '''
        if self.map[y][x] != PrintingDepartmentMap.PAPER_ROLL:
            return False

        top = max(y-1, 0)
        left = max(x-1, 0)
        bottom = min(y+1, self.height-1)
        right = min(x+1, self.width-1)

        cnt =  sum([1 if self.map[yy][xx] == PrintingDepartmentMap.PAPER_ROLL and \
                              not (xx == x and yy == y)
                    else 0
                    for yy in range(top, bottom+1)
                    for xx in range(left, right+1)])


        return cnt < PrintingDepartmentMap.MAX_ALLOWED_ROLLS

    def answer1(self):
        return sum([1 if self._can_move_paper_roll(x,y) else 0
                      for y in range(0, self.width)
                      for x in range(0, self.height)])

    def answer2(self):
        total_cnt = 0

        cnt=None
        while cnt is None or cnt > 0:
            cnt = 0

            for y in range(0, self.height):
                for x in range(0, self.width):
                    if self._can_move_paper_roll(x,y):
                        # Replace character at [x,y]
                        self.map[y] = self.map[y][:x] + PrintingDepartmentMap.SPACE + self.map[y][x+1:]

                        cnt += 1

            total_cnt += cnt

        return total_cnt


if __name__ == '__main__':
    test_map = PrintingDepartmentMap('test.txt')
    print(f'Test Answer 1: {test_map.answer1()}')
    print(f'Test Answer 2: {test_map.answer2()}')
    test_map.answer2()

    map = PrintingDepartmentMap('data.txt')
    print(f'Answer 1: {map.answer1()}')
    print(f'Answer 2: {map.answer2()}')
