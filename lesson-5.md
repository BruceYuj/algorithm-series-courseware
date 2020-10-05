## 本节课主要内容

1. 整数二分
2. 浮点数二分
3. 二分法的 5 种经典应用



## 整数二分

**二分的本质**：
如果我们能够通过某种方式将一个区间划分成两个区间，左边区间满足某种特性；右边区间不满足某种特性。
那么我们就能够通过二分法来寻找左区间的右边端点或者右区间的左边端点

=》有单调性一定可以二分，但是二分不一定要有单调性

```

binary_search(l , r): // 寻找右区间的左端点

    while l < r:
        mid = (l+r)//2

        if check(mid): r = mid
        else: l = mid+1

```

```
binary_search(l , r): // 寻找左区间的右端点

    while l < r:
        mid = (l+r+1)//2

        if check(mid): l = mid
        else: r = mid-1
```

**为什么是整数的时候会有很多边界问题呢？**
因为整数范围缩小到 2 时候，可能进入死循环。

- [例题 1](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
- [例题 2](https://leetcode-cn.com/problems/search-a-2d-matrix/)
- [例题 3](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array)
- [例题 4](https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/)
- [例题 5](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/)


## 浮点数二分

```
binary_search(l , r): // 寻找结果

    eps = 1e-6
    while r - l >= eps:
        mid = (l+r) / 2

        if check(mid): r = mid
        else: l = mid
```

常见的例子： 二分法求 sqrt(x)

## 二分法的经典应用
1. 对结果进行二分

2. min(max()) / max(min())

3. 求最大平均值 / 最小平均值

4. 求某种特殊的第 k 大
