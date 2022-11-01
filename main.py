rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
num = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)
if num == 0 and computer_choice == 1:
  print(f"Computer chose: {paper}\n")
  print("You lose")
elif num == 0 and computer_choice == 2:
  print(f"Computer chose: {scissors}\n")
  print("You win.")
if num == 1 and computer_choice == 2:
  print(f"Computer chose: {scissors}\n")
  print("You lose")
elif num == 1 and computer_choice == 0:
  print(f"Computer chose: {rock}\n")
  print("You win")
if num == 2 and computer_choice == 0:
  print(f"Computer chose: {rock}\n")
  print("You lose")
elif num == 2 and computer_choice == 1:
  print(f"Computer chose: {paper}\n")
  print("You win")
if num == computer_choice:
  print("Computer chose the same as you, tie.")
