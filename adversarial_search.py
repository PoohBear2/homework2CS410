import random
from typing import Dict, Tuple

from adversarial_search_problem import (
    Action,
    State as GameState,
)
from heuristic_adversarial_search_problem import HeuristicAdversarialSearchProblem


def minimax(asp: HeuristicAdversarialSearchProblem[GameState, Action], cutoff_depth=float('inf')) -> Tuple[Action, Dict[str, int]]:
    """
    Implement the minimax algorithm on ASPs, assuming that the given game is 
    both 2-player and zero-sum.


    Input:
        asp - a HeuristicAdversarialSearchProblem
        cutoff_depth - the maximum search depth, where 0 is the start state. 
                    Depth 1 is all the states reached after a single action from the start state (1 ply).
                    cutoff_depth will always be greater than 0.
    Output:
        an action (an element of asp.get_available_actions(asp.get_start_state()))
        a dictionary of statistics for visualization
            states_expanded: stores the number of states expanded during current search
                            A state is expanded when get_available_actions(state) is called.
    """
    best_action = None
    stats = {
        'states_expanded': 0
    }

    # TODO: Implement the minimax algorithm. Feel free to write helper functions.

    start = asp.get_start_state()
    if asp.is_terminal_state(start):
        stats['states_expanded'] += 1
        return best_action, stats

    def max_val(state: GameState, depth: int):
        if asp.is_terminal_state(state):
            return asp.get_result(state)
        if depth >= cutoff_depth:
            return asp.heuristic(state)
    
        stats['states_expanded'] += 1

        ans = -float('inf')
        actions = asp.get_available_actions(state)
        print("im here again")
        for action in actions:
            
            next = asp.transition(state, action)
            ans = max(ans, min_val(next, depth + 1))

        return ans
    
    def min_val(state: GameState, depth: int):
        if asp.is_terminal_state(state):
            return asp.get_result(state)
        if depth >= cutoff_depth:
            return asp.heuristic(state)
        
        stats['states_expanded'] += 1
        
        ans = float('inf')
        actions = asp.get_available_actions(state)
        print("im here")
        for action in actions:
            
            next = asp.transition(state, action)
            ans = min(ans, max_val(next, depth + 1))
        return ans
    
    stats['states_expanded'] += 1
    actions = asp.get_available_actions(start)
    ans = -float('inf')

    for action in actions:
        next = asp.transition(start, action)
        print(stats)
        temp = min_val(next, 1)
        if temp > ans:
            ans = temp
            best_action = action
        
    return best_action, stats



def alpha_beta(asp: HeuristicAdversarialSearchProblem[GameState, Action], cutoff_depth=float('inf')) -> Tuple[Action, Dict[str, int]]:
    """
    Implement the alpha-beta pruning algorithm on ASPs,
    assuming that the given game is both 2-player and constant-sum.

    Input:
        asp - an AdversarialSearchProblem
        cutoff_depth - the maximum search depth, where 0 is the start state,
                    Depth 1 is all the states reached after a single action from the start state (1 ply).
                    cutoff_depth will always be greater than 0.
    Output:
        an action (an element of asp.get_available_actions(asp.get_start_state()))
         a dictionary of statistics for visualization
            states_expanded: stores the number of states expanded during current search
                            A state is expanded when get_available_actions(state) is called.
    """
    best_action = None
    stats = {
        'states_expanded': 0  
    }
    
    # TODO: Implement the alpha-beta pruning algorithm. Feel free to use helper functions.
    
    start = asp.get_start_state()

    if asp.is_terminal_state(start):
        stats['states_expanded'] += 1
        return best_action, stats

    def max_val(state: GameState, depth: int, alpha: float, beta: float):
        if asp.is_terminal_state(state):
            return asp.get_result(state)
        if depth >= cutoff_depth:
            return asp.heuristic(state)
        
        stats['states_expanded'] += 1

        ans = -float('inf')
        actions = asp.get_available_actions(state)
        for action in actions:
            next = asp.transition(state, action)
            temp = min_val(next, depth + 1, alpha, beta)

            if temp > ans:
                ans = temp
            
            if temp >= beta:
                break

            alpha = max(alpha, temp)
        return ans
    
    def min_val(state: GameState, depth: int, alpha: float, beta:float):
        if asp.is_terminal_state(state):
            return asp.get_result(state)
        if depth >= cutoff_depth:
            return asp.heuristic(state)
        
        stats['states_expanded'] += 1

        ans = float('inf')
        actions = asp.get_available_actions(state)
        for action in actions:
            next = asp.transition(state, action)
            temp = max_val(next, depth + 1, alpha, beta)

            if temp < ans:
                ans = temp

            if temp <= alpha:
                break
        
            beta = min(beta, temp)
        
        return ans
    
    stats['states_expanded'] += 1
    actions = asp.get_available_actions(start)
    best_val = -float('inf')
    alpha = -float('inf')
    beta = float('inf')

    for action in actions:
        next = asp.transition(start, action)
        temp = min_val(next, 1, alpha, beta)

        if temp > best_val:
            best_val = temp
            best_action = action

        if best_val >= beta:
            break

        alpha = max(alpha, best_val)
    
    return best_action, stats