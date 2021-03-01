from requests import get, utils
response = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))
def currency_rates(code):
    content = response.split("<Valute ID=")
    for i in content:
        if code.upper() in i:
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))

if __name__ == "__main__":
    print(currency_rates("USD"))
    print(currency_rates("EUR"))

#-------------------------------------

import Task_4_4
print(Task_4_4.currency_rates("CRY"))


