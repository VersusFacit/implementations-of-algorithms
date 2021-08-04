
# Insertion Sort Complexity
# - Best    O(1) with optimization
# - Worst   O(n^2)
# - Average O(n^2)

def is_sorted(elems):
    return all(
        [x <= y for x, y in zip(elems, elems[1:])]
    )


def insertion_sort(elems):
    # best case optimization
    if is_sorted(elems):
        return elems

    for i in range(len(elems)):
        for sub_elem in elems[:i+1]:
            # new subarray unsorted so move copy to correct index
            if elems[i] < sub_elem:
                elems.insert(elems.index(sub_elem), elems[i])
                del elems[i+1]
                break

    return elems


# Test Code
test1 = [-1, 0, 1]
test2 = [1, 0, -1]
test3 = [-1, 3, 0, -3, 1, 2, 1]
test4 = list(range(1000, -1, -1))
test5 = list(range(0, 1000))


def x(elems): return insertion_sort(elems)


print(x([]))
print(x(test1))
print(x(test2))
print(x(test3))
print(x(test4) == list(range(0, 1001)))
print(x(test5) == list(range(0, 1000)))
