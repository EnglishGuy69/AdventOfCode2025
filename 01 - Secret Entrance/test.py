from main import SecretEntrance
from pathlib import Path

def validate(data_filepath: str, answer_filepath: str):
    if Path(answer_filepath).exists():
        with open(answer_filepath, 'r') as f:
            answer_1 = int(f.readline().strip())
            answer_2 = int(f.readline().strip())

            validator = SecretEntrance(data_filepath)
            assert validator.calc_part1() == answer_1
            assert validator.calc_part2() == answer_2

assert SecretEntrance._calc_count_v2(50, 'R', 50) == 1
assert SecretEntrance._calc_count_v2(50, 'L', 50) == 1
assert SecretEntrance._calc_count_v2(50, 'R', 150) == 2
assert SecretEntrance._calc_count_v2(5, 'L', 5) == 1
assert SecretEntrance._calc_count_v2(5, 'L', 10) == 1
assert SecretEntrance._calc_count_v2(5, 'L', 105) == 2
assert SecretEntrance._calc_count_v2(50, 'L', 1000) == 10

validate('./test.txt', './test_answer.txt')
validate('./data.txt', './answer.txt')

puzzle = SecretEntrance('./data.txt')
puzzle.display_results()
