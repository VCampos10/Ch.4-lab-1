
N = int(input())
result = [0] * (N+1)
pow = 1
for i in range(N+1):
    result[i] = pow
    pow *= 2
print (result) 