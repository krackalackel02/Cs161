# hw1.py
# Author: Paul Kallarackel
# Collaborators:
# This file implements five functions:
#   1. PAD(n): Computes the n-th number in the Padovan sequence.
#   2. SUMS(n): Computes the number of additions made when computing PAD(n).
#   3. ANON(tree): Replaces all leaves of a tree structure with '?'.
#   4. TREE_HEIGHT(tree): Computes the height of a tree.
#   5. TREE_ORDER(tree): Computes the postorder traversal of a tree.


# Question 1 - Padovan Sequence
def PAD(n):
    """
    Returns the n-th number in the Padovan sequence.
    Arguments:
        n (int): The index in the Padovan sequence.
    Returns:
        int: The value of the n-th Padovan number.
    """
    # Base case: if n is 0, 1, or 2, return 1
    if n == 0 or n == 1 or n == 2:
            return 1
    # Recursive case: return the sum of the two previous terms
    # in the Padovan sequence
    return PAD(n - 2) + PAD(n - 3)

# Question 1: PAD
print("PAD tests")
print(PAD(5))  # 3
print(PAD(3))  # 2
print(PAD(4))  # 2
print()


# Question 2 - Count number of additions in PAD
def SUMS(n):
    """
    Returns the number of additions performed to compute PAD(n).
    Arguments:
        n (int): The index in the Padovan sequence.
    Returns:
        int: The number of additions used in recursive PAD.
    """
    # Base case: if n is 0, 1, or 2, return 0
    # (no additions needed for these cases)
    if n == 0 or n == 1 or n == 2:
            return 0
    # Recursive case: return the number of additions needed
    # to compute the Padovan sequence for n
    return 1 + SUMS(n - 2) + SUMS(n - 3)

# Question 2: SUMS
print("SUMS tests")
print(SUMS(5))  # 3
print(SUMS(3))  # 1
print(SUMS(4))  # 2
print()


# Question 3 - Anonymize leaves in tree
def ANON(tree):
    """
    Replaces all leaves in the tree with '?'.
    Arguments:
        tree: A nested tuple structure representing a tree.
    Returns:
        A tree with the same structure, but all leaves replaced by '?'.
    """
    # Base case: if the tree is not a tuple, return '?'
    if not isinstance(tree, tuple):
            return "?"
    # Recursive case: replace each leaf with '?'
    # and return a new tuple with the same structure
    return tuple(ANON(subtree) for subtree in tree)

# Question 3: ANON
print("ANON tests")
print(ANON(42))  # '?'
print(ANON("FOO"))  # '?'
print(ANON((("L", "E"), "F", "T")))  # ((‘?’, ‘?’), ‘?’, ‘?’)
print(ANON((5, "FOO", 3.1, -0.2)))  # (‘?’, ‘?’, ‘?’, ‘?’)
print(ANON((1, ("FOO", 3.1), -0.2)))  # (‘?’, (‘?’, ‘?’), ‘?’)
print(ANON(((1, 2), ("FOO", 3.1), ("BAR", -0.2))))  # ((‘?’, ‘?’), (‘?’, ‘?’), (‘?’, ‘?’))
print(ANON(("R", ("I", ("G", ("H", "T"))))))  # (‘?’, (‘?’, (‘?’, (‘?’, ‘?’))))
print()

# Question 4 - Compute tree height
def TREE_HEIGHT(tree):
    """
    Computes the height of the tree.
    Arguments:
        tree: A nested tuple representing a tree.
    Returns:
        int: Height of the tree (0 for leaf nodes).
    """
    # Base case: if the tree is not a tuple, return 0
    # (height of a leaf is 0)
    if not isinstance(tree, tuple):
        return 0
    # Recursive case: return 1 plus the maximum height of the subtrees
    # (left, middle, right) of the tree
    return 1 + max(TREE_HEIGHT(subtree) for subtree in tree)

# Question 4: TREE_HEIGHT
print("TREE_HEIGHT tests")
print(TREE_HEIGHT(1))  # 0
print(TREE_HEIGHT((5, "FOO", 3.1, -0.2)))  # 1
print(TREE_HEIGHT((1, ("FOO", 3.1), -0.2)))  # 2
print(TREE_HEIGHT(("R", ("I", ("G", ("H", "T"))))))  # 4
print()

# Question 5 - Postorder traversal of ordered tree
def TREE_ORDER(tree):
    """
    Computes the postorder traversal of a tree.
    Arguments:
        tree: A nested tuple representing a tree.
    Returns:
        tuple: Postorder traversal of the tree as a flat tuple.
    """
    # Base case: if the tree is not a tuple, return a tuple with the tree itself
    # (this is a leaf node)
    if not isinstance(tree, tuple):
            return (tree,)
    # Recursive case: perform postorder traversal on the tree
    # and return a tuple with the left, middle, and right subtrees
    left, middle, right = tree
    return TREE_ORDER(left) + TREE_ORDER(right) + (middle,)

# Question 5: TREE_ORDER
print("TREE_ORDER tests")
print(TREE_ORDER(42))  # (42,)
print(TREE_ORDER(((1, 2, 3), 7, 8)))  # (1, 3, 2, 8, 7)
print(TREE_ORDER(((3, 7, 10), 15, ((16, 18, 20), 30, 100))))  # (3, 10, 7, 16, 20, 18, 100, 30, 15)
