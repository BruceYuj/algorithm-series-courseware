# 本节课主要内容
1. 归并排序
   - 递归方式
   - 迭代方式
2. 归并排序的应用

## 算法模板
```python
# 递归模板
def merge_sort(l, r): # 将 a[l,r] 归并排序
    if l >= r: return
    mid = (l+r)//2
    merge_sort(l, mid) # 递归排序左区间
    merge_sort(mid+1, r) # 递归排序右区间
    
    i = l 
    j = mid + 1
    k = l
    
    while i <= mid and j <= r: # 合并操作：处理两个区间都有值时
        if a[i] < a[j]:
            h[k] = a[i]
            k += 1
            i += 1
        else:
            h[k] = a[j]
            k += 1
            j += 1
    
    while i <= mid: # 合并操作：处理最后只有左区间有值时
        h[k] = a[i]
        i += 1
        k += 1
    
    while j <= r: # 合并操作：处理最后只有右区间有值时
        h[k] = a[j]
        j += 1
        k += 1
    
    for i in range(l, r+1): # 将有序的 h[l, r] 重新赋值给 a[l,r]
        a[i] = h[i]
```

```python
# 迭代模板
def merge_sort():
    le = 1
    
    while le < n:
        i = 0
        while i+le < n:
            j = min(i+2*le-1, n-1)
            merge(i, le, j)
            i = j+1
        le += le

 # 每次迭代的 merge 方法       
def merge(i, le, j):
    lo = i
    mid = lo + le  - 1
    hi = i + le
    k = i
    
    while lo <= mid and hi <= j:
        if a[lo] < a[hi]:
            h[k] = a[lo]
            k += 1
            lo += 1
        else:
            h[k] = a[hi]
            k += 1
            hi += 1
    
    while lo <= mid:
        h[k] = a[lo]
        k += 1
        lo += 1
    
    while hi <= j:
        h[k] = a[hi]
        k += 1
        hi += 1
    
    for i in range(i, j+1):
        a[i] = h[i]
```


## 归并排序的应用：求逆序对


## 本节课例题
1. [acwing: 787. 归并排序](https://www.acwing.com/problem/content/789/)
2. [acwing: 788. 逆序对的数量](https://www.acwing.com/problem/content/description/790/)
3. [leetcode: 21. 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)
4. [leetcode: 23. 合并K个升序链表](https://leetcode-cn.com/problems/merge-k-sorted-lists/)


