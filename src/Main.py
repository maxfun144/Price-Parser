from CustomExceptions.InvalidDataFileException import InvalidDataFileException
from CustomExceptions.InvalidLinkException import InvalidLinkException
from src.FileManager import FileManager
from src.ExcelManager import ExcelManager
from src.FileValidator import FileValidator

excelPath = "hello_world.xlsx"
diapasonsPath = "../data/diapasons.csv"
firmsPath = "../data/firms.csv"
excelManager = ExcelManager(excelPath)

diapasons = FileManager.readCSVto2DimensionalList(diapasonsPath, " ")
firms = FileManager.readCSVtoDict(firmsPath, ",")

# for key, value in firms:
#     print("Firms:\n========================\n")
#     print(key, " : ", value)

# for key in firms.keys():
#     print(key, " : ", firms[key])

# print("Firms:\n========================\n", firms)
# print(FileManager.readCSVtoDict(firms, ","))
try:
    FileValidator.checkDataFilesForCorrectness(diapasons, 5, diapasonsPath,
                                               firms, 2, firmsPath)
    print("Data files was loaded successfully.")
except InvalidDataFileException as e:
    print("Exceptions during loading the data files: ", e)

try:
    excelManager.updateExcel(diapasons, firms)
    print("Prices were updated successfully.")
except InvalidLinkException as e:
    print("Exceptions during updating prices: ", e)

# print(excelManager.getPrice( #old Price
#     "https://www.smart-doors.su/catalog/mezhkomnatnye_dveri/tradition_clever_line/2494/",
#     'class="price discount"+class="values_wrapper"'))

#
# print(excelManager.getPrice(
#     "https://www.smart-doors.su/catalog/mezhkomnatnye_dveri/tradition_clever_line/2494/",
#     'class="price"+class="values_wrapper"'))

# url = "https://finskie-dveri.ru/framuga-mejkomnatnaya"
# keywords = 'class="j-product__price__current price"'
# print(excelManager.getPrice(url, keywords))
