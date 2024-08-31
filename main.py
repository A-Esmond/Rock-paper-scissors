import random


def choices_conversion(choice):
  if choice == "rock":
    return 1
  elif choice == "paper":
    return 2
  else:
    return 3



def winner(cpu_choice, player_choice):
  cpu_choice = choices_conversion(cpu_choice)
  player_choice = choices_conversion(player_choice)
  if cpu_choice == player_choice:
    return 3
  elif  (player_choice == 1 and cpu_choice == 3) or \
   (player_choice == 2 and cpu_choice == 1) or \
   (player_choice == 3 and cpu_choice == 2):
    return 1
  else:
    return 2

def cpu_choice():
  cpu_choice = random.choice(["rock", "paper", "scissors"])
  return cpu_choice

def gametime():
  winner = 0
  player_score = 0
  cpu_score = 0
  while player_score < 10 and cpu_score < 10:
    player_choice = input("Enter your choice: ")
    cpu_choice()
    print(f"CPU choice: {cpu_choice}")
    winner = winner(cpu_choice, player_choice)
    if winner == 1:
      player_score += 1
    elif winner == 2:
      cpu_score += 1 
    else:
      print("Tie, no points awarded")
    print(f"Player score: {player_score}")
    print(f"CPU score: {cpu_score}")
    print("\nNext round")
  if player_score == 10:
    print("Player wins!")
  if cpu_score == 10:
    print("CPU wins!")
  resume = input("Would you like to play again? (y/n): ")
  if resume == "y":
    gametime()
  else:
    print("Thanks for playing!")


gametime()