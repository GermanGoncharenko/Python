def thesaurus(*args):
    name = {}
    for idx in sorted(args):
        m = idx[0]
        if m not in name:
            name[m] = []
        if m in name:
            name[m].append(idx)
    return name
print(thesaurus("Герман", "Евгений", "Ольга", "Ирина", "Константин", "Виктор", "Георгий", "Денис", "Виктория", "Екатерина"))
