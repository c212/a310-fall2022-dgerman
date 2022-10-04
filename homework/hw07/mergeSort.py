def merge(a, b):
    if a == [] and b == []:
        return []
    elif a == []:
        return b
    elif b == []:
        return a
    else:
        if a[0] < b[0]:
            return [ a[0] ] + merge(a[1:], b)
        else:
            return [ b[0] ] + merge(a, b[1:])

print(merge([], [1, 2, 3]))
print(merge([2, 4, 6], []))
print(merge([1, 3, 5], [2, 6, 8]))

import random

def sort(a):
    if len(a) <= 1:
        return a
    else: 
        index = random.randrange(0, len(a))
        return merge(sort(a[:index]), sort(a[index:]))
