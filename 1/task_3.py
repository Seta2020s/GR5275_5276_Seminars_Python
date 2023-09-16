a, b, c = map(int, input("Введите a, b и c через пробел: ").split())
if c < a * b and ((c % a == 0) or (c % b == 0)):
    print('yes')
else:
    print('no')