import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

board1 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

board2 =  [ [_, _, _, M, _],
            [_, R, _, M, _],
            [_, _, M, _, _],
            [_, _, _, _, _],
            [_, _, _, _, _] ]

def test_create_board():
    create_board()
    assert at((0,0)) == R
    assert at((0,4)) == M
    assert at((2,2)) == M
    assert at((3,1)) == R
    
def test_set_board():
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M    
    #eventually add some board2 and at least 3 tests with it

def test_get_board():  
    set_board(board1)
    assert board1 == get_board()
    #eventually add at least one more test with another board

def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
        string_to_location('B9')
    assert string_to_location('A1') == (0,0)
    assert string_to_location('C4') == (2,3)
    assert string_to_location('E5') == (4,4)    
    
def test_location_to_string():
    with pytest.raises(ValueError):
        string_to_location((3,7))
        string_to_location((8,2))
    assert location_to_string((1,1)) =='B2'
    assert location_to_string((0,3)) =='A4'
    assert location_to_string((4,2)) =='E3'

def test_at():
    set_board(board1)
    assert at((0,3))==M
    assert at((2,1))==R
    assert at((4,4))==_
    
def test_all_locations():
    assert all_locations()==[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
    
def test_adjacent_location():
    assert adjacent_location((1,2),'left')==(1,1)
    assert adjacent_location((1,2),'right')==(1,3)
    assert adjacent_location((1,2),'up')==(0,2)
    assert adjacent_location((1,2),'down')==(2,2)
    
def test_is_legal_move_by_musketeer():
    set_board(board1)
    assert is_legal_move_by_musketeer((2,2),'left')==True
    assert is_legal_move_by_musketeer((0,3),'down')==False
    with pytest.raises(ValueError):
        is_legal_move_by_musketeer((0,2),'down')
        is_legal_move_by_musketeer((3,1),'right')
        
def test_is_legal_move_by_enemy():
    set_board(board1)
    assert is_legal_move_by_enemy((1,2),'left')==True
    assert is_legal_move_by_enemy((2,1),'right')==False
    with pytest.raises(ValueError):
        is_legal_move_by_enemy((4,0),'down')
        is_legal_move_by_enemy((2,2),'up')
    
def test_is_legal_move():
    set_board(board1)
    assert is_legal_move((3,1),'down')==True
    assert is_legal_move((1,3),'up')==False
    assert is_legal_move((1,3),'left')==True
    assert is_legal_move((2,1),'right')==False
    
def test_can_move_piece_at():
    assert can_move_piece_at((1,3))==True
    assert can_move_piece_at((0,3))==False
    assert can_move_piece_at((4,3))==True
    
def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    set_board(board2)
    assert has_some_legal_move_somewhere('M') == False
    assert has_some_legal_move_somewhere('R') == True
    
def test_possible_moves_from():
    set_board(board1)
    assert possible_moves_from((0,0))==[]
    assert possible_moves_from((1,2))==['left','up']
    assert possible_moves_from((1,3))==['left','down']
    assert possible_moves_from((2,3))==['right','down']
    # Replace with tests

def test_is_legal_location():
    assert is_legal_location((1,1))==True
    assert is_legal_location((4,0))==True
    assert is_legal_location((5,1))==False

def test_is_within_board():
    assert is_legal_location(adjacent_location((0,0),'left'))==False
    assert is_legal_location(adjacent_location((2,2),'up'))==True
    assert is_legal_location(adjacent_location((3,1),'right'))==True
    assert is_legal_location(adjacent_location((4,2),'down'))==False
    
def test_all_possible_moves_for():
    assert all_possible_moves_for('R')==[(0,0)," "]
    # Replace with tests
    
def test_make_move():
    assert make_move((1,1),'M')== None
    # Return None, but the board should be updated
    
def test_choose_computer_move():
    assert choose_computer_move("M")==((0,0)," ")
    assert choose_computer_move("R")==((0,0)," ")
    # Replace with tests; should work for both 'M' and 'R'

def test_is_enemy_win():
    assert is_enemy_win()==True
    # Replace with tests


