# Homework 1 MARTH16B

import math

# Problem 1

def quadratic_sum(num_a, num_b, num_c):
    """Computes (a + b + c)^2 using the identity formula.""" 
    summation_result = (num_a + num_b + num_c) ** 2
    return summation_result

def geometric_mean(val_x, val_y):
    """Computes the geometric mean of two numbers."""
    return (val_x * val_y) ** 0.5

def distance_2d(coord_x1, coord_y1, coord_x2, coord_y2):
    """Computes the distance between two points in 2D space."""
    return ((coord_x2 - coord_x1) ** 2 + (coord_y2 - coord_y1) ** 2) ** 0.5

def weighted_average(data_x, data_y, weight_1, weight_2):
    """Computes the weighted average of two numbers."""
    return (data_x * weight_1 + data_y * weight_2) / (weight_1 + weight_2)

# Problem 2

def middle_chars(txt):
    """Returns the middle character(s) of a string."""
    length = len(txt)
    mid_idx = length // 2
    return txt[mid_idx] if length % 2 == 1 else txt[mid_idx - 1 : mid_idx + 1]

def swap_first_last(txt):
    """Swaps the first and last characters of a string."""
    if len(txt) <= 1:
        return txt
    return txt[-1] + txt[1:-1] + txt[0]

def reverse_concat(str_one, str_two):
    """Concatenates the reversed versions of two strings."""
    return str_one[::-1] + str_two[::-1]

# Problem 3

def digit_sum(num_value):
    """Computes the sum of digits of an integer."""
    absolute_value = abs(num_value)
    digit_list = [int(digit) for digit in str(absolute_value)]
    sum_of_digits = sum(digit_list)
    return sum_of_digits

def char_from_number(code_value):
    """Returns the ASCII character for a number between 32 and 126."""
    if 32 <= code_value <= 126:
        character_result = chr(code_value)
        return character_result
    return None

def concat_squares(num_m, num_n):
    """Concatenates the squares of two numbers as a string."""
    square_m = num_m ** 2
    square_n = num_n ** 2
    concatenated_result = str(square_m) + str(square_n)
    return concatenated_result