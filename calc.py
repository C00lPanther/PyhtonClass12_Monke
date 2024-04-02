def calc(choice,num1,num2):
    if choice == 1:
        total = num1 + num2
    elif choice == 2:
        total = num1 - num2
    elif choice ==3:
        total = num1*num2
    elif choice ==4:
        total = num1/num2
    else : 
        print('invalid number')
    return(total)
a = int(input('etner the first number'))
b = int(input('etner the second number'))
c = int(input('''Enter the respective option for the following actions - 
              1.ADD
              2.SUBTRACT
              3.MULTIPLE
              4.DIVIDE'''))
if c == 1:
        t = a + b
elif c == 2:
        t = a - b
elif c ==3:
        t = a*b
elif c ==4:
        t = a/b
else : 
        print('invalid number')
print(t)
print(calc(c,a,b))