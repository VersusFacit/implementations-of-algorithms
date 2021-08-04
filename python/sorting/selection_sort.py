
# Selection Sort Complexity
# - Best    O(1) with optimization
# - Worst   O(n^2)
# - Average O(n^2)

def is_sorted(elems):
    return all(
        [x <= y for x, y in zip(elems, elems[1:])]
    )


def selection_sort(elems):
    # best case optimization
    if is_sorted(elems):
        return elems

    for i in range(len(elems)-1):
        min_i = elems.index(min(elems[i:]))
        elems[i], elems[min_i] = elems[min_i], elems[i]

    return elems


# Test Code
test1 = [-1, 0, 1]
test2 = [1, 0, -1]
test3 = [-1, 3, 0, -3, 1, 2, 1]
test4 = list(range(1000, -1, -1))
test5 = list(range(0, 1000))


def x(elems): selection_sort(elems)


print(x(test1))
print(x(test2))
print(x(test3))
print(x(test4) == list(range(0, 1001)))
print(x(test5) == list(range(0, 1000)))
