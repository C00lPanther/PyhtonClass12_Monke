'''linear search'''
l=()
n=int(input('enter no of elements in tuple:'))
for i in range(n):
    l+= ((int(input('enter a tuple element:'))),)
print(l)
search=int(input('enter number to be found:'))
found=False
for i in range(len(l)):
    if l[i]==search:
        print('found')
        found=True
        print('it is at index',i)
else:
    if found==False:
        print('not found')
'''enter no of elements in tuple:5
enter a tuple element:2
enter a tuple element:5
enter a tuple element:7
enter a tuple element:3
enter a tuple element:4
(2, 5, 7, 3, 4)
enter number to be found:3
found
it is at index 3

enter no of elements in tuple:3
enter a tuple element:2
enter a tuple element:7
enter a tuple element:4
(2, 7, 4)
enter number to be found:10
not found'''
