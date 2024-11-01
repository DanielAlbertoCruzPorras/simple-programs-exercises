# Get the number of games won by each player
games_a = int(input("Games won by A: "))
games_b = int(input("Games won by B: "))

# Determine the result based on the rules of a tennis set
if (games_a >= 7 or games_b >= 7) or (abs(games_a - games_b) > 2):
    print("Invalid result")
elif games_a == 6 and games_b <= 4:
    print("A wins")
elif games_b == 6 and games_a <= 4:
    print("B wins")
elif games_a == 7 and games_b == 5:
    print("A wins")
elif games_b == 7 and games_a == 5:
    print("B wins")
elif games_a == 7 and games_b == 6:
    print("A wins")
elif games_b == 7 and games_a == 6:
    print("B wins")
else:
    print("Set not finished yet")

