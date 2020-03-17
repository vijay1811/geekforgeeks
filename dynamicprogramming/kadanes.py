
cuts = []

def maximum_subarr(arr,N):
    g_si ,g_li ,l_si ,l_li ,maxSum ,localSum = 0,0,0,0,arr[0],arr[0]
    for i in range(1,N):
        sum = localSum + arr[i]
        if sum < arr[i]:
            localSum, l_si,l_li= arr[i],i,i
        else:
            localSum = sum
            l_li += 1
        if localSum > maxSum:
           maxSum, g_si,g_li = localSum,l_si,l_li
    return maxSum

def solution():
    N = int(input())
    arr = [int(x) for x in input().split()]
    print(maximum_subarr(arr,N))
    return

def main():
    t = int(input())
    for i in range(t):
        solution()

if __name__ == "__main__":
    main()