file = open("test.txt")
print(file.read())      # Read all the content of file
print(file.read(5))

print(file.readline())  # Read single line at a time readline()
print(file.readline())

line = file.readline()
while line != "":
    print(line)
    line = file.readline()

for line in file.readline():
    print(line)


file.close()
