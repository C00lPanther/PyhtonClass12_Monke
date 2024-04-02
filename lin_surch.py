l = []
n = int(input('enter no of terms'))
for i in range(n):
    l.append(int(input()))

f = -1
x = int(input('enter the term to be found'))
for z in range(len(l)):
    if l[z]==x :
        f = z
if f==-1:
    print('number not found')
else:
    print('number found at',f)