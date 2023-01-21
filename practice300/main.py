# p = 1000
# i = 0.03
# y = 5

# v = (p * i) * y
# print(v)

# filename = "view.jpg"
# ext = filename[-4:]
# print(ext)
# string = "PKV-89415-PLN"
# print(string[:3] + string[-3:])


# text = "Python Course"

# print(text[::-1])

# var1 = ""
# var2 = " "
# var3 = "\n"

# print(type(var1), "\n", type(var2), "\n", type(var3))


# text = "Python programming"
# newtext = text.lower()

# newtext = list(set(newtext))
# newtext.remove(" ")
# newtext.sort()
# print(newtext)

# 'append' adds to the end of a list
# cities = ["Los Angeles", "New York", "Chicago"]

# cities.append("Houston")

# print(cities)


# 'insert' allows you to place the new item to9 an exact position

# filenames = ["view.jpg", "bear.jpg", "ball.png"]

# filenames.insert(0, "phone.jpg")
# filenames.remove("ball.png")
# print(filenames)

# 'extend' adds one list on to the end of another
# day1 = ["3984", "9042", "4829", "2380"]

# day2 = ["4231", "5234", "1345", "2455"]

# day1.extend(day2)
# print(day1)


# sort a tuple -- you have to turn it back into a tuple or it will convert to a list
# techs = ("python", "java", "sql", "aws")
# techs = tuple(sorted(techs))
# print(techs)


# hashtags = ["summer", "time", "vibes"]
# print("#" + "* ".join(hashtags))


# dict = {"USA": "Washington", "Germany": "Berlin", "Austria": "Vienna"}

# print(dict.keys())

# items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]

# newitems = [i for i in items if i % 2 == 0]
# print(newitems)
# items = [1, 5, 3, 2, 2, 4, 2, 4]

# text = "Python is a very popular programming language"
# new_list = text.lower()
# new_list = new_list.split(" ")
# print(new_list[:4])


# probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]

# new = [i for i in probabilities if i >= 0.5]
# print(new)

# result = []

# for i in probabilities:
#     if i >= 0.5:
#         result.append(1)
#     else:
#         result.append(0)
# print(result)

# items = ["x", "y", "z", "y", "x", "y", "y", "z", "x"]

# freq = {}
# for item in items:
#     if item not in freq.keys():
#         freq[item] = 1
#     else:
#         freq[item] += 1

# print(freq)

# def maximum(a,b):
#     if a > b:
#         return a
#     else:
#         return b

# def mutlti(*args):
#     result = 1
#     for i in args:
#         result *= i
#     return result

# testlist = ["test1.txt", "test2.txt", "test3.csv", "test4.png", "test5.png"]

# testgrp = ["*.txt", "*.csv"]


# for i in testlist:
#     if i.__contains__(".txt" or ".csv"):
#         print(i)
# for i in testlist:
#     if i.endswith(".txt"):
#         testgrp.append(i)
#         print(i)
#     elif i.endswith(".csv"):
#         testgrp.append(i)
#         print(i)
#         print(testgrp)
#     else:
#         testgrp.append(i)


# list1 = [1, 2, 0]
# list2 = [4, 5, 6, 1]

# for i in list1:
#     if i in list2:
#         result = True
#         break
# print(result)
# hashtags = ["holiday", "sport", "fit", None, "fashion"]

# for i in hashtags:
#     if i != str:
#         result = False
# print(result)

# number = 13

# if number > 1:
#     for i in range(2, number):
#         if number % i == 0:
#             print(f"{number} - not a prime number")
#             break
#     else:
#         print(f"{number} - prime number")
# else:
#     print(f"{number} - not a prime number")

# x = -1.5
# expression = "x**2 + x"
# print(eval(expression))

# var1 = "Python"
# var2 = "Python"
# var3 = ("Python",)
# var4 = ["Python"]
# var5 = {"Python"}

# print(isinstance(var1, tuple))
# print(isinstance(var2, tuple))
# print(isinstance(var3, tuple))
# print(isinstance(var4, tuple))
# print(isinstance(var5, tuple))

# characters = ["k", "b", "c", "j", "z", "w"]

# print(min(characters))
# print(max(characters))

stocks = ["playway", "boombit", "cd projekt"]
length = list(map(lambda stock: len(stock), stocks))
print(length)
