import random
print("Welcome to SAS Gaming Centre!")
def GamingCentre():
    choice=input("enter p to play or q to quit:")
    if choice=="p":
        print("1. Tic Tac Toe")
        print("2. Slot Machine")
        print("3. Bagels")
        game=input("Which game do you want to play?")
        if game=="1":
            tic_tac_toe()
        elif game=="2":
            slot()
            GamingCentre()
        elif game=="3":
            guess()
            GamingCentre()
    elif choice=="q":
        return 
    else:
        print("Invalid Input")
        GamingCentre()

def guess():
    def getSecretNum():
        #to get a secret number!!
        numbers=["1","2","3","4","5","6","7","8","9"]
        random.shuffle(numbers)
        secretnumber=""
        for i in range(3):
            secretnumber+=numbers[i]
        return secretnumber
    def getGuess ():
    #To get input
        while True:
            guess=input("Enter your guess. It should be of three digits:")
            if guess.isdigit() and len(guess)==3:
                return guess
            else:
                print("Ïnvalid Input. Please try again")
    def getClues(secretnumber,guess):
        #To get the clues!
        if guess==secretnumber:
            return "Yeah! you got it."
        else:
            clues=[]
            for i in range(3):
                if guess[i]==secretnumber[i]:
                    clues.append("Fermi")
                elif guess[i] in secretnumber:
                    clues.append("Pico")
            if len(clues)==0:
                clues.append("Bagels")
        return clues
    def playgame():
        # Main function in which all helper functions are called!
        print("Bagels. A number guessing game")
        print("I am have 3 digit number. Try to guess what is it!")
        print("There are some clues for you:")
        print("  Pico :\tOne digit is correct but in the wrong position.")
        print("  Fermi :\tOne digit is correct and in the right position.")
        print("  Bagels :\tNo digit is correct.")
        secretnumber1= getSecretNum()
        guessleft=10
        while guessleft>0:
            guess1=getGuess()
            clues1=getClues(secretnumber1, guess1)
            print("Clues:", " ".join(clues1))
            if "Fermi" in clues1 and "Pico" not in clues1 and len(clues1)==3:
                print ("You guessed the correct number!")
                break
            guessleft-=1
            print("Guesses left: ",(guessleft))
    
        print("The correct number was" ,(secretnumber1))
    playgame()
 
 
            

def slot():

    ROWS=3
    COLUMNS=3

    number_of_letters={"A":3,"B":3,"C":3}
    winning_on_lines={"A":2, "B":2, "C":2}

    #now how much the user won
    def check_win(cols,lines,winning_on_lines,bet):
        win_amount=0
        winning_line=[]
        for i in range(lines):
            letter=cols[0][i]
            for j in range(len(cols)):
                check_letter=cols[j][i]
                if letter!=check_letter:
                    break
            else:
                win_amount+=(winning_on_lines[letter])*bet
                winning_line.append(i+1)
        return win_amount,winning_line

    #now print the slot machine with its spin
    def slot_machine_spin(number_of_letters):
        all_letters=[]
        for letter,number_of_letter in number_of_letters.items():
            for i in range(number_of_letter):
                all_letters.append(letter) 
        cols=[]
        for i in range(ROWS):
            col=[]
            current_letters=all_letters[:]
            for j in range(COLUMNS):
                value=random.choice(all_letters)
                current_letters.remove(value)
                col.append(value)
            cols.append(col)
        return cols

    #print like a board
    def print_machine(cols):
        for i in range(len(cols[0])):
            for j in cols:
                print(j[i],end=" | ")
            print()

    #collect the deposit amount
    def deposit():
        while True:
            deposit_amount=input("What amount would you like to deposit? $")
            if deposit_amount.isnumeric():
                deposit_amount=int(deposit_amount)
                if deposit_amount>0:
                    break
                else:
                    print("Please enter a valid amount!")
            else:
                print("Please enter a valid amount!")
        return deposit_amount

    #how many lines to bet on
    def ask_number_of_lines():
        while True:
            lines=input("How many lines would you like to bet on between (1-3)?")
            if lines.isdigit():
                lines=int(lines)
                if lines > 0 and lines < 4:
                    break
                else:
                    print("Please enter valid number of lines!")
            else:
                print("Please enter a valid number of lines!") 
        return lines

    #get the bet
    def get_bet():
        while True:
            bet=input("How much would you like to bet on each line between $(1-500) ?")
            if bet.isdigit():
                bet=int(bet)
                if bet>0 and bet<501:
                    break
                else:
                    print("Bet must be between $(1-500)")
            else:
                print("Please enter a valid bet")
        return bet



    def spin(account):
        while True:
            number_of_lines=ask_number_of_lines()
            bet_amount=get_bet()
            Total_bet=bet_amount*number_of_lines
            if Total_bet>account:
                print("You donot have sufficient balance!")
                return 0
            else:
                print("You are betting",bet_amount,"on each of the",number_of_lines,"lines,","Your total bet =",Total_bet)
                break
        spin=slot_machine_spin(number_of_letters)
        print_machine(spin)
        win,win_line=check_win(spin,number_of_lines,winning_on_lines,bet_amount)
        print("You won",win)
        print("You won on the following line(s): ", *win_line)
        return win - Total_bet

    def main():
        print("WELCOME TO SAS SLOT MACHINE!")
        account=deposit()
        print("Current balance is: $",account)
        while True:
            turn=input("Press any key (except q) to play or q to quit the game.")
            if turn == "q":
                break
            account+=spin(account)
            print("You left with $",account)
    main()

def tic_tac_toe():
    #demo list is to show the box numbers in the board
    demo=[["1","2","3"],["4","5","6"],["7","8","9"]]
    for i in demo:
        #print the board using items of demo list
        print(" | ".join(i))
        print("---------")
    play=input("Press S to start: ")
    if play=="S" or play=="s":
        #Board_items_list is the nested list of board items
        Board_items_list  = []
        for i in range(3):
            lst = []
            for j in range(3):
                lst.append(" ")
            Board_items_list.append(lst)
    else:
        print("Please Press S to start: ")
        tic_tac_toe()
    num_tuple=("1", "2", "3", "4", "5", "6", "7", "8", "9")

    def board(Board_items_list):
        for i in Board_items_list:
            #print the board using items of board list
            print(" | ".join(i))
            print("---------")


    board(Board_items_list)


    def player1(Board_items_list):
        while True:
            move = input("Player X, enter your move (1-9): ")
            if move in num_tuple and Board_items_list[(int(move) - 1) // 3][(int(move) - 1) % 3] == " ":
                #replacing the space with X in the nested list
                Board_items_list[(int(move) - 1) // 3][(int(move) - 1) % 3] = "X"
                break
            else:
                print("Invalid input. Try again.")
        board(Board_items_list)


    def player2(Board_items_list):
        while True:
            move = input("Player O, enter your move (1-9): ")
            if move in num_tuple and Board_items_list[(int(move) - 1) // 3][(int(move) - 1) % 3] == " ":
                #replacing the space with O in the nested list
                Board_items_list[(int(move) - 1) // 3][(int(move) - 1) % 3] = "O"
                break
            else:
                print("Invalid input. Try again.")
        board(Board_items_list)

        #check if board is full yet
    def full_board(Board_items_list):
        for i in Board_items_list:
            if " " in i:
                return False
        return True
    
    def win(Board_items_list):
        #check columns
        for i in range(3):
            if Board_items_list[0][i] == Board_items_list[1][i] == Board_items_list[2][i] and Board_items_list[0][i] == 'X':
                print("Player X won")
                return True
            if Board_items_list[0][i] == Board_items_list[1][i] == Board_items_list[2][i] and Board_items_list[0][i] == 'O':
                print("Player O won")
                return True
        #check rows
        for j in range(3):
            if Board_items_list[j][0] == Board_items_list[j][1] == Board_items_list[j][2] and Board_items_list[j][0] == 'X':
                print("Player X won")
                return True
            if Board_items_list[j][0] == Board_items_list[j][1] == Board_items_list[j][2] and Board_items_list[j][0] == 'O':
                print("Player O won")
                return True
        #check diagnols
        if Board_items_list[0][0] == Board_items_list[1][1] == Board_items_list[2][2] and Board_items_list[0][0] == 'X':
            print("Player X won")
            return True
        if Board_items_list[0][0] == Board_items_list[1][1] == Board_items_list[2][2] and Board_items_list[0][0] == 'O':
            print("Player O won")
            return True
        if Board_items_list[0][2] == Board_items_list[1][1] == Board_items_list[2][0] and Board_items_list[0][2] == 'X':
            print("Player X won")
            return True
        if Board_items_list[0][2] == Board_items_list[1][1] == Board_items_list[2][0] and Board_items_list[0][2] == 'O':
            print("Player O won")
            return True

        return False

    #main function
    def play(Board_items_list):
        i = 0
        #continue till board is full
        while not full_board(Board_items_list):
            #continue only if no one has won yet
            if not win(Board_items_list):
                if i%2==0:
                    player1(Board_items_list)
                    i+=1
                else:
                    player2(Board_items_list)
                    i+=1
            else:
                #used print to print an extra line after the winner announcement
                print()
                GamingCentre()
        if full_board(Board_items_list):
            print("It's a tie")
            #Go to the first page of the gaming centre after this game is finished
            GamingCentre()

    play(Board_items_list)
GamingCentre()