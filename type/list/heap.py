import heapq as hq
import random



# Heap queue
# Used as a priority queue, like a tree.
# Item in i pos is smaller than in pos 2 * i and 2 * i + 1.

l1 = list(range(10))
random.shuffle(l1)
hq1 = []

# heappush
# Push item onto heap, maintaining the heap invariant.
for v in l1:
  hq.heappush(hq1, v)
l2 = l1.copy()

print(l1) # [0, 3, 8, 6, 4, 2, 5, 7, 1, 9]
print(hq1) # [0, 1, 2, 3, 4, 8, 5, 7, 6, 9]

# heapify
# Transform list into a heap, in-place, in O(len(heap)) time.
hq.heapify(l2) # l2 is now a heap
print(l2) # [0, 1, 2, 3, 4, 8, 5, 7, 6, 9]

# heappop
# Remove and return item at index (default last).
# Raises IndexError if list is empty or index is out of range.

hq1.pop()
print(hq1) # [0, 1, 2, 3, 4, 8, 5, 7, 6] # Removed 9

# heapreplace
'''
Pop and return the current smallest value, and add the new item.

This is more efficient than heappop() followed by heappush(),
and can be more appropriate when using a fixed-size heap.
Note that the value returned may be larger than item!
That constrains reasonable uses of this routine
unless written as part of a conditional replacement:

    if item > heap[0]:
        item = heapreplace(heap, item)
'''

hq.heapreplace(hq1, 23)
print(hq1) # [1, 3, 2, 6, 4, 8, 5, 7, 23]

# nlargest
# Find the n largest elements in a dataset.
print(hq.nlargest(3, hq1)) # [23, 8, 7]

# nsmallest
# Find the n smallest elements in a dataset.
print(hq.nsmallest(3, hq1)) # [1, 2, 3]
