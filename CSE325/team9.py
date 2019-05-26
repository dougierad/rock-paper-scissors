strategy_name = 'Devin: alternate scissors and rock'

def move(my_history, their_history):
    if len(my_history)==0:
        my_move = 's'
    elif len(my_history)%2 == 0:
        my_move = 's'
    else:
        my_move = 'r'
    return my_move
