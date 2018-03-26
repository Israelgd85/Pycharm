
def maximo (*n):
        b = 0
        a = 0
        i = 0
        maior = 0
        while i < len(n):
            ant = n[b]
            prox = n[a]
            if ant > prox:
                maior = ant
                a += 1
            else:
                maior = prox
                b += 1
                i += 1
        return(maior)
maximo(0,2,4)

