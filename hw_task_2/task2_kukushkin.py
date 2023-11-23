# task 1

input_string = 'Python php function spam'
stop_words = ['Python', 'php', 'go', 'C']

def remove_stop_words(input_string, stop_words):
    words = input_string.split()
    result_words = list(filter(lambda x: x not in stop_words, words))
    result_string = ' '.join(result_words)
    return result_string

#print(remove_stop_words(input_string, stop_words))

# task 2

inp_l = [1, 3, 4, 6, 7, 12, 15]
multiple_of = 3

def get_multiples(inp_l, multiple_of):
    res = list(filter(lambda x: x % multiple_of == 0, inp_l))
    return res

#res = get_multiples(inp_l, multiple_of)
#print(res)

#task 3
def add(*args):
    return tuple((filter(lambda x: isinstance(x, str), args)))

total = add(1, 2, 'string', 'strong', 'big', 8)
#print(total)

#task 4
inp = ['Python', 'php', 'go', 'C']
inp2 = ['Python', 'Tryton', 'Baton', 'C']

def join_lists(inp, inp2):

    result_words = list(filter(lambda x: x in inp, inp2))
    return result_words
# print(join_lists(inp, inp2))

#task 5
#---------



#task 6
def check_int(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        if isinstance(result, int):
            print(result)
        else:
            print('Исключение. Нечисловой результат')
    return wrapper

@check_int
def price_calculation(x, n):
    return x + n

#price_calculation(1, 2)
@check_int
def print_any_sign(x):
    for e in x:
        if isinstance(e, str):
            print(e)
            break

x = [1, 'hi', 2]

#print_any_sign(x)

#task 7


def restart_fn(fn):
    def wrapper(*args, **kwargs):
        try:
           fn(*args, **kwargs)
        except:
            fn(*args, **kwargs)
    return wrapper

@restart_fn
def print_sboi():
    print('Сбой')
    raise Exception

#print_sboi()

@restart_fn
def print_x(x):
    if isinstance(x, int):
        print(x)
    else:
        raise Exception
x = 10.0

#print_x(x)
#task 8

elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]
result = list(map(lambda x: (x[1], x[2]), filter(lambda x: True, elements)))
print(result)