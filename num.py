#To print a table
def table(x,n):
    for i in range(1,n+1):
        print(num*i)
    

nth = int(input('the integer till which we want the seq:'))
num = int(input('etner the number for the req table :'))
for i in range(1,nth):
    print(num*i)

table(num,nth)
'''
the integer till which we want the seq:12
etner the number for the req table :2
2
4
6
8
10
12
14
16
18
20
22
2
4
6
8
10
12
14
16
18
20
22
24
'''