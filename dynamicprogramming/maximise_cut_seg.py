
cuts = []

def maximize_cuts(N,x,y,z):
    # print(N)
    if N < 0 :
        return -1000000
    if N == 0 :
        return 0
    if cuts[N] == -100:
        cuts[N] = 1 + max(maximize_cuts(N-x,x,y,z),maximize_cuts(N-y,x,y,z),maximize_cuts(N-z,x,y,z))
    return cuts[N]

def solution():
    N = int(input())
    cuts.clear()
    for i in range(N+1):
        cuts.append(-100)
    x,y,z = [int(x) for x in input().split()]
    print(maximize_cuts(N,x,y,z))
    # print(*fibs ," ")
    return

def main():
    t = int(input())
    for i in range(t):
        solution()

if __name__ == "__main__":
    main()