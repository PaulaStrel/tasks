def bubble_sort_number(A,N):
    B=N*[0]
    for i in range(N):
        B[i]=i
    for i in range(1, N):
        for k in range(N - i):
             if A[k] > A[k + 1]:
                 A[k],A[k+1],B[k],B[k+1] = A[k+1], A[k],B[k+1], B[k]

    return B

print(bubble_sort_number([4,8,6,7,3],5))