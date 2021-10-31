from celery import shared_task
from news.models import NewsCeleryTasks
import requests
import xmltodict
import datetime
from bs4 import BeautifulSoup


@shared_task
def get_content_of_varzesh3_url(given_url):
    raw_url = requests.get(url=given_url)
    content = BeautifulSoup(raw_url.text, 'html.parser')
    final_content = content.find('div', {'class': 'col-xs-12 news-page--news-text text-justify'})
    if final_content == None:
        pass
    else:
        return final_content.text


def paralell_tasks(crawled_date, crawled_url, crawled_content, crawled_title):
    updating_news = NewsCeleryTasks.objects.filter(url=crawled_url,
    lastmod__gte=crawled_date)
    if updating_news.exists():
        updating_news.update(title=crawled_title,
        lastmod = crawled_date,
        content = crawled_content
        )
    else:
        saved_data = NewsCeleryTasks.objects.create(
            title = crawled_title,
            url = crawled_url,
            lastmod = crawled_date,
            content = crawled_content
        )
        saved_data.save()


@shared_task
def get_varzesh3_information_task():
    primary_url = 'https://www.varzesh3.com/'
    url = "https://www.varzesh3.com/sitemap/news"
    result = requests.get(url)
    data = xmltodict.parse(result.content)
    for j in range(len(data['urlset']['url'])):
        paralell_tasks(crawled_date=datetime.strptime(data['urlset']['url'][j]['lastmod'], '%Y-%m-%dT%H:%M:%S%z'),
        crawled_url=primary_url + data['urlset']['url'][j]['loc'][:14],
        crawled_content=get_content_of_varzesh3_url(primary_url + data['urlset']['url'][j]['loc'][:14]),
        crawled_title=data['urlset']['url'][j]['loc'][14:]
        )