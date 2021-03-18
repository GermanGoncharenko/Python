from re import compile

def email_parse(email_address):
    name = compile(r'([\w]+)\@((?<==@)[^.]+\.\w+)')
    if name.match(email_address):
        a, b = name.findall(email_address)[0]
        print(dict(name=a, domain=b))
    else:
        raise ValueError

try:
    email_parse('someone@geekbrains.ru')
    email_parse('someone@geekbrainsru')
except ValueError:
    print(f'Wrong email!')
    
