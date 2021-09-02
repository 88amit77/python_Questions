def divide(a,b):
    return a/b

# a=2
# b=4
# print(divide(a,b))

def decodiv(fun):
    def inner(a,b):
        if b>a:
            a,b=b,a
        return fun(a,b)
    return inner

newdiv=decodiv(divide)
a=2
b=4
print(newdiv(a,b))


a ='aaaaaabbbcc'
d={}
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i] = d[i]+1

print(d)
print(max(d.values()))
print(d.keys())

for key,value in d.items():
    if value==max(d.values()):
        print(key,value)
    else:
        pass