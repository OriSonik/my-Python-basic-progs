# Compare of dict and list speed and when to use it

# utils - messure time

import time
import random

REPAET = 10

#https://book.pythontips.com/en/latest/args_and_kwargs.html
def messure_time(fun_to_execute, *args, **kwargs):
    start = time.time()
    fun_to_execute(*args, **kwargs)
    end = time.time()
    print(fun_to_execute.__name__ + " function took " + str((end - start) * 1000.0) + " ms" )

# same using decorators
# https://realpython.com/primer-on-python-decorators/
# def messure_time_dec(fun_to_execute):
#     def wrap(*args, **kwargs):
#         start = time.time()
#         result = fun_to_execute(*args, **kwargs)
#         end = time.time()
#         print('{:s} function took {:.8f} ms'.format(fun_to_execute.__name__, (end - start)*1000.0))
#         return result
#     return wrap


def my_function_to_messure(long_list):
    sum_of_elements = 0
    print("Hello its my_function_to_messure")
    for elem in long_list:
        sum_of_elements = elem
    return sum_of_elements


# Input data
long_list_to_hadle = [random.randint(0, 100) for iter in range(1000000)]

# Using of first function
messure_time(my_function_to_messure, long_list_to_hadle)

# Using of second function
# my_function_to_messure = messure_time_dec(my_function_to_messure)
# my_function_to_messure(long_list_to_nadle)

#################################################
# Add new funtion based on messure_time function with modifcations:
# it should call function_to_execute REPATE times
# sum elapsed time and divide by REPATE
# print avg time of function execuption
#################################################

# TODO
def messure_avg_time(fun_to_execute, *args, **kwargs):
    pass

# Input data
# long_list_to_nadle = [random.randint(0, 100) for iter in range(100000)]

# Using of first function
# messure_avg_time(my_function_to_messure, long_list_to_nadle)

#########################################################################################################
# Create list of 50.000 random integers from 0 to 100
# Split list to two list where first contains numbers < 50 and second >= 50
# Split list to two dict where first contains numbers < 50 and second >= 50 (key=value)
#########################################################################################################

#TODO

#########################################################################################################
# Create list of 1.000.000 random integers from 0 to 100.000.000
# Create dict of 1.000.000 random integers from 0 to 100.000.000 (key = integer)(value = empty string)
# Get random number from 0 to 100.000.000 and check if it exist in list and dict
#########################################################################################################

#TODO

#########################################################################################################
# Create list of 50.000 random integers from 0 to 100
# Create dict of 50.000 random integers from 0 to 100
# Delete from list and dict all od numbers
# messure time of both approches
#########################################################################################################

#TODO