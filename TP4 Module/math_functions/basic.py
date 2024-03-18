def factorielle(n):
    if n == 0:
        return 1
    elif n < 0:
        print("Impossible")
    else:
        fact = 1
        for i in range(2, n + 1):
            fact = fact * i
        return fact