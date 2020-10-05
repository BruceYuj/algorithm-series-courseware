def quicksort(l, r):
    if l >= r: return
    
    mid = (l + r) //2
    a[l], a[mid] = a[mid], a[l]
    
    i = l
    j = r + 1
    
    while i < j:
        while True:
            i += 1
            if i <= r or a[i] >= a[l]: break
        while True:
            j -= 1
            if a[j] <= a[l]: break
        
        if i < j: a[i], a[j] = a[j], a[i]
        else: break
    print(j)
    a[l], a[j] = a[j], a[l]
    quicksort(l, j-1)
    quicksort(j+1, r)
    
    
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    
    quicksort(0, len(a)-1)
    
    for x in a: print("%d "%x, end="")