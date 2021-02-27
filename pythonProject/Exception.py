items = 5

if items != 5:
    raise Exception("Items could not match")

# 2nd way of exception
assert (items == 5)


# Try, Catch block
try:
    with open("test1.txt", 'r') as reader:
        reader.read()

except:
    print("Somehow I reached this block because their is failure in try block")

try:
    with open("test1.txt", 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("Somehow this block is printed no matter try and except block is fail or pass")
