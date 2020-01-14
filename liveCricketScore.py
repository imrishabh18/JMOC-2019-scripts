import requests
from bs4 import BeautifulSoup
from time import sleep

# Enter the espncricinfo url for the match you want to see the score
URL = 'https://www.espncricinfo.com/series/8654/game/1197770/canterbury-vs-otago-30th-match-super-smash-2019-20'
page = requests.get(URL)
soup = BeautifulSoup(page.content,'html.parser')

matchBetween = soup.find('div',class_='cscore_info-overview')
print(matchBetween.text)

p=1
while(p>=1):

    home = soup.find('li',class_='cscore_item cscore_item--home')
    homeScore = home.find('div',class_='cscore_score').text
    away = soup.find('li',class_='cscore_item cscore_item--away')
    awayScore = away.find('div',class_='cscore_score').text

    print(homeScore)
    print(awayScore)

    sleep(15)
