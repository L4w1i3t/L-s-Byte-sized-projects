import itertools

def generate_all_trees(labels, max_nodes):
    # Generates all rooted trees with up to max_nodes nodes, labeled with the given labels
    # Each tree is represented as a tuple: (label, [list of child trees])
    if max_nodes == 0:
        return [None]
    trees = []
    for nodes in range(1, max_nodes + 1):
        if nodes == 1:
            for label in labels:
                trees.append((label, []))
        else:
            for label in labels:
                for partition in partitions(nodes - 1):
                    child_combinations = [generate_all_trees(labels, size) for size in partition]
                    for children in itertools.product(*child_combinations):
                        trees.append((label, list(children)))
    return trees

def partitions(n, I=1):
    # Generates all integer partitions of n (order matters)
    yield (n,)
    for i in range(I, n//2 + 1):
        for p in partitions(n - i, i):
            yield (i,) + p

def is_homeomorphic_embedding(t1, t2):
    # Checks whether tree t1 is homeomorphically embeddable into tree t2
    if t1 is None:
        return True
    if t2 is None:
        return False
    if t1[0] != t2[0]:
        return False
    t1_children = t1[1]
    t2_children = t2[1]
    if len(t1_children) > len(t2_children):
        return False
    # Check if there's an injective mapping from t1's children to t2's children
    for child_indices in itertools.combinations(range(len(t2_children)), len(t1_children)):
        if all(is_homeomorphic_embedding(c1, t2_children[i]) for c1, i in zip(t1_children, child_indices)):
            return True
    return False

def generate_sequence(n):
    labels = [str(i) for i in range(1, n+1)]
    max_nodes = n  # Just define n during demonstration
    all_trees = generate_all_trees(labels, max_nodes)
    print(f"Generated {len(all_trees)} trees with up to {max_nodes} nodes and {n} labels.")
    # Sort trees for consistent ordering
    all_trees.sort(key=lambda x: tree_to_string(x))
    # Attempt to build the longest possible sequence
    max_sequence = []
    def build_sequence(sequence, remaining_trees):
        nonlocal max_sequence
        if len(sequence) > len(max_sequence):
            max_sequence = sequence.copy()
        for i, tree in enumerate(remaining_trees):
            embeddable = False
            for prev_tree in sequence:
                if is_homeomorphic_embedding(prev_tree, tree):
                    embeddable = True
                    break
            if not embeddable:
                sequence.append(tree)
                build_sequence(sequence, remaining_trees[:i] + remaining_trees[i+1:])
                sequence.pop()
    build_sequence([], all_trees)
    return max_sequence

def tree_to_string(tree):
    # Converts a tree to a string representation for sorting and display.
    if tree is None:
        return ''
    label, children = tree
    return f"{label}({','.join(tree_to_string(child) for child in children)})"

# Enter a number to make a tree (i.e. 1 is TREE(1), 3 is TREE(3), etc.). Has a check for if n is an integer
while True:
    try:
        n = int(input("Enter a number for your tree: "))
        sequence = generate_sequence(n)
        print(f"\nValid sequence length for TREE({n}): {len(sequence)}")
        for idx, tree in enumerate(sequence):
            print(f"Tree {idx + 1}: {tree_to_string(tree)}")
        break
    except ValueError:
        print("Enter an integer, GOOFY.")