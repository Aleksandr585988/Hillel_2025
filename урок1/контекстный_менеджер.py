filename = "scren_txt/names.txt"

# file = open(filename)
# data = file.read()
# file.close()
# print(data)

with open(filename) as file:
    lines = file.read()
    print(lines)