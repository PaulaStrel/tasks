def sort(A):
    for j in range (N-1):
        for k in range(N-j-1):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]
                B[k], B[k+1] = B[k+1] , B[k]


N = int(input())
A = [0] * N
B = [0] * N
C = [0] * N

l = 0
for i in range(N):
    B[i] = int(input())
for i in range(N):
    C[i] = B[i]
for i in range(N):
    while C[i] > 0:
        num = C[i] % 10
        l += num
        C[i] //= 10
    A[i] = l
    l = 0

sort(A)

for i in range(N):
    print(B[i], end=" ")
