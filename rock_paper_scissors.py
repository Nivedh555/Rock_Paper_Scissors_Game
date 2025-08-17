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
user_choose = int(input("What do you choose? choose 0 for rock, choose 1 for paper, choose 2 for scissors:"))
if user_choose == 0:
    print(rock)
elif user_choose == 1:
    print(paper)
elif user_choose == 2:
    print(scissors)
else:
    print("Invalid Input")

import random
list = [rock, paper, scissors]
computer = random.choice(list)
print(computer)

if (user_choose == 0 and computer == paper) or (user_choose == 1 and computer == scissors):
    print("You Loose")
elif (user_choose == 2 and computer == rock):
    print("You Loose")
elif (user_choose == 0 and computer == scissors) or (user_choose == 1 and computer == rock):
    print("You Win")
elif (user_choose == 2 and computer == paper):
    print("You Win")
else:
    print("Draw") 

