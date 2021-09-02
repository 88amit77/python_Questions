l=[1,2,3,4,5]

temp=l[-1]
l[-1]=l[0]
l[0]=temp
print(l)



def div(a,b):
    return a/b

def decodiv(function):
    def inner(a,b):
        if b>a:
            a,b=b,a
        # else :
        #     pass
        return function(a,b)
    return inner
a=2
b=5
# print(div(a,b))
final_div=decodiv(div)
print(final_div(a,b))
l=[3,1,2,10,9,4]
for i in range(len(l)-1,0,-1):
    for j in range(i):
        if l[j]<l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp


print(l)
##prime no
# n=10
# l2=[]
# for i in range(1,n+1):
#     if i>1:
#         for j in range(2,i+1):
#             if (i%j) == 0:
#                 break
#         else:
#             print(i)
#             l2.append(i)
#
#
# print(l2)
l=[]
# num=100
lower = 1
upper = 10
# for num in range(lower, upper + 1):
for num in range(1, 11):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       ##imp note for use of loop else here
       else:
           print(num)
           l.append(num)
print(l)