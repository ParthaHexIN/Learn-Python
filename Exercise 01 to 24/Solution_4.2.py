def sum_of_digitS(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digitS(n // 10)
print(sum_of_digitS(1234))