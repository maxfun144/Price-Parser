import re

from CustomExceptions.InvalidTableCellNumberException import InvalidTableCellNumberException


class TableCellHelper:

    @staticmethod
    def checkTableCellNumberForCorrectness(tableCellNumber: str):
        if len(tableCellNumber) == 0 or \
                not (re.match(r"^[A-Z]+[0-9]+$", tableCellNumber)) or \
                re.match(r"^0", str(re.match(r"^[A-Z]+[0-9]+$", tableCellNumber))):
            raise InvalidTableCellNumberException("\nIncorrect table cell number: '{}'.".format(tableCellNumber))

    @staticmethod
    def columnNumberToDecimal(tableCellNumber: str) -> int:
        mappingDict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9,
                       "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
                       "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
        base = 26
        decimalNumber = 0
        length = len(tableCellNumber)
        for i in range(length):
            decimalNumber += mappingDict[tableCellNumber[length - 1 - i]] * base ** i

        return decimalNumber

    @staticmethod
    def decimalToColumnNumber(decimal: int) -> str:
        mappingDict = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I",
                       10: "J", 11: "K", 12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q",
                       18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z"}
        base = 26
        if (decimal <= base):
            return mappingDict[decimal]
        else:
            return TableCellHelper.decimalToColumnNumber(decimal // base) + mappingDict[decimal % base]

    @staticmethod
    def getRowNumber(tableCellNumber: str) -> int:

        TableCellHelper.checkTableCellNumberForCorrectness(tableCellNumber)

        return int(re.findall(r"\d+", tableCellNumber)[0])

    @staticmethod
    def getRowNumberDecimal(tableCellNumber: str) -> int:

        TableCellHelper.checkTableCellNumberForCorrectness(tableCellNumber)

        return TableCellHelper.getRowNumber(tableCellNumber)

    @staticmethod
    def getColumnNumber(tableCellNumber: str) -> str:

        TableCellHelper.checkTableCellNumberForCorrectness(tableCellNumber)

        return re.findall(r"\D+", tableCellNumber)[0]

    @staticmethod
    def getColumnNumberDecimal(tableCellNumber: str) -> int:

        TableCellHelper.checkTableCellNumberForCorrectness(tableCellNumber)

        return TableCellHelper.columnNumberToDecimal(re.findall(r"\D+", tableCellNumber)[0])

    @staticmethod
    def incColumnNumber(tableCellNumber: str) -> str:

        TableCellHelper.checkTableCellNumberForCorrectness(tableCellNumber)

        return TableCellHelper.decimalToColumnNumber(
            TableCellHelper.columnNumberToDecimal(TableCellHelper.getColumnNumber(tableCellNumber)) + 1) + str(
            TableCellHelper.getRowNumber(tableCellNumber))

    @staticmethod
    def addColumnNumber(tableCellNumber: str, decimal: int) -> str:

        TableCellHelper.checkTableCellNumberForCorrectness(tableCellNumber)

        return TableCellHelper.decimalToColumnNumber(
            TableCellHelper.columnNumberToDecimal(TableCellHelper.getColumnNumber(tableCellNumber)) + decimal) + str(
            TableCellHelper.getRowNumber(tableCellNumber))

    @staticmethod
    def incRowNumber(tableCellNumber: str) -> str:

        TableCellHelper.checkTableCellNumberForCorrectness(tableCellNumber)

        return TableCellHelper.getColumnNumber(tableCellNumber) + str(TableCellHelper.getRowNumber(tableCellNumber) + 1)

    @staticmethod
    def addRowNumber(tableCellNumber: str, decimal: int) -> str:

        TableCellHelper.checkTableCellNumberForCorrectness(tableCellNumber)

        return TableCellHelper.getColumnNumber(tableCellNumber) + str(
            TableCellHelper.getRowNumber(tableCellNumber) + decimal)
