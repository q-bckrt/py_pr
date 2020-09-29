#a simple rock/paper/scissors game
#player vs. computer version
from random import randint

print("*************************")
print("** ROCK PAPER SCISSORS **")
print("*************************")

def get_player_input(p_name):
    inputok = False
    while True:
        hand = input(f"{p_name}'s choice: ").lower()
        if (not (hand == "rock" or hand == "paper" or hand == "scissors")
        or not hand):
            print("input must be either 'rock', 'paper' or 'scissors'")
        else:
            return hand
def get_comput_input():
    n = randint(0, 2)
    if n == 0:
        return "rock"
    elif n == 1:
        return "paper"
    else:
        return "scissors"


play_again = "y"
while play_again == "y":
    p_wins = 0
    c_wins = 0
    print("==>first to get 3 games win!<==\n")
    while p_wins < 3 and c_wins < 3:
        p1_hand = get_player_input("Player 1")
        p2_hand = get_comput_input()

        print("computer played:", p2_hand)
        if (p1_hand == "rock" and p2_hand == "scissors"
        or p1_hand == "paper" and p2_hand == "rock"
        or p1_hand == "scissors" and p2_hand == "paper"):
            print("Player 1 wins!")
            p_wins += 1
        elif p1_hand == p2_hand:
            print("Draw!")
        else:
            print("Computer wins!")
            c_wins += 1
        print(f"current score: player[{p_wins}] vs. computer[{c_wins}]")
    if c_wins < p_wins:
        print("you win!")
    else:
        print("computer win!")
    play_again = input("play again? (y/*): ")
