def function():
    l=list(map(int,input().split()))
    l=sorted(l)
    A=[0]*(len(l))
    A[0]=l[1]-l[0]
    A[1]=l[1]-l[0]
    for i in range(2,len(l)):
        A[i] = min(A[i-1],A[i-2])-l[i-1]+l[i]
    print(A[len(l)-1])

function()