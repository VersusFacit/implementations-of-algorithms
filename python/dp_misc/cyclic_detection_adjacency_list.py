'''Implementations of cycle detection in serialized directed adjacency lists
Experimentation born out of asking how to efficiently check for cycles
where the order of nodes from which one starts out is unknown. This is useful
in adjacency lists where cycle checking is advantageous before moving to tree
construction.
'''

import unittest


class CycleDetectedException(Exception):
    pass


def cycle_detection_test(algorithm):
    class TestCycleDetection(unittest.TestCase):
        def test_empty(self):
            tree_serialized = {}
            self.assertEqual(False, algorithm(tree_serialized))

        def test_only_root(self):
            tree_serialized = {
                1: [2]
            }
            self.assertEqual(False, algorithm(tree_serialized))

        def test_cyclic_root(self):
            tree_serialized = {
                1: [1]
            }
            self.assertEqual(True, algorithm(tree_serialized))

        def test_singlechild_root(self):
            tree_serialized = {
                1: [2]
            }
            self.assertEqual(False, algorithm(tree_serialized))

        def test_deep_tree(self):
            tree_serialized = {
                4: [5],
                1: [2],
                2: [3],
                3: [4],
                5: [6],
                6: [7]
            }
            self.assertEqual(False, algorithm(tree_serialized))

        def test_multichild_root(self):
            tree_serialized = {
                1: [2, 3, 4, 5]
            }
            self.assertEqual(False, algorithm(tree_serialized))

        def test_larger_tree_with_empty_childlist(self):
            tree_serialized = {
                1: [2, 3, 4],
                3: [5],
                4: [],  # sloppy data
                5: [6, 7],
                6: [8, 9]
            }
            self.assertEqual(False, algorithm(tree_serialized))

        def test_larger_tree_cyclic(self):
            tree_serialized = {
                1: [2, 3, 4],
                3: [5],
                5: [6, 7],
                6: [8, 9, 1]
            }
            self.assertEqual(True, algorithm(tree_serialized))

        def test_larger_multicyclic_tree(self):
            tree_serialized = {
                1: [2, 3, 4],
                3: [5],
                5: [6, 5],
                6: [8, 1]
            }
            self.assertEqual(True, algorithm(tree_serialized))

    return TestCycleDetection


# No-order JSON Serialized Adjacency Graph Cycle Check with DFS


def has_cycle_naive(adjacency_list):
    '''naive solution: runtime Ω (|V|) O(|V|^2) and auxiliary space θ(1)'''
    for node, children in adjacency_list.items():
        to_process = []  # running stack
        visited = []

        # begin iterating over reachable nodes (including previously reached)
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
    else:
        return False


class NaiveCycleDetectionTest(cycle_detection_test(has_cycle_naive)):
    pass

# No-order JSON Serialized Adjacency Graph Cycle Check with DFS and DP


def has_cycle_dp(adjacency_list):
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


class DpCycleDetectionTest(cycle_detection_test(has_cycle_dp)):
    pass
