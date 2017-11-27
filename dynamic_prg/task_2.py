N = int(input())

def insect(N):
	A = [-1] * (N+1)
	A[0] = 0
	A[1] = 1
	A[2] = 1

	for i in range(4,N+1):
		A[i] = A[i - 1] + A[i - 2]
		if i % 3 == 0:
			A[i] += A[int(i / 3)]
	return A[N]

print(insect(N))