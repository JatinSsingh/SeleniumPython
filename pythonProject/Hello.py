print("Jatin Ssingh")
print("*********************************************")
a = 3
print(a)
print("*********************************************")
string = "ABCD"
print(string)
print("*********************************************")
b, c, d = 2, 3.5, "JATIN Ssingh"
print("Value is " + str(b))
print(type(b))
print(type(c))
print(type(d))
print("*********************************************")
List = [1, 2, 3.5, 'Ram', 'Sita']
print(List[0])
print(List[2])
print(List[-1])
List.insert(3, 4)
print(List)
List.append("Hari")
print(List)
List[4] = "RAM"
del List[1]
print(List)
print("*********************************************")
Tuple = (5, 6, 7, 'Shyam')
print(Tuple[-1])
print(Tuple[1])
print("*********************************************")
Dict = {"a": 2, 3: "ABCD", "c": "Jatin Ssingh"}
print(Dict["c"])
print(Dict[3])
print("*********************************************")
Dict1 = {}
Dict1["Name"] = "Jatin Ssingh"
Dict1["Gender"] = "Male"
print(Dict1)
print(Dict1["Name"])
print("*********************************************")
greeting = "Good Morning"
if greeting == "Morning":
    print("Condition matches")
    print("Second line")
else:
    print("Condition don't match")
print("The End")
print("*********************************************")
obj = [1, 2, 3, 4, 5]
for i in obj:
    # print(i)
    print(i * 2)
print("*********************************************")
Sum = 0
for j in range(1, 6):
    Sum = Sum + j
print(Sum)
print("*********************************************")
for r in range(1, 10, 2):
    print(r)
print("*********************************************")
a = 5
while a > 1:
    if a == 3:
        break
    print(a)
    a = a - 1
print("While loop execution done")
print("*********************************************")
b = 9
while b > 1:
    if b == 5:
        b = b - 1
        continue
    if b == 2:
        break
    print(b)
    b = b - 1
print("Loop is executed")
print("*********************************************")


def Test(Designation):
    print("Jatin Ssingh" + Designation)


def Test1(h, p):
    print(h + p)


Test(" is a Software Test Engineer")
Test1(2, 3)
print("*********************************************")


def Test2(c, d):
    return c + d


print(Test2(5, 4))
print("*********************************************")


# In python, function is a group of related statements that performs a specific task.
def GreetMe():
    print("Good Morning")


GreetMe()
print("*********************************************")


class Calculator:
    num = 100  # class variables
    # default constructor

    def __init__(self, q, w):
        self.firstName = q
        self.secondName = w
        print("I am called automatically when object is created")

    def getData(self):
        print("I am executing as method in class")

    def Summation(self):
        return self.firstName + self.secondName + Calculator.num


obje = Calculator(2, 3)
obje.getData()
print(obje.Summation())
print("*********************************************")
str1 = "JatinSsingh.com"
str2 = "Consulting firm"
str3 = "JatinSsingh"

print(str1[1])
print(str2[0:4])
print(str3+str2)
print(str3 in str1)

var = str1.split(".")
print(var)
print(var[1])

str5 = "  Jatin Ssingh  "
print(str5.strip())
print(str5.rstrip())
print(str5.lstrip())
print("*********************************************")
file = open('test.txt')
# print(file.read())
# print(file.readline())
# print(file.readline())
print(file.readlines())
file.close()
print("*********************************************")
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

with open("test.txt", 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
# file = open('test.txt')
# file.close()
# with open('test.txt') as file:
# file = open('test.txt')
# file.close()

item = 0
if item != 2:
    pass
assert(item == 0)
print("*********************************************")
try:
    with open('test.txt', 'r') as reader:
        reader.read()
except:
    print('Some how i reached this block because there is failure in try block')

finally:
    print('Finally will execuated')
print("*********************************************") 

