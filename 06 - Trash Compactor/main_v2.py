import math
from typing import List
import re

class HomeworkQuestion:
    def __init__(self, operator: str):
        self.operator = operator
        self.numbers = []

    def append_number(self, n: int):
        self.numbers.append(n)

    def calculate(self):
        if self.operator == '*':
            return math.prod(self.numbers)
        elif self.operator == '+':
            return sum(self.numbers)
        else:
            raise NotImplementedError(f'Operator must be + or *, not {self.operator}')

    def __str__(self):
        return self.operator + '[' + ','.join([str(n) for n in self.numbers]) + ']'


class TrashCompactor:
    def __init__(self, filepath: str):
        self.questions: List[HomeworkQuestion] = []

        with open(filepath, 'r') as f:
            self._load(f)

    def _load(self, f):
        lines = list(f.readlines())
        lines = [l.strip('\n') for l in lines]

        operators = re.sub(r'\s+',' ', lines[-1]).split(' ')
        for operator in operators:
            self.questions.append(HomeworkQuestion(operator))

        self._extract_data(lines[:-1])

    def _extract_data(self, lines: List[str]):
        raise NotImplementedError('Override in derived class')

    def answer(self) -> int:
        return sum([q.calculate() for q in self.questions])


class TrashCompactorPart1(TrashCompactor):
    def __init__(self, filepath: str):
        super().__init__(filepath)

    def _extract_data(self, lines: List[str]) -> None:
        '''
        This function splits each line based on the spaces between the digits and adds each number to the
        question. The mapping from number to question is horizontally based.

        Args:
            lines: lines of digits and spaces

        Returns: None
        '''
        for line in lines:
            numbers = re.sub(r'\s+',' ', line.strip()).split(' ')
            for i, s_number in enumerate(numbers):
                if s_number.strip() != '':
                    self.questions[i].append_number(int(s_number))


class TrashCompactorPart2(TrashCompactorPart1):
    def __init__(self, filepath: str):
        super().__init__(filepath)

    def _extract_data(self, lines: List[str]) -> None:
        '''
        This function strips off the numbers vertically, stripe by stripe. When all spaces is detected, we move
        to the next question. Each vertical number is added to the same question until 'all spaces' is detected.

        Args:
            lines: lines of digits and spaces

        Returns:

        '''
        q = 0
        while len(lines[0]) > 0:
            s = ''
            for i, line in enumerate(lines):
                if len(line) > 0:
                    s += line[0]
                    lines[i] = lines[i][1:]

            if s.strip() == '':
                q += 1
            else:
                self.questions[q].append_number(int(s))

        pass

if __name__ == '__main__':
    test_compactor_1 = TrashCompactorPart1('test.txt')
    print(f'Test Answer 1: {test_compactor_1.answer()}')

    test_compactor_2 = TrashCompactorPart2('test.txt')
    print(f'Test Answer 2: {test_compactor_2.answer()}')

    compactor_1 = TrashCompactorPart1('data.txt')
    print(f'Answer 1: {compactor_1.answer()}')

    compactor_2 = TrashCompactorPart2('data.txt')
    print(f'Answer 2: {compactor_2.answer()}')
