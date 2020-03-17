

def lis1(arr,n,i,memo):
    if n== 0:
        return 0
    idx = len(arr)-n
    if memo[i+1][n-1] == -100:
        if i == -1 or arr[idx]>arr[i] :
            memo[i+1][n-1] = max(1+lis1(arr,n-1,idx,memo),lis1(arr,n-1,i,memo))
        else:
            memo[i+1][n-1] = lis1(arr,n-1,i,memo)
    return memo[i+1][n-1]


def lis(arr,n,e):
    if n==0:
        return 0
    idx = len(arr)-n
    if arr[idx] > e:
        return max(1 + lis(arr,n-1,arr[idx]),lis(arr,n-1,e))
    else:
        return lis1(arr,n-1,e)

def solution():
    n = int(input())
    arr = [int(x) for x in input().split()]
    memo = [[-100 for i in range(n)] for j in range(n+1)]
    print(lis1(arr,n,-1,memo))

def main():
    t = int( input())
    for i in range(t):
        solution()

if __name__ == "__main__":
    main()