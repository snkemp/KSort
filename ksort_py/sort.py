
### Quick sort
def quick_sort(S):
    n = len(S)
    stack = [(0, n-1)]

    def partition(low, high):
        j = low-1
        pivot = S[high]

        for i in range(low, high):
            if S[i] < pivot:
                j += 1
                S[i], S[j] = S[j], S[i]

        S[j+1], S[high] = S[high], S[j+1]
        return j+1


    while stack:
        low, high = stack.pop()
        p = partition(low, high)

        if p+1 < high:
            stack.append((p+1, high))
        if p-1 > low:
            stack.append((low, p-1))

    return S

### Merge Sort
def merge_sort(S):
    n = len(S)
    stack = []

    def merge(low, mid, high):
        T = []
        i = low
        j = mid+1
        while i <= mid and j <= high:
            if S[i] < S[j]:
                T.append(S[i])
                i += 1
            else:
                T.append(S[j])
                j += 1

        while i <= mid:
            T.append(S[i])
            i += 1
        while j <= high:
            T.append(S[j])
            j += 1
        S[low:high+1] = T

    def sort(low, high):
        if low < high:
            mid = (low+high) >> 1
            stack.append((merge, low, mid, high))
            stack.append((sort, low, mid))
            stack.append((sort, mid+1, high))

    stack.append((sort, 0, n-1))
    while stack:
        func, *args = stack.pop()
        func(*args)

    return S

### Heap sort
def heap_sort(S):
    N = len(S)
    n = N >> 1
    depth = (N+1).bit_length() -1

    # Heapify (max heap, so we can place at the back later)
    for d in range(depth-1, -1, -1):

        num = 1 << d
        k = num-1
        for i in range(k, k+num):

            # Sift down
            pos = i
            sel = (pos << 1) + 1
            cur = S[pos]
            while sel < N:
                if sel+1 < N and S[sel+1] > S[sel]:
                    sel += 1

                if S[sel] <= cur:
                    break

                S[pos] = S[sel]
                pos = sel
                sel = (pos << 1) + 1

            S[pos] = cur

    # Sort
    for i in range(N-1, -1, -1):
        S[0], S[i] = S[i], S[0]

        pos = 0
        cur = S[0]
        sel = (pos << 1) + 1
        while sel < i:
            if sel+1 < i and S[sel+1] > S[sel]:
                sel += 1

            if S[sel] <= cur:
                break

            S[pos] = S[sel]
            pos = sel
            sel = (pos << 1) + 1

        S[pos] = cur

    return S

# Output
algorithms = [
    # ('Quick Sort', quick_sort),  # XXX For some reason this is performing very poorly. Will investigate soon
    ('Merge Sort', merge_sort),
    ('Heap  Sort', heap_sort)
]
