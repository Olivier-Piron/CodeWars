import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.codewars.com/users/leaderboard'
page = requests.get(url)

soup = bs(page.content , 'html.parser')

names = soup.find_all(class_ = "is-big")

users = []
i = 0

for name in names:
    i += 1
    user = name.find('a')
    if i > 2:
        users.append(user.text)
    

print(len(users), users)



def solution():
  # do it
  return
