##Write a Python Program to print Prime Numbers between 1 numbers and 100
'''note:-In most of the programming languages (C/C++, Java, etc),
the use of else statement has been restricted with the if conditional statements.
But Python also allows us to use the else condition with for loops. The else block just
 after for/while is executed only when the loop is NOT terminated by a break statement.'''
l=[]
# num=100
lower = 1
upper = 10

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
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
###to check num is prime or not
# a = 3
# if a > 1:
#     for i in range(2, a):
#         if a % i == 0:
#             print("not a prime no")
#             break
#
#         print("its a prime no")
#
# else:
#     print("plz enter no greater than 1")








