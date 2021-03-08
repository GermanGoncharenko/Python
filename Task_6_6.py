from sys import argv
with open("bakery.csv", "a", encoding="utf-8") as donut_a:
    with open("bakery.csv", "r", encoding="utf-8") as donut_r:
        if len(argv) == 1:
            print(donut_r.read())
        elif len(argv) == 2:
            if "," in argv[1]:
                donut_r.read()
                print(argv[1], file=donut_a)
            else:
                print(*donut_r.readlines()[int(argv[1]) - 1:], sep="")
        else:
            print(*donut_r.read().split()[int(argv[1]):int(argv[2]) + 1], sep="\n")
