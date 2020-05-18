from openpyxl import load_workbook
import requests
from bs4 import BeautifulSoup
import re

from requests.exceptions import InvalidSchema, MissingSchema, ConnectionError

from src.TableCellHelper import TableCellHelper
from CustomExceptions.InvalidKeywordException import InvalidKeywordException
from CustomExceptions.InvalidLinkException import InvalidLinkException


class ExcelManager:
    def __init__(self, filePath):
        self.filePath = filePath  # Excel file we work with
        try:
            self.workbook = load_workbook(filename=filePath)
        except FileNotFoundError:
            raise FileNotFoundError("\nThe file '{}' doesn't exist.".format(filePath))
        # self.sheet = self.workbook.get_sheet_by_name('Parsed sheet')
        self.sheet = self.workbook.active
        self.ignoreSymbols = [""]
        # print("Active table sheet: ", self.workbook.active.title)

    def save(self):
        self.workbook.save(filename=self.filePath)

    def readFromTableCell(self, tableCellNumber: str):
        return self.sheet[tableCellNumber].value

    def writeToTableCell(self, tableCellNumber: str, valueToWrite: str):
        self.sheet[tableCellNumber] = valueToWrite

    """
    throws 'InvalidKeywordException'
    throws 'InvalidLinkException'
    """

    @staticmethod
    def getPrice(url: str, keywords: str):

        try:
            page = requests.get(url)
        except (InvalidSchema, MissingSchema, ConnectionError) as e:
            raise InvalidLinkException("\nIncorrect link: '{}'.".format(url))

        if page.status_code != 200:
            raise InvalidLinkException("\nIncorrect link: '{}'.".format(url))

        soup = BeautifulSoup(page.content, "html.parser")
        args = []
        keywords = keywords.split("+")

        for i in range(len(keywords)):
            try:
                args = list(map(lambda x: re.findall(r"[^\'\"]+", x)[0], keywords[i].split("=")))
            except IndexError:
                if len(args) != 2:
                    raise InvalidKeywordException("\nIncorrect keyword format: '{}'.".format(keywords[i]))

            if args[0] == "class":
                soup = soup.find_all(lambda tag: (tag.get('class') == args[1].split(" ") or tag.get('class') == args[
                    1]) and tag.text.strip() != "")  # and tag.text != "")
            elif args[0] == "id":
                soup = soup.find_all(lambda tag: (tag.get('id') == args[1].split(" ") or tag.get('id') == args[
                    1]) and tag.text.strip() != "")
            elif args[0] == "itemprop":
                soup = soup.find_all(lambda tag: (tag.get('itemprop') == args[1].split(" ") or tag.get('itemprop') ==
                                                  args[1]) and tag.text.strip() != "")
            else:
                soup = []

            if len(soup) == 0:
                raise InvalidKeywordException(
                    "\nIncorrect keyword (no element with such keyword on the web-page)\nWeb-page: '{}'.\nKeyword: '{}'.".format(
                        url, keywords[i]))

            soup = soup[0]

        return re.findall(r"[\d ]+", soup.text)[0].replace(" ", "")


    def updateTableCellsPair(self, tableCellWithLink, tableCellWithPrice, keyword):
        link = str(self.readFromTableCell(tableCellWithLink))

        if link in self.ignoreSymbols:
            return

        if not (re.match(r"https?://", link)):
            self.writeToTableCell(tableCellWithPrice, "**Error")
            raise InvalidLinkException("\nIncorrect link: '{}'.".format(link))

        try:
            self.writeToTableCell(tableCellWithPrice, self.getPrice(link, keyword))
        except InvalidLinkException as e:
            self.writeToTableCell(tableCellWithPrice, "**Error")
            raise InvalidLinkException(e)
        except InvalidKeywordException as e:
            self.writeToTableCell(tableCellWithPrice, "**Error")
            raise InvalidKeywordException(e)

        return


    def updateTableCellsDiapason(self, tableCellsWithLinksDiapason: list, tableCellsWithPricesDiapason: list, keyword: str) -> str:

        errors = ""

        tableCellWithLinkStart = tableCellsWithLinksDiapason[0]
        tableCellWithLinkEnd = tableCellsWithLinksDiapason[1]
        tableCellWithPriceStart = tableCellsWithPricesDiapason[0]
        tableCellWithPriceEnd = tableCellsWithPricesDiapason[1]

        if self.diapasonGoesRight(tableCellWithLinkStart, tableCellWithLinkEnd):
            for i in range(TableCellHelper.getColumnNumberDecimal(tableCellWithLinkStart),
                           TableCellHelper.getColumnNumberDecimal(tableCellWithLinkEnd) + 1):
                try:
                    self.updateTableCellsPair(tableCellWithLinkStart, tableCellWithPriceStart, keyword)
                except (InvalidLinkException, InvalidKeywordException) as e:
                    errors += "{}\n    Cell number: '{}' --> '{}' (**Error)".format(str(e), tableCellWithLinkStart,
                                                                                    tableCellWithPriceStart)

                tableCellWithLinkStart = TableCellHelper.incColumnNumber(tableCellWithLinkStart)
                if self.diapasonGoesRight(tableCellWithPriceStart, tableCellWithPriceEnd):
                    tableCellWithPriceStart = TableCellHelper.incColumnNumber(tableCellWithPriceStart)
                elif self.diapasonGoesDown(tableCellWithPriceStart, tableCellWithPriceEnd):
                    tableCellWithPriceStart = TableCellHelper.incRowNumber(tableCellWithPriceStart)


        elif self.diapasonGoesDown(tableCellWithLinkStart, tableCellWithLinkEnd):
            for i in range(TableCellHelper.getRowNumberDecimal(tableCellWithLinkStart),
                           TableCellHelper.getRowNumberDecimal(tableCellWithLinkEnd) + 1):

                try:
                    self.updateTableCellsPair(tableCellWithLinkStart, tableCellWithPriceStart, keyword)
                except (InvalidLinkException, InvalidKeywordException) as e:
                    errors += "{}\n    Cell number: '{}' --> '{}' (**Error)".format(str(e), tableCellWithLinkStart,
                                                                                    tableCellWithPriceStart)

                tableCellWithLinkStart = TableCellHelper.incRowNumber(tableCellWithLinkStart)
                if self.diapasonGoesDown(tableCellWithPriceStart, tableCellWithPriceEnd):
                    tableCellWithPriceStart = TableCellHelper.incRowNumber(tableCellWithPriceStart)
                elif self.diapasonGoesRight(tableCellWithPriceStart, tableCellWithPriceEnd):
                    tableCellWithPriceStart = TableCellHelper.incColumnNumber(tableCellWithPriceStart)

        return errors
    # tableCellsRangeLink = ["A1", "A4"]
    # tableCellsRangePrices = ["B1", "B4"]
    # keywords = "class=j-product__price__current price"
    # filePath = "hello_world.xlsx"
    #
    # doEverything(tableCellsRangeLink, tableCellsRangePrices, keywords, filePath)

    def updateExcel(self, diapasons, firms):

        errors = ""
        # self.checkDataFilesForCorrectness(diapasons, firms)

        for diapason in diapasons:
            localErrors = self.updateTableCellsDiapason(diapason[:2], diapason[2:4], firms[diapason[4]])
            if localErrors:
                errors += "\n\n------Diapason: '{}'{}".format(":".join(diapason[:2]), localErrors)

        self.save()

        if errors:
            raise InvalidLinkException(errors)


    def diapasonGoesRight(self, tableCellStart, tableCellEnd):
        return TableCellHelper.getRowNumberDecimal(tableCellStart) == TableCellHelper.getRowNumberDecimal(tableCellEnd)


    def diapasonGoesDown(self, tableCellStart, tableCellEnd):
        return TableCellHelper.getColumnNumberDecimal(tableCellStart) == TableCellHelper.getColumnNumberDecimal(
            tableCellEnd)
