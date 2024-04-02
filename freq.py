import random
l = []
for i in range (50):
    l.append(random.randint(1,10))
x = l.copy()
print(l)
a = len(l)
while a>0:
    freq = x.count(x[0])
    print ( x[0] ,':' , freq)
    z = x[0]
    for j in range(freq):
        x.remove(z)
    a = len(x)
#OR THIS METHOD
print(l) 
FREQ = { }
for m in l:
    if m not in FREQ :
        FREQ[m] = l.count(m)

for k in FREQ:
    print( k , ':', FREQ[k])

