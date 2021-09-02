# data_list = ['orange', 'mango', 'apple', 'orange', 'mango', 'apple',
#              ['orange', 'mango', 'apple','orange', 'mango', 'apple',
#               ['orange', 'mango', 'apple',],
#               'apple', 'orange', 'mango', 'apple'],
#              'orange', 'mango', 'apple']
# d={}
# for i in data_list:
#     for j in i:
#         print(j)
#         if j in d:
#             d[j]+=1
#         else:
#             d[j]=1
#
# print(d)


# output = {"orange":7, "apple":8, "mango":7}
# l=[23, 5 ,89,34,21, 56]
#
# for i in range(len(l)-1,0,-1):
#     for j in range(i):
#         if l[j]<l[j+1]:
#             temp=l[j]
#             l[j]=l[j+1]
#             l[j+1]=temp
# print(l)

##what is the time complexity of this above code
##hint stack quee
def get_final_path(home_path, dest_path):
    '''
    Args:
      :home_path(str): home path
      :dest_path(str): dest path
    Returns:
      :final_path(str):
    final_path: concat of home_path & dest_path
      conditions
        1. Strip any '.' and '..' in dest_path from final path
        2. On remoivng '..' remove the preceeding directory from the final path.
           (behaves like *nix filesystem')
 Examples:
        :home_path: '/home/raja'
        :dest_path: 'a/b/c/./../d/e/f/../g/../h'
        :final_path: /home/raja/a/b/d/e/h'
        :home_path: '/home/raja'
        :dest_path: '../../../../../././../../'
        :final_path: '/'
    '''
# s="a/b/c/./../d/e/f/../g/../h"
# a=s.replace("..","")


