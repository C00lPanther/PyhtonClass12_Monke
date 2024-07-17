def greet(time):
    if time<12 :
        print('good morning')
    elif time>=12 and time<17:
        print('good afternoon')
    else:
        print('good evening')
    
    
h=int(input('enter the current hour in 24hrs sys'))
m = int(input('etner the minutes'))
if h<12 :
    print('good morning')
elif h>=12 and h<17:
    print('good afternoon')
else:
    print('good evening')

greet(h)
'''
enter the current hour in 24hrs sys16
etner the minutes45
good afternoon
good afternoon

enter the current hour in 24hrs sys20
etner the minutes30
good evening
good evening
'''