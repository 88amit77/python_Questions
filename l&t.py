class test:
    def __init__(self,name):
        ##class variable
        self.name = name
    def name(self,name):

        return name


ob = test('amit')
print(ob.name)

l=[1,1,1,2,2,3]
# l3=set(l)
# print(l3)
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)

print(l2)
num=456
final=0
while num >0:
    n=num%10
    final=final+n
    num=num//10
    if final>9:
        continue
    else:
        break


print(final)

#####
names = ['amit','sumit','namu']
copynames = tuple(names)
print(copynames)
print(id(names))
print(id(copynames))
print(names is copynames)


names = ['amit','sumit','namu']
copynames = list(names)
print(copynames)
print(id(names))
print(id(copynames))
print(names is copynames)


###
###this is ok
a1={1:"amit",2:"sumit"}
###this is also ok
a2={1:"amit",1:None}
###this is also ok
a3={1:"amit",1:"sumit"}
###this is also ok
a4={1:"amit",None:"sumit"}
print(a4)
print(a4.get(3,"no data found"))



