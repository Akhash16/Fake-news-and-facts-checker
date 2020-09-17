from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='cc8998f479954041b5f845f0b4491050')

news_sources = newsapi.get_sources()
#for source in news_sources['sources']:
    #print(source['name'])
source1 = []
source2 = []

top_headlines = newsapi.get_top_headlines(q='corona',language='en',)
for article in top_headlines['articles']:
    source1.append(article['source']['name'])
    #title1.append(article['title'])
    #description1.append(article['description'])



all_articles = newsapi.get_everything(q='corona virus',language='en',)
for article in all_articles['articles']:
    source2.append(article['source']['name'])
    #title2.append(article['title'])
    #description2.append(article['description'])

#print(top_headlines['articles'])
#print(all_articles['articles'])
#print(type(article['source']['name']))
if(top_headlines['articles'] == []  and all_articles['articles'] == []):
    print('FAKE')
else:
    print('REAL','\n',source2[0])