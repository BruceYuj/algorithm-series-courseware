## 本节课主要内容

1. 整数二分
2. 浮点数二分
3. 二分法的 5 种经典应用


## 整数二分

**二分的本质**：
如果我们能够通过某种方式将一个区间划分成两个区间，左边区间满足某种特性；右边区间不满足某种特性。
那么我们就能够通过二分法来寻找左区间的右边端点或者右区间的左边端点

**有单调性一定可以二分，但是二分不一定要有单调性**

### 代码模板
```
binary_search(l , r): // 模板一：寻找右区间的左端点

    while l < r:
        mid = (l+r)//2

        if check(mid): r = mid
        else: l = mid+1
```

```
binary_search(l , r): // 模板二：寻找左区间的右端点

    while l < r:
        mid = (l+r+1)//2

        if check(mid): l = mid
        else: r = mid-1
```

**为什么是整数的时候会有很多边界问题呢？**
因为整数范围缩小到 2 时候，可能进入死循环。

### 基本整数二分法题目
1. [leetcode: 例题 1 - 34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
2. [leetcode: 例题 2 - 74. 搜索二维矩阵](https://leetcode-cn.com/problems/search-a-2d-matrix/)
3. [leetcode: 例题 3 - 153. 寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array)
4. [leetcode: 例题 4 - 81. 搜索旋转排序数组 II](https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/)
5. [leetcode: 例题 5 - 154. 寻找旋转排序数组中的最小值 II](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/)

**课后习题**
1. [leetcode: 162. 寻找峰值](https://leetcode-cn.com/problems/find-peak-element/)
2. [leetcode: 275. H 指数 II](https://leetcode-cn.com/problems/h-index-ii/)
3. [codeforces edu 4 道题目](https://codeforces.com/edu/course/2/lesson/6/1/practice)

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

### 浮点数二分例题
1. [acwing: 790. 数的三次方根](https://www.acwing.com/problem/content/792/)

**课后习题**
1. [acwing: 696. 哈默队长(Google Kickstart2013 Practice Round Problem B)](https://www.acwing.com/problem/content/description/698/)

## 二分法的经典应用
### 1. 对结果进行二分
1. [leetcode: 1011. 在 D 天内送达包裹的能力](https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days/)
2. [leetcode: 1482. 制作 m 束花所需的最少天数](https://leetcode-cn.com/problems/minimum-number-of-days-to-make-m-bouquets/)
3. [leetcode: 778. 水位上升的泳池中游泳](https://leetcode-cn.com/problems/swim-in-rising-water/)   


4. [leetcode: 1482. 制作 m 束花所需的最少天数](https://leetcode-cn.com/problems/minimum-number-of-days-to-make-m-bouquets/)
5. [leetcode: 1292. 元素和小于等于阈值的正方形的最大边长](https://leetcode-cn.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/)
6. [leetcode: 875. 爱吃香蕉的珂珂](https://leetcode-cn.com/problems/koko-eating-bananas/)
7. [leetcode: 287. 寻找重复数](https://leetcode-cn.com/problems/find-the-duplicate-number/)
8. [acwing(头条 2019 笔试):680. 剪绳子](https://www.acwing.com/problem/content/682/)
9.  [acwing(第八届蓝桥杯): 1227. 分巧克力](https://www.acwing.com/problem/content/description/1229/)
10. [acwing(头条 2019 笔试): 730. 机器人跳跃问题](https://www.acwing.com/problem/content/description/732/)
11. [acwing: 1028. 复制书稿](https://www.acwing.com/problem/content/description/1030/)
12. [codeforces edu 8 道题目](https://codeforces.com/edu/course/2/lesson/6/2/practice)   
13. [leetcode: 793. 阶乘函数后K个零](https://leetcode-cn.com/problems/preimage-size-of-factorial-zeroes-function/)
14. [leetcode: 719. 找出第 k 小的距离对](https://leetcode-cn.com/problems/find-k-th-smallest-pair-distance/)

### 2. min(max()) / max(min())
1. [leetcode: 410. 分割数组的最大值](https://leetcode-cn.com/problems/split-array-largest-sum/)
2. [acwing: 519. 跳石头](https://www.acwing.com/problem/content/521/)
3. [leetcode plus: 774. minimize-max-distance-to-gas-station](https://leetcode-cn.com/problems/minimize-max-distance-to-gas-station/)
4. [acwing: 2436. 串分割](https://www.acwing.com/problem/content/description/2438/)
5. [codeforces 4 道经典题目](https://codeforces.com/edu/course/2/lesson/6/3/practice)

### 3. 求最大平均值 / 最小平均值
1. [acwing: 02. 最佳牛围栏](https://www.acwing.com/problem/content/description/104/)
2. [luogu: 1404. 求平均值(poj2018)](https://www.luogu.com.cn/problem/P1404)

3. [acwing: 2430. 送礼物](https://www.acwing.com/problem/content/description/2432/)
4. [某公司笔试题](https://www.acwing.com/community/content/537/)
5. [acwing: 361. 观光奶牛(图+二分)](https://www.acwing.com/problem/content/description/363/)
6. [codeforces 3 道经典题目](https://codeforces.com/edu/course/2/lesson/6/4/practice)


### 4. 求某种特殊的第 k 大 / 小
1. [leetcode: 668. 乘法表中第k小的数](https://leetcode-cn.com/problems/kth-smallest-number-in-multiplication-table/)
2. [leetcode: 878. 第 N 个神奇数字](https://leetcode-cn.com/problems/nth-magical-number/)

3. [leetcode: 786. 第 K 个最小的素数分数](https://leetcode-cn.com/problems/k-th-smallest-prime-fraction/)
4. [acwing: 1236. 递增三元组](https://www.acwing.com/problem/content/description/1238/)
5. [codeforces 3 道经典题目](https://codeforces.com/edu/course/2/lesson/6/5/practice)

## 其他涉及题目
在算法题目中结合多种技巧解决一道题目是很常见的事，下面就给大家列举一些**二分法**结合其他算法的题目，这些题目就不讲解了，有问题可以在答疑群里面提出来。

**数学+二分**：
1. [leetcode: 483. 最小好进制](https://leetcode-cn.com/problems/smallest-good-base/) 
2. [628. 美丽的数（google kickstart 2016 round E problem B）](https://www.acwing.com/problem/content/description/630/)

**二分+dp：** [acwing: 472. 跳房子](https://www.acwing.com/problem/content/description/474/)

**二分+差分：**[acwing: 503. 借教室](https://www.acwing.com/problem/content/description/505/)

**贪心+二分：**  LIS 问题（动态规划专题讲解）