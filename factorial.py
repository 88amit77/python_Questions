###find the factorial of a number

def factorial(n):
    f = 1
    for i in range(1,n+1):
        f=f*i
    return f

num=3
print("factor of num ->"+str(num)+" is =",factorial(num))