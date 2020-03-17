

def find_water(k,i,j):
    # print(k,i,j)
    if i == 1:
        if k < 1:
            return k
        else:
            return 1
    memos = [[]]*i
    for i1 in range(i):
        memos[i1] = [0]*(i1+1)
    if k > 1:
        memos[0][0] = k
        k -= 1
    else:
        return memo[i-1][j-1]

    for i1 in range(1,i):
        # print(i1,i)
        for j1 in range(i1+1):
            # print(i1,j1)
            val = 0
            if j1 == 0:
                k -= 1/2
                memos[i1][j1] = (memos[i1-1][0]-1)/2
            elif i1 == j1:
                k -= 1/2
                memos[i1][j1] = (memos[i1-1][j1-1]-1)/2
            else:
                k -= 1
                if memos[i1-1][j1]-1 >0:
                    memos[i1][j1] += (memos[i1-1][j1]-1)/2
                if memos[i1-1][j1-1]-1 > 0:
                    memos[i1][j1] += (memos[i1-1][j1-1]-1)/2
            if memos[i1][j1] < 0:
                memos[i1][j1] = 0
            # if k < 0:
            #     break
    # print(memos)
    if memos[i-1][j-1]>=1:
        return 1
    else:
        return memos[i-1][j-1]

def solution():
    k ,i,j = int(input()),int(input()),int(input())
    print(find_water(k,i,j))

def main():
    t =int(input())
    for i in range(t):
        solution()

if __name__ == "__main__":
    main()