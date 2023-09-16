n = int(input("Введите трехзначное число: "))
res = 0
while n > 0:
    res += n % 10
    n //= 10

print(res)