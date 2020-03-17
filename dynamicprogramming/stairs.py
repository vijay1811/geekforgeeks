fibs = []


def stairs(n):
    for i in range(n+1):
        if i == 0 or i == 1:
            fibs[i] = 1
            continue
        fibs[i] = (fibs[i-1]+fibs[i-2])%int(10**9+7)
    return fibs[n]

def solution():
    n = int(input())
    fibs.clear()
    for i in range(n+1):
        fibs.append(0)
    print(stairs(n))
    # print(*fibs ," ")
    return

def main():
    t = int(input())
    for i in range(t):
        solution()

if __name__ == "__main__":
    main()