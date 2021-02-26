num = 9

while num > 1:
    if num != 5:
        print(num)

    num = num - 1

print("While loop is executed_1")
print("***************************")

num = 9

while num > 1:
    if num == 5:
        break
    print(num)

    num = num - 1

print("While loop is executed_2")
print("***************************")

num = 9

while num > 1:
    if num == 5:
        num = num - 1
        continue       # Skip the current iteration
    if num == 3:
        break
    print(num)

    num = num - 1

print("While loop is executed_3")