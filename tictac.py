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
    print("-----------------")
    print()
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

def ticTac():
    clear()
    user = True
    # Rules
    print("> Enter the cell number that you wish to select(Note the first player is X)")
    print(" 7 | 8 | 9 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 1 | 2 | 3 ")
    # Create game positions
    gameCells = ["1","2","3","4","5","6","7","8","9"]

    # Game logic:
    while(True):
        # command = input("> ")
        # if(validateInput(command)):
        #     if(gameCells[int(command)-1]=="~"):
        #         addToList(gameCells,user,command)
        #     else:
        #         command = input("""> This cell is occupied select another
        #                         > """)
        # else:
        #     command = input("""> This is not valid input please select a number between 1-9
        #                     >  """)
        newFrame(gameCells)
        break




    newFrame(gameCells)



def main():
    ticTac()



main()