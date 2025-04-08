# Question 1 - Padovan Sequence
def PAD(n):
    if n == 0 or n == 1 or n == 2:
            return 1
    return PAD(n - 2) + PAD(n - 3)

# Question 2 - Count number of additions in PAD
def SUMS(n):
    if n == 0 or n == 1 or n == 2:
            return 0
    return 1 + SUMS(n - 2) + SUMS(n - 3)

# Question 3 - Anonymize leaves in tree
def ANON(tree):
    if not isinstance(tree, tuple):
            return "?"
    return tuple(ANON(subtree) for subtree in tree)

# Question 4 - Compute tree height
def TREE_HEIGHT(tree):
    if not isinstance(tree, tuple):
        return 0
    return 1 + max(TREE_HEIGHT(subtree) for subtree in tree)

# Question 5 - Postorder traversal of ordered tree
def TREE_ORDER(tree):
    if not isinstance(tree, tuple):
            return (tree,)
    left, middle, right = tree
    return TREE_ORDER(left) + TREE_ORDER(right) + (middle,)