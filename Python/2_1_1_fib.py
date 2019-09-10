# n根棍子，棍子i的长度是a_i，现在挑选出3个棍子组成最长的周长的三角形
# 若不能组成三角形，输出0
# 限制条件：
# 0 <= n <= 100
# 1 <= a_i <= 1000

# 考虑到限制条件，O(n^3)算法大概需要10^6，计算出来是没有问题的

def fib_recur(n):
    if n <= 1:
        return n 
    return fib_recur(n - 1) + fib_recur(n - 2)
        
memo = [0] * (10 ** 5 + 1)

def fib_memo(n):
    if n <= 1:
        return n 
    if memo[n] != 0:
        return memo[n]
    else:
        memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
        return memo[n]
def main():
    n = 45
    print(fib_memo(n))

if __name__ == '__main__':
    main()
