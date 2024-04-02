'''
To double the odd nos and half the even in the tuple
'''
t=eval(input('enter a tuple of nos.'))
x=()
for i in range(len(t)):
    if t[i]%2==0:
        x= x + ((t[i]/2),)
    else:
        x= x + ((t[i]*2),)
print(x)
'''
enter a tuple of nos.(3,5,7,3,5,7,5,3,8)
(6, 10, 14, 6, 10, 14, 10, 6, 4.0)

enter a tuple of nos.(0,10,8,4,5,7,12,1,6,7)
(0.0, 5.0, 4.0, 2.0, 10, 14, 6.0, 2, 3.0, 14)
'''