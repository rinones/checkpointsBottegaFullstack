from decimal import Decimal
import math

# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.

my_list = [1, 2, 3]
my_tuple = ('a', 'b', 'c')
my_float = 5/3
my_integer = 1
my_decimal = Decimal(5/3)
my_dictionary = {
    'x' : 100,
    'y' : 200
    }
print("Exercise 1:")
print("my_list:", my_list)
print("my_tuple:", my_tuple)
print("my_float:", my_float)
print("my_integer:", my_integer)
print("my_decimal:", my_decimal)
print("my_dictionary:", my_dictionary)
print("-" * 30)

# Exercise 2: Round your float up. 

my_float_round = math.ceil(my_float)
print("Exercise 2:")
print("my_float_round:", my_float_round)
print("-" * 30)
 
# Exercise 3: Get the square root of your float. 

my_float_sqrt = math.sqrt(my_float)
print("Exercise 3:")
print("my_float_sqrt:", my_float_sqrt)
print("-" * 30)

# Exercise 4: Select the first element from your dictionary. 

first_element = my_dictionary[list(my_dictionary.keys())[0]]
print("Exercise 4:")
print("first_element:", first_element)
print("-" * 30)
 
# Exercise 5: Select the second element from your tuple. 

second_element = my_tuple[1]
print("Exercise 5:")
print("second_element:", second_element)
print("-" * 30)
 
# Exercise 6: Add an element to the end of your list. 

# my_list = my_list + [4]
my_list.append(4)
print("Exercise 6:")
print("my_list after adding 4:", my_list)
print("-" * 30)
 
# Exercise 7: Replace the first element in your list. 

my_list[0] = 5
print("Exercise 7:")
print("my_list after replacing first element with 5:", my_list)
print("-" * 30)
 
# Exercise 8: Sort your list alphabetically. 

my_list.sort()
print("Exercise 8:")
print("my_list after sort:", my_list)
print("-" * 30)
 
# Exercise 9: Use reassignment to add an element to your tuple. 

my_tuple += (4,)
print("Exercise 9:")
print("my_tuple after adding 4:", my_tuple)
print("-" * 30)
