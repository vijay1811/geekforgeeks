# y = [int(x) for x in input().split()] 
# print(y)
import sys

fibs = []

def fib(n):
    for i in range(n):
        
    if fibs[n] != 0:
        return fibs[n]
    if n == 0:
        fibs[n] = 1
        return fibs[n]
    if n ==1 :
        fibs[n] = fib(n-1)
        return fibs[n]
    fibs[n] = fib(n-1)+fib(n-2)
    return fibs[n]

def solution():
    n = int(input())
    fibs.clear()
    for i in range(n):
        fibs.append(0)
    fib(n-1)
    print(*fibs ," ")
    return

def main():
    sys.setrecursionlimit(100000)
    t = int(input())
    for i in range(t):
        solution()

if __name__ == "__main__":
    main()