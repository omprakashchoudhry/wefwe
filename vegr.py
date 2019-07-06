n=int(input())
for i in range(n):
    N=list(map(int,input().split()))
    N.sort()
    print(N[0])
