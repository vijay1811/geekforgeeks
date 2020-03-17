
def max_tip(n,x,y,a,b,memo):
    if n==0:
        return 0
    key = "{},{},{}".format(n,x,y)
    if memo.get(key) == None:
        if x == 0:
            memo[key] = b[n-1] + max_tip(n-1,x,y-1,a,b,memo)
        elif y == 0:
            memo[key] = a[n-1] + max_tip(n-1,x-1,y,a,b,memo)
        else:
            memo[key] =  max(b[n-1] + max_tip(n-1,x,y-1,a,b,memo),a[n-1] + max_tip(n-1,x-1,y,a,b,memo))
    return memo.get(key)

def solution():
    memo = {}
    n,x,y = [int(x) for x in input().split() ]
    a = [ int(x) for x in input().split() ]
    b = [ int(x) for x in input().split()]
    print(max_tip(n,x,y,a,b,memo))

def main():
    t = int(input())
    for i in range(t):
        solution()

if __name__ == "__main__":
    main()