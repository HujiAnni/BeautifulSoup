import requests
from bs4 import BeautifulSoup
res=requests.get('https://events.berkeley.edu/?view=summary&timeframe=day&date=2020-07-15&tab=all_events')
html_berkeley=res.text
soup=BeautifulSoup(html_berkeley,'html.parser')
events_name=soup.find_all(class_='event-title')
for item in events_name:
    link=item.find('a')
    print(item.text,'\n'+'events.berkeley.edu/'+str(link['href']))
