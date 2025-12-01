from math import floor

class SecretEntrance:
    SAFE_COMBINATIONS=100
    INITIAL_NUMBER=50
    def __init__(self, filepath: str):
        self.instructions: (str, int) = []
        with open(filepath, 'r') as f:
            for line in f.readlines():
                if len(line.strip()) == 0:
                    continue
                direction = line[0]
                amount = int(line.strip()[1:])
                self.instructions.append((direction, amount))

    def calc_zeros(self):
        n = SecretEntrance.INITIAL_NUMBER
        cnt = 0
        for (direction, amount) in self.instructions:
            m = 1 if direction == 'R' else -1
            n = (n + (m*amount)) % SecretEntrance.SAFE_COMBINATIONS
            if n == 0:
               cnt += 1
        return cnt

    def _calc_count_v2(self, n: int, direction: str, amount: int) -> int:
        if direction == 'R':
            return floor((n + amount) // SecretEntrance.SAFE_COMBINATIONS)
        else:
            return floor(((SecretEntrance.SAFE_COMBINATIONS - n) % SecretEntrance.SAFE_COMBINATIONS + amount) // SecretEntrance.SAFE_COMBINATIONS)

    def calc_zeros_v2(self):
        n = SecretEntrance.INITIAL_NUMBER
        cnt = 0
        for (direction, amount) in self.instructions:
            m = 1 if direction == 'R' else -1
            cnt += self._calc_count_v2(n=n, direction=direction, amount=amount)

            n = (n + (m*amount)) % SecretEntrance.SAFE_COMBINATIONS
        return cnt

if __name__ == '__main__':
    test1 = SecretEntrance('./test.txt')
    assert test1.calc_zeros() == 3
    assert test1.calc_zeros_v2() == 6

    part1 = SecretEntrance('./data.txt')
    print(f'Part 1: {part1.calc_zeros()}')

    part2 = SecretEntrance('./data.txt')
    assert part2._calc_count_v2(50, 'R', 50) == 1
    assert part2._calc_count_v2(50, 'L', 50) == 1
    assert part2._calc_count_v2(50, 'R', 150) == 2
    assert part2._calc_count_v2(5, 'L', 5) == 1
    assert part2._calc_count_v2(5, 'L', 10) == 1
    assert part2._calc_count_v2(5, 'L', 105) == 2
    assert part2._calc_count_v2(50, 'L', 1000) == 10

    print(f'Part 2: {part2.calc_zeros_v2()}')
