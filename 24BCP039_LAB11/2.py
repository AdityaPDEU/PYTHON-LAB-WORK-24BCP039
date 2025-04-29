# def len_function(a):
#     return{f"length :{len(a)}"}
# a=input("enter string: ")
# print(len_function(a))

# def add():
#     a=int(input("enter number1:"))
#     b=int(input("enter number2:"))
#     c=a+b
#     print(a,"+",b,"=",c)
# add()

# def fun1():
#     pa"
#     def fun2():
#         print("inside fun2....")
#     print("Again back in fun1.....",a)
#     fun2()
# fun1()

# def order3(a,b,c):
#     l=max(a,b,c)
#     s=min(a,b,c)
#     m=a+b+c-l-s
#     return s,m,l
# print(order3(5,10,7))
# s,m,l=order3(10,5,7)
# print(s)
# print(l)
# print(m)

# def interest(p,r,n):
#     return(p*r*n/100)
# s=interest(100,5,2)
# print(s)

# def add_many(*args):
#     s=0
#     for i in args:
#         if type(i)==int and type(i)==float:
#             s=s+i
#     return s
# print(add_many(10,20,30,40,50,5285,284,12,8975,4.25,2.556,53.56,547.985))

# def recfibo(n):
#     if n == 0 or n==1:
#         return 0 or 1
#     else:
#         return recfibo(n - 1) + recfibo(n - 2)
# def generate_fibonacci_series(a):
#     series = []
#     for i in range(a):
#         series.append(recfibo(i))
#     return series
# a=int(input("enter no.term:"))
# print(f"Fibonacci series:{generate_fibonacci_series(a)}")

# def recgcd(n,d):
#     if n%d==0:
#         return d
#     else:
#         return recgcd(d, n%d)
# a=48
# b=18
# result=recgcd(a,b)
# print(result)    

# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n* fact(n-1)
# a=int(input("number:"))
# print(fact(a))

# def recsod(n):
#     if n == 0:
#         return 0
#     else:
#         return n % 10 + recsod(n // 10)

# number = 5
# result = recsod(number)
# print(f"Sum of digits of {number} is: {result}")

