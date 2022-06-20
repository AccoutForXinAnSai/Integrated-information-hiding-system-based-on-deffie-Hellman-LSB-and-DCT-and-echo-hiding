import math
import random
from prime import eladuosai
from prime import primitive_root


# A，B得到各自的计算数
def get_calculation(p, a, X):
    Y = (a ** X) % p
    return Y


# A，B得到交换计算数后的密钥
def get_key(X, Y, p):
    key = (Y ** X) % p
    return key


def get_Diffie_Hellman_key():
    # 得到规定的素数
    lower = 10000
    upper = 100000
    li_prime = eladuosai(lower, upper)
    p = li_prime[random.randint(0, len(li_prime))]
    # 得到素数的原根列表
    list_primitive_root = primitive_root(p)
    # 得到A的私钥
    SK_A = random.randint(0, p - 1)
    # 得到B的私钥
    SK_B = random.randint(0, p - 1)
    # 得待A的计算数
    YA = get_calculation(p, int(list_primitive_root[-1]), SK_A)
    # 得到B的计算数
    YB = get_calculation(p, int(list_primitive_root[-1]), SK_B)
    # 交换后A的密钥
    key_A = get_key(SK_A, YB, p)
    # 交换后B的密钥
    key_B = get_key(SK_B, YA, p)
    assert key_A == key_B
    return key_A, SK_A, SK_B
