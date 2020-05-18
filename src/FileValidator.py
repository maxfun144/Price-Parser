from CustomExceptions.InvalidDataFileException import InvalidDataFileException
from CustomExceptions.InvalidTableCellNumberException import InvalidTableCellNumberException
from src.TableCellHelper import TableCellHelper


class FileValidator:

    @staticmethod
    def checkDataFilesForCorrectness(diapasons: list, numberOfDiapasonsFields: int, diapasonsFilePath: str,
                                     firms: dict, numberOfFirmsFields: int, firmsFilePath: str) -> str:
        errors = ""
        lineNumber = 0
        for line in diapasons:
            lineNumber += 1
            if len(line) != numberOfDiapasonsFields:
                errors += \
                    "\nIncorrect number of fields in the line: '{}'."\
                    "\n    Expected: '{}'."\
                    "\n    Found: '{}'."\
                    "\n    File: '{}'"\
                    "\n    Line number: '{}'."\
                        .format(" ".join(line), numberOfDiapasonsFields, len(line), diapasonsFilePath, lineNumber)
                continue
            try:
                FileValidator.checkDiapasonForCorrectness(line[0], line[1])
                FileValidator.checkDiapasonForCorrectness(line[2], line[3])
            except InvalidDataFileException as e:
                errors += \
                    "{} "\
                    "\n    File: '{}'"\
                    "\n    Line number: '{}'."\
                        .format(e, diapasonsFilePath, lineNumber)

            if not (line[4] in firms.keys()):
                errors += \
                    "\nCan't find firm '{}'."\
                    "\n    File: '{}'"\
                    "\n    Line number: '{}'."\
                    .format(line[4], diapasonsFilePath, lineNumber)
        # lineNumber = 0
        # for line in firms:
        #     lineNumber += 1
        #     if len(line) != numberOfFirmsFields:
        #         errors += \
        #             "\nIncorrect number of fields in the line: '{}'."\
        #             "\n    Expected: '{}'."\
        #             "\n    Found: '{}'."\
        #             "\n    File: {}"\
        #             "\n    Line number: {}."\
        #             .format(" ".join(line), numberOfFirmsFields, len(line), firmsFilePath, lineNumber)
        if errors:
            raise InvalidDataFileException(errors)


    @staticmethod
    def checkDiapasonForCorrectness(tableCellStart, tableCellEnd):

        try:
            TableCellHelper.checkTableCellNumberForCorrectness(tableCellStart)
            TableCellHelper.checkTableCellNumberForCorrectness(tableCellEnd)
        except InvalidTableCellNumberException as e:
            raise InvalidDataFileException(e)

        if ((TableCellHelper.getRowNumberDecimal(tableCellStart) != TableCellHelper.getRowNumberDecimal(
                tableCellEnd) and
             TableCellHelper.getColumnNumberDecimal(tableCellStart) != TableCellHelper.getColumnNumberDecimal(
                    tableCellEnd)) or
                TableCellHelper.getRowNumberDecimal(tableCellStart) > TableCellHelper.getRowNumberDecimal(
                    tableCellEnd) or
                TableCellHelper.getColumnNumberDecimal(tableCellStart) > TableCellHelper.getColumnNumberDecimal(
                    tableCellEnd)):
            raise InvalidDataFileException("\nInvalid diapason: '{}:{}'.".format(tableCellStart, tableCellEnd))
