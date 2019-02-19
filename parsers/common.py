import numpy as np
import re


class HcParser():

    _REGEX_NUM = r'-?\d+(?:\.\d+)?'
    _REGEX_CHR = r'[A-Za-z]'

    def __init__(self, file_name):
        with open(file_name, 'r') as fd:
            self.lines = [line.rstrip('\n') for line in fd]

    def _extract_floats(self, line):
        return [float(n) for n in re.findall(self._REGEX_NUM, line)]

    def _extract_ints(self, line):
        return [int(n) for n in re.findall(self._REGEX_NUM, line)]

    # extracts all alphabet chars
    def _extract_chars(self, line):
        return re.findall(self._REGEX_CHR, line)

    def to_list(self, index, transform=_extract_ints):
        return transform(self, self.lines[index])

    def to_matrix(self, start_row, end_row, transform=_extract_chars):
        arr = []
        for l in self.lines[start_row:end_row + 1]:
            arr.append(transform(self, l))
        return np.array(arr)
