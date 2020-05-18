import csv


def csv_reader(file_obj):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj)
    print(reader)
    data = []
    for row in reader:
        data.append(row)
        # print(" ".join(row))
    print(data)


csv_path = "data/data.csv"
with open(csv_path, "r") as f_obj:
    csv_reader(f_obj)



# f = open("data/data.csv", "r")
# print(f.read())
# g = open("data/relatives.csv", "r")
# print(g.read())