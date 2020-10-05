## 本节课主要内容

1. 快速排序算法以及模板
2. 快速选择算法以及模板
3. 两个算法的典型题目应用

```python
# 快排模板 1
def quick_sort(l , r):
    if l >= r: return

    mid = (l+r)//2
    a[l], a[mid] = a[mid], a[l]
    
    i = l
    j = r+1
    while i < j:
        while True:
            i += 1
            if i > r or a[i] >= a[l]: break
        
        while True:
            j -= 1
            if j < l or a[j] <= a[l]: break
        
        if i < j: a[i], a[j] = a[j], a[i]
        
    
    a[l], a[j] = a[j], a[l]
    
    quick_sort(l, j-1)
    quick_sort(j+1, r)
```

```python
# 快排模板 2
def quick_sort(l , r):
    if l >= r: return

    mid = (l+r)//2

    i = l-1
    j = r+1
    x = a[mid]
    while i < j:
        while True:
            i += 1
            if i > r or a[i] >= x: break
        
        while True:
            j -= 1
            if j < l or a[j] <= x: break
        
        if i < j: a[i], a[j] = a[j], a[i]
        
    
    
    quick_sort(l, j)
    quick_sort(j+1, r)
```