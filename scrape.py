import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/news')
response2 = requests.get('https://news.ycombinator.com/news?p=2')
soupObject = BeautifulSoup(response.text, 'html.parser')
soupObject2 = BeautifulSoup(response2.text, 'html.parser')

links = soupObject.select('.titlelink')
subtex = soupObject.select('.subtext')
links2 = soupObject2.select('.titlelink')
subtex2 = soupObject2.select('.subtext')

mega_links = links + links2
mega_subtext = subtex + subtex2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)


def create_custom_hk(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)
     

pprint.pprint(create_custom_hk(mega_links, mega_subtext))