import unittest

from asps.game_dag import DAGState, GameDAG
from asps.heuristic_ttt_problem import HeuristicTTTProblem, X, O, SPACE
from asps.heuristic_connect_four import HeuristicConnectFourProblem
from adversarial_search import alpha_beta, minimax


class IOTest(unittest.TestCase):
    """
    Tests IO for adversarial search implementations.
    Contains basic/trivial test cases.

    Each test function instantiates an adversarial search problem (DAG) and tests
    that the algorithm returns a valid action.

    It does NOT test whether the action is the "correct" action to take.
    """

    def _check_result(self, result, dag):
        """
        Tests whether the result is one of the possible actions of the dag.
        Input:
            result - the return value of an adversarial search problem.
                     This should be an action.
            dag - the GameDAG that was used to test the algorithm.
        """
        self.assertIsNotNone(result, "Output should not be None")
        start_state = dag.get_start_state()
        potential_actions = dag.get_available_actions(start_state)
        self.assertIn(result, potential_actions, "Output should be an available action")

    def test_minimax(self):
        """
        Test minimax on a basic GameDAG.
        """
        X = True
        _ = False
        matrix = [
            [_, X, X, _, _, _, _],
            [_, _, _, X, X, _, _],
            [_, _, _, _, _, X, X],
            [_, _, _, _, _, _, _],
            [_, _, _, _, _, _, _],
            [_, _, _, _, _, _, _],
            [_, _, _, _, _, _, _],
        ]
        start_state = DAGState(0, 0)
        terminal_evaluations = {3: -1, 4: -2, 5: -3, 6: -4}

        dag = GameDAG(matrix, start_state, terminal_evaluations)
        result, stats = minimax(dag)
        self._check_result(result, dag)

    def test_alpha_beta(self):
        """
        Test alpha-beta pruning on a basic GameDAG.
        """
        X = True
        _ = False
        matrix = [
            [_, X, X, _, _, _, _],
            [_, _, _, X, X, _, _],
            [_, _, _, _, _, X, X],
            [_, _, _, _, _, _, _],
            [_, _, _, _, _, _, _],
            [_, _, _, _, _, _, _],
            [_, _, _, _, _, _, _],
        ]
        start_state = DAGState(0, 0)
        terminal_evaluations = {3: -1, 4: -2, 5: -3, 6: -4}

        dag = GameDAG(matrix, start_state, terminal_evaluations)
        result, stats = alpha_beta(dag)
        self._check_result(result, dag)

    def test_minimax_result(self):
        X = True
        _ = False
        matrix = [
            [_, X, X, _, _, _, _],
            [_, _, _, X, X, _, _],
            [_, _, _, _, _, X, X],
            [_, _, _, _, _, _, _],
            [_, _, _, _, _, _, _],
            [_, _, _, _, _, _, _],
            [_, _, _, _, _, _, _],
        ]
        start_state = DAGState(0, 0)
        terminal_evaluations = {3: -1, 4: -2, 5: -3, 6: -4}

        dag = GameDAG(matrix, start_state, terminal_evaluations)
        result, stats = minimax(dag)
        
        self.assertEqual(result, 1)

    def test_alpha_beta_result(self):
        """
        Test alpha-beta pruning on a basic GameDAG.
        """
        X = True
        _ = False
        matrix = [
            [_, X, X, _, _, _, _],
            [_, _, _, X, X, _, _],
            [_, _, _, _, _, X, X],
            [_, _, _, _, _, _, _],
            [_, _, _, _, _, _, _],
            [_, _, _, _, _, _, _],
            [_, _, _, _, _, _, _],
        ]
        start_state = DAGState(0, 0)
        terminal_evaluations = {3: -1, 4: -2, 5: -3, 6: -4}

        dag = GameDAG(matrix, start_state, terminal_evaluations)
        result, stats = alpha_beta(dag)
        self.assertEqual(result, 1)


    def test_alpha_beta_states(self):
        """
        Test alpha-beta pruning on a basic GameDAG.
        """
        X = True
        _ = False
        matrix = [
            [_, X, X, _, _, _, _],
            [_, _, _, X, X, _, _],
            [_, _, _, _, _, X, X],
            [_, _, _, _, _, _, _],
            [_, _, _, _, _, _, _],
            [_, _, _, _, _, _, _],
            [_, _, _, _, _, _, _],
        ]
        start_state = DAGState(0, 0)
        terminal_evaluations = {3: -1, 4: -2, 5: -3, 6: -4}

        dag = GameDAG(matrix, start_state, terminal_evaluations)
        result, stats = alpha_beta(dag)
        self.assertEqual(stats["states_expanded"], 5)

    def test_minimax_states(self):
        X = True
        _ = False
        matrix = [
            [_, X, X, _, _, _, _],
            [_, _, _, X, X, _, _],
            [_, _, _, _, _, X, X],
            [_, _, _, _, _, _, _],
            [_, _, _, _, _, _, _],
            [_, _, _, _, _, _, _],
            [_, _, _, _, _, _, _],
        ]
        start_state = DAGState(0, 0)
        terminal_evaluations = {3: -1, 4: -2, 5: -3, 6: -4}

        dag = GameDAG(matrix, start_state, terminal_evaluations)
        result, stats = minimax(dag)
        
        self.assertEqual(stats["states_expanded"], 7)

if __name__ == "__main__":
    unittest.main()
