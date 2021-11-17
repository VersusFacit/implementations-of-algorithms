'''demonstration of a generic tree

Because tree types are created with a special purpose in mind (and with special
constraints to meet those goals), many trees are mutually irreducible.
A generic tree without additional rules is an acyclical directed graph where
each node excluding the root is reachable by exactly one path.
'''

import unittest


class Node(object):
    '''allow arbitrary size nodes'''
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children

    def get_val(self):
        return self.val

    def set_children(self, val):
        self.children = val

    def __eq__(self, other):
        return self.val == other.val and self.children == other.children


class Tree(object):
    '''arbitrary serialization scheme using JSON set adjacency model, which
    can be further compressed algorithmically'''
    def __init__(self, dct):
        self.root = self.deserialize(dct)

    def serialize(self):
        '''invokes algorithm to build dictionary and returns json'''
        pass

    def _find_roots(self, dct):
        '''root defined as node without any parents'''
        '''O(n) time (assuming ideal hash) and O(n) auxiliary space'''

        NOT_YET = object()
        hash_map = {}
        for k, v in dct.items():
            # address elements in adjacency list
            for i in v:
                hash_map[i] = False

            # address keys of adjacency lists
            status = hash_map.get(k, NOT_YET)
            if NOT_YET == status:
                hash_map[k] = True   # could be root
            elif status:
                hash_map[k] = False  # can't be root

        return [k for k, v in hash_map.items() if v]

    def _build_from_root(self, root, dct):
        '''naive traversal which does not check for cycles'''
        children = dct.get(root.get_val(), [])
        root.set_children(
            [self._build_from_root(Node(child), dct) for child in children]
        )
        return root

    def _check_for_cycles_in_dct(self, adjacency_list):
        '''dp solution: runtime θ(|V|) and auxiliary space θ(|V|)'''
        skipable = set()  # nodes do not contain cycles
        for node, children in adjacency_list.items():
            to_process = []  # running stack
            visited = []

            # skip previously reached
            if node in skipable:
                continue

            # begin iterating over node
            visited.append(node)
            for child in children:
                to_process.append(child)

            while len(to_process) > 0:
                current = to_process.pop()
                if current in visited:
                    return True
                else:
                    visited.append(current)
                    for child in adjacency_list.get(current, []):
                        to_process.append(child)

            # Add subproblems to skipable
            for acyclic_node in visited:
                skipable.add(acyclic_node)
        else:
            return False

    def deserialize(self, dct):
        '''convert json into tree and return root node'''

        # check for cycles
        self._check_for_cycles_in_dct(dct)

        # get root
        roots = self._find_roots(dct)
        if len(roots) < 1:
            raise ValueError(f'{dct} has no root node.')
        elif len(roots) > 1:
            raise ValueError(f'{dct} has more than one root node.')

        # build tree
        return self._build_from_root(Node(roots[0]), dct)

    def get_root(self):
        return self.root

    def __str__(self):
        return self.serialize()


class TestTree(unittest.TestCase):
    def test_tree_construction(self):
        tree = {
            1: [2, 3, 4],
            3: [5, 6],
            5: [7]
            # 7: [1]
        }
        self.assertEqual(
            Tree(tree).get_root(),
            Node(1, [
                Node(2),
                Node(3, [
                    Node(5, [
                        Node(7)
                    ]),
                    Node(6)
                ]),
                Node(4)
            ])
        )

    def test_small_tree_construction(self):
        tree = {
            1: []
        }
        self.assertEqual(Tree(tree).get_root(), Node(1, []))

    def test_no_root(self):
        tree = {
            1: [2, 3, 4],
            2: [5, 6, 1],
        }
        with self.assertRaises(ValueError):
            Tree(tree)

    def test_cyclic_tree(self):
        tree = {
            1: [2],
            2: [3],
            3: [4],
            4: [5],
            5: [6],
            6: [7],
            7: [8],
            8: [9],
            9: [1],
        }
        with self.assertRaises(ValueError):
            Tree(tree)

    def test_deep_tree_construction(self):
        tree = {
            1: [2],
            2: [3],
            3: [4],
            4: [5]
        }
        self.assertEqual(
            Tree(tree).get_root(),
            Node(1, [Node(2, [Node(3, [Node(4, [Node(5, [])])])])])
        )
