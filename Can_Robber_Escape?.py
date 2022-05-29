n=int(input())
arr=list(map(int,input().split()))
Odd=0
for i in range(0,n):
    if arr[i]%2:
        Odd+=1
if Odd>2:
    print("NO")
else:
    print("YES")