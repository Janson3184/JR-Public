

class Node:
    def __init__(self, label):
        self.label = label
        self.child_right = self.child_left = None

    def other_name(self, level=0):
        print('\t' * level + repr(self.label))
        for child in [self.child_right, self.child_left]:
            if child is not None:
                child.other_name(level+1)                       # Recursion


def reverse(starting_node):

    if starting_node is not None:

        reverse(starting_node.child_right)  # Recursion
        reverse(starting_node.child_left)

        starting_node.child_left, starting_node.child_right = starting_node.child_right, starting_node.child_left


def print_tree(starting_node):

    if starting_node is not None:

        print(starting_node.label)

        print_tree(starting_node.child_left)    # Recursion
        print_tree(starting_node.child_right)


def standalone_other(root, level=0):        # as a standalone function that doesn't rely on class.
    print('\t' * level + repr(root.label))
    for child in [root.child_right, root.child_left]:
        if child is not None:
            standalone_other(child, level+1)

root = Node(1)

root.child_left = Node(2)
root.child_left.child_left = Node(4)
root.child_left.child_right = Node(6)

root.child_right = Node(3)
root.child_right.child_left = Node(7)
root.child_right.child_right = Node(5)

root.child_right.child_right.child_left = Node(9)

print_tree(root)
print('\nReversing...\n')
root.other_name()
standalone_other(root)
reverse(root)

print_tree(root)

print('othername')
root.other_name()
standalone_other(root)