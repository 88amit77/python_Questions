##question1
import json


prices ={
    'ACME': 45.23,
    'APPL': 612.73,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
##to conver dict to json
res = json.dumps(prices)
print(res)
## to convert json to dict
d=json.loads(res)
print(d)


###question2
dictionary={
    'ACME': 45.23,
    'APPL': 612.73,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

all_values = prices.values()
max_value = max(all_values)
min_value = min(all_values)
#max_value = dictionary[max(dictionary, key=dictionary.get)]
# max_value = max(dictionary.values())
# print(max_value)
#
#
# def get_key(val):
#     for key, value in dictionary.items():
#         if val == value:
#             return key
#
#     return "key doesn't exist"
# #all_values is a list
# key1=get_key(max_value)
# print(get_key(max_value))
# data={}
# data[]
# print(max_value)
# print(min_value)

# import pandas as pd
# a1=json.loads(prices)
# a=pd.read_json(a1)
# print(a)
# data=pd.read_csv('z.csv')
# data['company'].min()
# a={ value for key,value in prices.items() if prices.values() > 200}
###question3
rows = [
    {'fname': 'zrian', 'lname':'Jones','uid':1003},
    {'fname': 'David', 'lname':'Beez','uid':1004},
    {'fname': 'John', 'lname':'Clees','uid':1005},
    {'fname': 'Big', 'lname':'Jones','uid':1006},
]

newlist = sorted(rows, key=lambda k: k['fname'])
print(newlist)
###sort dict on the basis of keys
dict_data = {'Apple': 10, 'Banana': 5,'Orange':4,'Guava':6}
s=sorted(dict_data)
print("s=",s)
#
for key in sorted(dict_data):
    print((key,dict_data[key]))
# ###dict to data frame
# import pandas as pd
# dict_data1 = []
# dict_data1.append(dict_data)
# a1=pd.DataFrame.from_dict(dict_data1)
# # a1=pd.DataFrame.from_dict(dict_data,orient ='index')
# print("a1",a1)

###question==4
# '''Suppose you have a User table with Username, First_Name, Last_Name and Email. Write
# a query to return User whose first name starts with R or last name starts with D'''
# ##method==1
# data=User.objects.filter(first_name__contains='R', last_name__contains='D')
# ##method=2
# Entity.objects.filter(
#     Q(first_name__istartswith="R") | Q(last_name__istartswith="D") |
#     Q(first_name__istartswith="A") | Q(last_name__istartswith="T")
#     )

#Entity.objects.filter(
#     Q(first_name__istartswith="R") | Q(last_name__istartswith="D")
#     )