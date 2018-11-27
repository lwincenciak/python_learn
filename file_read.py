# open("badge.csv", "r")
# modes:    r - read
#           w - write
#           a - append
#           r+ - read and write
# opened files must be closed
# assign an open file to a variable, then variable.close()


queen_file = open("queen.txt", "r")
print(queen_file.readable())
# print(queen_file.read())      # read the whole file and print its content
# print(queen_file.readline())  # read the 1st line and place the cursor at the 2nd line
# print(queen_file.readline())  # read the 2nd line and place the cursor at the 3rd line
# print(queen_file.readlines()[0])  # number of the line: 0 is the first
for person in queen_file.readlines():
    print(person)
queen_file.close()
