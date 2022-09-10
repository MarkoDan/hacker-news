import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/news')
soupObject = BeautifulSoup(response.text, 'html.parser')
#print(soupObject.head)
# print(soupObject.find_all('div'))
# print(soupObject.title)
# print(soupObject.a)
# print(soupObject.find(id="score_32787251"))

# print(soupObject.select('.score'))

# print(soupObject.select('#score_32780388'))

link = soupObject.select('.titlelink')
votes = soupObject.select('.score')
print(votes[2])

print(votes[0].get('id'))