def GCD(a,b):
    # a>b
    while b:# b가 0이면 탈출
        a, b = b, a%b
    return a

ex_a = 6
ex_b = 9
print(GCD(ex_b,ex_a))