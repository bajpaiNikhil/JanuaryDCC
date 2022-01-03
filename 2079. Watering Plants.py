plants = [7,7,7,7,7,7,7]
capacity = 8
result = 0
can = capacity
for index, value in enumerate(plants):
    if can < value:
        result += 2 * index
        can = capacity
    result += 1
    can -= value
print(result)
