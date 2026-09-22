#====== 1.Using sum() =======
string = input("enter the string:")
vowels = "aeiouAEIOU"
count = sum(string.count(vowel) for vowel in vowels)
print("The number of vowels in the given string are:",count)
#======End of program======#

#======2. using findAll()======#
import re
string = input("Enter string: ")
vowels = r'[aeiouAEIOU]'
count = len(re.findall(vowels, string))
print(count)
#======End of program======#
