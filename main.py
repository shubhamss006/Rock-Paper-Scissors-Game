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
print(f"computer choose :{computer_choice}")
print(image[computer_choice])

if your_choice==0 and computer_choice ==2:
    print("you win!")
elif your_choice >= 3 or your_choice <0:
    print("invalid input retry")
elif computer_choice==0 and your_choice==2:
    print("you loose")
elif computer_choice > your_choice:
    print("computer win")
elif your_choice > computer_choice:
    print("you win!")
elif your_choice==0 and computer_choice== 1 :
    print("you win")
elif computer_choice==0 and your_choice ==1:
    print("you loose")
elif your_choice == computer_choice:
    print("its tie play rematch")

else :
    print("you put a wrong input so the replay the the with correct input!")
