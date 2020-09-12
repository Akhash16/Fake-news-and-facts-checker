
from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='cc8998f479954041b5f845f0b4491050')

news_sources = newsapi.get_sources()
for source in news_sources['sources']:
    print(source['name'])


top_headlines = newsapi.get_top_headlines(
    q='Vasanth&Co owner died',
    language='en',
)
for article in top_headlines['articles']:
    print('Title : ',article['title'])
    print('Description : ',article['description'],'\n\n')



all_articles = newsapi.get_everything(
    q='Vasanth&Co owner died',
    language='en',   
)
for article in all_articles['articles']:
    print('Source : ',article['source']['name'])
    print('Title : ',article['title'])
    print('Description : ',article['description'],'\n\n')    
