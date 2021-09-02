'''
Define a class Rectangle which takes two arguments l and b and with method area gives area of rectangle.
	Inherit Rectangle in another class Square and use method area define in rectangle to find area of square.
'''

class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

class Square(Rectangle):
    def square_area(self):
        return self.length**2

newRectangle = Rectangle(2, 4)
print("Area of rectangle:",newRectangle.rectangle_area())

ob=Square(5,2)
print(print("Area of square:",ob.square_area()))


'''How do you find all pairs of an integer array whose sum is equal to a given number? '''

num=20
l=[]
for i in range(21):
    # print(i)
    for j in range(i):
        # print(j)
        if i+j==20:
            l.append(i)
            l.append(j)


print(l)