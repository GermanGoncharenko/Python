from requests import get, utils
response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
structure = response.content.decode(encoding=encodings)
print(structure)

