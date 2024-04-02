'''
Toremove duplicates in a list
'''
import random
l=[]
for i in range(50):
    l.append(random.randint(1,10))
print(l)
final=[]
for i in l:
    if i not in final:
        final.append(i)
print('shortend list is', final)
'''
[9, 7, 5, 1, 3, 3, 5, 7, 8, 10, 9, 3, 3, 1, 2, 1, 9, 6, 3, 4, 4, 7, 1, 4, 5, 9, 7, 2, 1, 10, 5, 2, 10, 8, 3, 2, 2, 8, 10, 8, 6, 3, 4, 10, 8, 9, 3, 10, 1, 9]
shortend list is [9, 7, 5, 1, 3, 8, 10, 2, 6, 4]

[1, 8, 4, 6, 2, 6, 2, 3, 6, 10, 10, 7, 7, 10, 10, 8, 2, 6, 6, 7, 3, 8, 8, 6, 10, 9, 2, 10, 8, 7, 4, 10, 1, 6, 2, 3, 7, 1, 10, 8, 8, 10, 9, 6, 4, 2, 10, 1, 6, 10]
shortend list is [1, 8, 4, 6, 2, 3, 10, 7, 9]
'''