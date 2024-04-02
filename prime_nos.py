n = int(input('enter the number till which you want to search'))
print('the primes are :')
for i in range(2,n+1,1):
    x=0
    for k in range(1,i//2 + 2 ,1):
        if x>1:
            break
        elif i%k == 0 :
            x=x+1
    else :
        print(i)