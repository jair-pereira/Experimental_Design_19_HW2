import numpy as np
import time
import argparse

parser = argparse.ArgumentParser(description="Run a sorting algorithm. Outputs time, number of comparison, edit distance, and algortihm name.")

# size, algorithm, fail
parser.add_argument("-n", default=1000, help="size of array (default 1k)",
                    type=int)
parser.add_argument("-a", "--algorithm", default="bubble",
                    choices=["bubble","quick"],
                    help="sorting algorithm (default bubble)")
parser.add_argument("-f", "--fail", default=1.0, type=float,
                    help="probability of comparison success (default 1.0)")

def compare(i,j):
    if np.random.random() < param.fail:
        return i < j
    else:
        return j < i

def bubblesort(l):
    count = 0;
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            count += 1;
            if not compare(l[j],l[j+1]):
                l[j],l[j+1] = l[j+1],l[j]
    return count;


def partition(arr, low, high):
    i = low-1
    c = 0
    pivot = arr[high]

    for j in range(low , high):
        c += 1
        if compare(arr[j],pivot):
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1, c

def quicksort(arr,low,high):
    c = 0
    if low < high:
        pi, cp = partition(arr,low,high)
        c += cp
        c += quicksort(arr, low, pi-1)
        c += quicksort(arr, pi+1, high)
        return c
    return 0

def edit_distance(l):
    s1 = list(l)
    s2 = list(l)
    s2.sort()

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]


if __name__ == "__main__":
    param = parser.parse_args()

    data = np.random.random(param.n)

    start = time.time()
    if (param.algorithm == "bubble"):
        count = bubblesort(data)
    else:
        count = quicksort(data,0,len(data)-1)
    end = time.time()
    dist = edit_distance(data)

    output = [str(end - start), str(count), str(dist), param.algorithm]
    print(', '.join(output))
