# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem
        """
        util.FixedRandom.__init__(self);
        #util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    
    from game import Directions
    
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
#     print "Start:", problem.getStartState()
#     print "Is the start a goal?", problem.isGoalState(problem.getStartState())
#     print "Start's successors:", problem.getSuccessors(problem.getStartState())
#     print type(problem.getSuccessors(problem.getStartState()))
#     
    
    
    "*** YOUR CODE HERE ***"
    visited = []
    answer = []
    hash = {}
    unvisited = util.Stack()
    unvisited.push(problem.getStartState())
    hash[problem.getStartState()] = (("",("0","0")))
    while(not(unvisited.isEmpty())):        
        current = unvisited.pop()
        visited.append(current)
        if(problem.isGoalState(current)): #reached goal. reverse the answer and return it.
            while(current != problem.getStartState()):
                answer.append(hash.get(current)[0])
                current = hash.get(current)[1]
            actualAns = []
            for index in range(answer.__len__(),0,-1):
                actualAns.append(answer[index-1])
            return actualAns
        successors = problem.getSuccessors(current)
        for node in successors:
            if( node[0] not in visited):
                unvisited.push(node[0]);
                hash[node[0]]=(node[1],current) 
    return []           
 
          
    
    
    

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    open = util.Queue()
    open.push(problem.getStartState())
    visited = []
    answer = []
    hash = {}
    hash[problem.getStartState()] = (("",("0","0")))
    while(not(open.isEmpty())):      
        current = open.pop()
        visited.append(current)
        if(problem.isGoalState(current)==True):
            while(current != problem.getStartState()):
                answer.append(hash.get(current)[0])
                current = hash.get(current)[1]
            actualAns = []
            for i in range(answer.__len__(),0,-1):
                actualAns.append(answer[i-1])
            return actualAns
        successors = problem.getSuccessors(current)
        for nodes in successors:
            if(nodes[0] not in hash):
                if((visited.__contains__(nodes[0]))==False):
                    open.push(nodes[0]);
                    hash[nodes[0]]=(nodes[1],current) # (direction, coordinates of parent)
    return answer

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    open = util.PriorityQueue()
    open.push(problem.getStartState(),0)
    visited = []
    answer = []
    hash = {} 
    hash[problem.getStartState()] = (("",("0","0"),0))
    while(not (open.isEmpty())):      
        current = open.pop()
        visited.append(current)
        if(problem.isGoalState(current)==True):
            while(current != problem.getStartState()):
                answer.append(hash.get(current)[0])
                current = hash.get(current)[1]
            actualAns = []
            for i in range(answer.__len__(),0,-1):
                actualAns.append(answer[i-1])
            return actualAns
        successors = problem.getSuccessors(current)
        for nodes in successors:
            if( (nodes[0] not in hash) or(hash.get(nodes[0])[2]) > nodes[2]+hash.get(current)[2]):
                if(nodes[0] not in visited):
                    hash[nodes[0]]=(nodes[1],current,(nodes[2]+hash.get(current)[2]))
                    open.push(nodes[0],nodes[2]+hash.get(current)[2]);                   
                    
    return answer

    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    open = util.PriorityQueue()
    open.push(problem.getStartState(),0)
    visited = []
    answer = []
    hash = {}
    hash[problem.getStartState()] = (("",("0","0"),heuristic(problem.getStartState(), problem)))
    while(not(open.isEmpty())):      
        current = open.pop()
        if(current in visited):
            continue
        visited.append(current)
        if(problem.isGoalState(current)):
            while(current != problem.getStartState()):
                answer.append(hash.get(current)[0])
                current = hash.get(current)[1]
            newAns = []
            for i in range(answer.__len__(),0,-1):
                newAns.append(answer[i-1])
            return newAns
        successors = problem.getSuccessors(current)
        for nodes in successors:
            if( (hash.get(nodes[0])==None) or(hash.get(nodes[0])[2]) > nodes[2]+hash.get(current)[2]): 
                if(nodes[0] not in visited):
                    hash[nodes[0]]=(nodes[1],current,(hash.get(current)[2]+nodes[2])) 
                    open.push(nodes[0],(nodes[2]+hash.get(current)[2] + heuristic(nodes[0], problem)));                  
    return answer


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
