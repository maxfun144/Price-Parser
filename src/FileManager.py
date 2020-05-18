class FileManager:

    separator = " "


    @staticmethod
    def readCSVto2DimensionalList(filePath: str, separator="separator"):
        if separator != "separator": FileManager.separator = separator
        try:
            with open(filePath, "r") as f:
                return list(map(lambda x: x.strip().split(FileManager.separator), f.readlines()))
        except FileNotFoundError:
            raise FileNotFoundError("\nThe file '{}' doesn't exist.".format(filePath))


    @staticmethod
    def readCSVtoList(filePath: str, separator="separator"):
        if separator != "separator": FileManager.separator = separator
        try:
            with open(filePath, "r") as f:
                return f.readlines()
        except FileNotFoundError:
            raise FileNotFoundError("\nThe file '{}' doesn't exist.".format(filePath))


    @staticmethod
    def readCSVtoDict(filePath: str, separator="separator"):
        if separator != "separator": FileManager.separator = separator
        try:
            with open(filePath, "r") as f:
                dic = {}
                for line in f.readlines():
                    line = line.strip().split(FileManager.separator, 1)
                    dic[line[0]] = line[1]
                return dic
        except FileNotFoundError:
            raise FileNotFoundError("\nThe file '{}' doesn't exist.".format(filePath))


    @staticmethod
    def writeCSV(filePath: str, data: list, separator="separator"):
        if separator != "separator": FileManager.separator = separator
        try:
            with open(filePath, "w") as f:
                for row in data:
                    f.write(FileManager.separator.join(row))
                    f.write("\n")
        except FileNotFoundError:
            raise FileNotFoundError("\nThe file '{}' doesn't exist.".format(filePath))
        return

    @staticmethod
    def loadExcelSheet():
        pass

    @staticmethod
    def loadExcelWorkbook():
        pass

    @staticmethod
    def setSeparator(separator: str):
        FileManager.separator = separator


    @staticmethod
    def getSeparator() -> str:
        return FileManager.separator
