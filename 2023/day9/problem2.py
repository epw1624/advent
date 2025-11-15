def all_zeros(layer):
    for num in layer:
        if num != 0:
            return False
    return True

def extrapolate(nums):
    cur_layer = nums
    layers = [cur_layer]

    while not all_zeros(cur_layer):
        next_layer = []
        for i in range(1, len(cur_layer)):
            next_layer.append(cur_layer[i] - cur_layer[i - 1])
        layers.append(next_layer)
        cur_layer = next_layer


    cur_val = 0
    for i in range(1, len(layers)+1):
        cur_val = layers[len(layers) - i][0] - cur_val
    
    return cur_val



with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

    sum = 0

    for line in lines:
        nums = list(map(int, line.split(' ')))
        sum += extrapolate(nums)

    print(sum)