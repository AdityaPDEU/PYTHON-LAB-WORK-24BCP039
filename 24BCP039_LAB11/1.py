# def count_case(string):
#     lower=0
#     upper=0
#     for char in string:
#         if "a"<= char <= "z":
#             lower+=1
#         elif "A" <= char <="Z":
#             upper+=1
#     return{"lower is":lower,"upper is":upper}

# str=input("enter string:")
# print(count_case(str))
def calculate(n):
    for i in range(n):
     n1=int(str(n)*1)
    print(n1)
    n2=int(str(n)*2)
    print(n2)
    n3=int(str(n)*3)
    print(n3)
    return{"total":n1+n2+n3}
a=int(input("enter:"))  
c=calculate(a)  
print(c)

def calculate(n, terms):
    current_number ="0"
    total=0
    for i in range(0,n):
        current_number += str(n)  # Concatenating the number
        num = int(current_number)  # Convert to integer
        print(num)  # Print each term
        total += num  # Add to total
    return {"total": total}
a = int(input("Enter a number: "))  
t = int(input("Enter the number of terms: "))  
result = calculate(a, t)  
print(result)


