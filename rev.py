#reverse a number
def RevNum(num):
    rev = 0
    rem = 0
    while num>0:
        rem=num%10
        rev = rev*10 + rem
        num = num //10
    return(rev)

a = int(input('enter a number'))
x = a
b = 0
c = 0
while a>0:
    b=a%10
    c = c*10 + b
    a = a //10
print(c)
print(RevNum(x))
'''
enter a number34761
16743
16743

enter a number5761
1675
1675
'''