def HammingDistance(p, q):
    hamming_distance = 0
    n = min(len(p),len(q))
    for i in range(n):
        if p[i] != q[i]:
            hamming_distance += 1
    return hamming_distance
