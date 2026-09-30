first = input()
second = input()

if first == "rock" and second == "rock":
    print("Draw")
if first == "paper" and second == "paper":
    print("Draw")
if first == "scissors" and second == "scissors":
    print("Draw")


if first == "rock" and second == "paper":
    print("Player 2")
if first == "rock" and second == "scissors":
    print("Player 1")


if first == "paper" and second == "rock":
    print("Player 1")
if first == "paper" and second == "scissors":
    print("Player 2")

if first == "scissors" and second == "paper":
    print("Player 1")
if first == "scissors" and second == "rock":
    print("Player 2")
