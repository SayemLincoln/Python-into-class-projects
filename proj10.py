#proj10 by Sayem Lincoln
from cards import Card, Deck

BANNER = """
    __        _____ _   _ _   _ _____ ____  _ _ _ 
    \ \      / /_ _| \ | | \ | | ____|  _ \| | | |
     \ \ /\ / / | ||  \| |  \| |  _| | |_) | | | |
      \ V  V /  | || |\  | |\  | |___|  _ <|_|_|_|
       \_/\_/  |___|_| \_|_| \_|_____|_| \_(_|_|_)

"""


RULES = """
     ____        _             _        ____
    | __ )  __ _| | _____ _ __( )___   / ___| __ _ _ __ ___   ___
    |  _ \ / _` | |/ / _ \ '__|// __| | |  _ / _` | '_ ` _ \ / _ \\
    | |_) | (_| |   <  __/ |    \__ \ | |_| | (_| | | | | | |  __/
    |____/ \__,_|_|\_\___|_|    |___/  \____|\__,_|_| |_| |_|\___|

    Cells:       Cells are numbered 1 through 4. They can hold a
                 single card each.

    Foundations: Foundations are numbered 1 through 4. They are
                 built up by rank from Ace to King for each suit.
                 All cards must be in the foundations to win.

    Tableaus:    Tableaus are numbered 1 through 8. They are dealt
                 to at the start of the game from left to right
                 until all cards are dealt. Cards can be moved one
                 at a time from tableaus to cells, foundations, or
                 other tableaus. Tableaus are built down by rank
                 and cards must be of the same suit.

"""


MENU = """

    Game commands:
    
    TC x y    Move card from tableau x to cell y
    TF x y    Move card from tableau x to foundation y
    TT x y    Move card from tableau x to tableau y
    CF x y    Move card from cell x to foundation y
    CT x y    Move card from cell x to tableau y
    R         Restart the game with a re-shuffle
    H         Display this menu of commands
    Q         Quit the game
    
"""
   
     
def valid_fnd_move(src_card, dest_card):
   #booleans for finding scr_card's and dsr_card's rank and suit
    if dest_card == ' ' and src_card.rank() == 1 or dest_card != ' ' and\
                            src_card.suit() == dest_card.suit() and \
                            src_card.rank() - dest_card.rank() == 1:

        return 0
    elif dest_card == ' ' and src_card.rank() != 1: #rank checking
        return 1
    elif dest_card.suit() != src_card.suit(): #suit checking
        return 2
    elif src_card.rank() - dest_card.rank() != 1: #rank checking
        return 3

  
      
def valid_tab_move(src_card, dest_card):
    #booleans for finding scr_card's and dsr_card's rank and suit
    if dest_card == ' ' or src_card.suit() == dest_card.suit() and dest_card.rank() - src_card.rank() == 1: #rank and suit checking
        return 0
    else:
        if dest_card.suit() != src_card.suit(): #suit checking
            return 1
        elif dest_card.rank() - src_card.rank() != 1: #rank checking
            return 2
    
def tableau_to_cell(tab, cell, tab_index, cell_index):
    #booleans for tab and cell indexing
    if cell[cell_index - 1] != ' ':
        raise RuntimeError('Invalid move: Cell is not empty')
    else:
        cell[cell_index - 1] = tab[tab_index - 1].pop() #cell indexing
            
def tableau_to_foundation(tab, fnd, tab_index, fnd_index):
         #booleans for tab and fnd check and indexing 
    if not len(tab[tab_index - 1]): #tab indexing
        raise RuntimeError('Invalid move: Tab column is empty')
    check = valid_fnd_move(tab[tab_index - 1][-1], fnd[fnd_index - 1]) #tab indexing
    if  not check: #tab checking and indexing
        fnd[fnd_index - 1] = tab[tab_index - 1].pop()  #fnd cindexing
    else:      
        if check == 1:
            raise RuntimeError('Invalid move: Source card is not an Ace')
        elif check == 2:
            raise RuntimeError('Invalid move: Wrong suit')
        else:
            raise RuntimeError('Invalid move: Wrong rank')
            
            
def tableau_to_tableau(tab, tab1_index, tab2_index):
     #booleans for tab check and indexing 
    if not len(tab[tab1_index - 1]):  #tab indexing
        raise RuntimeError('Invalid move: Tab1 column is empty')
    if len(tab[tab2_index - 1]) != 0:  #tab indexing
        check = valid_tab_move(tab[tab1_index - 1][-1], tab[tab2_index - 1][-1]) #tab indexing
    else:        
        check = 0
    if not check: #tab checking and indexing       
        tab[tab2_index - 1].append(tab[tab1_index - 1].pop()) #tab indexing
    else: #tab checking
        if check == 1:
            raise RuntimeError('Invalid move: Wrong suit')
        elif check == 2:
            raise RuntimeError('Invalid move: Wrong rank')


def cell_to_foundation(cell, fnd, cell_index, fnd_index):
        #booleans for cell check and indexing 
    if cell[cell_index - 1] == ' ':  #cell indexing
        raise RuntimeError('Invalid move: Cell is empty')
    check = valid_fnd_move(cell[cell_index - 1], fnd[fnd_index - 1])
    if not check:   #cell indexing
        fnd[fnd_index - 1] = cell[cell_index - 1]
        cell[cell_index - 1] = ' '
    else:   #cell checking
        if check == 1:
            raise RuntimeError('Invalid move: Source card is not an Ace')
        elif check == 2:
            raise RuntimeError('Invalid move: Wrong suit')
        else:
            raise RuntimeError('Invalid move: Wrong rank')


def cell_to_tableau(cell, tab, cell_index, tab_index):
       #booleans for cell check and indexing 
    if cell[cell_index - 1] == ' ':      #cell indexing
        raise RuntimeError('Invalid move: Cell is empty')
    if len(tab[tab_index - 1]) != 0:     #cell indexing
        check = valid_tab_move(cell[cell_index - 1], tab[tab_index - 1][-1])
    else:    #checking for tab and cell indexing
        check = 0
    if not check: #tab checking and indexing 
        tab[tab_index - 1].append(cell[cell_index - 1])
        cell[cell_index - 1] = ' '
    else:
        if check == 1:
            raise RuntimeError('Invalid move: Wrong suit')
        elif check == 2:
            raise RuntimeError('Invalid move: Wrong rank')
              
              
def is_winner(cell, tab):
       #boolean and looping for checking whether character is X or not
    if all([x == ' ' for x in cell]) and max([len(column) for column in tab]) == 0:
        return True
    else:
        return False


def setup_game():
    """
    The game setup function. It has 4 cells, 4 foundations, and 8 tableaus. All
    of these are currently empty. This function populates the tableaus from a
    standard card deck. 

    Tableaus: All cards are dealt out from left to right (meaning from tableau
    1 to 8). Thus we will end up with 7 cards in tableaus 1 through 4, and 6
    cards in tableaus 5 through 8 (52/8 = 6 with remainder 4).

    This function will return a tuple: (cells, foundations, tableaus)
    """
    
    #You must use this deck for the entire game.
    #We are using our cards.py file, so use the Deck class from it.
    stock = Deck()
    #The game piles are here, you must use these.
    cells = [' ', ' ', ' ', ' ']   #list of 4 lists
    foundations = [' ', ' ', ' ', ' ']    #list of 4 lists
    tableaus = [[], [], [], [], [], [], [], []] #list of 8 lists
    stock.shuffle()
    for i in range(len(stock)):
        tableaus[i % 8].append(stock.deal())
    return cells, foundations, tableaus


def display_game(cells, foundations, tableaus):
    """
    Add your function header here.
    """
    #Labels for cells and foundations
    print("    =======Cells========  ====Foundations=====")
    print("     --1----2----3----4--  --1----2----3----4--")
    print("    ", end="")
    print("   {0!s: <05}{1!s: <05}{2!s: <05}{3!s: <05}  {4!s: <05}{5!s: <05}{6!s: <05}{7!s: <05}".format(*cells, *foundations))
    # to print a card using formatting, convert it to string:
    # print("{}".format(str(card)))

    print()
    #Labels for tableaus
    print("    =================Tableaus=================")
    print("    ---1----2----3----4----5----6----7----8---")
    max_length = max([len(column) for column in tableaus]) #loop for length of column
    to_print_tableaus = [column + [' ']*(max_length - len(column)) for column in tableaus]
    for i in range(max_length): #loop for max_length
        to_print_row = [row[i] for row in to_print_tableaus]
        print("      {0!s: <05}{1!s: <05}{2!s: <05}{3!s: <05}{4!s: <05}{5!s: <05}{6!s: <05}{7!s: <05}".format(*to_print_row))



#Here is the main body of function
print(RULES)

cells, fnds, tabs = setup_game() #function callbacks
display_game(cells, fnds, tabs)  #function callbacks

print(MENU)
command = input("prompt :> ").strip().lower()  #input statement
while command != 'q':  #loop for quit
    try:  #booleans for finding index
        parameters = command.split()
        if parameters[0] in ('tf', 'tt', 'cf', 'ct', 'tc') and len(parameters) == 3:
            if parameters[0][0] == 't':
                if not 8 >= int(parameters[1]) >= 1:    
                    raise RuntimeError("Column index is out of range")
            elif parameters[0][0] == 'c':
                if not 4 >= int(parameters[1]) >= 1:
                    raise RuntimeError("Cell index is out of range")
            if parameters[0][1] == 't':
                if not 8 >= int(parameters[2]) >= 1:
                    raise RuntimeError("Column index is out of range")
            elif parameters[0][1] == 'f':
                if not 4 >= int(parameters[2]) >= 1:
                    raise RuntimeError("Foundation index is out of range")
            elif parameters[0][1] == 'c':
                if not 4 >= int(parameters[2]) >= 1:
                    raise RuntimeError("Cell index is out of range")
        elif len(parameters) == 1:            #boolean for h input
            if parameters[0] == 'h':
                print(MENU)
                display_game(cells, fnds, tabs)
                command = input("prompt :> ").strip().lower()
                continue
            elif parameters[0] == 'r':  #boolean for r input
                print(RULES)
                print(MENU)
                cells, fnds, tabs = setup_game()
                display_game(cells, fnds, tabs)
                command = input("prompt :> ").strip().lower()
                continue
            else:
                raise RuntimeError('Wrong command - ' + parameters[0])
        else:      #booleans for list maping according to input
            raise RuntimeError('Wrong format of command')
        if parameters[0] == 'tf':
            tableau_to_foundation(tabs, fnds, *list(map(int, parameters[1:3])))
        elif parameters[0] == 'tt':
            tableau_to_tableau(tabs, *list(map(int, parameters[1:3])))
        elif parameters[0] == 'cf':
            cell_to_foundation(cells, fnds, *list(map(int, parameters[1:3])))
        elif parameters[0] == 'ct':
            cell_to_tableau(cells, tabs, *list(map(int, parameters[1:3])))
        else:
            tableau_to_cell(tabs, cells, *list(map(int, parameters[1:3])))


    #Any RuntimeError you raise lands here
    except RuntimeError as error_message:
        print("{:s}\nTry again.".format(str(error_message)))
    except ValueError:
        print("Second and third parameters should be numeric")
    except AssertionError:
        print("Second or third parameter(or both) is out of range")
    except IndexError:
        print("Need an input.")
    display_game(cells, fnds, tabs)
    if is_winner(cells, tabs):
        print("You won the game!")
        break
    command = input("prompt :> ").strip().lower()


