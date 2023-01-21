car_brands = ["bmw ", "ferari", "mclaren", "  toyoya  ", "  ford "]

normalization_functions = [str.strip, str.lower]


def normalize_brands(brand_list, functions):
    normalize_brands = []
    for brand in brand_list:
        for func in functions:
            brand = func(brand)
        normalize_brands.append(brand)
    return normalize_brands


normalized_brands = normalize_brands(car_brands, normalization_functions)
print(normalized_brands)


# Python Lambda Functions
# Basic Syntax
# lambda arguments : expression

cubic = lambda number: number**3
print(cubic(2))

# Multiple parameter example
exponential = lambda multiplier, number, exponent: multiplier * (number**exponent)
print(exponential(2, 2, 3))


# Examples using lambda functions with other built-in functions
numbers = [2, 4, 5]
cubics = list(map(lambda number: number**3, numbers))
print(cubics)

filtered_list = list(filter(lambda number: number % 2 == 0, numbers))
print(filtered_list)


# Lambda functions as arguments
# Basic syntax
# To use a list comprehension to replace a regular for loop, we can make:

# [expression for item in list]

# Which is the same as doing:
# for item in list:
#     expression

# If we want some conditional to apply the expression, we have:

# [expression for item in list if conditional ]
# Which is the same as doing:

# for item in list:
#     if conditional:
#         expression

# Regular way
numbers = [1, 2, 3, 4, 5]
# new_list = []

# for n in numbers:
#     new_list.append(n**3)


# Using list comprehensions

new_list = [n**3 for n in numbers]
print(new_list)

cube_list = [n**3 for n in numbers if n > 3]
print(cube_list)


def cube(number):
    return number**3


func_list = [cube(n) for n in numbers if n > 3]
print(func_list)


word = "movie"
sliced = word[::-1]
print(sliced)
