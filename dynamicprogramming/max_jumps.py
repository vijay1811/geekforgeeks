import sys

jumps = []

def min_jumps_iter(arr):
    if arr[0] == 0 :
        return -1
    jumps  = [-1]*len(arr)
    jumps[0] = 0
    for i in range(1,len(arr)):
        for j in range(i):
            if i <= j+ arr[j]:
                jumps[i] = 1+jumps[j]
                break
        if jumps[i] == -1:
            break
    return jumps[len(arr)-1]
 

def min_jumps(arr,N):
    if N >= len(arr):
        return 0
    if arr[N] + N >= len(arr)-1:
        jumps[N] = 1
    if arr[N] == 0 :
        jumps[N] = -1
    if jumps[N] == -2:
        min = 100000000
        for i in range(1,arr[N]+1):
          j =  min_jumps(arr,N+i)
          if min > j and j >= 0:
             min = j
        if  min == 100000000:
            jumps[N] = -1
        else:
            jumps[N] = 1 + min
    return jumps[N]

def solution():
    N = int(input())
    jumps.clear()
    x = [-2]*N
    jumps.extend(x)
    arr = [int(x) for x in input().split()]
    # print(min_jumps(arr,0))
    print(min_jumps_iter(arr))
    return

def main():
    sys.setrecursionlimit(100000)
    t = int(input())
    for i in range(t):
        solution()

if __name__ == "__main__":
    main()