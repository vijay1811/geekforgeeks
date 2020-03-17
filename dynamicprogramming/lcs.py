import sys

def lcsNew(str1,str2,m,n,memo):
    if m <= 0 or n <= 0 :
        return 0
    if memo[n-1][m-1] == -100:
        if str1[m-1] == str2[n-1]:
            memo[n-1][m-1] =  1 + lcsNew(str1,str2,m-1,n-1,memo)
        else:
            memo[n-1][m-1] = max(lcsNew(str1,str2,m-1,n,memo),lcsNew(str1,str2,m,n-1,memo))
    return memo[n-1][m-1]

def lcs(str1,str2,m,n,memo):
    if m <= 0 or n <= 0 :
        return 0
    i,j = len(str1) - m,len(str2)-n
    if memo[n-1][m-1] == -100:
        n1,mx = n,0
        for j1 in range(j,len(str2)):
            n1 -= 1
            length = 0
            m1 = m
            for k in range(i,len(str1)):
                m1 -= 1 
                if str1[k] == str2[j1]:
                    l = 1+ lcs(str1,str2,m1,n1,memo)
                    if l > length:
                        length = l
                    break
                else:
                   memo[n1-1][m1-1] 
            if mx < length :
                mx = length
        memo[n-1][m-1] = mx
    return memo[n-1][m-1]
    
def solution():
    M,N = [int(x) for x in input().split()]
    str1,str2 = input(),input()
    memo = [[-100 for i in range(M)] for j in range(N)] 
    print(lcsNew(str1,str2,M,N,memo))
    for m in memo:
        print(m)
    return

def main():
    sys.setrecursionlimit(10000000)
    t = int(input())
    for i in range(t):
        solution()

if __name__ == "__main__":
    main()