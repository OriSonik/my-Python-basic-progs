import random
board = ["A", "   ", "   ", "   ", "B", "   ", "   ", "   ", "C", "   ", "   ", "   "]  # empty board - starting point
validInput = ["a1", "a2", "a3", "1a", "2a", "3a", "1b", "2b", "3b", "b1", "b2", "b3", "c1", "c2", "c3", "1c", "2c", "3c"]


def firstExplanation():
    print("Type a number to pick one of options.\n")


def menu():
    print("Options:")
    print("1.   Play against stupid AI")
    print("2.   Play against smart AI")
    print("3.   Play up to 3 wins against smart AI")
    print("4.   2-Players Mode")
    print("5.   2-Players Mode up to 3 wins")
    print("6.   How to play?")
    print("7.   Print board")
    print("8.   Quit")
    user_input = input("Enter a number: ")
    user_input = user_input  # makes every input lowercase

    if user_input == "quit" or user_input == "8":   # exit
        print("Farewell, traveller!")
        exit()
    elif user_input == "1":     # single player against stupid AI
        computerMode()
    elif user_input == "2":     # single player against smart AI
        smartComputerMode()
    elif user_input == "3":     # extended single player against AI
        computerMode3Wins()
    elif user_input == "4":     # 2-players mode
        twoPlayersMode()
    elif user_input == "5":     # extended 2-players mode (up to 3 wins)
        twoPlayersMode3Wins()
    elif user_input == "6":     # how to play
        print("\n\nEach player is supposed to pick the proper field. The options varies from 1a to 3c. "
              "\nYou will see the board printed before the first move.\n"
              "\nTo pick the field you should insert for example \"1a\" or \"a1\" or \"1A\" or \"1A\"."
              "\nThe result of example above is the same but all of these inputs are valid."
              "\nIf you pick wrong field, you will have another chances to insert proper one.\n\n")
        menu()
    elif user_input == "7":     # print board
        print("\n\nYou want to see how the board looks like before you start, huh? Well, okay, it is not prohibited. There you go:\n")
        resetBoard()
        printBoard()
        print("\n\n")
        menu()
    else:
        print("\n\nGuy, what the hell? There is no such thing. Try again or else...\n\n")
        menu()


def printBoard():   # printing board
    a = 0
    space = " " * 3
    print(space + "1" + space + "2" + space + "3")
    while a < 12:  # function which prints the board
        if a % 4 == 0 and a != 0:
            print("\n  ------------")
        print(str(board[a]) + "|", end="")
        a += 1
        if a % 12 == 0:
            print("\n  ------------")


def chooseSign():   # function which asks first player to choose a sign and assigns the second sign to second player
    firstPlayerInput = input("Player 1: Pick sign X or O: ").upper()  # upper to capitilise all letters
    if firstPlayerInput == "X":  # assigning signs to players
        print("You picked \"X\". Congratulations, it is super-duper awesome choice!")
        return " X ", " O "
    elif firstPlayerInput == "O" or firstPlayerInput == "0":
        print("You picked \"O\". Congratulations, it is absolutely uber flawless choice!")
        return " O ", " X "
    elif firstPlayerInput != "O" or "X" or "0":
        print("Mate, what's wrong with you? There is no such sign as " + str(firstPlayerInput) + ". We picked \"X\" for you!")
        return " X ", " O "


def winEvent(playerSign, player, board):  # checking whether winning condition were met
    condition1 = board[1] == board[2] == board[3] == playerSign
    condition2 = board[5] == board[6] == board[7] == playerSign
    condition3 = board[9] == board[10] == board[11] == playerSign
    condition4 = board[1] == board[5] == board[9] == playerSign
    condition5 = board[2] == board[6] == board[10] == playerSign
    condition6 = board[3] == board[7] == board[11] == playerSign
    condition7 = board[1] == board[6] == board[11] == playerSign
    condition8 = board[3] == board[6] == board[9] == playerSign
    if condition1 or condition2 or condition3 or condition4 or condition5 or condition6 or condition7 or condition8:
        return True

def isEmptyField(sign, boardNumber, player):    # checks if field is empty
    if board[boardNumber] == "   ":
        board[boardNumber] = sign
        printBoard()
    else:
        print("This field is already taken. Try something else!")
        playerMove(player, sign)


def pickValidation(userInput, sign, player):    # analyzes whether input is valid or not
    if userInput in validInput:
        for number in range(1, 4):  # goes through range till it reaches the input inserted by player
            if (userInput == str(number) + "a") or (userInput == "a" + str(number)):
                isEmptyField(sign, number, player)
            elif (userInput == str(number) + "b") or (userInput == "b" + str(number)):
                isEmptyField(sign, number + 4, player)
            elif (userInput == str(number) + "c") or (userInput == "c" + str(number)):
                isEmptyField(sign, number + 8, player)
        return True


def resetBoard():
    board[1] = board[2] = board[3] = board[5] = board[6] = board[7] = board[9] = board[10] = board[11] = "   "


def threeWinsStanding(firstPlayerPoints, secondPlayerPoints):
    if firstPlayerPoints == 3 or secondPlayerPoints == 3:
        if firstPlayerPoints == 3:
            print("Congratulations! Player 1 won extended game!")
            menu()
        if secondPlayerPoints == 3:
            print("Congratulations! Player 2 won extended game!")
            menu()
        return False
    else:
        return True


def twoPlayersMode3Wins():
    firstPlayerSign, secondPlayerSign = chooseSign()
    firstPlayer = "Player 1"
    secondPlayer = "Player 2"
    resetBoard()
    printBoard()
    firstPlayerPoints = 0
    secondPlayerPoints = 0
    tieGame = "Boring game. It is a tie... No points for any of you"
    currentStanding = "The current standing is:\nFirst player has %d points.\nSecond player has %d points."


    while board.count("   ") != 0:
        if freeFields() and threeWinsStanding(firstPlayerPoints, secondPlayerPoints):
            playerMove(firstPlayer, firstPlayerSign)
        if winEvent(firstPlayerSign, firstPlayer, board) == True:  # validation whether there is a winner or not
            firstPlayerPoints += 1
            print(currentStanding % (firstPlayerPoints, secondPlayerPoints))
            if firstPlayerPoints != 3:  # prevents from printing in case the game has ended
                resetBoard()
                printBoard()
            if firstPlayerPoints == 3:
                print(firstPlayer + " won. Congratulations!")
        if board.count("   ") == 0:
            resetBoard()
            print(tieGame)
            print(currentStanding % (firstPlayerPoints, secondPlayerPoints))
            printBoard()

        if freeFields() and threeWinsStanding(firstPlayerPoints, secondPlayerPoints):
            playerMove(secondPlayer, secondPlayerSign)
        if winEvent(secondPlayerSign, secondPlayer, board) == True:  # validation whether there is a winner or not
            secondPlayerPoints += 1
            print(currentStanding % (firstPlayerPoints, secondPlayerPoints))
            if secondPlayerPoints != 3:  # prevents from printing in case the game has ended
                resetBoard()
                printBoard()
            if secondPlayerPoints == 3:
                print(secondPlayer + " won. Congratulations!")
        if board.count("   ") == 0:
            resetBoard()
            print(tieGame)
            print(currentStanding % (firstPlayerPoints, secondPlayerPoints))
            printBoard()


def twoPlayersMode():
    firstPlayerSign, secondPlayerSign = chooseSign()
    firstPlayer = "Player 1"
    secondPlayer = "Player 2"
    resetBoard()
    printBoard()

    while board.count("   ") != 0:
        if freeFields():
            playerMove(firstPlayer, firstPlayerSign)
        if winEvent(firstPlayerSign, firstPlayer, board) == True:  # validation whether there is a winner or not
            print(firstPlayer + " won. Congratulations!")
            menu()
        if freeFields():
            playerMove(secondPlayer, secondPlayerSign)
        if winEvent(secondPlayerSign, secondPlayer, board) == True:  # validation whether there is a winner or not
            print(secondPlayer + " won. Congratulations!")
            menu()

    print("Boring game. It is a tie...")
    menu()


def pickRandomField():  # selects random field in board for Computer purposes
    random1 = random.randint(1, 3)
    if random1 == 1:
        y = random.randint(1, 3)
    if random1 == 2:
        y = random.randint(5, 7)
    if random1 == 3:
        y = random.randint(9, 11)
    return y  # returns random value


def computerMove(sign):
    pickRandomField()
    storeRandomNumber = pickRandomField()
    z = 0
    while z < 1:
        if board[storeRandomNumber] == "   ":
            board[storeRandomNumber] = sign
            printBoard()
            pickRandomField()
            z += 1
        else:
            storeRandomNumber = pickRandomField()


def computerMode3Wins():
    firstPlayerSign, secondPlayerSign = chooseSign()
    firstPlayer = "Player 1"
    secondPlayer = "Computer"
    resetBoard()
    printBoard()
    firstPlayerPoints = 0
    secondPlayerPoints = 0
    tieGame = "Boring game. It is a tie... No points for any of you"
    currentStanding = "The current standing is:\nFirst player has %d points.\nSecond player has %d points."
    whoGoesFirst = random.randint(0,1)


    while board.count("   ") != 0:
        if whoGoesFirst == 0 or whoGoesFirst == 3:
            if whoGoesFirst == 0 and secondPlayerPoints != 3:
                print("Player 1 starts.")
                whoGoesFirst = 3
            if freeFields() and threeWinsStanding(firstPlayerPoints, secondPlayerPoints):
                playerMove(firstPlayer, firstPlayerSign)
            if winEvent(firstPlayerSign, firstPlayer, board) == True:  # validation whether there is a winner or not
                firstPlayerPoints += 1
                print("Player 1 won the round.")
                print(currentStanding % (firstPlayerPoints, secondPlayerPoints))
                whoGoesFirst = random.randint(0, 1)
                if firstPlayerPoints != 3:  # prevents from printing in case the game has ended
                    resetBoard()
                    printBoard()
            if board.count("   ") == 0:
                resetBoard()
                print(tieGame)
                print(currentStanding % (firstPlayerPoints, secondPlayerPoints))
                whoGoesFirst = random.randint(0, 1)
                printBoard()

        if whoGoesFirst == 1 or whoGoesFirst == 3:
            if whoGoesFirst == 1 and secondPlayerPoints != 3:
                print("Computer starts.")
                whoGoesFirst = 3
            if freeFields() and threeWinsStanding(firstPlayerPoints, secondPlayerPoints):
                smartComputerMove(secondPlayerSign)
                printBoard()
            if winEvent(secondPlayerSign, secondPlayer, board) == True:  # validation whether there is a winner or not
                secondPlayerPoints += 1
                print("Computer won the round.")
                print(currentStanding % (firstPlayerPoints, secondPlayerPoints))
                whoGoesFirst = random.randint(0, 1)
                if secondPlayerPoints != 3:  # prevents from printing in case the game has ended
                    resetBoard()
                    printBoard()
            if board.count("   ") == 0:
                resetBoard()
                print(tieGame)
                print(currentStanding % (firstPlayerPoints, secondPlayerPoints))
                whoGoesFirst = random.randint(0, 1)
                printBoard()


def computerMode():
    firstPlayerSign, secondPlayerSign = chooseSign()
    firstPlayer = "Player 1"
    secondPlayer = "Computer"
    resetBoard()
    printBoard()

    while board.count("   ") != 0:
        if freeFields():
            playerMove(firstPlayer, firstPlayerSign)
        if winEvent(firstPlayerSign, firstPlayer, board) == True:  # validation whether there is a winner or not
            print(firstPlayer + " won. Congratulations!")
            menu()
        if freeFields():
            computerMove(secondPlayerSign)
        if winEvent(secondPlayerSign, secondPlayer, board) == True:  # validation whether there is a winner or not
            print(secondPlayer + " won. Congratulations!")
            menu()
    print("Boring game. It is a tie...")
    menu()


def smartComputerMove(secondPlayerSign):
    if secondPlayerSign == " X ":   # assigning signs
        firstPlayerSign = " O "
    if secondPlayerSign == " O ":
        firstPlayerSign = " X "

    listOfMoves = [1, 2, 3, 5, 6, 7, 9, 10, 11]     # this is a list of possible boards to select
    copiedBoard = []    # creates empty list
    for x in board:     # makes a copy of board
        copiedBoard.append(x)

    # if Player started first, pick center field
    if board.count(firstPlayerSign) > board.count(secondPlayerSign):
        if board[6] == "   ":
            board[6] = secondPlayerSign
            return True

    # check if Computer can win and takes advantage of it
    for a in listOfMoves:
        if copiedBoard[a] == "   ":   # checks if there is a free space
            copiedBoard[a] = secondPlayerSign  # overwrites a free space
            if winEvent(secondPlayerSign, "Player 1", copiedBoard):   # checks if Computer won
                board[a] = secondPlayerSign
                return a
            else:
                copiedBoard[a] = "   "  # cleans field which doesn't makes Computer win

    # check if Player can win and block him
    for a in listOfMoves:
        if copiedBoard[a] == "   ":   # checks if there is a free space
            copiedBoard[a] = firstPlayerSign  # overwrites a free space
            if winEvent(firstPlayerSign, "Player 1", copiedBoard):   # checks if player won
                board[a] = secondPlayerSign
                return a
            else:
                copiedBoard[a] = "   "  # cleans field which doesn't makes computer win

    # if enemy picked two opposite fields and if Computer picked center one, pick middle
    if board[1] == firstPlayerSign and board[11] == firstPlayerSign:
        if board[6] == secondPlayerSign:
            pickMiddleField(secondPlayerSign)
        return True
    if board[3] == firstPlayerSign and board[9] == firstPlayerSign:
        if board[6] == secondPlayerSign:
            pickMiddleField(secondPlayerSign)
        return True

    # picking any of corner available
    cornerBoard = [1, 3, 9, 11]
    random1 = random.randint(0, 3)
    counter = 0
    while counter < 1:
        if board[cornerBoard[random1]] == "   ":
            board[cornerBoard[random1]] = secondPlayerSign
            counter += 1
            return True
        else:
            random1 = random.randint(0, 3)

    # pick middle if available
    if board[6] == "   ":
        board[6] = secondPlayerSign
        return True

    # otherwise pick middle fields
    pickMiddleField(secondPlayerSign)
    return True


def pickMiddleField(secondPlayerSign):
    cornerBoard = [2, 5, 7, 10]
    random1 = random.randint(0, 3)
    counter = 0
    while counter < 1:
        if board[cornerBoard[random1]] == "   ":
            board[cornerBoard[random1]] = secondPlayerSign
            counter += 1
            return True
        else:
            random1 = random.randint(0, 3)

def smartComputerMode():
    firstPlayerSign, secondPlayerSign = chooseSign()
    firstPlayer = "Player 1"
    secondPlayer = "Computer"
    resetBoard()
    printBoard()
    whoGoesFirst = random.randint(0,1)

    while board.count("   ") != 0:
        if whoGoesFirst == 0 or whoGoesFirst == 3:
            if whoGoesFirst == 0:
                print("Player 1 starts.")
                whoGoesFirst = 3
            if freeFields():
                playerMove(firstPlayer, firstPlayerSign)
            if winEvent(firstPlayerSign, firstPlayer, board) == True:  # validation whether there is a winner or not
                print("Congrats. First player has won!")
                menu()

        if whoGoesFirst == 1 or whoGoesFirst == 3:
            if whoGoesFirst == 1:
                print("Computer starts.")
                whoGoesFirst = 3
            if freeFields():
                smartComputerMove(secondPlayerSign)
                printBoard()
            if winEvent(secondPlayerSign, secondPlayer, board) == True:  # validation whether there is a winner or not
                print("Computer has won:(")
                menu()

    print("Boring game. It is a tie...")
    menu()


def freeFields():
    if board.count("   ") > 0:
        return True

def playerMove(player, sign):
        userInput = input(player + "(" + sign + "): Pick the field (like 1a, 2a, 3b): ").lower()
        if pickValidation(userInput, sign, player) != True:
            print("Your input is wrong. Please, try again.")
            playerMove(player, sign)

firstExplanation()
menu()