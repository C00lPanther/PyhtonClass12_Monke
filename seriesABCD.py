n = int(input('enter the term '))
for i in range(1,n+1,1):
    for k in range( 65 , 65+i , 1):
        print(chr(k) , end = '')
    print()
