#!/usr/bin/env python

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return "Node:" + str(self.val)

    def __repr__(self):
        return "Node:" + str(self.val)


def insert(root, node):
    if not root:
        root = node
    else:
        if root.val > node.val:
            if root.left == None:
                root.left = node
            else:
                insert(root.left, node)
        else:
            if root.right == None:
                root.right = node
            else:
                insert(root.right, node)


def in_order_traverse(node):
    if not node:
        return in_order_traverse(node.left), print(node), in_order_traverse(node.right)


def pre_order_traverse(node):
    if not node:
        return print(node), pre_order_traverse(node.left), pre_order_traverse(node.right)


def post_order_traverse(node):
    if not node:
        return post_order_traverse(node.left), post_order_traverse(node.right), print(node)


def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))


def min_height(root):
    if not root:
        return 0
    return 1 + min(min_height(root.left), min_height(root.right))


def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def is_balanced(root):
    if not root:
        return True

    lh = height(root.left)
    rh = height(root.right)

    if (abs(lh - rh) <= 1 and is_balanced(root.left) and is_balanced(root.right)):
        return True
    return False


def search(root, value):
    if not root:
        return None
    if root.val == value:
        return root
    elif value < root.val:
        return search(root.left, value)
    else:
        return search(root.right, value)


def print_level_order(root):
    for d in range(1, height(root) + 1):
        level = print_level(root, d, [])
        if level:
            print("level ", d, " is ", level)


def print_level(root, level, nodelist=[]):
    if not root:
        return None
    if level == 1:
        nodelist.append(root)
    else:
        print_level(root.left, level - 1, nodelist)
        print_level(root.right, level - 1, nodelist)
    return nodelist


def to_list(root, nlist=[]):
    if root:
        nlist.append(root.val)
        to_list(root.left, nlist)
        to_list(root.right, nlist)
    return nlist


def load_from_list(nlist):
    root = None
    if list and len(nlist) > 0:
        # create the root node from first item in list
        root = Node(nlist[0])
        for n in range(1, len(nlist)):
            insert(root, Node(nlist[n]))
    return root


def find_common_ancestor(root, n1, n2):
    if (n2 < n1) or not root or root.val == n1 or root.val == n2:
        return None
    if root.left and (root.left.val == n1 or root.left.val == n2):
        return root.val
    if root.right and (root.right.val == n1 or root.right.val == n2):
        return root.val

    if (root.val > n1 and root.val < n2):
        return root.val
    if (root.val < n1 and root.val < n1):
        return find_common_ancestor(root.right, n1, n2)
    if (root.val > n1 and root.val > n2):
        return find_common_ancestor(root.left, n1, n2)


def is_subtree(root, node):
    found = search(root, node.val)
    if found and found != root:
        return equals(found, node)
    return False


def equals(node1, node2):
    if not node1 and not node2:
        return True
    if node1 and node2:
        if node1.val == node2.val:
            return equals(node1.left, node2.left) and equals(node1.right, node2.right)
    return False


if __name__ == "__main__":
    root = Node(20)
    insert(root, Node(9))
    insert(root, Node(22))
    insert(root, Node(6))
    insert(root, Node(12))
    insert(root, Node(16))
    insert(root, Node(25))
    insert(root, Node(21))
    insert(root, Node(10))

    print("In order traverse", in_order_traverse(root))

    print("Pre order traverse", pre_order_traverse(root))

    print("Post order traverse", post_order_traverse(root))

    print("Tree height is ", height(root))

    print("Min height is ", min_height(root))

    print("Tree is balanced = ", is_balanced(root))

    print("Search for 7 ", search(root, 7))
    print("Search for 4 ", search(root, 4))
    print("Search for 20 ", search(root, 20))

    print("count nodes ", count_nodes(root))

    # print "print level order", print_level_order(root)
    # nlist = to_list(root)
    # print "to list ", nlist
    # new_root = load_from_list(nlist)
    # print "load from list ", pre_order_traverse(new_root)

    print("find common ancestor 6, 16:", find_common_ancestor(root, 6, 16))
    print("find common ancestor 12, 16:", find_common_ancestor(root, 12, 16))
    print("find common ancestor 21, 25:", find_common_ancestor(root, 21, 25))
    print("find common ancestor 20, 22:", find_common_ancestor(root, 20, 22))

    tree1 = Node(12)
    insert(tree1, Node(10))
    insert(tree1, Node(16))

    tree2 = Node(12)
    insert(tree2, Node(10))
    insert(tree2, Node(13))

    tree3 = Node(20)
    insert(tree3, Node(9))
    insert(tree3, Node(22))
    insert(tree3, Node(6))
    insert(tree3, Node(12))
    insert(tree3, Node(16))
    insert(tree3, Node(25))
    insert(tree3, Node(21))
    insert(tree3, Node(10))

    print("Tree 1 is subtree ", is_subtree(root, tree1))
    print ("Tree 2 is subtree ", is_subtree(root, tree2))
    print("Tree 3 is subtree ", is_subtree(root, tree3))
    print("Tree 3 equals ", equals(root, tree3))