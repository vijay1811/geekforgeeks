
import sys

def coin_change(N,coins,n,cuts):
    idx = len(coins) - n
    if N < 0:
        return 0
    if N==0:
        return 1
    if n == 1:
        if N%coins[idx] == 0:
           cuts[n-1][N-1] = 1 
        else:
           cuts[n-1][N-1] = 0
    if cuts[n-1][N-1] == -100:
        cuts[n-1][N-1] = coin_change(N-coins[idx],coins,n,cuts) + coin_change(N,coins,n-1,cuts)
    return cuts[n-1][N-1]

def solution():
    N = int(input())
    coins = [int(x) for x in input().split()]
    note = int(input())
    cuts = [[-100 for i in range(note)] for j in range(N)] 
    print(coin_change(note,coins,N,cuts))
    return

def main():
    sys.setrecursionlimit(10000000)
    t = int(input())
    for i in range(t):
        solution()

if __name__ == "__main__":
    main()