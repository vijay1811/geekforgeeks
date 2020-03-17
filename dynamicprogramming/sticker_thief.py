import sys

loot = []

def max_loot(arr,N):
    if N >= len(arr):
        return 0
    if loot[N] == 0:
        loot[N] = max(max_loot(arr,N+2)+arr[N],max_loot(arr,N+1))
    return loot[N]

def solution():
    N = int(input())
    loot.clear()
    for i in range(N):
        loot.append(0)
    arr = [int(x) for x in input().split()]
    print(max_loot(arr,0))
    return

def main():
    sys.setrecursionlimit(100000)
    t = int(input())
    for i in range(t):
        solution()

if __name__ == "__main__":
    main()