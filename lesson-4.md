## 本节课主要内容

1. 快速排序算法以及模板
2. 快速选择算法以及模板
3. 两个算法的典型题目应用

## 算法模板
```python
# 快排模板 1
def quick_sort(l , r):
    if l >= r: return 

    mid = (l+r)//2
    a[l], a[mid] = a[mid], a[l] # 将选取的划分元素和 l 进行交换
    
    i = l
    j = r+1
    while i < j: # 根据划分元素将 [l, r] 划分成两个区间，左区间都 <= 划分元素； 右区间都 >= 划分元素
        while True:
            i += 1
            if i > r or a[i] >= a[l]: break
        
        while True:
            j -= 1
            if j < l or a[j] <= a[l]: break
        
        if i < j: a[i], a[j] = a[j], a[i]
        
    
    a[l], a[j] = a[j], a[l] # 将划分元素交换到其最终有序的位置上
    
    quick_sort(l, j-1) # 递归处理左区间
    quick_sort(j+1, r) # 递归处理右区间
```

```python
# 快排模板 2
def quick_sort(l , r):
    if l >= r: return

    mid = (l+r)//2

    i = l-1
    j = r+1
    x = a[mid]
    while i < j: # 根据划分元素将 [l, r] 划分成两个区间，左区间都 <= 划分元素； 右区间都 >= 划分元素
        while True:
            i += 1
            if i > r or a[i] >= x: break
        
        while True:
            j -= 1
            if j < l or a[j] <= x: break
        
        if i < j: a[i], a[j] = a[j], a[i]
        
    
    
    quick_sort(l, j) # 递归处理左区间
    quick_sort(j+1, r) # 递归处理右区间
```

## 本节课例题
1. [acwing: 785. 快速排序](https://www.acwing.com/problem/content/description/787/)
2. [acwing: 786. 第k个数](https://www.acwing.com/problem/content/788/)