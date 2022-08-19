class TreeNode:
    def __init__(self, nodes=None):
        self.nodes = nodes or []
        self.children = []


def build_list(sibling_levels):
    """Build the challenge output list from the sibling_levels."""
    def build_recursive(levels, tree_node):
        if levels:  # Intermediate nodes.
            check_level = levels[0]  # We only need to check the first level.
            for node in tree_node.nodes:
                output_list.append(node)
                for group in check_level:
                    checking_node = group[0]  # Only the first node is necessary.
                    if node.parent(checking_node):
                        new_tree_node = TreeNode(group)
                        tree_node.children.append(new_tree_node)
                        # Go the following levels.
                        build_recursive(levels[1:], new_tree_node)
                        break
        else:  # Leaf nodes.
            for node in tree_node.nodes:
                output_list.append(node)

    output_list = []
    root = TreeNode(sibling_levels.levels[0][0])
    build_recursive(sibling_levels.levels[1:-1], root)
    # Last node is the [$total, $total, ...]
    return [sibling_levels.levels[-1]] + output_list
