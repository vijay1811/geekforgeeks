
# 8 : max({1}{7},{2}{6},{3}{5},{4}{4},{5}{3},{6}{2},{7}{1},{8}{0}}

def max_profit(prices,n,memo):
    if n <=0 :
        return 0
    mp = 0
    if memo[n-1] == -100:
        for i in range(n):
            p = prices[i] + max_profit(prices,n-i-1)
            if mp < p:
                mp = p
        memo[n-1] = mp
    return memo[n-1]

def solution():
    n = int(input())
    prices = [int(x) for x in input().split()]
    memo = [-100]*n
    print(max_profit(prices,n,memo))
    return

def main():
    T = int(input())
    for i in range(T):
        solution()

if __name__ == "__main__":
    main()