from celery import shared_task
import requests
from requests.api import request
import xmltodict
import datetime
from bs4 import BeautifulSoup
import psycopg2
from psycopg2.extras import execute_values


dict_of_news = {}
list_of_news = []
primary_url = 'https://www.varzesh3.com/'
url = "https://www.varzesh3.com/sitemap/news"
result = requests.get(url)
data = xmltodict.parse(result.content)

@shared_task
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)


start_date = datetime.date(2021, 10, 13)
end_date = datetime.date(2021, 10, 14)

@shared_task
def get_content_of_varzesh3_url(given_url):
    raw_url = requests.get(url=given_url)
    content = BeautifulSoup(raw_url.text, 'html.parser')
    final_content = content.find('div', {'class': 'col-xs-12 news-page--news-text text-justify'})
    if final_content == None:
        pass
    else:
        return final_content.text


@shared_task
def get_varzesh3_information():
    for single_date in daterange(start_date, end_date):
        single_date = single_date.strftime("%Y-%m-%d")
        for j in range(len(data['urlset']['url'])):
            if single_date == data['urlset']['url'][j]['lastmod'][0:10]:
                dict_of_news['task_id'] = request.id
                dict_of_news['url'] = primary_url + data['urlset']['url'][j]['loc'][:14]
                dict_of_news['title'] = data['urlset']['url'][j]['loc'][14:]
                dict_of_news['lastmod'] = datetime.strptime(
                    data['urlset']['url'][j]['lastmod'][0:10], '%Y-%m-%d')
                dict_of_news['content'] = get_content_of_varzesh3_url(primary_url + data['urlset']['url'][j]['loc'][:14])
                list_of_news.append(dict_of_news.copy())

    columns = list_of_news[0].keys()
    query = "INSERT INTO news_newscelerytasks ({}) VALUES %s".format(','.join(columns))
    values = [[value for value in news.values()] for news in list_of_news]

    execute_values(psycopg2.cursor, query, values)
    psycopg2.connection.commit()
