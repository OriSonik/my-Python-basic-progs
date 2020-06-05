import random

def check_color_accuracy(index):
  if user_input[index] == random_color[index]:
    print('[correct]')
  elif user_input[index] in random_color:
    print('[swap]')
  else:
    print('[wrong]')

print('Welcome to the Mastermind')
print('Each digit represents one color, remember...')
print('You will need to guess a 4-digit number, representing a 4-counter row of colors')
print('Only one rule applies - the 4 digit code is within 1000 - 9999 range')
print(' ')
user_name = input('What is your name, Player? ')
print('Ready to become the Mastermind Master, ' + user_name + '?')
print('Start...')

random_color = str(random.randint(1000,10000))

user_input = None
while user_input != random_color:
  user_input = input('Guess the 4 counters: ')
  check_color_accuracy(0) 
  check_color_accuracy(1)
  check_color_accuracy(2)
  check_color_accuracy(3)

print('Congratulations, you are the new Mastermind Master!')