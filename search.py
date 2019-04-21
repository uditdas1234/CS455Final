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

################################################################################
#Citation:                                                                     
#Credit                                                                        
#    http://ai.berkeley.edu/search.html                                        
#    https://github.com/richss/CS455-search-python/blob/master/uninformed.ipynb
#    https://www.redblobgames.com/pathfinding/a-star/implementation.html
#    https://gist.github.com/Kautenja/72cd5494adc12dcbfeea3e79e7b3c3ac
#    http://code.activestate.com/recipes/576723-dfs-and-bfs-graph-traversal/
#    https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
################################################################################
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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
################################################################################
#Citation:                                                                     
#Credit                                                                        
#    http://ai.berkeley.edu/search.html                                        
#    https://github.com/richss/CS455-search-python/blob/master/uninformed.ipynb
#    https://www.redblobgames.com/pathfinding/a-star/implementation.html
#    https://gist.github.com/Kautenja/72cd5494adc12dcbfeea3e79e7b3c3ac
#    http://code.activestate.com/recipes/576723-dfs-and-bfs-graph-traversal/
#    https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
################################################################################
    from game import Directions

    #initialization
    closedL = []
    curN = util.Stack()
    curN.push((problem.getStartState(),[],0))
    (curS,move,pathCost)= curN.pop()
    
    closedL.append(curS)

    while not problem.isGoalState(curS): 
        successors = problem.getSuccessors(curS) 
        for childN in successors:
            if (not childN[0] in closedL) or (problem.isGoalState(childN[0])): 
                curN.push((childN[0],move + [childN[1]],pathCost + childN[2])) 
                closedL.append(childN[0]) 
        (curS,move,pathCost)= curN.pop()
  
    return move
  

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
################################################################################
#Citation:                                                                     
#Credit                                                                        
#    http://ai.berkeley.edu/search.html                                        
#    https://github.com/richss/CS455-search-python/blob/master/uninformed.ipynb
#    https://www.redblobgames.com/pathfinding/a-star/implementation.html
#    https://gist.github.com/Kautenja/72cd5494adc12dcbfeea3e79e7b3c3ac
#    http://code.activestate.com/recipes/576723-dfs-and-bfs-graph-traversal/
#    https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
################################################################################
    curN = util.Queue()
    closedL = []
    curN.push((problem.getStartState(),[],0))
    (curS,move,pathCost) = curN.pop()
    closedL.append(curS)
    while not problem.isGoalState(curS): 
        successors = problem.getSuccessors(curS) 
        for childN in successors:
            if not childN[0] in closedL: 
                curN.push((childN[0],move + [childN[1]],pathCost + childN[2])) 
                closedL.append(childN[0]) 
        (curS,move,pathCost) = curN.pop()
    return move

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
################################################################################
#Citation:                                                                     
#Credit                                                                        
#    http://ai.berkeley.edu/search.html                                        
#    https://github.com/richss/CS455-search-python/blob/master/uninformed.ipynb
#    https://www.redblobgames.com/pathfinding/a-star/implementation.html
#    https://gist.github.com/Kautenja/72cd5494adc12dcbfeea3e79e7b3c3ac
#    http://code.activestate.com/recipes/576723-dfs-and-bfs-graph-traversal/
#    https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
################################################################################
    from game import Directions
    curN = util.PriorityQueue() 
    closedL = []
    curN.push((problem.getStartState(),[],0),0 + heuristic(problem.getStartState(),problem)) 
    (curS,move,pathCost) = curN.pop()
    closedL.append((curS,pathCost + heuristic(problem.getStartState(),problem)))
    while not problem.isGoalState(curS): 
        successors = problem.getSuccessors(curS) 
        for childN in successors:
            closed = False
            total_cost = pathCost + childN[2]
            for (closedS,closedCost) in closedL:
                if (childN[0] == closedS) and (total_cost >= closedCost): 
                    closed = True
                    break
            if not closed:        
                curN.push((childN[0],move + [childN[1]],pathCost + childN[2]),pathCost + childN[2] + heuristic(childN[0],problem)) 
                closedL.append((childN[0],pathCost + childN[2])) 
        (curS,move,pathCost) = curN.pop()
    return move

def iterativeDeepeningSearch(problem):
    """This function is for the first of the grad students questions"""
    "*** MY CODE HERE ***"
################################################################################
#Citation:                                                                     
#Credit                                                                        
#    http://ai.berkeley.edu/search.html                                        
#    https://github.com/richss/CS455-search-python/blob/master/uninformed.ipynb
#    https://www.redblobgames.com/pathfinding/a-star/implementation.html
#    https://gist.github.com/Kautenja/72cd5494adc12dcbfeea3e79e7b3c3ac
#    http://code.activestate.com/recipes/576723-dfs-and-bfs-graph-traversal/
#    https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
################################################################################
    from game import Directions
    curN = util.Stack()
    limit = 1;
    while True: 
        closedL = []
        curN.push((problem.getStartState(),[],0))
        (curS,move,pathCost) = curN.pop()
        closedL.append(curS)
        while not problem.isGoalState(curS): 
            successors = problem.getSuccessors(curS) 
            for childN in successors:
                if (not childN[0] in closedL) and (pathCost + childN[2] <= limit): 
                    curN.push((childN[0],move + [childN[1]],pathCost + childN[2])) 
                    closedL.append(childN[0]) 
            if curN.isEmpty(): 
                break
            (curS,move,pathCost) = curN.pop()
        if problem.isGoalState(curS):
            return move
        limit += 1  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ids = iterativeDeepeningSearch
