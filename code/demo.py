import math
import sys
input = sys.stdin.readline

def check(x):
    s = [0] * (n+1)
    minV = [0] * (n+1)
    for i in range(1, n+1):
        s[i] = s[i-1] + a[i] - x
        minV[i] = min(minV[i-1], s[i])
    
    for i in range(m, n+1):
        if s[i] - minV[i-m] >= -1e-8:
            return True
    
    return False


if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [0] * (n+1)

    l = 0
    r = 0
    for i in range(1, n+1):
        a[i] = int(input())
        r = max(r, a[i])

    while r - l >= 1e-8:
        mid = (r+l) / 2

        if check(mid): l = mid
        else: r = mid
    
    print(math.floor(r*1000))