import requests
from bs4 import BeautifulSoup

base_url = "https://nba.udn.com/"
home_url = base_url + "nba/index?gr=www"
res = requests.get(home_url)
soup = BeautifulSoup(res.text, 'html.parser')

for news in soup.find(id='news_body').find_all('dt'):
    title = news.find('h3').text
    story_path = news.find('a')['href']
    story_url = base_url + story_path
    pic_url = news.find('img')['src']

    news_data = [title, pic_url]

    soup_story = BeautifulSoup(requests.get(story_url).text, 'html.parser')\
    [news_data.append(para.text) for para in soup_story.find_all('p')[
        1:] if len(para.text) is not 0]

    news_data[:].save()