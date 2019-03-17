try:
    print(2/0)
except ZeroDivisionError:
    print('error')


def safe_call(a, b):
    if(b==0):
        raise ValueError('not correct b')
    try:
        print(a/b)
    except ZeroDivisionError as err:
        print(err)

safe_call(1,-2)
safe_call(1,12312)
safe_call(1,0)