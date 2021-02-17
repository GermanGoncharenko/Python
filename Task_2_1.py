box = [15 * 3, 15 / 3, 15 // 3, 15 ** 3]
for idx in range(len(box)):
    if isinstance(box[idx], int):
        print(isinstance(box[idx], int))
    elif isinstance(box[idx], float):
        print(isinstance(box[idx], float))
