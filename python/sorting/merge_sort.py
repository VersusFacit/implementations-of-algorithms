
# Divide and conquer (recursive) merge sort time complexity
# - best    O(1) with optimization
# - worst   O(nlog(n)) n for each of log(n) subproblem groups
# - average O(nlog(n))
#
# Array based divide and conquer (recursive) merge sort space complexity
# - base array      O(n)
# - auxiliary space O(n) on any iteration during copying in merge()
# - stack frames    O(log n)
# - sentinels       O(1) during copying in merge()
#
# S(n) = Ω(n) from base; S(n) = O(n) from auxiliary, and frames with copied
#       sublists
#   * O(1) + O(log n) if passing by reference or ordering using indexes
#       (in situ)

# Hence, T(n) = O(nlog(n)), S(n) = O(n) = O(n) + O(2n) + O(logn) + O(1)
# * base, stack frames, and O(2n) during the copy phase of the merge()
#   operation, with O(2n) setting an imprecise upper bound for odd n
# * S(n) the same even with static arrays (Python's are dynamic)

def is_sorted(elems):
    return all(
        [x <= y for x, y in zip(elems, elems[1:])]
    )


def merge(l1, l2):

    # recommendation of https://stackoverflow.com/
    # questions/1966591/hasnext-in-python-iterators#comment28352762_15606960
    sentinel = object()

    merged_lists = []
    l1_iter = iter(l1+[sentinel])
    l2_iter = iter(l2+[sentinel])

    curr_l1 = next(l1_iter)
    curr_l2 = next(l2_iter)
    while curr_l1 is not sentinel and curr_l2 is not sentinel:
        if curr_l1 <= curr_l2:
            merged_lists.append(curr_l1)
            curr_l1 = next(l1_iter)
        else:
            merged_lists.append(curr_l2)
            curr_l2 = next(l2_iter)

    while curr_l1 is not sentinel:
        merged_lists.append(curr_l1)
        curr_l1 = next(l1_iter)

    while curr_l2 is not sentinel:
        merged_lists.append(curr_l2)
        curr_l2 = next(l2_iter)

    return merged_lists


def merge_sort(elems):
    # best case optimization
    if is_sorted(elems):
        return elems

    def merge_sort_loop(elems):
        if len(elems) <= 1:
            return(elems)

        j = len(elems) // 2
        return merge(
            merge_sort_loop(elems[0:j]),
            merge_sort_loop(elems[j:len(elems)])
        )

    return merge_sort_loop(elems)


# Test Code
test1 = [-1, 0, 1]
test2 = [1, 0, -1]
test2b = [1, 0, -1, -2]
test3 = [-1, 3, 0, -3, 1, 2, 1]
test3b = [1, 1, 1, 1, -1, -1, -1]
test4 = list(range(1000, -1, -1))
test5 = list(range(0, 1000))


def x(elems): merge_sort(elems)


print(x([]))
print(x(test1))
print(x(test2))
print(x(test2b))
print(x(test3))
print(x(test3b))
print(x(test4) == list(range(0, 1001)))
print(x(test5) == list(range(0, 1000)))
