####Armstrong Number Program In Python
##example 153=1**3 + 5**3 + 3**3

def armstrong(num1):
    total=0
    num=num1
    while num>0:
        n=num % 10
        print(n)
        total=total+n**3
        num=num//10
    print("num--",num1)
    print("total--", total)
    if num1==total:
        return "num is armstrong"
    else:
        return "num is not armstrong"


num=153
print(armstrong(num))


l=[1,2,3]
s=set(l)
print(s)