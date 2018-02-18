from othello_rules import *


def evaluate(state):
    """
    Returns 1 if '#' has won, -1 if 'O' has won, and 0 if the game has ended in a draw.
    If the game is not over, returns score / 100, giving a number from -0.64 to 0.64.
    This way, search will prefer winning to merely being ahead by any amount.
    """

    points = score(state)
    if game_over(state):
        if points == 0:
            return 0
        elif points < 0:
            return -1
        elif points > 0:
            return 1
    else:
        return score(state)/100.0

def minimax(state, player, max_depth):
    """
    Returns the value of state with player to play. max_depth gives the search depth; if 0, returns the evaluation
    of state.
    """
    score = evaluate(state)
    if score in [-1, 0, 1]:
        return score
    if max_depth == 0:
        return score

    successors = [successor(state, move, player) for move in legal_moves(state, player)]
    if player == '#':
        return max([minimax(s, 'O', max_depth - 1) for s in successors])
    if player == 'O':
        return min([m for m in [minimax(s, 'O', max_depth - 1) for s in successors] if m is not None])

def best_move(state, player, max_depth):
    """Returns player's best move. max_depth, which must be at least 1, gives the search depth."""
    moves = legal_moves(state, player)
    if player == '#':
        return max(moves, key=lambda m: minimax(successor(state, m, player), 'O', max_depth - 1))
    if player == 'O':
        return min(moves, key=lambda m: minimax(successor(state, m, player), '#', max_depth - 1))


if __name__ == '__main__':
    game = INITIAL_STATE
    while not game_over(game):
        print('# to play')
        print(prettify(game))
        print('Thinking...')
        m = best_move(game, '#', 5)
        print(m)
        game = successor(game, m, '#')
        if not game_over(game):
            while True:
                print('O to play')
                print(prettify(game))
                m = input('Enter row and column (0-7, separated by a space) or pass: ')
                if m != 'pass':
                    m = tuple([int(n) for n in m.split()])
                print(m)
                if m in legal_moves(game, 'O'):
                    break
            game = successor(game, m, 'O')
    print(prettify(game))
    result = score(game)
    if result > 0:
        print('# wins!')
    elif result == 0:
        print('Draw.')
    else:
        print('O wins!')
