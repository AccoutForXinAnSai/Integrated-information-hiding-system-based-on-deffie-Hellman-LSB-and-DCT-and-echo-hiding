def multimod(a, k, n):  # 快速幂取模
    ans = 1
    while (k != 0):
        if k % 2:  # 奇数
            ans = (ans % n) * (a % n) % n
        a = (a % n) * (a % n) % n
        k = k // 2  # 整除2
    return ans


def primitive_root(n):
    k = (n - 1) // 2
    li = []
    for i in range(2, n - 1):
        if multimod(i, k, n) != 1:
            li.append(i)
    return li


def eladuosai(lower, upper):
    l = list(range(1, upper + 1))
    l[0] = 0
    for i in range(2, upper + 1):
        if l[i - 1] != 0:
            for j in range(i * 2, upper + 1, i):
                l[j - 1] = 0
    result = [x for x in l if x != 0 and x > lower]
    return result
