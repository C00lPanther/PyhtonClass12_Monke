#To try the use of try_excpet block
try:
    a=int(input('enter a number: '))
    b=int(input('enter a number: '))
    c = a/b
    print(c)
except ValueError:
    print('wrong input enter an integer')
except TypeError:
    print('wrong input cant operate string')
except ZeroDivisionError:
    print('enter a correct value for b i.e. 0')
except  Exception as e :
    print('the respective error is', e)
else:
    print('The code has no errors')
finally:
    print('The code has been executed')
'''
enter a number: 1
enter a number: three
wrong input enter an integer
The code has been executed

enter a number: 3
enter a number: 4
0.75
The code has no errors
The code has been executed
'''