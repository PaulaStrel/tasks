def fac(n, times = 0):
    if n == 0:
        print(times)
        return 1
    else:
        return n * fac(n - 1, times + 1)
print(fac(5))
