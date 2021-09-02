input_str = '''A Backend Engineer,
 self-motivated learner with a passion for design and engineering.
Proficient at Django and Django Rest Framework.
 Goal oriented professional,
 Goal oriented professional
  capable of working independently or as part of team. Beyond coding,
 I enjoy working in an evolving industry. '''


# print(input_str[163:])

data=input_str.split('\n')
# print(data[-2:])
# data1=data[-2:]
# print(data1[0])
# print(data1[1])


###print this pattern

#        *
#       * *
#      * * *
#     *     *

# for row in range(7):
#     for col in range(5):
#         if ((col==0 or col==4) and row!=0) or ((row==0 or row==3)and (col>0 and col<4)):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

for row in range(5):
    for col in range(4):
        if ((col==0 or col==3) and row !=0) or ((row==0 or row==2) and (col>0 and col<3)):
            print("*",end="")
        else:
            print(end=" ")
    print()

# for row in range(5):
#     for col in range(4):
#         if ((col==0 or col==3) and row!=0) or ((row==0 or row==2) and (col>0 and col<3)):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()