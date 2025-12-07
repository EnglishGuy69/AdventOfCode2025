f'''
    Author: Guy Pickering
    Date: Dec 3, 2025

    Part 1:
    Find the largest 'joltage' using 2 digits - the largest 2 digits of each number in the list - left to right.
    
    Part 2:
    Find the largest 'joltage' using 12 digits - the largest 12 digits of each number in the list - left to right.
'''

from typing import List, Tuple

class Lobby:
    def __init__(self, filepath: str):
        self.banks = []

        with open(filepath, 'r') as f:
            self.banks = [[int(b) for b in l.strip()] for l in f.readlines() if l.strip() != '']

    @staticmethod
    def _find_largest_digit(digit_list: List[int]) -> Tuple[int, int]:
        '''
        This function looks through the list of integers and finds the largest number (and its position). This may
        be called with only portions of a bank.

        Args:
            digit_list: list of integers

        Returns: (digit, position

        '''
        found_digit = found_position = None
        for a_position, a_digit in enumerate(digit_list):
            if a_digit == 9:  # If we find a 9, that is the best we can do...return
                return a_digit, a_position
            elif found_digit is None or a_digit > found_digit:
                found_digit = a_digit
                found_position = a_position

        return found_digit, found_position


    def find_largest_joltage(self, digit_list: List[int], num_digits: int=2) -> int:
        '''
        This is a recursive function that looks for the largest 'n' digits based on the num_digits argument. It will
        start at the left and look for the largest number, with the constraint that there must be enough digits
        remaining to the right to support num_digits. If there are only num_digits left to the right, it must pick
        up the first digit in the (sub-)bank.

        Args:
            digit_list: a full (or partial) bank of integers
            num_digits: The number of remaining digits to find

        Returns: The maximum joltage for the bank

        '''
        if num_digits == 1:
            digit, position = Lobby._find_largest_digit(digit_list)
            return digit
        else:
            digit, position = Lobby._find_largest_digit(digit_list[:-(num_digits - 1)])
            remaining_digits = self.find_largest_joltage(digit_list[position + 1:], num_digits - 1)

            joltage = int(f'{digit}{remaining_digits}')

            return joltage

    def answer1(self):
        return sum([self.find_largest_joltage(bank) for bank in self.banks])


    def answer2(self):
        return sum([self.find_largest_joltage(bank, 12) for bank in self.banks])


if __name__ == '__main__':
    lobby_test = Lobby('test.txt')
    print(f'Test Answer 1: {lobby_test.answer1()}')
    print(f'Test Answer 2: {lobby_test.answer2()}')


    lobby = Lobby('data.txt')
    print(f'Answer 1: {lobby.answer1()}')
    print(f'Answer 2: {lobby.answer2()}')
