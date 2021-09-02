##Write a Sort function to sort the elements in a list
l=[4,1,7,2,8,5]

###method 1
###for sorting list using sort function
l1=sorted(l)
l3=[]
##to reverse list
for i in reversed(l1):
    l3.append(i)

print("l1==",l1)
print("l3==",l3)

###method 2
def max(l):
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            ###for ascending order
            # if l[j] > l[j+1]:
            ###for descending order
            if l[j] < l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp

max(l)
print(l)
##method 3
l=[1,2,3,4,0]
my_list = sorted(l, reverse=True)
print(my_list)


a = [(1, 5), (2,1), (3, 2), (5, 3)]
a.sort(key=lambda x: x[1],reverse=True )
print(a)


