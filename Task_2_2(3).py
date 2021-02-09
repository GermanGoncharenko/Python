box = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
box1 = []
for idx in box:
    if idx.replace("+", "").replace("-", "").isdigit():
        if idx[0] == "+" or idx[0] == "-":
            box1.append(f'"{idx[0] + idx[1:]}"')
        else:
            box1.append(f'"0{idx}"')
    else:
        box1.append(idx)
print(box1)
print(" ".join(box1))
