import random
a = []
l = []

for i in range(10):
    a.append(random.randint(1,10))
s = len(a)
print(a)
for k in range(0,s-1,2):
    a[k] , a[k+1] = a[k+1] , a[k]
print(a)