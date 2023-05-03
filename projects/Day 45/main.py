# import requests
# import bs4
#
# # with open('website.html', encoding='utf-8') as fp:
# #     soup = bs4.BeautifulSoup(fp.read(), 'html.parser')
# #
# # print(soup.find_all(name='p'))
# #
# # print(soup.select('#name'))
#
# URL = "https://news.ycombinator.com/news"
# response = requests.get(URL)
# response.raise_for_status()
#
# soup = bs4.BeautifulSoup(response.text, 'html.parser')
# # print(soup.prettify())
#
# for score in soup.select('.score'):
#     score.getText()
#
# scores = {
#     int(score.getText().split(' ')[0]): score.get('id').split('_')[1]
#     for score in soup.select('.score')
# }
#
# max_score = max(scores.keys())
# ele = soup.select(f"[id='{scores[max_score]}']")[0]
# ele = ele.select('.titleline')[0]
#
# print(ele.getText())
# print(ele.select('a')[0].get('href'))
# print(max_score)

import bs4
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response.raise_for_status()
response = response.text
soup = bs4.BeautifulSoup(response)

movie_list = []
for item in soup.select("div[data-test^='listicle-item-']"):
    movie_list.append(item.select('img')[0].get('alt'))
movie_list.reverse()

with open('movies.txt', 'w+', newline='') as fp:
    for i in range(len(movie_list)):
        fp.write(f'{i + 1}) {movie_list[i]}\n')
