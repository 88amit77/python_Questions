###Write a Python program to print set of duplicates in a list
l=[1,1,2,3,4,4,5]
x1=set([x for x in l if l.count(x)>1])
print(x1)

###Write a Python program to print number of words in a given sentence
##method 1
data='my name is amit'
count=0
for i in data.split(" "):
    count=count+1
print(count)
##method 2
s=data.split(" ")
a=len(s)
print("a--",a)

## Write a Python program to count no of times element present in a from given string
def element(name,c) :
 co=0
 for i in name:
     # print(i)
     if c==i:
         co=co+1
 return co
name="my name is amit kumar tiwari"
c='a'
print(element(name,c))

####Find out common letters between two strings Using Python
a='NAINA'
b='REENE'
l=[]
###method1
for i in a:
    for j in b:
        if j in a:
            l.append(j)

print("common",set(l))
##method2
a1=set(a)
b1=set(b)
print(a1)
print(b1)
c=a1&b1
print(c)

####Count the frequency of words appearing in a string Using Python
data='my name is amit and my brother name is sumit'
d={}
for i in data.split(" "):
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1

print(d)

####Count the frequency of char appearing in a string Using Python
data='namrata'
d={}
for i in data:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1

print(d)

###Conversion of two list into Dictionary Using Python
l1=[1,2,3]
l2=['amit','sumit','namrata']
l3=dict(zip(l1,l2))
print(l3)
