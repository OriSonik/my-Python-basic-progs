import random

def get_guess():
  
  # Ustanawianie dlugosci hasla oraz 10 zyc dla gracza
  dashes = "-" * len(secret_city)
  guesses_left = 10
  
  # Ta petla dziala dopoki OBA warunki sa spelnione:
  # 1. Liczba pozostalych zyc wieksza od -1
  # 2. String pustych liter nie jest tozsamy z poszukiwana nazwa miasta
  while guesses_left > -1 and not dashes == secret_city:
    
    # Print ilosc 'pustych miejsc' i pozostalych zyc gracza
    print(dashes)
    print (str(guesses_left))
    
    # Popros gracza o wprowadzenie odgadywanej nazwy miasta
    guess = input("Zgadnij litere: ")
    
    # Warunek wypisany po wprowadzeniu nieprawidlowej wartosci odgadywanej litery
    if len(guess) != 1:
      print ("Zgadnij tylko 1 litere!")
      
    # Update "pustych" miejsc w odgadywanej nazwie miasta i komunikat o sukcesie wprowadzania
    elif guess in secret_city:
      print ("Ta litera pojawia sie w odgadywanej nazwie miasta!")
      dashes = update_dashes(secret_city, dashes, guess)
      
    # Komunikat o nieodgadnietej literze wraz z informacja o odjeciu 1 zycia
    else:
      print ("Tej litery nie ma w nazwie. Tracisz jedno \' zycie \'!")
      guesses_left -= 1
    
  if guesses_left <= 0:
    print ("Przegrywasz. Poszukiwana nazwa miasta to: " + str(secret_city))
  
  # Jeśli w końcu ciag "pustych" liter zrowna sie wartoscia z poszukiwanym slowem - info o wygranej
  else:
    print ("Gratulacje! Wygrywasz! Poszukiwana nazwa miasta to: " + str(secret_city))
    
# Update string'u "pustych" liter zastepujac je literami odgadnietymi przez uzytkownika
def update_dashes(secret, cur_dash, rec_guess):
  result = ""
  
  for i in range(len(secret)):
    if secret[i] == rec_guess:
      result = result + rec_guess     # Dodaje prawidlowo odgadniete litery do string'a wynikowego
      
    else:
      # Dodaje "pusta" litere w indeksie i do string'a wynikowego, jesli litera nie zostala odgadnieta
      result = result + cur_dash[i]
      
  return result


capital_cities = []
with open('00capitals.txt') as f:
    for line in f:
        capital_cities.append(line.rstrip('\n'))
        

secret_city = random.choice(capital_cities)
get_guess()
