box = [56.32, 33.3, 65.47, 45.54, 61, 89.2, 97.84, 25.8,
       11, 37.74, 73.77, 99.99, 87, 24.1, 59.32, 90.66,
       41, 18.7, 91.89, 20]
r = 0
k = 0
for idx in box:
    m = str(idx).split('.')
    if len(m) == 2:
        r, k = m
    print(f'{r} руб {int(k):02d} коп, ', end="")
print(f'')
print(f'ID original: {id(box)} - {box}')
box.sort()
print(f'ID ordered: {id(box)} - {box}')
box_reversed = box[::-1]
print(f'ID back ordered: {id(box_reversed)} - {box_reversed}')
print(box[-5:])
