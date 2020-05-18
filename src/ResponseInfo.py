from enum import Enum


class ResponseInfo(Enum):

    UNDEFINED = "UNDEFINED"
    OK = "OK"
    FileNotFoundException = "FileNotFoundException",
    InvalidDataFileException = "InvalidDataFileException",
    TimeIntervalIsNotSufficient = "TimeIntervalIsNotSufficient",
    InvalidLinkException = "InvalidLinkException"

    def __str__(self):
        return str(self.value)




