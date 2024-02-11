a=input()
b=input()
c=input()
result = int(a) * int(b) * int(c)
for i in range(10):
    print(str(result).count(str(i)))