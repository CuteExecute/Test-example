VERSION = 'v 1.0'

def sum(x, y):
    # Remove the validation to reflect a negative result in extended testing
    # if(isint(x) and isint(y)):
    #     pass
    # else:
    #     print ("Calculator only works with numbers.")
    res = int(x) + int(y)
    print(f'Result = {res}')

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

a = input("Enter first value:")
b = input("Enter second value:")
sum(a, b)