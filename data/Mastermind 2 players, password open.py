player1_input = list(input('Graczu numer 1, podaj sekretny 4-cyfrowy kod: '))

def check_digit_accuracy(index):
  if player2_input[index] == player1_input[index]:
    print('[dobrze]')
  elif player2_input[index] in player1_input:
    print('[zmien miejsce]')
  else:
    print('[zle]')

print('Witaj w Mastermind, Graczu numer 2...')
print('Jestes gotowy/a na podjecie wyzwania...?')
print('Przed Toba zadanie polegajace na znalezieniu 4-cyfrowej liczby')
print(' ')
user_name2 = input('Jak masz na imie? ')
print('Mozemy zaczynac przygode, ' + user_name2 + '?')
print('3... 2... 1... Start...')

player2_input = None
while player2_input != player1_input:
  player2_input = input('Zgadnij 4 cyfry: ')
  check_digit_accuracy(0) 
  check_digit_accuracy(1)
  check_digit_accuracy(2)
  check_digit_accuracy(3)

print('Congratulations, you are the new Mastermind Master!' + user_name2 )