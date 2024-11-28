def handshakes(N):
    if N == 0:
        return 1

    if N % 2 == 1:
        return 0

    comb = 0
    for i in range(0, N, 2):
        comb += handshakes(i) * handshakes(N-i-2)

    return comb


N = 10
print(handshakes(N))