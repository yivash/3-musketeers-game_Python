# The Three Musketeers Game

# In all methods,
#   A 'location' is a two-tuple of integers, each in the range 0 to 4.
#        The first integer is the row number, the second is the column number.
#   A 'direction' is one of the strings "up", "down", "left", or "right".
#   A 'board' is a list of 5 lists, each containing 5 strings: "M", "R", or "-".
#        "M" = Musketeer, "R" = Cardinal Richleau's man, "-" = empty.
#        Each list of 5 strings is a "row"
#   A 'player' is one of the strings "M" or "R" (or sometimes "-").
#
# For brevity, Cardinal Richleau's men are referred to as "enemy".
# 'pass' is a no-nothing Python statement. Replace it with actual code.

def create_board():
    global board
    """Creates the initial Three Musketeers board and makes it globally
       available (That is, it doesn't have to be passed around as a
       parameter.) 'M' represents a Musketeer, 'R' represents one of
       Cardinal Richleau's men, and '-' denotes an empty space."""
    m = 'M'
    r = 'R'
    board = [ [r, r, r, r, m],
              [r, r, r, r, r],
              [r, r, m, r, r],
              [r, r, r, r, r],
              [m, r, r, r, r] ]

def set_board(new_board):
    """Replaces the global board with new_board."""
    global board
    board = new_board

def get_board():
    """Just returns the board. Possibly useful for unit tests."""
    return board

def string_to_location(s):
    """Given a two-character string (such as 'A5'), returns the designated
       location as a 2-tuple (such as (0, 4)).
       The function should raise ValueError exception if the input
       is outside of the correct range (between 'A' and 'E' for s[0] and
       between '1' and '5' for s[1]
       """
    positions={'A':0,'B':1,'C':2,'D':3,'E':4}
    if s[0] not in positions or (int(s[1])-1) not in positions.values():
        raise ValueError('Incorrect input')
    location=positions[s[0]], int(s[1])-1
    return location

def location_to_string(location):
    """Returns the string representation of a location.
    Similarly to the previous function, this function should raise
    ValueError exception if the input is outside of the correct range
    """
    positions={'A':0,'B':1,'C':2,'D':3,'E':4}
    for i in location:
        if i not in positions.values():
            raise ValueError('Incorrect input')
    k = [key for key, value in positions.items() if value == location[0]][0]
    return k+str(location[1]+1)
    
def at(location):
    """Returns the contents of the board at the given location.
    You can assume that input will always be in correct range."""
    return board[location[0]][location[1]]

def all_locations():
    """Returns a list of all 25 locations on the board."""
    All_locs = list()
    for i in range(len(board)):
        for j in range(len(board[0])):
            All_locs.append((i,j))
    return All_locs  

def adjacent_location(location, direction):
    """Return the location next to the given one, in the given direction.
       Does not check if the location returned is legal on a 5x5 board.
       You can assume that input will always be in correct range."""
    adj_loc=None 
    if direction=='left':
        adj_loc=(location[0],location[1]-1)
    if direction=='right':
        adj_loc=(location[0],location[1]+1)
    if direction=='up':
        adj_loc=(location[0]-1,location[1])
    if direction=='down':
        adj_loc=(location[0]+1,location[1])
    return adj_loc
    
def is_legal_move_by_musketeer(location, direction):
    """Tests if the Musketeer at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'M'"""
    if at(location)=='M':
        return is_within_board(location, direction) and at(adjacent_location(location, direction))=='R'
    else:
        raise ValueError('Incorrect input')            
    
def is_legal_move_by_enemy(location, direction):
    """Tests if the enemy at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'R'"""
    if at(location)=='R':
        return is_within_board(location, direction) and at(adjacent_location(location, direction))=='-'
    else:
        raise ValueError('Incorrect input')  
    
def is_legal_move(location, direction):
    """Tests whether it is legal to move the piece at the location
    in the given direction.
    You can assume that input will always be in correct range."""
    if at(location)=='M':
        return is_legal_move_by_musketeer(location, direction)
    elif at(location)=='R':
        return is_legal_move_by_enemy(location, direction)
    
def can_move_piece_at(location):
    """Tests whether the player at the location has at least one move available.
    You can assume that input will always be in correct range.
    You can assume that input will always be in correct range."""
    directions=['left','right','up','down']
    legal_moves=0
    for x in directions:
        if is_legal_move(location, x)==True:
            legal_moves+=1
    return legal_moves!=0
    
def has_some_legal_move_somewhere(who):
    """Tests whether a legal move exists for player "who" (which must
    be either 'M' or 'R'). Does not provide any information on where
    the legal move is.
    You can assume that input will always be in correct range."""
    if who=='M':
        legal_moves_m=0
        for x in all_locations():
            if at(x)=='M' and can_move_piece_at(x)==True:
                legal_moves_m+=1
        return legal_moves_m!=0
    elif who=='R':
        legal_moves_r=0
        for x in all_locations():
            if at(x)=='R' and can_move_piece_at(x)==True:
                legal_moves_r+=1
        return legal_moves_r!=0
    
def possible_moves_from(location):
    """Returns a list of directions ('left', etc.) in which it is legal
       for the player at location to move. If there is no player at
       location, returns the empty list, [].
       You can assume that input will always be in correct range."""
    directions=['left','right','up','down']
    legal_dir=list()
    for x in directions:
        if is_legal_move(location,x):
            legal_dir.append(x)
    return legal_dir
    
def is_legal_location(location):
    """Tests if the location is legal on a 5x5 board.
    You can assume that input will always be a pair of integers."""
    return 0<=location[0]<=4 and 0<=location[1]<=4
    
def is_within_board(location, direction):
    """Tests if the move stays within the boundaries of the board.
    You can assume that input will always be in correct range."""
    return is_legal_location(adjacent_location(location, direction))
        
def all_possible_moves_for(player):
    """Returns every possible move for the player ('M' or 'R') as a list
       (location, direction) tuples.
       You can assume that input will always be in correct range."""
    if player=='M':
        all_loc_m=list()
        all_moves_m=list()
        for v in all_locations():
            if at(v)=='M':
                all_loc_m.append(v)
        for i in all_loc_m:
            for j in possible_moves_from(i):
                if is_legal_move_by_musketeer(i,j):
                    all_moves_m.append((i,j))
        return all_moves_m

    if player=='R':
        all_loc_r=list()
        all_moves_r=list()
        for z in all_locations():
            if at(z)=='R':
                all_loc_r.append(z)
        for k in all_loc_r:
            for n in possible_moves_from(k):
                if is_legal_move_by_enemy(k,n):
                    all_moves_r.append((k,n))
        return all_moves_r
                 
def make_move(location, direction):
    """Moves the piece in location in the indicated direction.
    Doesn't check if the move is legal. You can assume that input will always
    be in correct range."""
    global board
    new_board=list()
    if at(location)=='M':
        for i in range(len(board)):
            new_board.append([])
            for j in range(len(board[0])):
                if location==(i,j):
                    new_board[i].append('-')
                elif adjacent_location(location, direction)==(i,j):
                    new_board[i].append('M')
                else:
                    new_board[i].append(board[i][j])
    elif at(location)=='R':
        for i in range(len(board)):
            new_board.append([])
            for j in range(len(board[0])):
                if location==(i,j):
                    new_board[i].append('-')
                elif adjacent_location(location, direction)==(i,j):
                    new_board[i].append('R')
                else:
                    new_board[i].append(board[i][j])
    board=new_board             
    
def choose_computer_move(who):
    """The computer chooses a move for a Musketeer (who = 'M') or an
       enemy (who = 'R') and returns it as the tuple (location, direction),
       where a location is a (row, column) tuple as usual.
       You can assume that input will always be in correct range."""
    if who=='M':
        return best_move_M() 
    else:
        return best_move_R()
    
def is_enemy_win():
    """Returns True if all 3 Musketeers are in the same row or column."""
    return M_locations()[0][0]==M_locations()[1][0]==M_locations()[2][0] or M_locations()[0][1]==M_locations()[1][1]==M_locations()[2][1]

def M_locations():
    """Returns list of all locations for Musketeers as (location) tuples."""
    all_locs=list()
    for i in all_locations():
        if at(i)=='M':
            all_locs.append(i)
    return all_locs        

def sum_distances(locs_list):
    """Returns sum of euclidean distances between positions on board of all Musketeer players."""
    Tot=0
    import math
    for k,l in [(0,1),(0,2),(1,2)]:
        Tot+=round(math.sqrt((locs_list[k][0]-locs_list[l][0])**2+(locs_list[k][1]-locs_list[l][1])**2),2)
    return Tot

def centre_of_M(locs_list):
    """Returns position of central point of all Musketeer players."""
    x,y=0,0
    for i in locs_list:
        x+=i[0]
        y+=i[1]
    return round(x/3,2),round(y/3,2)

def best_move_M():
    """Returns move for Musketeers, that leads to maximum spread of their players over the board."""
    max=0
    best=None
    locs=M_locations()
    for i in all_possible_moves_for('M'):
        for j in range(0,len(locs)):
            if i[0]==locs[j]:
                locs[j]=adjacent_location(i[0],i[1])
                if sum_distances(locs)>max:
                    max=sum_distances(locs)
                    best=i
                    locs=M_locations()
    return best

def best_move_R():
    """Returns move for enemies, that allowed them to maneuver into direction where centre of all Musketeer`s position is located."""
    r=all_possible_moves_for('R')
    best=r[0]
    centre=centre_of_M(M_locations())
    min=abs(centre[0]-adjacent_location(best[0],best[1])[0])+abs(centre[1]-adjacent_location(best[0],best[1])[1])
    for i in all_possible_moves_for('R'):
        if abs(centre[0]-adjacent_location(i[0],i[1])[0])+abs(centre[1]-adjacent_location(i[0],i[1])[1])<min:
            best=i
    return best
    
#---------- Communicating with the user ----------
#----you do not need to modify code below unless you find a bug
#----a bug in it before you move to stage 3

def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    for i in range(0, 5):
        print(ch, "|", end = " ")
        for j in range(0, 5):
            print(board[i][j] + " ", end = " ")
        print()
        ch = chr(ord(ch) + 1)
    print()

def print_instructions():
    print()
    print("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.""")
    print()

def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user

def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""    
    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    move = input("Your move? ").upper().replace(' ', '')
    if (len(move) >= 3
            and move[0] in 'ABCDE'
            and move[1] in '12345'
            and move[2] in 'LRUD'):
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
    print("Illegal move--'" + move + "'")
    return get_users_move()

def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(users_side)
    else: # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')         
        make_move(location, direction)
        describe_move("Musketeer", location, direction)
        
def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(users_side)
    else: # Computer plays enemy
        (location, direction) = choose_computer_move('R')         
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board

def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print(who, 'moves', direction, 'from',\
          location_to_string(location), 'to',\
          location_to_string(new_location) + ".\n")

def start():
    """Plays the Three Musketeers Game."""
    users_side = choose_users_side()
    board = create_board()
    print_instructions() 
    print_board()
    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                break
        else:
            print("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
        else:
            print("The Musketeers win!")
            break
