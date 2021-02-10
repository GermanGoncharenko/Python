box = []
idx = 0
amount = 0
total = 0
for a in range(1, 1000, 2):
    box.append(a)
for idx in range(len(box)):
    box[idx] **= 3
    idx += 1
print(box)
idx = 0
while idx < len(box):
    q = box[idx] % 10
    w = box[idx] % 100
    e = w // 10
    r = box[idx] % 1000
    t = r // 100
    y = box[idx] % 10000
    u = y // 1000
    i = box[idx] % 100000
    o = i // 10000
    p = box[idx] % 1000000
    s = p // 100000
    d = box[idx] % 10000000
    f = d // 1000000
    g = box[idx] % 100000000
    h = g // 10000000
    j = box[idx] % 1000000000
    k = j // 100000000
    total = q + e + t + u + o + s + f + h + k
    if total % 7 == 0:
        amount += box[idx]
    idx += 1
print(amount)
amount = 0
idx = 0
for idx in range(len(box)):
    box[idx] += 17
    idx += 1
print(box)
idx = 0
while idx < len(box):
    q = box[idx] % 10
    w = box[idx] % 100
    e = w // 10
    r = box[idx] % 1000
    t = r // 100
    y = box[idx] % 10000
    u = y // 1000
    i = box[idx] % 100000
    o = i // 10000
    p = box[idx] % 1000000
    s = p // 100000
    d = box[idx] % 10000000
    f = d // 1000000
    g = box[idx] % 100000000
    h = g // 10000000
    j = box[idx] % 1000000000
    k = j // 100000000
    total = q + e + t + u + o + s + f + h + k
    if total % 7 == 0:
        amount += box[idx]
    idx += 1
print(amount)
