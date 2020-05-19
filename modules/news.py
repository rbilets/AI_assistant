from newsapi import NewsApiClient
from ADT.news_ADT import NewsADT
from ADT.arrayqueue import ArrayQueue


def get_news(pref, amount=5):

    country = 'ua'
    if pref.lower() == 'united states':
        country = 'us'

    api_key = 'adadc440e29c4aadafb038c127d8eabd'

    newsapi = NewsApiClient(api_key=api_key)
    top_headlines = newsapi.get_top_headlines(country=country)

    news = ArrayQueue()

    for i in range(top_headlines['totalResults']):
        if i == amount:
            break
        article = NewsADT()
        article.add_title(top_headlines['articles'][i]['title'])
        article.add_description(top_headlines['articles'][i]['description'])
        article.add_url(top_headlines['articles'][i]['url'])
        news.add(article)
    return news


if __name__ == '__main__':
    news_queue = get_news(pref='Uk', amount=4)
    while not news_queue.isEmpty():
        print(news_queue.pop().get_title())
