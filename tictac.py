import os


def clear():
    #   Clears the terminal(for most of the os)
    os.system('cls' if os.name == 'nt' else 'clear')

# Make sure the input is valid 
def validateInput(userInput):
    try:
        number = int(userInput)
        if 1 <= number <= 9:
            return True
        else:
            return False
    except ValueError:
        return False


def newFrame(gameCells):
    clear()
    for i in range(0,9):
        if i % 3 == 0 and i!=0:
            print()
            print("-----------------")
        print(f"| {gameCells[i]} |",end =" ")

def addToList(gameCells,user,number):

    if(user):
        gameCells[int(number)-1] = "X"
    else:
        gameCells[int(number)-1] = "O"        




def checkForWin(gameCells):
    # Rows
    if(gameCells[0] != "~" and gameCells[0]==gameCells[1]==gameCells[2]):
        return gameCells[0]
    if(gameCells[3] != "~" and gameCells[3] == gameCells[4] == gameCells[5]):
        return gameCells[3]
    if(gameCells[6] != "~" and gameCells[6]== gameCells[7] == gameCells[8]):
        return gameCells[6]
    # Columns 
    if(gameCells[0] != "~" and gameCells[0]==gameCells[3]==gameCells[6]):
        return gameCells[0]
    if(gameCells[1] != "~" and gameCells[1]==gameCells[4]==gameCells[7]):
        return gameCells[1]
    if(gameCells[2] != "~" and gameCells[2]==gameCells[5]==gameCells[8]):
        return gameCells[2]
    # Diagonals
    if(gameCells[0] != "~" and gameCells[0]==gameCells[4]==gameCells[8]):
        return gameCells[0]
    if(gameCells[2] != "~" and gameCells[2]==gameCells[4]==gameCells[6]):
        return gameCells[2]










def ticTac():
    clear()
    user = True
    # Rules
    print("> Enter the cell number that you wish to select(Note the first player is X)")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    # Create game positions
    gameCells = ["~","~","~","~","~","~","~","~","~"]



    # Game logic:
    while(True):
        if( checkForWin(gameCells) == "X" or checkForWin(gameCells) == "O"):
            clear()
            print(f"{checkForWin(gameCells)} is the winner")
            break
        print()
        command = input("> ")
        if(validateInput(command)):
            if(gameCells[int(command)-1]=="~"):
                addToList(gameCells,user,command)
                user = not user
            else:
                command = input("""> This cell is occupied select another
                                > """)
        else:
            command = input("""> This is not valid input please select a number between 1-9
                            >  """)
        newFrame(gameCells)




    newFrame(gameCells)



def main():
    ticTac()


if __name__ == "__main__":
    main()