import sys


def counts(n,memo):
    if n <=0 :
        return 0
    if memo[n-1] == -1:
        if n ==1:
            return 2
        if n == 2:
            return 3
        memo[n-1] = (counts(n-1,memo) + counts(n-2,memo))%(10**9 + 7)
    return memo[n-1]

def solution():
    N = int(input())
    print(counts(N,[-1]*100))
    return

def main():
    sys.setrecursionlimit(10000000)
    t = int(input())
    for i in range(t):
        solution()

if __name__ == "__main__":
    main()