import random
def roll():
    min_roll = 1
    max_roll = 6
    roll = random.randint(min_roll,max_roll)

    return roll

while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 5:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
player_score = [0 for i in range(players)]

while max(player_score) < max_score:
    for player_idx in range(players):
        print("\nplayer number",player_idx + 1,"turn just started")
        print("ur total scores is",player_score[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("would u like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("turn down u got 1")
                current_score = 0
                break

            else:
                current_score += value
                print("you rolled a ",value)

            print("ur score is ",current_score)

        player_score[player_idx] += current_score
        print("ur total score is",player_score[player_idx])

max_score = max(player_score)
winning_index = player_score.index(max_score)
print("player number ", winning_index + 1, "is the winner with the score of", max_score)







