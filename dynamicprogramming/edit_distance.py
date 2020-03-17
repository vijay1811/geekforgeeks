import sys

def mini_dist(str1,str2,m,n,memo):
    # print(str1,str2)
    if m == 0 :
        return n
    if n == 0 :
        return m
    if memo[n-1][m-1] == -100 :
        if str1[m-1] == str2[n-1]:
            memo[n-1][m-1] = mini_dist(str1,str2,m-1,n-1,memo)
        else:
            memo[n-1][m-1] = 1 + min(mini_dist(str1,str2,m,n-1,memo),mini_dist(str1,str2,m-1,n,memo),mini_dist(str1,str2,m-1,n-1,memo))
        
    return memo[n-1][m-1]

def solution():
    M,N = [int(x) for x in input().split()]
    str1,str2 = input().split()
    memo = [[-100 for i in range(M)] for j in range(N)] 
    print(mini_dist(str1,str2,M,N,memo))
    # print(lcs(str1,str2,M,N,memo))
    # for m in memo:
    #     print(m)
    return

def main():
    sys.setrecursionlimit(10000000)
    t = int(input())
    for i in range(t):
        solution()

if __name__ == "__main__":
    main()