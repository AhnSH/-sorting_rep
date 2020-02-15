import random
import time

def rand_ints(n):
    random.seed(100)
    return random.sample(range(1, 100000), n)

def quick_sort(arr):
    if not arr:
        return []
    pivot = arr[0]
    remains = arr[1:]
    smaller = [x for x in remains if x < pivot]
    larger = [x for x in remains if x >= pivot]
    return quick_sort(smaller) + [pivot] + quick_sort(larger)

def insert_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def merge_sort(arr):
    if not arr:
        return []
    elif len(arr)==1:
        return arr
    else:
        half = len(arr) // 2
        return merge(merge_sort(arr[:half]), merge_sort(arr[half:]))


def merge(a1, a2):
    if a1 and a2:
        if a1[0] < a2[0]:
            return [a1[0]] + merge(a1[1:], a2)
        else:
            return [a2[0]] + merge(a1, a2[1:])
    elif a1:
        return a1
    elif a2:
        return a2
    else:
        return []

def merge_rep_sort(arr):
    if not arr:
        return []
    elif len(arr)==1:
        return arr
    else:
        half = len(arr) // 2
        return merge_rep(merge_rep_sort(arr[:half]), merge_rep_sort(arr[half:]))

def merge_rep3_sort(arr):
    if len(arr) < 5:
        return insert_sort(arr)
    else:
        half = len(arr) // 2
        return merge_rep(merge_rep3_sort(arr[:half]), merge_rep3_sort(arr[half:]))


def merge_rep(a1, a2):
    a3 = []
    i,j = 0,0
    maxi, maxj = len(a1), len(a2)
    while True:
        if i < maxi and j < maxj:
            if a1[i] < a2[j]:
                a3.append(a1[i])
                i += 1
            else:
                a3.append(a2[i])
                j += 1
        elif i < maxi:
            for k in range(i, maxi):
                a3.append(a1[k])
            break
        elif j < maxj:
            for k in range(j, maxj):
                a3.append(a2[k])
            break
    return a3

if __name__ == '__main__':
    v = rand_ints(900)
    # print(v)
    t1 = time.time()
    v2 = quick_sort(v)
    t2 = time.time()
    print('quick_sort time', t2 - t1)

    # t1 = time.time()
    # v2 = insert_sort(v)
    # t2 = time.time()
    # print('insert_sort time', t2 - t1)
    # v3 = merge_sort(v)
    # v3 = insert_sort(v)
    t1 = time.time()
    v2 = merge_sort(v)
    t2 = time.time()
    print('merge_sort time', t2 - t1)
    #
    t1 = time.time()
    v2 = merge_rep_sort(v)
    t2 = time.time()
    print('merge_rep_sort time', t2 - t1)
    #
    t1 = time.time()
    v2 = merge_rep3_sort(v)
    t2 = time.time()
    print('merge_rep3_sort time', t2 - t1)

    t1 = time.time()
    for i in range(100):
        v2 = sorted(v)
    t2 = time.time()
    # v2 = sorted(v)
    print('sorted time', t2 - t1)