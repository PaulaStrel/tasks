def horse(x,y):
    A=[[x+2,y+1],[x+2,y-1],[x+1,y+2],[x+1,y-2],[x-2,y+1],[x-2,y-1],[x-1,y+2],[x-1,y-2]]
    return A

x=int(input())
y=int(input())
x1=int(input())
y1=int(input())

A=horse(x,y)

steps=-1
if x==x1 and y==y1:
    steps=0
else:
    for i in range(8):
        if [x1,y1] == A[i]:
            steps=1
        elif A[i][0]>0 and A[i][1]>0:
            A=horse(A[i][0],A[i][1])
            for i in range(8):
                if [x1, y1] == A[i] and A[i][0]>=0 and A[i][1]>=0:
                    steps= 2
        A=horse(x,y)

print(steps)
