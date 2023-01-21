import math
import random

new_numbers = [2**i for i in range(1, 11) if i > 5]
print(new_numbers)


math_numbers = [math.sqrt(i) for i in range(1, 11) if i % 2 == 0]
print(math_numbers)


team1 = random.choice(["mike", "derek", "doug"])
team2 = random.choice(["dave", "rickey", "pete"])


big_team = team1 + team2
team_paired = list(zip(team1, team2))

ran_team = random.choices(team_paired)
print(f"{team1} vs {team2}")



