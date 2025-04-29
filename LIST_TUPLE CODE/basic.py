# def fun1():
#     print("its good")
#     def fun2():
#         print("")
#     print("Again back to the fun1")
#     fun2()
# fun1()
# print(type(fun1))
# def add():
#     a=int(input("enter a:"))
#     b=int(input("enter b:"))
#     print(a,"+",b,"=")
# add()

# def is_palindrome(s):
#     # Remove spaces and convert to lowercase
#     s = s.replace(" ", "").lower()
#     # Check if the string is the same forwards and backwards
#     return s == s[::-1]

# # Example usage
# input_string = "racecar"
# if is_palindrome(input_string):
#     print(f'"{input_string}" is a palindrome.')
# else:
#     print(f'"{input_string}" is not a palindrome.')

def count_number(str):
    s = str.count()
    return s
    
string="ADItyaaaaaaaa"
word = count_number(string)
print("the a is",{word})

