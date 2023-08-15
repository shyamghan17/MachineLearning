# def hello_func(greeting, name='You'):
#     return '{}, {}'.format(greeting, name)
# print(hello_func('Hi', 'hello'))

def stuent_info(*args, **kwargs):
    print(args)
    print(kwargs)
stuent_info('Math', 'Art', name='Ghanshyam', age=28)
