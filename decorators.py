###decorators in python
##normal function
##example=1
def div(a,b):
    print(a/b)

# a=2
# b=4
# print(div(a,b))

##decorator
def deco(func):

    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

div1=deco(div)
div1(2,4)

##example=2
def first(a):
    return a

def deco(funct):
    def inner(a1):
        if a1:
            a1=a1+" and i am a cool guy"
        return funct(a1)
    return inner

a="my name is amit"
div2=deco(first)
print(div2(a))