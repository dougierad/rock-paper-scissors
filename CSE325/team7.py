'''The function move(my_history, their_history) must return 'r', 'p', or 's'.
my_history and their_history are strings of the same length, perhaps length zero.
'''

strategy_name = 'Beat What They Threw Against Me Last with a twist'

def beat_move(move_to_beat):
    if move_to_beat == 'r':
        return 'p'
    elif move_to_beat == 'p':
        return 's'
    else:
        return 'r'
import random   
 
def move(my_history, their_history):
    if len(their_history) < 1:
        my_move = 'r'
    else:
        if len(my_history)%4 == 0:
            my_move = random.choice(['p','s'])
        else:
            my_move = beat_move(their_history[-1])
        
    return my_move
    
