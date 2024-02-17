n = int(input())
result =[]
for i in range(1,n,1):
    x = list(map(int, str(i)))
    sum=0
    for k in range(x.__len__()):
        sum+=x[k]
    if(i+sum == n):
        result.append(int(i))
if(result.__len__() == 0):
    print(0)
else:
    print(min(result))