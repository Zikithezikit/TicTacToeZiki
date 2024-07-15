import os


def clear():
    #   Clears the terminal(for most of the os)
    os.system('cls' if os.name == 'nt' else 'clear')


def newFrame(gameCells):
    clear()
    print("-----------------")
    for i in range(0,3):
        for j in range(0,3):
            print(f"| {gameCells[i + j]} |",end =" ")
        print()
        print("-----------------")

        

def ticTac():
    clear()
    # Rules
    print("> Enter the cell number that you wish to select ")
    print(" 7 | 8 | 9 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 1 | 2 | 3 ")
    # Create game positions
    gameCells = ["~","~","~","~","~","~","~","~","~"]

    # Game logic:
    while(True):
        command = input("> ")
        





    newFrame(gameCells)



def main():
    ticTac()



main()