import re

class TrashCompactorPart1:
    OPERATORS=['*','+']

    def __init__(self, filepath: str):
        self.numbers = []
        self.operators = []

        with open(filepath, 'r') as f:
            self._read_file_part_1(f)

    def _read_file_part_1(self, f):
        for line in f.readlines():
            line = line.strip()
            if line[0] in TrashCompactorPart1.OPERATORS:
                self.operators = re.sub(r'\s+', ' ', line).split(' ')
            else:
                self.numbers.append([int(x) for x in re.sub(r'\s+', ' ', line).split(' ')])

        for n in self.numbers:
            assert len(n) == len(self.operators)


    def _operate(self, t: int, x: int, op: str):
        if op == '*':
            return t * x
        elif op == '+':
            return t + x
        else:
            raise NotImplementedError(f'Operator {op} not supported')

    def answer1(self):
        ret = 0
        for i, op in enumerate(self.operators):
            t = 1 if op == '*' else 0

            for n in self.numbers:
                t = self._operate(t, n[i], op)

            ret += t

        return ret


class TrashCompactorPart2:
    OPERATORS=['*','+']

    def __init__(self, filepath: str):
        self.numbers = []
        self.operators = []

        with open(filepath, 'r') as f:
            self._read_file_part_2(f)

    def _read_file_part_2(self, f):
        lines = []

        for line in f.readlines():
            lines.append(line.strip('\n'))

        ops = lines[len(lines)-1]
        numbers = lines[:-1]

        found_numbers = []
        while numbers[0]:
            if len(ops) > 0 and ops[0] in TrashCompactorPart2.OPERATORS:
                self.operators.append(ops[0])

            s = ''
            for n in numbers:
                if len(n) > 0:
                    s += n[0]

            if s.strip() == '':
                self.numbers.append(found_numbers)
                found_numbers = []
            else:
                found_numbers.append(int(s.strip()))

            numbers = [l[1:] for l in numbers]
            ops = ops[1:] if len(ops) > 0 else ''

        if found_numbers:
            self.numbers.append(found_numbers)

    def _operate(self, t: int, x: int, op: str):
        if op == '*':
            return t * x
        elif op == '+':
            return t + x
        else:
            raise NotImplementedError(f'Operator {op} not supported')

    def answer2(self):
        ret = 0
        for i, op in enumerate(self.operators):
            t = 1 if op == '*' else 0

            for n in self.numbers[i]:
                t = self._operate(t, n, op)

            ret += t

        return ret

if __name__ == '__main__':
    test_compactor_1 = TrashCompactorPart1('test.txt')
    print(f'Test Answer 1: {test_compactor_1.answer1()}')

    test_compactor_2 = TrashCompactorPart2('test.txt')
    print(f'Test Answer 2: {test_compactor_2.answer2()}')

    compactor_1 = TrashCompactorPart1('data.txt')
    print(f'Answer 1: {compactor_1.answer1()}')

    compactor_2 = TrashCompactorPart2('data.txt')
    print(f'Answer 2: {compactor_2.answer2()}')
