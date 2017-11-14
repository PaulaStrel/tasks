def bubble_sort(N):
    A=N*[0]
    B=N*[0]
    for i in range(N):
        A[i]=int(input())
    for i in range(N):
        B[i]=int(input())
    for i in range(1, N):
        for k in range(N - i):
             if A[k] > A[k + 1]:
                 A[k],A[k+1],B[k],B[k+1] = A[k+1], A[k],B[k+1], B[k]
             if A[k] == A[k+1]:
                 if B[k]>B[k+1]:
                    B[k], B[k + 1] = B[k + 1], B[k]


    print(A)
    print(B)

bubble_sort(int(input()))