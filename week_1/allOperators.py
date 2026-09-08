#Arithmetic Operators
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
print("\n Arithmetic Operators:")
print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}") # Addition
print(f"a - b = {a - b}") # Subtraction
print(f"a * b = {a * b}") # Multiplication
if b != 0:
 print(f"a / b = {a / b}") # Division
 print(f"a // b = {a // b}") # Floor Division
 print(f"a % b = {a % b}") # Modulus
else:
 print("Division, Floor Division, and Modulus are not defined for b = 0.")
print(f"a ** b = {a ** b}") # Exponentiation

#Relational Operators
print("\nRelational Operators:")
print(f"a == b: {a == b}") # Equal to
print(f"a != b: {a != b}") # Not equal to
print(f"a > b: {a > b}") # Greater than
print(f"a < b: {a < b}") # Less than
print(f"a >= b: {a >= b}") # Greater than or equal to
print(f"a <= b: {a <= b}") # Less than or equal to

#Assignment Operators
print("\nAssignment Operators:")
x = a
print(f"x = a: x = {x}") # Simple assignment
x += b
print(f"x += b: x = {x}") # Addition assignment
x -= b
print(f"x -= b: x = {x}") # Subtraction assignment
x *= b
print(f"x *= b: x = {x}") # Multiplication assignment
if b != 0:
 x /= b
 print(f"x /= b: x = {x}") # Division assignment
 x //= b
 print(f"x //= b: x = {x}") # Floor Division assignment
 x %= b
 print(f"x %= b: x = {x}") # Modulus assignment
x **= 2
print(f"x **= 2: x = {x}") # Exponentiation assignment

#Logical Operators
print("\nLogical Operators:")
p = True
q = False
print(f"p = {p}, q = {q}")
print(f"p and q: {p and q}") # Logical AND
print(f"p or q: {p or q}") # Logical OR
print(f"not p: {not p}") # Logical NOT

#Bit wise Operators
print("\nBitwise Operators:")
m = 10 # 1010 in binary
n = 4 # 0100 in binary
print(f"m = {m}, n = {n}")
print(f"m & n: {m & n}") # Bitwise AND
print(f"m | n: {m | n}") # Bitwise OR
print(f"m ^ n: {m ^ n}") # Bitwise XOR
print(f"~m: {~m}") # Bitwise NOT
print(f"m << 1: {m << 1}") # Bitwise left shift
print(f"m >> 1: {m >> 1}") # Bitwise right shift

#Ternary Operator
print("\nTernary Operator:")
max_value = a if a > b else b
print(f"The maximum of a and b is: {max_value}")
#Membership Operators
print("\nMembership Operators:")
list_example = [1, 2, 3, 4, 5]
print(f"2 in list_example: {2 in list_example}") # Checks if 2 is in the list
print(f"10 not in list_example: {10 not in list_example}") # Checks if 10 is not in the list
#Identity Operators
print("\nIdentity Operators:")
x = 5
y = 5
print(f"x is y: {x is y}") # Checks if x and y refer to the same object
print(f"x is not y: {x is not y}") # Checks if x and y refer to different objects