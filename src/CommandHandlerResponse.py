from src.ResponseInfo import ResponseInfo


def reverseDictionary(dictionary: dict) -> dict:
    newDictionary = {}

    for key in dictionary.keys():
        newDictionary[dictionary[key]] = key

    return newDictionary


class CommandHandlerResponse:

    #  |status| < 10 - OK
    #  status < -10 - Fatal Error
    #  status > 10 - PossibleToResolveError

    statusToResponseInfo = {0: ResponseInfo.UNDEFINED,
                            1: ResponseInfo.OK,
                            11: ResponseInfo.TimeIntervalIsNotSufficient,
                            12: ResponseInfo.InvalidLinkException,
                            -11: ResponseInfo.FileNotFoundException,
                            -12: ResponseInfo.InvalidDataFileException
                            }

    responseInfoToStatus = reverseDictionary(statusToResponseInfo)


    def __init__(self, status=0, responseInfo=ResponseInfo.UNDEFINED, successMessage="", errorsMessage=""):

        self.successMessage = successMessage
        self.errorsMessage = errorsMessage
        self.status = status
        self.responseInfo = responseInfo

        if status == 0:
            self.status = self.convertResponseInfoToStatus(responseInfo)
        elif responseInfo == ResponseInfo.UNDEFINED:
            self.responseInfo = self.convertStatusToResponseInfo(status)

    def __str__(self) -> str:
        return "\nResponse Object" \
               "\n    status = ....... '{}'" \
               "\n    responseInfo = . '{}'" \
               "\n    successMessage = '{}'" \
               "\n    errorsMessage =  '{}'".format(self.status,
                                                    self.responseInfo,
                                                    self.successMessage,
                                                    self.errorsMessage)


    def getResponseInfo(self) -> ResponseInfo:
        return self.responseInfo


    def getStatus(self) -> int:
        return self.status


    def getSuccessMessage(self) -> str:
        return self.successMessage


    def getErrorsMessage(self) -> str:
        return self.errorsMessage


    @staticmethod
    def convertResponseInfoToStatus(responseInfo: ResponseInfo) -> int:
        try:
            return CommandHandlerResponse.responseInfoToStatus[responseInfo]
        except KeyError:
            return 0

    @staticmethod
    def convertStatusToResponseInfo(status: int) -> ResponseInfo:
        try:
            return CommandHandlerResponse.statusToResponseInfo[status]
        except KeyError:
            return ResponseInfo.UNDEFINED
