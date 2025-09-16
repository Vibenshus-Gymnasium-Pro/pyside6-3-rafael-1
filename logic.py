# Cross and circle locations
x = [0,0,0,0,0,0,0,0,0]
o = [0,0,0,0,0,0,0,0,0]
# Possible wins
WINS = [[1,1,1,0,0,0,0,0,0], [0,0,0,1,1,1,0,0,0], [0,0,0,0,0,0,1,1,1], [1,0,0,1,0,0,1,0,0], [0,1,0,0,1,0,0,1,0], [0,0,1,0,0,1,0,0,1], [1,0,0,0,1,0,0,0,1], [0,0,1,0,1,0,1,0,0]]

def reset():
    """ This function resets the locations of the crosses and circles. """
    global x, o
    x = [0,0,0,0,0,0,0,0,0]
    o = [0,0,0,0,0,0,0,0,0]

def check_for_wins():
    """ This function checks for wins and returns the winner if there is any. """
    for win in WINS:
        index = 0
        x_hits = 0
        o_hits= 0
        for spot in win:
            # Check for spots with x
            if x[index] and spot:
                x_hits += 1
            # Check for spots with y
            if o[index] and spot:
                o_hits += 1
            # Check for wins:
            if x_hits >= 3:
                return "x"
            if o_hits >= 3:
                return "o"
            index += 1
