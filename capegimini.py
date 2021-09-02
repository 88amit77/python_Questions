###question what are decorators how to make it
def dev(a,b):
    print(a/b)

def dev2(fun):
    def inner(a,b):
        # print(a,b)
        if b>a:
            a, b = b, a
            # print(a, b)
        return fun(a,b)
    return inner

a=2
b=5
dev4=dev2(dev)
# dev4(a,b)
print(dev4(a,b))

###question 2
####print the char which is high in count in the string
a ='aaaaaabbbcc'
d={}
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1

# print(d)

a=max(d.values())
# print(a)
for key,value in d.items():
    if value==a:
      print(key,":",value)
    else:
        pass

####question what will print(a1) will print
a=10
b=10
c=id(a)==id(b)
print("c-",c)

###question 5
a1=10
def xyz():
    a1=21
print(xyz())
print(a1)
