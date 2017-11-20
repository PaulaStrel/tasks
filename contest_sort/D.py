N = int(input())
A = [0] * N

for i in range(N):
    A[i]=int(input())

def sort_even(A):
    for num in range(0,N-1):
        for j in range(num+1,N):
            if (A[j] % 2 == 0) and (A[num] % 2 == 0):
                if A[num] > A[j]:
                    A [j] , A[num] = A[num] , A[j]

sort_even(A)

for i in range(N):
    print(A[i], end=' ')