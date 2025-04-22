def BFS(TREE):
    """
    Performs a left-to-right breadth-first traversal on a tuple-based tree structure.

    Args:
        TREE: A tree represented as nested tuples (internal nodes) and strings (leaf nodes).

    Returns:
        A tuple of leaf nodes visited in left-to-right breadth-first order.
    """
    queue = [TREE]
    leaves = []

    while len(queue) > 0:
        node = queue[0]
        queue = queue[1:]

        if isinstance(node, tuple):
            for child in node:
                queue.append(child)
        else:
            leaves.append(node)

    return tuple(leaves)

print(BFS("ROOT"))
#('ROOT’,)
print(BFS(((("L", "E"), "F"), "T")))
#('T’, ’F’, ’L’, ’E’)
print(BFS(("R", ("I", ("G", ("H", "T"))))))
#('R’, ’I’, ’G’, ’H’, ’T’)
print(BFS((("A", ("B",)), ("C",), "D")))
#('D’, ’A’, ’C’, ’B’)
print(BFS(("T", ("H", "R", "E"), "E")))
#('T’, ’E’, ’H’, ’R’, ’E’)
print(BFS(("A", (("C", (("E",), "D")), "B"))))
#('A’, ’B’, ’C’, ’D’, ’E’)



def DFS(TREE):
    """
    Performs a left-to-right depth-first traversal on a tuple-based tree structure.

    Args:
        TREE: A tree represented as nested tuples (internal nodes) and strings (leaf nodes).

    Returns:
        A tuple of leaf nodes visited in left-to-right depth-first order.
    """
    if not isinstance(TREE, tuple):
        return (TREE,)

    result = ()
    for subtree in TREE:
        result = result + DFS(subtree)

    return result

print(DFS("ROOT"))
# → ('ROOT',)

print(DFS(((("L", "E"), "F"), "T")))
# → ('L', 'E', 'F', 'T')

print(DFS(("R", ("I", ("G", ("H", "T"))))))
# → ('R', 'I', 'G', 'H', 'T')

print(DFS(((("A", ("B",)), ("C",), "D"))))
# → ('A', 'B', 'C', 'D')

print(DFS(("T", ("H", "R", "E"), "E")))
# → ('T', 'H', 'R', 'E', 'E')

print(DFS(("A", (("C", (("E",), "D")), "B"))))
# → ('A', 'C', 'E', 'D', 'B')


def DFID(TREE, D):
    """
    Performs right-to-left depth-first iterative deepening traversal up to depth D.

    Args:
        TREE: A tree represented as nested tuples (internal nodes) and strings (leaf nodes).
        D: An integer representing the depth limit.

    Returns:
        A tuple of leaf nodes visited using right-to-left depth-first iterative-deepening search.
    """
    result = ()
    for depth in range(D + 1):
        result = result + DLS(TREE, depth)
    return result

def DLS(TREE, depth):
    """
    Performs depth-limited search to a given depth.

    Args:
        TREE: A tree node.
        depth: The current depth limit.

    Returns:
        A tuple of leaf nodes found during this limited search.
    """
    if not isinstance(TREE, tuple):
        return (TREE,)
    
    if depth == 0:
        return ()

    result = ()
    i = len(TREE) - 1
    while i >= 0:
        result = result + DLS(TREE[i], depth - 1)
        i = i - 1
    return result

print(DFID("ROOT", 0))
# → ('ROOT',)

print(DFID(((("L", "E"), "F"), "T"), 3))
# → ('T', 'T', 'F', 'T', 'F', 'E', 'L')

print(DFID(("R", ("I", ("G", ("H", "T")))), 4))
# → ('R', 'I', 'R', 'G', 'I', 'R', 'T', 'H', 'G', 'I', 'R')

print(DFID(((("A", ("B",)), ("C",), "D")), 3))
# → ('D', 'D', 'C', 'A', 'D', 'C', 'B', 'A')

print(DFID(("T", ("H", "R", "E"), "E"), 2))
# → ('E', 'T', 'E', 'E', 'R', 'H', 'T')

print(DFID(("A", (("C", (("E",), "D")), "B"),), 5))
# → ('A', 'B', 'A', 'B', 'C', 'A', 'B', 'D', 'C', 'A', 'B', 'D', 'E', 'C', 'A')



# These functions implement a depth-first solver for the homer-baby-dog-poison
# problem. In this implementation, a state is represented by a single tuple
# (homer, baby, dog, poison), where each variable is True if the respective entity is
# on the west side of the river, and False if it is on the east side.
# Thus, the initial state for this problem is (False False False False) (everybody
# is on the east side) and the goal state is (True True True True).

# The main entry point for this solver is the function DFS_SOL, which is called
# with (a) the state to search from and (b) the path to this state. It returns
# the complete path from the initial state to the goal state: this path is a
# list of intermediate problem states. The first element of the path is the
# initial state and the last element is the goal state. Each intermediate state
# is the state that results from applying the appropriate operator to the
# preceding state. If there is no solution, DFS_SOL returns [].
# To call DFS_SOL to solve the original problem, one would call
# DFS_SOL((False, False, False, False), [])
# However, it should be possible to call DFS_SOL with any intermediate state (S)
# and the path from the initial state to S (PATH).

# First, we define the helper functions of DFS_SOL.

# FINAL_STATE takes a single argument S, the current state, and returns True if it
# is the goal state (True, True, True, True) and False otherwise.
def FINAL_STATE(S):
    return S == (True, True, True, True)


# NEXT_STATE returns the state that results from applying an operator to the
# current state. It takes two arguments: the current state (S), and which entity
# to move (A, equal to "h" for homer only, "b" for homer with baby, "d" for homer
# with dog, and "p" for homer with poison).
# It returns a list containing the state that results from that move.
# If applying this operator results in an invalid state (because the dog and baby,
# or poisoin and baby are left unsupervised on one side of the river), or when the
# action is impossible (homer is not on the same side as the entity) it returns [].
# NOTE that NEXT_STATE returns a list containing the successor state (which is
# itself a tuple)# the return should look something like [(False, False, True, True)].
def NEXT_STATE(S, A):
    h, b, d, p = S
    if A == 'h':
        nh = not h
        if (b == h and d == h) or (b == h and p == h):
            return []
        return [(nh, b, d, p)]
    elif A == 'b' and h == b:
        nh = nb = not h
        if (d == h and h != b) or (p == h and h != b):
            return []
        return [(nh, nb, d, p)]
    elif A == 'd' and h == d:
        nh = nd = not h
        if (b == h and h != d) or (p == h and b == h and h != d):
            return []
        return [(nh, b, nd, p)]
    elif A == 'p' and h == p:
        nh = np = not h
        if (b == h and h != p) or (d == h and b == h and h != p):
            return []
        return [(nh, b, d, np)]
    return []


# SUCC_FN returns all of the possible legal successor states to the current
# state. It takes a single argument (S), which encodes the current state, and
# returns a list of each state that can be reached by applying legal operators
# to the current state.
def SUCC_FN(S):
    actions = ['h', 'b', 'd', 'p']
    result = []
    for a in actions:
        ns = NEXT_STATE(S, a)
        if ns:
            result.extend(ns)
    return result


# ON_PATH checks whether the current state is on the stack of states visited by
# this depth-first search. It takes two arguments: the current state (S) and the
# stack of states visited by DFS (STATES). It returns True if S is a member of
# STATES and False otherwise.
def ON_PATH(S, STATES):
    return S in STATES


# MULT_DFS is a helper function for DFS_SOL. It takes two arguments: a list of
# states from the initial state to the current state (PATH), and the legal
# successor states to the last, current state in the PATH (STATES). PATH is a
# first-in first-out list of states# that is, the first element is the initial
# state for the current search and the last element is the most recent state
# explored. MULT_DFS does a depth-first search on each element of STATES in
# turn. If any of those searches reaches the final state, MULT_DFS returns the
# complete path from the initial state to the goal state. Otherwise, it returns
# [].
def MULT_DFS(STATES, PATH):
    for state in STATES:
        if FINAL_STATE(state):
            return PATH + [state]
        if not ON_PATH(state, PATH):
            result = DFS_SOL(state, PATH + [state])
            if result:
                return result
    return []


# DFS_SOL does a depth first search from a given state to the goal state. It
# takes two arguments: a state (S) and the path from the initial state to S
# (PATH). If S is the initial state in our search, PATH is set to []. DFS_SOL
# performs a depth-first search starting at the given state. It returns the path
# from the initial state to the goal state, if any, or [] otherwise. DFS_SOL is
# responsible for checking if S is already the goal state, as well as for
# ensuring that the depth-first search does not revisit a node already on the
# search path (i.e., S is not on PATH).
def DFS_SOL(S, PATH):
    if FINAL_STATE(S):
        return PATH + [S]
    if ON_PATH(S, PATH):
        return []
    successors = SUCC_FN(S)
    return MULT_DFS(successors, PATH + [S])
