def n_primos(int):
    primo = 0
    for i in range(2, int+1):
        n = 0
        p = 0
        div = 0
        while p <= int:
            p += 1
            n += 1
            if (i % n == 0):
                div += 1
                continue
        if (div == 2):
            primo += 1
    return(primo)

n_primos(101)