from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter import filedialog as fd

from GUI.Request import Request
from GUI.TextDirection import TextDirection
from src.CommandHandler import CommandHandler
from src.CommandHandlerResponse import CommandHandlerResponse
from src.ResponseInfo import ResponseInfo


startWindow = Tk()

filePath = ""
# startFrame = Frame(master=startWindow, relief=RAISED, borderwidth=5)
# startFrame.grid(row=0, column=0, sticky="w")
#
# startButton = Button(master=startFrame, text="Запустить программу.", width=30, height=3)

commandHandler = CommandHandler()
def updateExcel():

    if filePath == "":
        return

    addText(reportTextField, "\nUpdating Excel document, please, wait...")
    response = commandHandler.updateExcel({
        Request.filePath: filePath
    })

    if response.getResponseInfo() == ResponseInfo.TimeIntervalIsNotSufficient:
        addText(reportTextField, "\nThe excel document was already updated recently!")

    elif CommandHandlerResponse.convertResponseInfoToStatus(response.getResponseInfo()) < 0:
        addText(reportTextField, response.getSuccessMessage() + response.getErrorsMessage())
        addText(reportTextField, "\nUpdating Excel document was stopped.")
    else:
        addText(reportTextField, response.getSuccessMessage() + response.getErrorsMessage())


def addText(fieldText: Text, message: str, direction=TextDirection.BELOW, disableAfterAdding=True):
    fieldText.config(state=NORMAL)

    if direction == TextDirection.NEXT:
        fieldText.insert(END, " " + message)
    elif direction == TextDirection.BELOW:
        fieldText.insert(END, "\n" + message)
    elif direction == TextDirection.ABOVE:
        fieldText.insert(1.0, message + "\n")
    elif direction == TextDirection.REPLACE:
        fieldText.replace(1.0, END, message)

    if disableAfterAdding:
        fieldText.config(state=DISABLED)

    startWindow.update()


def chooseFile():
    global filePath
    filePath = fd.askopenfilename(initialdir="~/", title="Выберете документ.", filetypes=(("Excel files", "*.xlsx"), ("", "*.xls")))
    # filePathEntry.config(state=NORMAL)
    filePathEntry.insert(0, filePath)
    # filePathEntry.config(state=DISABLED)
    startWindow.update()


upperFrame = Frame()
upperFrame.grid(row=0, column=0, padx=5, pady=5, sticky="w")

startButton = Button(upperFrame, text="Запустить программу.", command=updateExcel, width=30, height=3)
startButton.grid(row=0, column=0, padx=5, pady=5, sticky="w")

chooseFileFrame = Frame(upperFrame)
chooseFileFrame.grid(row=0, column=1, padx=5, pady=5, sticky="w")

chooseFileButton = Button(chooseFileFrame, text="Выбрать excel документ", command=chooseFile, width=30, height=3)
chooseFileButton.grid(row=0, column=0, padx=5, pady=5, sticky="w")

filePathScrollbar = Scrollbar(chooseFileFrame, orient='horizontal')
filePathScrollbar.grid(row=2, column=0, sticky="we")

filePathEntry = Entry(chooseFileFrame, xscrollcommand=filePathScrollbar.set)
filePathEntry.grid(row=1, column=0, padx=5, pady=5, sticky="we")
# filePathEntry.config(state=DISABLED)

filePathScrollbar.config(command=filePathEntry.xview)

reportTextField = scrolledtext.ScrolledText(startWindow, undo=True)
reportTextField.grid(row=1, column=0, sticky="nswe")
reportTextField.config(state=DISABLED)

startWindow.rowconfigure(1, weight=1)
startWindow.columnconfigure(0, weight=1)

startWindow.update()
startWindow.minsize(startWindow.winfo_width(), startWindow.winfo_height())

startWindow.title("Главное окно")

startWindow.mainloop()