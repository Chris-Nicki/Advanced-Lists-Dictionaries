import shutil

def line_break():
    terminal_width = shutil.get_terminal_size().columns
    line = '=' * terminal_width
    print(line)

###################################################################################

print("Advanced Operations on Python Lists")

line_break()
# Task 1: Implement a function to create a new list using list comprehension that contains squares of numbers from 1 to n, where n is a parameter.

def square_number(n):
    return [i * i for i in range(1, n + 1)]

print(square_number(20))

line_break()

# Task 2: Implement a function that has 3 parameters representing a list and 2 indices that will reverse a sublist within the list from index i to j (inclusive).
lst = [30, 31, 32, 33, 42, 44 , 85]
i = 0
j = 4

def sort_list(lst, i, j):
   
    new_list = lst [i:j + 1]
    new_list.reverse()
    lst[ i:j + 1] =new_list
    return lst

print(sort_list(lst, i, j))



line_break()

#Task 3: Implement a function to merge two sorted lists into a single sorted list without using the built-in sorted function of list.sort method. 

list_a = [1, 5, 7]
list_b = [2, 4]

def merge_list(list_a, list_b):
    list_c = [0]*(len(list_a)+ len(list_b))
    a = 0
    b = 0 
    c = 0
    while a < len(list_a) and b < len(list_b):
        if list_a[a] < list_b[b]:
            list_c[c] = list_a[a]
            a += 1
        else:
            list_c[c] = list_b[b] 
            b += 1
        c += 1
    while a < len(list_a):
        list_c[c] = list_a[a]
        a += 1
        c += 1
    while b < len(list_b):
        list_c[c] = list_b[b]
        b += 1
        c += 1
    return list_c
   

print(merge_list(list_a, list_b))

line_break()

print("Dictionary Manipulations and Optimization")

line_break()

# Task 1: Implement a function to merge two dictionaries, preserving the values of common keys # from the second dictionary

# dict_1 = {"a": 1, "b": 2, "c": 3}
# dict_2 = {"b": 4, "c": 5, "d": 6}

#  Expected Output
# {"a": 1, "b": 4, "c": 5, "d": 6}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"b": 4, "c": 5, "d": 6}

def merged_dict(dict_1, dict_2):
    dict_3 = dict_1.copy()
    dict_3.update(dict_2)

    return dict_3

print(merged_dict(dict_1, dict_2))

line_break()

# Task 2: Implement a function to find the difference of two dictionaries, i.e., keys that are #only in one of the dictionaries along with their values. 

#dict_1 = {"a": 1, "b": 2, "c": 3}
#dict_2 = {"b": 4, "c": 5, "d": 6}

## Expected Output
#{"a": 1, "d": 6}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"b": 4, "c": 5, "d": 6}

def dict_difference(dict_1, dict_2):
    
    dict_3 = {}

    for key, value in dict_1.items():
        if key not in dict_2:
            dict_3[key] = value

    for key, value in dict_2.items():
        if key not in dict_1:
            dict_3[key] = value
    
    return dict_3
print(dict_difference(dict_1,dict_2))

line_break()

# Task 3: Implement a function to count the frequency of each unique word in a list using a dictionary. *Bonus* Ignore case 

words = ['dog', 'cat', 'Dog', 'Cat', 'dog']
def frequency(words):
    count = {}
    
    for word in words:
        lower_word = word.lower()
        if lower_word in count:
            count[lower_word] += 1
        else:
            count[lower_word] = 1
    return count

print(frequency(words))