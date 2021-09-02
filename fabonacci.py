###Write a Python program to print Fibonacci Series
##example 0,1,1,2,3,5,8,13
l=[]
def F(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return F(a-1)+F(a-2)



for i in range(12):
    # print(F(i))
    l.append(F(i))
print(l)

