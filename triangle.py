#To find the area of a triangle
def tr(a,b,c):
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**(1/2)
    print('the area of triangle is :', area)

x = int(input('enter the length of first side:'))
y = int(input('enter the length of first side:'))
z = int(input('enter the length of first side:'))
l = (x+y+z)/2
ar = (l*(l-x)*(l-y)*(l-z))**(1/2)
print('the area of triangle is :', ar)

tr(x,y,z)
'''
enter the length of first side:3
enter the length of first side:4
enter the length of first side:5
the area of triangle is : 6.0
the area of triangle is : 6.0

enter the length of first side:12
enter the length of first side:13
enter the length of first side:5
the area of triangle is : 30.0
the area of triangle is : 30.0
'''