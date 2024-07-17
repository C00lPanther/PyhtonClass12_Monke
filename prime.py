#To find wether a number is prime
def prime(a):
    if a>1:
          for i in range(2, int((a**0.5)+1),1):
               if a%i == 0:
                    print(a,'is not a prime')
                    break
          else:
               print(a,'is a prime')
    else:
         print(a,'is a not prime')

b = int(input('enter a number :'))
if b>1:
     for i in range(2, int((b**0.5)+1) ,1):
        if b%i==0:
             print('the number is composite')
             break
     else:
          print(b,'is a prime')
        
               
else :
     print('the number is not prime')

prime(b)
'''
enter a number :7
7 is a prime
7 is a prime

enter a number :12
the number is composite
12 is not a prime
'''