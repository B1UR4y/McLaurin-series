from math import *


def f3(x, n):
    answer = 1
    for i in range(1, n+1):
        answer += ((-1)**i) * (x**(2 * i) / factorial(2 * i))
    return answer


def f9(x, m, n):
    answer = 1
    for i in range(1, n+1):
        m_prod = m
        for j in range(1, i):
            m_prod *= (m - j)
        answer += (m_prod * x**i) / factorial(i)
    return answer
