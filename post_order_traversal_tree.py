#list to tree

class Tree(object):
    """this is a multi-leaf tree"""
    def __init__(self, val=None):
        self.root = val
        self.leaf = []

def list_to_tree(atree, alist):
    """convert list of lists to multi-leaf tree with recursion"""
    if alist == [] or isinstance(alist, basestring):
        return
    atree.root = alist[0]
    alist.pop(0)
    for index, val in enumerate(alist):
        atree.leaf.append(Tree(val))
        list_to_tree(atree.leaf[-1], val)
    return atree

def post_order_traversal(tree_list):
    atree = list_to_tree(Tree(),tree_list)
    result = []

    def postorder(tree):
        """recursive implementation"""
        if tree is None:
            return
        for leaf in tree.leaf:
            postorder(leaf)
        result.append(tree.root)
    
    postorder(atree)
    return result


Tree1 = [1, [2, [4], [5], [3]]] # this is not like graphic
Tree2 = ['f', ['b', ['a'], ['d', ['c'], ['e']]], ['g', ['i', ['h']]]]
Tree3 = ['re', ['b', ['orn'], ['ate']], ['alize', ['s']], ['lief'], ['d', ['der']]]
assert post_order_traversal(Tree1) == [4,5,2,3,1]  # right answer: [4, 5, 3, 2, 1]
assert post_order_traversal(Tree2) == ['a', 'c', 'e', 'd', 'b', 'h', 'i', 'g', 'f']
assert post_order_traversal(Tree3) == ['orn', 'ate', 'b', 's', 'alize', 'lief', 'der', 'd',
're']
