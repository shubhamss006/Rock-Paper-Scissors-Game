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
image = [rock , paper,scissors]
your_choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if your_choice<=2 or your_choice>=0:
    print(image[your_choice])
computer_choice =random.randint(0,2)
print(f"Computer choose :{computer_choice}")
print(image[computer_choice])

if your_choice==0 and computer_choice ==2:
    print("You win!")
elif your_choice >= 3 or your_choice <0:
    print("Invalid input retry")
elif computer_chose==0 and your_chose==2:
    print("You lose")
elif computer_chose > your_chose:
    print("Computer win")
elif your_chose > computer_chose:
    print("You win!")
elif your_chose==0 and computer_chose== 1 :
    print("You win")
elif computer_chose==0 and your_chose ==1:
    print("You lose")
elif your_chosee == computer_chose:
    print("its tie play rematch")

else :
    print("you put a wrong input so the replay the the with correct input!")
