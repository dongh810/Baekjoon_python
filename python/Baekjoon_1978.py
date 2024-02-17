x = int(input())
nums = map(int,input().split())
result = 0
for num in nums:
    a = 0
    if num >1:
        for i in range(2,num):
            if num % i ==0:
                a += 1
        if a == 0:
            result +=1
print(result)