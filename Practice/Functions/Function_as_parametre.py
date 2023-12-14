def square(x):
    return x**2

def opt_number(func,num):
    result=func(num)
    return result


print(opt_number(square,4))