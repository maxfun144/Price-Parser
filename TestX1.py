import re
loveIs = 1

while loveIs:
    tableCellNumber = input()
    # print("OK" if bool(re.match(r"(^[A-Z]+[0-9]{2,100}$)|(^[A-Z]+[1-9]$)", tableCellNumber)) else "НЕ ok")
    print("OK" if not bool(re.match(r"^0", tableCellNumber)) else "НЕ ok")