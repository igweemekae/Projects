import random

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

#Write your code below this line 👇
gameImages = [rock, paper, scissors]

userChoice = int(input("What do you choose? choose 0 for Rock, 1 for Paper or 2 for Scissors"))
print(gameImages)[userChoice]

computerChoice = random.randint(0,2)
print(f"Computer chose {computerChoice}")
print(gameImages[computerChoice])

if userChoice >= 3 or userChoice < 0:
    print("You typed an invalid number, you lose!")
elif userChoice == 0 and computerChoice == 2:
    print("Hey! you win!")
elif computerChoice == 0 and userChoice == 2:
    print("Hey! you loose")
elif computerChoice > userChoice:
    print("You loose")