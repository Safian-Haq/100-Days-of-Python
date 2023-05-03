


def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f'function name: {function.__name__}\n'
              f'function args: {args}\n'
              f'function kwargs: {kwargs}\n'
              f'function returns: {function(*args,**kwargs)}\n')
        return function(*args, **kwargs)
    return wrapper

@logging_decorator
def just_func():
    pass

@logging_decorator
def one_arg_func(arg):
    pass

@logging_decorator
def args_func(*args):
    pass

@logging_decorator
def kwargs_func(**kwargs):
    pass

@logging_decorator
def a_function(a,b,c):
    return a * b * c

if __name__ == '__main__':

    just_func()
    one_arg_func(1)
    args_func(1,2,3,4)
    kwargs_func(username='SafianHaq', password='Password123')
    a_function(1,2,3)
