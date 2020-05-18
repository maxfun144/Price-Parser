




"""
Throws FileNotFoundError
"""

def readCSV(filePath: str):
    # try:
    with open(filePath, "r") as f:
        return list(map(lambda x: x.split(), f.readlines()))
    # except FileNotFoundError:
    #     raise Exception("Error: The file doesn't exist.")


def writeCSV(filePath: str, data: list, separator="\t"):
    with open(filePath, "w") as f:
        for row in data:
            f.write(separator.join(row))
            f.write("\n")
    return

# print("Iterating  down the rows.")
# for i in range(getRowNumber(cellStart1), getRowNumber(cellEnd1) + 1):
#     print(cellStart1)
#     cellStart1 = addRowNumber(cellStart1, 2)
#
# print("Iterating  right the columns.")
# for i in range(getColumnNumberDecimal(cellStart2), getColumnNumberDecimal(cellEnd2) + 1):
#     print(cellStart2)
#     cellStart2 = addColumnNumber(cellStart2, 4)



