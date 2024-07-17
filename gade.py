#To find grade of a person
def grade(a):
    if a>90:
        print('A')
    elif a>70 and a<=90:
        print('B')
    elif a >50 and a<=70 :
        print('D')
    elif a>30 and a<=50:
        print('E')
    else :
        print('reappear')

b = int(input('enter your marks:'))
if b>90:
        print('A')
elif b>70 and b<=90:
        print('B')
elif b >50 and b<=70 :
        print('D')
elif b>30 and b<=50:
        print('E')
else :
        print('reappear')

grade(b)
'''
enter your marks:98
A
A

enter your marks:76
B
B
'''