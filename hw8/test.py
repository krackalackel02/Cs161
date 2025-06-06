import math

# Data provided in the image
data = {
    'x1': {'A': 't', 'B': 't', 'C': 't', 'D': 'Yes', '#': 1},
    'x2': {'A': 't', 'B': 't', 'C': 'f', 'D': 'Yes', '#': 6},
    'x3': {'A': 't', 'B': 'f', 'C': 't', 'D': 'No', '#': 3},
    'x4': {'A': 't', 'B': 'f', 'C': 'f', 'D': 'No', '#': 1},
    'x5': {'A': 'f', 'B': 't', 'C': 't', 'D': 'Yes', '#': 1},
    'x6': {'A': 'f', 'B': 't', 'C': 'f', 'D': 'No', '#': 6},
    'x7': {'A': 'f', 'B': 'f', 'C': 't', 'D': 'Yes', '#': 2},
    'x8': {'A': 'f', 'B': 'f', 'C': 'f', 'D': 'No', '#': 2},
}

def calculate_entropy(yes_count, no_count):
    """Calculates entropy for a given set of 'Yes' and 'No' counts."""
    total = yes_count + no_count
    if total == 0:
        return 0
    p_yes = yes_count / total
    p_no = no_count / total
    entropy = 0
    if p_yes > 0:
        entropy -= p_yes * math.log2(p_yes)
    if p_no > 0:
        entropy -= p_no * math.log2(p_no)
    return entropy

def get_class_distribution(subset):
    """Returns the count of 'Yes' and 'No' classes in a subset."""
    yes_count = sum(d['#'] for d in subset.values() if d['D'] == 'Yes')
    no_count = sum(d['#'] for d in subset.values() if d['D'] == 'No')
    return yes_count, no_count

def calculate_current_entropy(subset, node_name="current"):
    """Calculates the entropy of a given subset."""
    yes_count, no_count = get_class_distribution(subset)
    total_instances = yes_count + no_count
    
    print(f"  {node_name} Node: Total 'Yes' instances: {yes_count}, Total 'No' instances: {no_count}")
    if total_instances == 0:
        print(f"  {node_name} Node Entropy: 0.0000 (No instances)")
        return 0.0
    
    current_entropy = calculate_entropy(yes_count, no_count)
    print(f"  {node_name} Node Entropy calculation: -({yes_count}/{total_instances}) * log2({yes_count}/{total_instances}) - ({no_count}/{total_instances}) * log2({no_count}/{total_instances})")
    print(f"  {node_name} Node Entropy: {current_entropy:.4f}")
    return current_entropy

def find_best_split(subset, attributes_to_consider, current_level_prefix=""):
    """
    Finds the best attribute to split on for a given subset.
    """
    if not attributes_to_consider:
        print(f"{current_level_prefix} No more attributes to split on.")
        return None, None

    yes_count, no_count = get_class_distribution(subset)
    if yes_count == 0 or no_count == 0:
        print(f"{current_level_prefix} All instances in this node belong to the same class. No need to split.")
        return None, None # Already a pure node

    current_entropy = calculate_current_entropy(subset, node_name=f"{current_level_prefix} Current")

    information_gains = {}
    total_subset_instances = sum(d['#'] for d in subset.values())

    print(f"\n{current_level_prefix} --- Evaluating splits for node with entropy {current_entropy:.4f} ---")

    for attr in attributes_to_consider:
        attribute_values = sorted(list(set(d[attr] for d in subset.values())))
        weighted_entropy_for_attr = 0
        
        print(f"\n{current_level_prefix}   Considering attribute '{attr}':")

        for value in attribute_values:
            branch_subset = {k: v for k, v in subset.items() if v[attr] == value}
            branch_yes, branch_no = get_class_distribution(branch_subset)
            branch_total = branch_yes + branch_no
            
            print(f"{current_level_prefix}     For '{attr}' = '{value}':")
            print(f"{current_level_prefix}       'Yes' instances: {branch_yes}")
            print(f"{current_level_prefix}       'No' instances: {branch_no}")
            print(f"{current_level_prefix}       Total instances: {branch_total}")

            if branch_total > 0:
                entropy_branch = calculate_entropy(branch_yes, branch_no)
                print(f"{current_level_prefix}       Entropy('{value}') calculation: -({branch_yes}/{branch_total}) * log2({branch_yes}/{branch_total}) - ({branch_no}/{branch_total}) * log2({branch_no}/{branch_total})")
                print(f"{current_level_prefix}       Entropy('{value}'): {entropy_branch:.4f}")
                
                weight = branch_total / total_subset_instances
                print(f"{current_level_prefix}       Weight for '{value}': {branch_total}/{total_subset_instances} = {weight:.4f}")
                weighted_entropy_for_attr += weight * entropy_branch
                print(f"{current_level_prefix}       Weighted contribution: {weight:.4f} * {entropy_branch:.4f} = {weight * entropy_branch:.4f}")
            else:
                print(f"{current_level_prefix}       No instances for '{attr}' = '{value}'. Entropy is 0.")

        print(f"{current_level_prefix}   Total weighted entropy for attribute '{attr}': {weighted_entropy_for_attr:.4f}")
        information_gain = current_entropy - weighted_entropy_for_attr
        information_gains[attr] = information_gain
        print(f"{current_level_prefix}   Information Gain for '{attr}': {current_entropy:.4f} - {weighted_entropy_for_attr:.4f} = {information_gain:.4f}")

    if not information_gains: # No attributes to split on, or all attributes have 0 gain
        return None, None
        
    best_attribute = max(information_gains, key=information_gains.get)
    if information_gains[best_attribute] <= 0: # If no gain or negative gain, stop splitting
        print(f"{current_level_prefix} No significant information gain. Stopping split for this node.")
        return None, None
    
    print(f"\n{current_level_prefix} The best attribute to split on is '{best_attribute}' with an Information Gain of {information_gains[best_attribute]:.4f}")
    return best_attribute, information_gains[best_attribute]

def build_tree_step(current_data, current_attributes, level=0, path=""):
    """
    Simulates one step of building a decision tree, showing the best split
    and the resulting subsets for the next level.
    """
    indent = "  " * level
    node_name = f"Node {path}" if path else "Root Node"
    print(f"\n{indent}--- Building {node_name} (Level {level}) ---")

    yes_count, no_count = get_class_distribution(current_data)
    total_instances = yes_count + no_count

    if total_instances == 0:
        print(f"{indent}  This node is empty. Returning.")
        return

    if yes_count == 0:
        print(f"{indent}  All instances are 'No'. This is a leaf node.")
        return {'class': 'No', 'count': no_count}
    if no_count == 0:
        print(f"{indent}  All instances are 'Yes'. This is a leaf node.")
        return {'class': 'Yes', 'count': yes_count}
    
    if not current_attributes:
        # If no attributes left, it's a leaf node (majority class)
        predicted_class = 'Yes' if yes_count >= no_count else 'No'
        print(f"{indent}  No attributes left to split on. This is a leaf node (majority class: {predicted_class}).")
        return {'class': predicted_class, 'yes_count': yes_count, 'no_count': no_count}

    best_attr, gain = find_best_split(current_data, current_attributes, current_level_prefix=indent)

    if best_attr is None:
        # No good split found, make it a leaf node (majority class)
        predicted_class = 'Yes' if yes_count >= no_count else 'No'
        print(f"{indent}  No best attribute found for splitting. This is a leaf node (majority class: {predicted_class}).")
        return {'class': predicted_class, 'yes_count': yes_count, 'no_count': no_count}

    tree_node = {'attribute': best_attr, 'children': {}}
    remaining_attributes = [attr for attr in current_attributes if attr != best_attr]

    attribute_values = sorted(list(set(d[best_attr] for d in current_data.values())))
    for value in attribute_values:
        subset = {k: v for k, v in current_data.items() if v[best_attr] == value}
        if subset:
            print(f"\n{indent}  --- Splitting on '{best_attr}' = '{value}' ---")
            tree_node['children'][value] = build_tree_step(subset, remaining_attributes, level + 1, path=f"{path}.{best_attr}={value}" if path else f"{best_attr}={value}")
        else:
            print(f"\n{indent}  --- No instances for '{best_attr}' = '{value}'. Skipping this branch. ---")

    return tree_node

# Start building the tree
initial_attributes = ['A', 'B', 'C']
decision_tree = build_tree_step(data, initial_attributes)

print("\n--- Decision Tree Structure (Simplified) ---")
# This is a simplified representation of the tree structure.
# For a more detailed print of the tree, you would need a dedicated function.
def print_tree(node, indent_level=0):
    indent = "  " * indent_level
    if 'class' in node:
        if 'yes_count' in node: # Non-pure leaf
            print(f"{indent}Leaf: Class '{node['class']}' (Yes: {node['yes_count']}, No: {node['no_count']})")
        else: # Pure leaf
            print(f"{indent}Leaf: Class '{node['class']}'")
    else:
        print(f"{indent}Split on Attribute: {node['attribute']}")
        for value, child in node['children'].items():
            print(f"{indent}  Value '{value}':")
            print_tree(child, indent_level + 2)

print_tree(decision_tree)