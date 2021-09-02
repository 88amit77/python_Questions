# # price range 5-10 lPA   or 15 - 20 lPA
import Card
import Q as Q
query=Card.objects.filter(Q(price__gt=500000) & Q(price__lt=1000000)) & Card.objects.filter(Q(price__gt=1500000) & Q(price__lt=2000000))

###anagrams question
str1="earth"
str2="heart"
str11=sorted(str1)
str22=sorted(str2)
if str11 ==  str22:
    print("anagrams")
else:
    print("not anagram")

# ##break statment
##convert list to a tuple
l=[1,2,3,4]
t=tuple(l)

# rebitantque
##print 2nd last and 3rd last element
s="india"
s1=s.replace("india","australia")
last=s1[-3:-1]

print(last)

###what are signals in django and when they triggers after data base creation or before??
'''django.db.models.signals.pre_save & django.db.models.signals.post_save

Sent before or after a model’s save() method is called.

django.db.models.signals.pre_delete & django.db.models.signals.post_delete

Sent before or after a model’s delete() method or queryset’s delete() method is called.

django.db.models.signals.m2m_changed

Sent when a ManyToManyField on a model is changed.

django.core.signals.request_started & django.core.signals.request_finished'''
###
#What is Django mixin?
'''A Mixin is a special kind of inheritance in Python (and other object-oriented languages) 
and it's starting to get a big rise in Django / Web Application Development. 
You can use a Mixin to allow classes in Python to share methods between any class that inherits from that Mixin.'''