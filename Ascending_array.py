n = int(input())
arr = list(map(int,input().split()))
c = 0
for i in range(0,n):
    if i==n-1:
        break
    if arr[i]<arr[i+1]:
        c+=1
if c==n-1:
    print("yes")
else:
    print("no")