import sys

def mss(arr,n,i,memo):
    if n== 0:
        return 0
    idx = len(arr)-n
    if memo[i+1][n-1] == -100:
        if i == -1 or arr[idx]>arr[i] :
            memo[i+1][n-1] = max(arr[idx]+mss(arr,n-1,idx,memo),mss(arr,n-1,i,memo))
        else:
            memo[i+1][n-1] = mss(arr,n-1,i,memo)
    return memo[i+1][n-1]

def solution():
    n = int(input())
    arr = [int(x) for x in input().split()]
    memo = [[-100 for i in range(n)] for j in range(n+1)]
    print(mss(arr,n,-1,memo))

def main():
    sys.setrecursionlimit(100000000)
    t = int( input())
    for i in range(t):
        solution()

if __name__ == "__main__":
    main()