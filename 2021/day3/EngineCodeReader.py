from collections import Counter
from typing import List


class EngineCodeReader:
    """Reads submarine engine diagnostics."""

    def __init__(self, codes: List[str]) -> None:
        self.codes = codes
        self.bitCounts = self._getBitCounts()

    def _getBitCounts(self) -> List[int]:
        bitCounts = {}
        for code in self.codes:
            bitPos = len(code) - 1
            for bit in code:
                if not bitCounts.get(bitPos):
                    bitCounts[bitPos] = {0: 0, 1: 0}
                if bit == '1':
                    bitCounts[bitPos][1] += 1
                else:
                    bitCounts[bitPos][0] += 1
                bitPos -= 1
        return bitCounts

    def getPowerConsumption(self) -> int:
        gamma = 0
        epsilon = 0
        i = len(self.bitCounts.keys()) - 1
        while i >= 0:
            gamma = gamma << 1
            epsilon = epsilon << 1
            if self.bitCounts[i][0] > self.bitCounts[i][1]:
                gamma ^= 0
                epsilon ^= 1
            else:
                gamma ^= 1
                epsilon ^= 0
            i -= 1
        return gamma * epsilon

    def getLifeSupportRating(self) -> int:
        """Adapted from https://www.reddit.com/r/adventofcode/comments/r7r0ff/comment/hn4gzr0/?utm_source=share&utm_medium=web2x&context=3"""
        oxygenCodes = self.codes[:]
        co2Codes = self.codes[:]

        for i in range(len(self.codes[0])):
            oxygenCounter = Counter([code[i] for code in oxygenCodes])
            co2Counter = Counter([code[i] for code in co2Codes])
            if len(oxygenCodes) > 1:
                if oxygenCounter['0'] > oxygenCounter['1']:
                    oxygenCodes = [
                        code for code in oxygenCodes if code[i] == '0']
                else:
                    oxygenCodes = [
                        code for code in oxygenCodes if code[i] == '1']
            if len(co2Codes) > 1:
                if co2Counter['0'] > co2Counter['1']:
                    co2Codes = [code for code in co2Codes if code[i] == '1']
                else:
                    co2Codes = [code for code in co2Codes if code[i] == '0']

        return int(oxygenCodes[0], 2) * int(co2Codes[0], 2)
