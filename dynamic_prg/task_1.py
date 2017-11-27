N = int(input())

def insect(N):
    A= [0] * N
    A[0] = 1
    A[1] = 1
    A[2] = 2

    for i in range(3,N):
        A[i] = A[i-3] + A[i-2] + A[i-1]
    print(A[N-1])

insect(N) 