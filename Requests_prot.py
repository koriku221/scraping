import requests

r = requests.get('http://news.yahoo.co.jp')

print(r.headers)
print("-----------")
print(r.encoding)
print(r.content)
