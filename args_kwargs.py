#To demonstrate the usageof *args and **kwargs
def msg1(*args):
    for word in args:
        print(word)

def msg2(**kwargs):
    for num,word in kwargs.items():
        print("{} is {}".format(num,word))

msg1('Hello', 'welcome', 'to', 'python')
print()
msg2( first= 'hello' , second = 'welcome' , third = 'to', fourth = 'pyhton')

'''
Hello
welcome
to
python

first is hello
second is welcome
third is to
fourth is pyhton
'''