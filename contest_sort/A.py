N = int(input())
A = [0] * N

for i in range(N):
    A[i]=int(input())

def bubble_sort(A):

    for i in range(1, N):
        for k in range(N - i):
             if A[k] > A[k + 1]:
                 A[k],A[k+1] = A[k+1],A[k]

    return A

print(bubble_sort(A))