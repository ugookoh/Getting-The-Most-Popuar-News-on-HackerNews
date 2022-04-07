from bs4 import BeautifulSoup
import requests
URL = 'https://news.ycombinator.com/'

response = requests.get(URL)
website = response.text
soup = BeautifulSoup(website, "html.parser")

titles = soup.find_all(class_="titlelink")
scores = soup.find_all(class_="score")
titles_list = []
links_list = []
scores_list = []

for title in titles:
    item_title = title.getText()
    item_link = title.get('href')
    titles_list.append(item_title)
    links_list.append(item_link)

for score in scores:
    points = score.getText()
    array_of_points = [int(s) for s in points.split() if s.isdigit()]
    scores_list.append(array_of_points[0])

highest_news_score = max(scores_list)
highest_news_index = scores_list.index(highest_news_score)
highest_news_title = titles_list[highest_news_index]
highest_news_link = links_list[highest_news_index]

print('\n\n')
print('The current most popular news on YCombinator Hackernews')
print(f'Title : {highest_news_title}')
print(f'Link : {highest_news_link}')
print(f'Upvotes : {highest_news_score}')
print('\n\n')
