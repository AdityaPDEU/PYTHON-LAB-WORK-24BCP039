# write a program that define a function sum_avg() to accepts marks of student of five sub. calculates total and average.
def sum_avg():
    sub1=input("enter marks of sub1:")
    sub2=input("enter marks of sub2:")
    sub3=input("enter marks of sub3:")
    sub4=input("enter marks of sub4:")
    sub5=input("enter marks of sub5:")
    sum=sub1+sub2+sub3+sub4+sub5
    avg=(sub1+sub2+sub3+sub4+sub5)/5   
    print(f"sum:{sum}")
    print(f"avg:{avg}")

sum_avg()