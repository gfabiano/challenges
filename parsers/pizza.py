from .common import HcParser


class HcPizzaParser(HcParser):

    def extract_MT(self, line):
        return [1 if c == 'T' else 0
                for c in self._extract_chars(line)]



