def sort(A):
    for j in range (1, N*M):
        for k in range(0, N*M-j):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]


N = int(input())
M = int(input())

A= [0] * (N*M)

for i in range(N*M):
    A[i] = int(input())

sort(A)

c = 0
for i in range(M*N):
    print(A[i],end=' ')
    c += 1
    if c == M:
        print()
        c = 0