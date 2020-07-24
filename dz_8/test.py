import random


def st_ring(temp):
    nums = []
    while len(nums) < 5:
        elem = str(random.randint(1, 90))
        if elem not in temp:
            nums.append(elem)
            temp.append(elem)
    nums = list(nums) + list(' ' * 7)
    random.shuffle(nums)
    return ' '.join(nums)


temp = []
for _ in range(3):
    print(st_ring(temp))