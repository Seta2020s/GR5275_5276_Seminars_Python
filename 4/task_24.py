"""В фермерском хозяйстве в Карелии выращивают чернику.
Она растёт на круглой грядке, причём кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних. 
Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью,
поэтому ко времени сбора на них выросло различное число ягод — 
на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, 
которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки."""


def max_berry_harvest(N, bushes):
    bush_dict = {}
    
    for i in range(N):
        bush_dict[i] = bushes[i]
    
    valid_positions = set()
    
    for i in range(N):
        if i - 1 not in valid_positions and i not in valid_positions and i + 1 not in valid_positions:
            valid_positions.add(i)
    
    max_harvest = 0
    for position in valid_positions:
        harvest = bush_dict[position] + bush_dict.get(position - 1, 0) + bush_dict.get(position + 1, 0)
        max_harvest = max(max_harvest, harvest)
    
    return max_harvest

N = int(input("Введите количество кустов: "))
bushes = list(map(int, input("Введите урожайность на каждом кусте через пробел: ").split()))

result = max_berry_harvest(N, bushes)
print(result)