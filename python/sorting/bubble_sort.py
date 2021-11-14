'''
    bubble_sorts: demo of different ways to implement bubble sort on array
    INFO: uses list slicing in lieu of index math. Implicit hits to
    time/space growth (at the implementation level).
'''

# Time: O(n^2) -- more precisely O(1+2+...+n) in all cases. Ω(n) swap check.
# Space: Depends


def iterative_bubble_sort(li):
    '''
    Iterative solution.
    Advantages: O(1) auxiliary space.
    Disadvantages: Iterative thinking; subproblems represented only by index.
    '''
    for i in range(len(li)-1):
        for j in range(0, len(li)-1-i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li


def recursive_bubble_sort(li):
    '''
    General recursive solution.
    Advantages: Illustrates subproblems and 'visually' builds solution set.
    Disadvantages: O(n) auxiliary space from solution set & O(n) stack frames.
    '''
    if len(li) == 0:
        return []

    for i in range(len(li)-1):
        if li[i] > li[i+1]:
            li[i], li[i+1] = li[i+1], li[i]

    return recursive_bubble_sort(li[:-1]) + li[-1:]


def tail_recursive_bubble_sort(li, acc=[]):
    '''
    Tail recursive solution.
    Advantages: Stack overflow impossible. Illustrates subproblems.
    Disadvantages: O(n) auxiliary space by way of sorted algorithm.
    '''
    if len(li) == 0:
        return acc

    for i in range(len(li)-1):
        if li[i] > li[i+1]:
            li[i], li[i+1] = li[i+1], li[i]

    return tail_recursive_bubble_sort(li[:-1], acc=li[-1:]+acc)


li = [2, 4, 6, 3, 1]
print(iterative_bubble_sort(li))

li = [2, 4, 6, 3, 1]
print(recursive_bubble_sort(li))

li = [2, 4, 6, 3, 1]
print(tail_recursive_bubble_sort(li))
