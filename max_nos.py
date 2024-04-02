n = int(input())
s = n//2 
for i in range(1,s+1,1):
    for k in range(i,s+1,1):
        print(' ' , end='')
    for m in range(1,i+1,1):
        print('*', end=' ')
    print()
for i in range(s+1,0,-1):
    for k in range(s+1,i,-1):
        print(' ' , end='')
    for m in range(1,i+1,1):
        print('*' , end= ' ')
    print()

for i in range(1,s+1,1):
    print(' '*(s+1-i) , end='')
    for k in range(1,i+1,1):
        print('*', end=' ')
    print()
for i in range(s+1,0,-1):
    print(' '*(s+1-i) , end='')
    for k in range(1,i+1,1):
        print('*' , end=' ')
    print()


