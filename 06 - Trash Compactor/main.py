'''
    Author: Guy Pickering
    Date: Dec 6, 2025

    Part 1:
    Read the numbers above each operator and then calculate the sum or product of those numbers and add them up.

    Part 2:
    Read the numbers vertically above each operator and then calculate the sum or product of those numbers and add them
    up.
'''

import re
from io import TextIOWrapper


class TrashCompactorPart1:
    OPERATORS=['*','+']

    def __init__(self, filepath: str):
        self.numbers = []
        self.operators = []

        with open(filepath, 'r') as f:
            self._read_file(f)

    def _read_file(self, f: TextIOWrapper):
        '''
        This function reads each line of the file and splits the row into fields by removing any multiple spaces
        and then splitting into tokens. All rows not container an operator ('*' or '+') get added to the
        'numbers' list (of lists) while the operators are put in the 'operators' list.
        
        
        Args:
            f: The file handle to be read

        Returns: None (updates self.numbers and self.operators)

        '''
        for line in f.readlines():
            line = line.strip()
            tokens = re.sub(r'\s+', ' ', line).split(' ')

            if line[0] in TrashCompactorPart1.OPERATORS:
                self.operators = tokens
            else:
                self.numbers.append([int(x) for x in tokens])

        # Validate that each row of numbers contains the same number of numbers as there are operators...
        for n in self.numbers:
            assert len(n) == len(self.operators)


    def _operate(self, t: int, x: int, op: str) -> int:
        '''

        Args:
            t: the total
            x: the new number to be added/multiplied by the total
            op: operator '*' or '+'

        Returns:

        '''
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
            self._read_file(f)

    def _read_file(self, f):
        lines = []

        # Read _all_ lines into an array
        for line in f.readlines():
            lines.append(line.strip('\n'))

        # extract the operators and numbers lines into variables
        ops = lines[len(lines)-1]
        numbers = lines[:-1]

        found_numbers = []
        while numbers[0]:   # For each vertical slice of data in the incoming file...
            # Append each operator to the self.operators array when we find them.
            if len(ops) > 0 and ops[0] in TrashCompactorPart2.OPERATORS:
                self.operators.append(ops[0])

            # extract a slice of numbers (and/or spaces) from the incoming numbers lines
            s = ''
            for n in numbers:
                if len(n) > 0:
                    s += n[0]

            # If the full slice is spaces, we can close out the numbers and add to the self.numbers
            if s.strip() == '':
                self.numbers.append(found_numbers)
                found_numbers = []
            else:
                found_numbers.append(int(s.strip()))

            # Remove the first character (vertical slice) from each line
            numbers = [l[1:] for l in numbers]
            ops = ops[1:] if len(ops) > 0 else ''

        # Close out any remaining numbers
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
