# n根棍子，棍子i的长度是a_i，现在挑选出3个棍子组成最长的周长的三角形
# 若不能组成三角形，输出0
# 限制条件：
# 0 <= n <= 100
# 1 <= a_i <= 1000

# 考虑到限制条件，O(n^3)算法大概需要10^6，计算出来是没有问题的

def solve(a):
    # 三重循环计算出最长周长
    max_len = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            for k in range(j + 1, len(a)):
                length = a[i] + a[j] + a[k]
                ma = max(a[i], a[j], a[k])
                rest = length - ma 
                # 三个数字中最大的值小于剩下的两个值之和即可
                if rest > ma:
                    max_len = max(length, max_len)
    return max_len

def solve_ver_2(a):
    # 先对a排序，然后结合双指针法判定
    a.sort(reverse=True)
    # 外层主循环，是遍历三角形的第一个最大的数
    for i in range(len(a) - 2):
        left, right = i + 1, i + 2
        # 只可能是后面紧跟着的两个，如果紧跟着的两个的和都不大于最长边，那么就不可能产生符合要求的了
        if a[i] < a[left] + a[right]:
            return a[i] + a[left] + a[right]
    return 0

def main():
    a1 = [2, 3, 4, 5, 10]
    a2 = [4, 5, 10, 20]

    res = solve_ver_2(a1)
    print("max length: ", res)

    res = solve_ver_2(a2)
    print("max length: ", res)

if __name__ == '__main__':
    main()
