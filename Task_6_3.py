from json import dump
from itertools import zip_longest
with open ("name.csv", "r", encoding="utf-8") as name:
    with open("hobby.csv", "r", encoding="utf-8") as hobby:
        box = zip_longest((" ".join(us.split(",")) for us in name), hobby, fillvalue=None)
        my_box = {str(el[0]).strip(): (el[1].strip()) for el in box}
        with open('dict_n_h.json', 'w', encoding='utf-8') as f:
            if "None" in my_box:
                print(1)
            else:
                dump(my_box, f, ensure_ascii=False, indent=4)
                print(my_box)
