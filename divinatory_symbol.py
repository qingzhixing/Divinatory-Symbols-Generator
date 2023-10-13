from enum import Enum
import random
import string

# 爻


class TrigramLine(Enum):
    SHAO_YANG = 0
    SHAO_YIN = 1
    LAO_YANG = 2
    LAO_YIN = 3
    EMPTY = 4

    def isYang(singleLine) -> bool:
        return singleLine % 2 == 0

    def intToTrigramLine(intNum):
        match intNum:
            case 6:
                return TrigramLine.LAO_YIN
            case 7:
                return TrigramLine.SHAO_YANG
            case 8:
                return TrigramLine.SHAO_YIN
            case 9:
                return TrigramLine.LAO_YANG
            case _:
                return TrigramLine.EMPTY

    def trigramLineToString(singleLine) -> string:
        match singleLine:
            case TrigramLine.SHAO_YANG:
                return "少阳"
            case TrigramLine.SHAO_YIN:
                return "少阴"
            case TrigramLine.LAO_YANG:
                return "老阳"
            case TrigramLine.LAO_YIN:
                return "老阴"
            case TrigramLine.EMPTY:
                return "空"
            case _:
                return "(Unknown)"
# 卦象


class DivinatorySymbol:
    trigramLines = list()

    def __init__(self) -> None:
        self.trigramLines = [
            TrigramLine.EMPTY,
            TrigramLine.EMPTY,
            TrigramLine.EMPTY,
            TrigramLine.EMPTY,
            TrigramLine.EMPTY,
            TrigramLine.EMPTY
        ]

    def generateTrigramLines(self):
        for index in range(6):
            rand = random.randint(6, 9)
            self.trigramLines[6 - index -
                              1] = TrigramLine.intToTrigramLine(rand)

    def _debugPrintConsole(self):
        for index, element in enumerate(self.trigramLines):
            print(f"{index}: {element} - {TrigramLine.trigramLineToString(element)}")
