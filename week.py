'''
To get the day according to the day number entered
'''
d=['Monday','tuesday','wednesday','thursday','friday','saturday',
'sunday']
n=int(input('give day number'))
if n<1 or n>7:
    print('invalid input')
else:
    print('day is',d[n-1])
'''
give day number5
day is friday

give day number10
invalid input
'''