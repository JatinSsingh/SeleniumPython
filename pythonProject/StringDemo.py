string = "Jatin Ssingh is a Software Test Engineer"
string1 = " having 2.5 Years Experience"
string2 = "Jatin Ssingh"

print(string[1])
print(string[0:12])         # If u want substring in python
print(string + string1)     # Concatenation
print(string2 in string)    # Substring checking

var = string.split("is a")  # Split separate/divide the string
print(var)
print(var[0])

string3 = " JATIN SSINGH "  # Strip remove the front and end spaces from string
print(string3.strip())
print(string3.lstrip())
print(string3.rstrip())
