# task 1
s = ''
def define_string_len(s):
    print(len(s))

#define_string_len(s)

# task 2

list1 = [1, 5, 8]
list2 = [1, 5, 8, 9]

def compare_to_lists(list1, list2):
    if len(list1) > len(list2):
        print(len(list1))
    else:
        print(len(list2))

# compare_to_lists(list1, list2)

# task 3

input_list = [1, 2, 4, 5]
new_value = ['один', 2, 8]
def add_value_to_list(input_list, new_value):
    input_list.append(new_value)
    print(input_list)

#add_value_to_list(input_list, new_value)

# task 4


def evaluate_number(numb):
    min_val, max_val = -100, +100
    if numb < min_val or numb > max_val:
        print("-")
    else:
        print('+')

#numb = -100
#evaluate_number(numb)

# task 5

def check_string(str_1, str_2):
    if str_1 in str_2:
        print('ДА')
    else:
        print('НЕТ')

str_1 = 'test'
str_2 = 'test1'

#check_string(str_1, str_2)

# task 6
def check_int_status(check_list):
    result = 0
    for i in check_list:
        if i > 0:
           result = result + 1
        else:
            pass
    print(result)

check_list = [0, 1, -1, -3, -5, 2, 3]

#check_int_status(check_list)

# task 7

years = 5
months = 7

def count_days(years, months):
    print((years*12+months)*29)

#count_days(years, months)

#stringOfWords = 'one two three four'

# task 9


def count_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


#n = 10
#print(count_factorial(n))