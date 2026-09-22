
# Multiplication table (from 1 to 10) in Python
num = int(input("enter the number of which table you want:"))
# To take input from the user
# num = int(input("Display multiplication table of? "))
# Iterate 10 times from i = 1 to 10
for i in range(1, 21):
   print(num, 'x', i, '=', num*i)