def bomb(N):
    A = [[0] * N for i in range(4)]
    A[0][0] = 1
    A[1][0] = 1
    A[2][0] = 0
    A[3][0] = 0
    for i in range(1,N):
        A[0][i]=A[0][i-1]+A[2][i-1]
        A[1][i]=A[0][i-1]+A[2][i-1]
        A[2][i]=A[1][i-1]+A[3][i-1]
        A[3][i]=A[1][i-1]
    summ = 0
    for i in range(4):
        summ += A[i][N-1]
    print(summ)
bomb(int(input()))