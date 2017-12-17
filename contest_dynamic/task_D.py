def jump(N):
    A = [0] * N
    for i in range(N):
        A[i] = int(input())
    B = [0] * N
    if N > 1:
        B[1] =abs(A[0]-A[1])
        for i in range(2,N):
            B[i] = min(abs(A[i]-A[i-1]) + B[i-1],3 * abs(A[i]-A[i-2]) + B[i-2])
    print(B[N-1])

jump(int(input()))