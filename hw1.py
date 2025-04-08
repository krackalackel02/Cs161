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


# Question 1: PAD
print("PAD tests")
print(PAD(5))  # 3
print(PAD(3))  # 2
print(PAD(4))  # 2
print()

# Question 2: SUMS
print("SUMS tests")
print(SUMS(5))  # 3
print(SUMS(3))  # 1
print(SUMS(4))  # 2
print()

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

# Question 4: TREE_HEIGHT
print("TREE_HEIGHT tests")
print(TREE_HEIGHT(1))  # 0
print(TREE_HEIGHT((5, "FOO", 3.1, -0.2)))  # 1
print(TREE_HEIGHT((1, ("FOO", 3.1), -0.2)))  # 2
print(TREE_HEIGHT(("R", ("I", ("G", ("H", "T"))))))  # 4
print()

# Question 5: TREE_ORDER
print("TREE_ORDER tests")
print(TREE_ORDER(42))  # (42,)
print(TREE_ORDER(((1, 2, 3), 7, 8)))  # (1, 3, 2, 8, 7)
print(TREE_ORDER(((3, 7, 10), 15, ((16, 18, 20), 30, 100))))  # (3, 10, 7, 16, 20, 18, 100, 30, 15)
