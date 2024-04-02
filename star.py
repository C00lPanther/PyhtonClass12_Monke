n = int(input('enter the lines of star'))
s = n//2

for i in range( 1 , s+1 , 1):
    for j in range (1,s+2-i,1):
        print(' ' , end='')
    for k in range (1, (i-1)*2 + 2 ,1):
        print('*' , end = '')
    print()

for i in range(0 , s+1 , 1):
    for j in range(0,i,1):
        print(' ' , end='')
    for k in range( 0 , n - i*2 , 1):
        print('*' , end = '')
    print()

#OR THE OTHER METHOD IS THIS

for i in range(1 , s+1 ,1):
    print( ' '*(s-i+1) + '*'*(1 + (i-1)*2) )
for i in range(1 , s+2 ,1):
    print( ' '*(i-1) + '*'*( n - (i-1)*2 ) )
