'''
To only print the odd elements of tuple
'''
t=eval(input('enter a tuple of nos.'))
for i in range(len(t)):
    if i%2==0:
        continue
    else:
        print(t[i])
'''
enter a tuple of nos.(9,5,10,4,8,7,19)
5
4
7

enter a tuple of nos.(3,5,6,1,9,5,4,6)
5
1
5
6
'''