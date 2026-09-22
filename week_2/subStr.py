def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("NO")
    else:
        print("YES")
# driver code
string = input("enter the string:")
sub_str = input("enter the substring:")
check(string, sub_str)