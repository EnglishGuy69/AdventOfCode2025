'''
    Author: Guy Pickering
    Date: Dec 7, 2025

    Part 1:
    Identify the splitters that are hit by the beam that is coming down starting at the 'S' and which splits
    each time it hits a splitter ('^').

    Part 2:
    Identify the total number of 'timelines' or combonations of paths from the 'S' to the bottom through the various
    splitters.
'''

from typing import List, Dict, Optional


class Laboratories:
    SPLITTER='^'
    START='S'
    def __init__(self, filepath: str):
        self.start_row = None                   # The row where the 'S' exists
        self.start_col = None                   # The column where the 'S' exists
        self.splitters: List[List[int]] = []    # List of Lists of splitter columns
        self.width = None                       # The width of the input data grid (number of columns)

        with open(filepath, 'r') as f:
            for i, line in enumerate(f.readlines()):
                if self.width is None:
                    self.width = len(line)

                start_col = line.find(Laboratories.START)
                if start_col >= 0:
                    self.start_col = start_col
                    self.start_row = i
                else:
                    self.splitters.append([i for i, c in enumerate(line.strip()) if c == Laboratories.SPLITTER])

        # Remove any rows with no splitters
        self.splitters = [s
                          for s in self.splitters if len(s) > 0]

    def _split_beams(self, incoming_beam: int) -> List[int]:
        '''
        This function take an incoming beam, and assuming it has hit a splitter, calculate the outgoing beams
        that will be created by the splitter, accounting for splitters that are in the first or last column.

        Args:
            incoming_beam: The column (x coordinate) the parent beam starts in 

        Returns: An array of outgoing beams - can be 1 or 2 beams

        '''
        outgoing_beams = []

        if incoming_beam > 0:               # Split the beam left if we are not in the leftmost column
            outgoing_beams.append(incoming_beam - 1)

        if incoming_beam < self.width-1:    # Split the beam right if we are not in the rightmost column
            outgoing_beams.append(incoming_beam + 1)

        return outgoing_beams

    def answer1(self):
        beams = [self.start_col]

        num_splitters = 0
        for splitters in self.splitters:
            new_beams = beams  # Start with all parent beams passing through...
            remove_beams = []
            
            for incoming_beam in beams:
                if incoming_beam in splitters:
                    split_beams = self._split_beams(incoming_beam)

                    # Merge split_beams into new_beams, removing duplicates...
                    new_beams.extend(split_beams)
                    new_beams = list(set(new_beams))

                    # tag parent beam to be removed if it hit a splitter
                    if len(split_beams) > 0:
                        remove_beams.append(incoming_beam)
                        num_splitters += 1

            # Remove parent beams that have been tagged for removal due to split
            beams = sorted([b for b in new_beams if b not in remove_beams])

        return num_splitters

    def calc_combinations(self,
                          level: int,
                          incoming_beam: int,
                          result_cache: Optional[Dict]=None) -> int:
        '''

        Args:
            level: Row number from 0...num layers of splitters
            incoming_beam: Column (x coordinate) of the beam coming down
            result_cache: Pre-calculated combination count for 'level|column' beam

        Returns:

        '''

        if result_cache is None:  # Initial cache is empty
            result_cache = {}

        if level >= len(self.splitters): # If we exceed the bottom, assume combo of 1 for parent pbeam
            return 1

        # Internal function to calculate the number of child combinations, leveraging the cached result
        # if available or caching the recursive result if not.
        def calc_child_combinations(a_beam: int) -> int:
            if f'{level}|{a_beam}' in result_cache:
                return result_cache[f'{level}|{a_beam}']
            else:
                child_combos = self.calc_combinations(level + 1, a_beam, result_cache)
                result_cache[f'{level}|{a_beam}'] = child_combos
                return child_combos

        splitters = self.splitters[level]
        combinations = 0
        if incoming_beam in splitters:
            split_beams = self._split_beams(incoming_beam)

            combinations += sum([calc_child_combinations(beam) for beam in split_beams])
        else:   # Pass through the parent beam if it does not hit a splitter
                combinations += calc_child_combinations(incoming_beam)

        return combinations


    def answer2(self):
        start_beam = self.start_col
        return self.calc_combinations(level=0, incoming_beam=start_beam)

if __name__ == '__main__':
    test_lab = Laboratories('test.txt')
    print(f'Test Answer 1: {test_lab.answer1()}')
    print(f'Test Answer 2: {test_lab.answer2()}')

    lab = Laboratories('data.txt')
    print(f'Answer 1: {lab.answer1()}')
    print(f'Answer 2: {lab.answer2()}')

