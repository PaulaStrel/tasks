def g_sorting(N):
    A=[0]*N
    for i in range(N):
        A[i]=int(input())
    base=A[int(input())]
    n=0
    for i in range(N):
        if A[i]>base:
            n+=1
    print(n)
g_sorting(int(input()))