

def decode_rec(inp,n):
    input = str(inp) 
    if n == len(input):
        return 1
    if input[n] == "0":
        return 0
    result = decode_rec(inp,n+1)
    if len(input)-n >= 2 and 10 <= int(input[n:n+2]) <=26:
        result += decode_rec(inp,n+2)
    return result

def solution():
    N = int(input())
    inp= input()
    # inp.strip('0')
    print(decode_rec(inp,0))
    return

def main():
    # sys.setrecursionlimit(100000)
    t = int(input())
    for i in range(t):
        solution()

if __name__ == "__main__":
    main()



# def decode(input):
#     s =  str(input)
#     if len(s) == 1:
#         return 1
#     count = 1
#     countLocal = 1

#     for i in range(1,len(s)):
#         c = int(s[i])
#         if s[i-1] == "0" or s[i] == "0":
#             return 0
#         if s[i-1] == "1":
#            countLocal += 1
#         elif s[i-1] == "2" and c <= 6:
#             countLocal += 1
#         else:
#             count *= countLocal
#             countLocal = 1    
#     return count*countLocal
