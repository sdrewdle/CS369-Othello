from copy import deepcopy


def diagram_to_state(diagram):
    """Converts a list of strings into a list of lists of characters (strings of length 1.)"""
    return [list(a) for a in diagram]


INITIAL_STATE = diagram_to_state(['........',
                                  '........',
                                  '........',
                                  '...#O...',
                                  '...O#...',
                                  '........',
                                  '........',
                                  '........'])


def count_pieces(state):
    """Returns a dictionary of the counts of '#', 'O', and '.' in state."""
    result = {'#': 0, 'O': 0, '.': 0}
    for row in state:
        for square in row:
            result[square] += 1

    return result


def prettify(state):
    """
    Returns a single human-readable string representing state, including row and column indices and counts of
    each color.
    """
    visual = ' 01234567\n'
    result = {'#': 0, 'O': 0, '.': 0}
    i = 0

    for row in state:
        for square in row:
            result[square] += 1

    for row in state:
        updatedRow = ''.join(row)
        visual += (str(i) + updatedRow + str(i) + '\n')
        i = int(i)
        i += 1
    visual += ' 01234567\n'

    visual += (str(result) + '\n')

    return visual


def opposite(color):
    """opposite('#') returns 'O'. opposite('O') returns '#'."""
    if color is '#':
        return 'O'
    elif color is 'O':
        return '#'


def flips(state, r, c, color, dr, dc):
    """
    Returns a list of pieces that would be flipped if color played at r, c, but only searching along the line
    specified by dr and dc. For example, if dr is 1 and dc is -1, consider the line (r+1, c-1), (r+2, c-2), etc.

    :param state: The game state.
    :param r: The row of the piece to be  played.
    :param c: The column of the piece to be  played.
    :param color: The color that would play at r, c.
    :param dr: The amount to adjust r on each step along the line.
    :param dc: The amount to adjust c on each step along the line.
    :return A list of (r, c) pairs of pieces that would be flipped.
    """
    flip_list = []
    i = 1
    while True:
        nr = r + i*dr
        nc = c + i*dc
        if nr < 0 or nr > 7 or nc > 7 or nc < 0:
            break

        if state[nr][nc] is ".":
            break

        flip_list.append((nr, nc))
        if state[nr][nc] is color:
            flip_list.pop()
            return flip_list
        i += 1
    return []





OFFSETS = ((-1, 0), (-1, 1), (0, 1), (1, 1),
           (1, 0), (1, -1), (0, -1), (-1, -1))


def flips_something(state, r, c, color):
    """Returns True if color playing at r, c in state would flip something."""
    for cord in OFFSETS:
        x = flips(state, r, c, color, cord[0], cord[1])
        if x:
            return True
    return False


def legal_moves(state, color):
    """
    Returns a list of legal moves ((r, c) pairs) that color can make from state. Note that a player must flip
    something if possible; otherwise they must play the special move 'pass'.
    """
    x = []
    for r,row in enumerate(state):
        for c,item in enumerate(row):
            if item is "." and flips_something(state,r,c,color):
                x.append( (r,c) )
    if(len(x) is 0):
        return ['pass']
    return x


def successor(state, move, color):
    """
    Returns the state that would result from color playing move (which is either a pair (r, c) or 'pass'.
    Assumes move is legal.
    """
    # TODO You have to write this


def score(state):
    """
    Returns the scores in state. More positive values (up to 64 for occupying the entire board) are better for '#'.
    More negative values (down to -64) are better for 'O'.
    """
    total = 0
    for row in state:
        for tile in row:
            if tile is 'O':
                total -= 1
            if tile is '#':
                total += 1
    return total


def game_over(state):
    """
    Returns true if neither player can flip anything.
    """
    # TODO You have to write this
