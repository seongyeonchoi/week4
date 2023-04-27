n, x=map(int, input(). split())
num=list(map(int, input(). split()))
for i in range (0,n):
    num.append(random.randint(0,1000))
    if num[i]<x:
        print(num[i], end='')
    