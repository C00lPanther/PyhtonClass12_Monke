'''
To input numbers from user and reverse the list
'''
l=[]
n=int(input('enter number of element for the list:'))
for i in range(n):
    x=int(input('enter a number'))
    l=l+[x]
print(l)
print(l[::-1])
'''
enter number of element for the list:4
enter a number6
enter a number18
enter a number3
enter a number4
[6, 18, 3, 4]
[4, 3, 18, 6]

enter number of element for the list:3
enter a number2
enter a number6
enter a number4
[2, 6, 4]
[4, 6, 2]
'''