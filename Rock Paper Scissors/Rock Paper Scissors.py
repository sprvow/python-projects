
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
#import random
#choices = [rock, paper, scissors]
#answer = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
#print(choices[answer])

# Същото и за компютъра:
#comp_choose = random.randint(0, 2)
#print("Computer chose:")
#print(choices[comp_choose])

#if answer == comp_choose:
#    print("It's a draw.")
#elif (answer == 0 and comp_choose == 2) or \
#     (answer == 1 and comp_choose == 0) or \
#     (answer == 2 and comp_choose == 1):
#     print("You win!")
#else:
#    print("You lose.")

game = [rock , paper , scissors]
user_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
if user_choice >= 0 and user_choice <=2:
    print(game[user_choice])
import random
print("Computer choose:")
comp_choice = random.randint(0, 2)
if comp_choice >= 0 and comp_choice <= 2:
    print(game[comp_choice])

if user_choice < 0 or user_choice >= 3:
    print("Invalid number. You lose!")
elif user_choice == 0 and comp_choice == 2:
    print("You win!")
elif user_choice == 1 and comp_choice == 0:
    print("You win!")
elif user_choice == 2 and comp_choice == 1:
    print("You win")
elif user_choice == 0 and comp_choice == 0:
    print("It's a draw!")
elif user_choice == 1 and comp_choice == 1:
    print("It's a draw!")
elif user_choice == 2 and comp_choice == 2:
    print("It's a draw!")
else:
    print("You lose!")

    # Задача 3: Камък, ножица, хартия (Challenge 🥷)
    # 🧠 Списъци, random, input, логика, if условия

    # 🔹 Използвай списък с камък, ножица, хартия
    # 🔹 Потребителят въвежда число (0, 1 или 2)
    # 🔹 Компютърът избира random
    # 🔹 Покажи кой печели
    # 🔹 Но: ❗️без elif, само if + else

   # rock = '''
   #      _______
   #  ---'   ____)
   #        (_____)
   #        (_____)
   #        (____)
   #  ---.__(___)
   #  '''
   #
   #  paper = '''
   #      _______
   #  ---'   ____)____
   #            ______)
   #            _______)
   #           _______)
   #  ---.__________)
   #  '''
   #
   #  scissors = '''
   #      _______
   #  ---'   ____)____
   #            ______)
   #         __________)
   #        (____)
   #  ---.__(___)
   #  '''
   #
   #  all = [rock, paper, scissors]
   #  user_choise = int(input("Type a number: 0 for rock, 1 for paper, 2 for scissors. "))
   #  if user_choise == 0:
   #      print(rock)
   #  if user_choise == 1:
   #      print(paper)
   #  if user_choise == 2:
   #      print(scissors)
   #  if user_choise <= 0 or user_choise >= 3:
   #      print("Invalid Number.")
   #
   #  import random
   #
   #  comp_choice = random.choice(all)
   #  print(f"Computer choose:\n {comp_choice}")
   #
   #  if user_choise == comp_choice:
   #      print("It's a draw!")
   #  if user_choise == 0 and comp_choice == 2:
   #      print("You win!")
   #  if user_choise == 1 and comp_choice == 0:
   #      print("You win!")
   #  if user_choise == 2 and comp_choice == 1:
   #      print("You win!")
   #  else:
   #      print("You lose!")