from heuristic_adversarial_search_problem import HeuristicAdversarialSearchProblem
from .ttt_problem import TTTState, TTTProblem

SPACE = " "
X = "X"  # Player 0 is X
O = "O"  # Player 1 is O
PLAYER_SYMBOLS = [X, O]


class HeuristicTTTProblem(TTTProblem, HeuristicAdversarialSearchProblem):

    def heuristic(self, state: TTTState) -> float:
        """
        TODO: Fill this out with your own heuristic function! You should make sure that this
        function works with boards of any size; if it only works for 3x3 boards, you won't be
        able to properly test ab-cutoff for larger board sizes!
        """
        
        score = 0

        for row in state.board:
            consecutive_X = 0
            consecutive_O = 0
            for cell in row:
                if cell == X:
                    consecutive_X += 1
                    if consecutive_O > 1:
                        score -= 10 ** (consecutive_O - 1)
                    consecutive_O = 0
                elif cell == O:
                    consecutive_O += 1
                    if consecutive_X > 1:
                        score += 10 ** (consecutive_X - 1)
                    consecutive_X = 0
                else:
                    consecutive_X = 0
                    consecutive_O = 0

        return score


        pass