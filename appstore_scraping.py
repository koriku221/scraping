import requests
from bs4 import BeautifulSoup
import csv
import pprint
import urllib.robotparser
import sys
from cachecontrol import CacheControl
from cachecontrol.caches import FileCache


session = requests.session()
cached_session = CacheControl(session, cache=FileCache('.webcache'))
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
headers = {"User-Agent": user_agent}
url = ("https://rss.itunes.apple.com/api/v1/jp/ios-apps/new-apps-we-love/all/10/explicit.rss")
rp = urllib.robotparser.RobotFileParser()
rp.set_url("https://rss.itunes.apple.com/robots.text")
rp.read()
if not rp.can_fetch(user_agent, url):
    sys.exit("permission denied")

response = cached_session.get(url, headers = headers)
print(f'from_cache:{response.from_cache}')
print(f'status_code:{response.status_code}')
#print(response.text)

#print(response.content)

soup = BeautifulSoup(response.content,"lxml")
#print(soup.prettify)

#Beautifulsoup.find_all() ：要素名または属性で検索し、該当する全ての要素を返す
#print(soup.find_all("item")) 
#Beautifulsoup.find(), Beautifulsoup.：要素名または属性で検索し、該当する最初の要素を返す
#print(soup.item)

"""
#タイトル列挙
soup_titles =[item.title for item in soup.find_all("item")]     #item内のtitleのみ抽出 -> list
print(soup_titles)

titles = [title.text for title in soup_titles]      #titleタグを除去
print(titles)
"""

#CSV
soup_items = soup.find_all("item")
#print(soup_items)


item_ids = []
for item in soup_items:
    
    item_id = []
    item_id.append(item.title.text)             
    item_id.append(item.description.text) 
    
    for category in item.find_all("category"):     #categoryのみ複数ある為

        item_id.append(category.text)

    #print(item_id)
    item_ids.append(item_id)

#print(item_ids)

# with open('appstore.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows(item_ids)
