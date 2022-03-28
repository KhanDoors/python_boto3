# x= 0
# while x < 5:
#     print("Not there yet, x=" + str(x))
#     x = x + 1

# print("x=" + str(x))

# def attepmts(n):
#     x = 1
#     while x <= n:
#         print("Not there yet, x=" + str(x))
#         x += 1
#     print("done")

# attepmts(5)

# for x in range(5):
#     print("Not there yet, x=" + str(x))

# friends = ["Jim", "Karen", "Kevin"]
# for friend in friends:
#     print("Hello " + friend)

# values = [17, 42, 30, 40, 45]
# sum = 0
# length = 0
# for value in values:
#     sum += value
#     length += 1

# print("Totla Sum: " + str(sum) + " Average: " + str(sum/length))

# product = 1
# for n in range(1,10):
#     product = product * n
# print(product)

# def to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5/9

# for fahrenheit in range(0,101,5):
#     print("Fahrenheit: " + str(fahrenheit) + " Celsius: " + str(to_celsius(fahrenheit)))

# for left in range(7):
#     for right in range(left, 7):
#         print("[" + str(left) + "|" + str(right) + "]", end=" ")
#     print()


# teams = ["Dragons", "Wolves", "Raptors", "Sharks", "Grizzlies"]
# for home_teams in teams:
#     for away_teams in teams:
#         if home_teams != away_teams:
#            print("Game: " + home_teams + " vs. " + away_teams)

#     print()


def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n - 1)
    print("Returning " + str(result) + " from factorial of " + str(n))
    return result


factorial(5)
