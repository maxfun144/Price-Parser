from time import time

from CustomExceptions.InvalidDataFileException import InvalidDataFileException
from CustomExceptions.InvalidLinkException import InvalidLinkException
from CustomExceptions.UnsupportedCommandException import UnsupportedCommandException
from src.ExcelManager import ExcelManager
from src.FileManager import FileManager
from src.CommandHandlerResponse import CommandHandlerResponse
from src.FileValidator import FileValidator
from src.Function import Function
from src.ResponseInfo import ResponseInfo
from GUI.Request import Request


class CommandHandler:

    # To protect the program from overclicking!
    # functionName -- maxInterval in milliseconds

    minimalTimeInterval = {Function.updateExcel: 200000
                           }

    # functionName -- last Call in milliseconds
    lastExecutionTime = {Function.updateExcel: 0}


    def executeCommand(self, command: str, args: dict) -> CommandHandlerResponse:

        if command == Function.updateExcel:
            return self.updateExcel(args)

        elif command == "":
            pass

        elif command == "":
            pass

        elif command == "":
            pass

        elif command == "":
            pass

        elif command == "":
            pass

        elif command == "":
            pass

        elif command == "":
            pass

        elif command == "":
            pass

        elif command == "":
            pass

        elif command == "":
            pass
        else:
            raise UnsupportedCommandException("Command '{}' isn't supported.".format(command))
            # Заменить на 'response' ??


    def updateExcel(self, args: dict) -> CommandHandlerResponse:
        
        if not (self.timeIntervalIsSufficient(Function.updateExcel)):
            return CommandHandlerResponse(responseInfo=ResponseInfo.TimeIntervalIsNotSufficient)

        self.updateLastExecutionTime(Function.updateExcel)
        # try:
        #     filePath = args["excelPath"]
        #     diapasonsPath = args["diapasonsPath"]
        #     ...
        # except Some--Exception:
        #     raise InvalidArgumrent Exception
        #         or CommandHandlerResponse

        excelPath = args[Request.filePath]
        diapasonsPath = "../data/diapasonsDad.csv"
        firmsPath = "../data/firms.csv"
        excelManager = ExcelManager(excelPath)

        try:
            diapasons = FileManager.readCSVto2DimensionalList(diapasonsPath, " ")
            firms = FileManager.readCSVtoDict(firmsPath, ",")

            FileValidator.checkDataFilesForCorrectness(diapasons, 5, diapasonsPath,
                                                       firms, 2, firmsPath)
            excelManager.updateExcel(diapasons, firms)

            return CommandHandlerResponse(responseInfo=ResponseInfo.OK,
                                          successMessage="\nExcel was updated successfully!")

        except FileNotFoundError as e:
            return CommandHandlerResponse(responseInfo=ResponseInfo.FileNotFoundException,
                                          errorsMessage=str(e))

        except InvalidDataFileException as e:
            return CommandHandlerResponse(responseInfo=ResponseInfo.InvalidDataFileException,
                                          errorsMessage=str(e))

        except InvalidLinkException as e:
            return CommandHandlerResponse(responseInfo=ResponseInfo.InvalidLinkException,
                                          successMessage="\nExcel was partially updated.",
                                          errorsMessage=str(e))


    def timeIntervalIsSufficient(self, function: Function) -> bool:
            return int(time() * 1000) - self.lastExecutionTime[function] > self.minimalTimeInterval[function]
    
    
    def updateLastExecutionTime(self, function: Function):
        self.lastExecutionTime[function] = int(time() * 1000)
        
        
# commandHandler = CommandHandler()
# dic = {}
# commandHandler.updateExcel(dic)

# commandHandler = CommandHandler()
# response = commandHandler.updateExcel({})
# response = commandHandler.updateExcel({})