# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    order_stack = util.Stack()
    points_visited = {}
    path = []
    
    order_stack.push((problem.getStartState(), path))

    while order_stack.isEmpty() is False:
        present_state, path_action = order_stack.pop()
        if present_state in points_visited:
            continue
        points_visited[present_state]=True
        if problem.isGoalState(present_state):
            path = path_action
            break
        for next_state, action, _ in problem.getSuccessors(present_state):
            if next_state not in points_visited:
                order_stack.push((next_state, path_action + [action]))
            else:
                points_visited[next_state]=True

    return path
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    order_queue = util.Queue()
    points_visited = {}
    path=[]

    order_queue.push((problem.getStartState(), path))
    
    while order_queue.isEmpty() is False:
        present_state, path_action = order_queue.pop()
        if present_state in points_visited:
            continue
        points_visited[present_state]=True
        if problem.isGoalState(present_state):
            path=path_action
            break
        for next_state, action, _ in problem.getSuccessors(present_state):
            if next_state not in points_visited:
                order_queue.push((next_state, path_action + [action]))
            else:
                points_visited[next_state]=True
    return path
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    order_Pqueue = util.PriorityQueue()
    points_visited = {}
    path=[]

    order_Pqueue.push((problem.getStartState(), path),0)
    
    while order_Pqueue.isEmpty() is False:
        present_state, path_action = order_Pqueue.pop()
        present_cost = problem.getCostOfActions(path_action)
        if (present_state in points_visited):
            continue
        points_visited[present_state] = present_cost
        if problem.isGoalState(present_state):
            path=path_action
            break
        for next_state, action, next_cost in problem.getSuccessors(present_state):
            if next_state not in points_visited or (next_cost <= points_visited[next_state]):
                new_path=path_action + [action]
                order_Pqueue.update((next_state, new_path),present_cost+next_cost)
            else:
                points_visited[next_state]=present_cost
    return path 
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    order_Pqueue = util.PriorityQueue()
    points_visited = {}
    path=[]

    order_Pqueue.push((problem.getStartState(), path),0)
    
    while order_Pqueue.isEmpty() is False:
        present_state, path_action = order_Pqueue.pop()
        present_cost = 0+heuristic(present_state,problem)
        if (present_state in points_visited):
            continue
        points_visited[present_state] = present_cost
        if problem.isGoalState(present_state):
            path=path_action
            break
        for next_state, action, next_cost in problem.getSuccessors(present_state):
            if next_state not in points_visited or (next_cost <= points_visited[next_state]):
                new_path=path_action + [action]
                order_Pqueue.update((next_state,
                                    new_path),problem.getCostOfActions(new_path)+heuristic(next_state,problem))
            else:
                points_visited[next_state]=present_cost
    return path 
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
