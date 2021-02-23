# List Examples

a, b, c = 5, 6.5, "Jatin Ssingh"
print("Value is " + str(a))
# OR,
print("{} {}".format("value is:", a))
print(type(b))

List = [1, 2, "Jatin Ssingh", 4, 5]
print(List[0])

List.append(6)
print(List)

List.insert(3, "JATIN SSINGH")
print(List)

List[1] = 5
print(List)

del List[0]
print(List)

print(List[-1])
print(List[1:3])

# Tuple is Immutable(can't edit the tuples)

Tuple = ("Jatin Ssingh", 5, 9)
print(Tuple)

# Dictionary Examples

Dict = {"a": 2, 5: "Jatin Ssingh", "JATIN SSINGH": 9}
print(Dict["a"])
print(Dict[5])

Dicti = {}
Dicti["Name"] = "Jatin Ssingh"
Dicti["Profile"] = "Software Test Engineer"
Dicti["Experience"] = "2 Years"
print(Dicti)
print(Dicti["Profile"])






