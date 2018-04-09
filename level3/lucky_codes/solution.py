def answer(l):
    divides = [[] for _ in l]
    for idx, num in enumerate(l):
        if num != 0:
            divides[idx] = [i for i in range(idx+1, len(l)) if l[i] % num == 0]
    count = 0
    for i in divides:
        for j in i:
            count += len(divides[j])
    return count