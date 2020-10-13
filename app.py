from flask import Flask,render_template,request
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup as soup
import validators
from newsapi import NewsApiClient
from googleapiclient.discovery import build
import pickle
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

app = Flask(__name__,template_folder='templates')

with open('model.pickle', 'rb') as mod:
    model = pickle.load(mod)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search.html")
def search():
    return render_template("search_v2.html")

@app.route("/search_query",methods=['POST','GET'])
def store():
    msg = request.form.get('user_query')


    valid=validators.url(msg)
    if valid==True:
        my_url = msg
        req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
        uClient = urlopen(req)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html,'html.parser')
        title = page_soup.h1.text

        newsapi = NewsApiClient(api_key='cc8998f479954041b5f845f0b4491050')
        news_sources = newsapi.get_sources()
        top_headlines = newsapi.get_top_headlines(q = title, language = 'en',)
        all_articles = newsapi.get_everything(q = title, language = 'en',)
        
        source2 = []
        description2 = []
        
        for article in all_articles['articles']:
                source2.append(article['source']['name'])
                description2.append(article['description'])
        
        if(top_headlines['articles'] == []  and all_articles['articles'] == []):
            pred = model.predict([title])
            ans = "The news is mostly " + pred[0]
            return ans
        else:
            ans1 = 'The news is REAL\nSource : {0}\nDescription : {1}'.format(source2[0],description2[0])
            
            return ans1


    else:
        
        list_of_stopwords = list(stopwords.words('english'))
        tokenized_text = word_tokenize(msg)
        clean_msg = ''
        for word in tokenized_text:
            word = word.lower()
            if not word in list_of_stopwords and word != '.' and word != "''" and word!="``"and word !=']' and word !='!' and word !='%' and word !='&' and word !='?' and word !='//' and word !=';' and word !='|' and word != ' ' and word != "'" and word !='"' and  word !='[' and word != '@' and word != ',' and word !='#' and word !='..' and word !='-' and word !='(' and word !=')' and word != '...' and word != '/' and word !=':':
                clean_msg += word + ' '
                
                
        #news api part        
        source1 = []
        description1 = []
        newsapi = NewsApiClient(api_key='cc8998f479954041b5f845f0b4491050')
        news_sources = newsapi.get_sources()
        all_articles = newsapi.get_everything(q = clean_msg, language = 'en',)
        for article in all_articles['articles']:
            source1.append(article['source']['name'])
            description1.append(article['description'])


        if(all_articles['articles'] == []):

            API_KEY='AIzaSyBEbc15F1s35_bgvC8eupXt0MpGkV92PnA'
            SERVICE=build("factchecktools","v1alpha1",developerKey=API_KEY)
            userQuery=clean_msg

            request1=SERVICE.claims().search(query=userQuery)
            response=request1.execute()
            
            if bool(response):
                result  = response['claims'][0]['claimReview'][0]['textualRating']
                website = response['claims'][0]['claimReview'][0]['publisher']['name']
                url = response['claims'][0]['claimReview'][0]['url']
                resp.message(result)
                resp.message(website)
                resp.message(url)
                ans2 = 'Result : {0}\nWebsite : {1}\nURL : {2}'.format(result,website,url)

                return ans2
                
            else:
                ans3 = "The news is FAKE"

                return ans3
            
        else:
            ans4 = 'The news is REAL\nSource : {0}\nDescription : {1}'.format(source1[0], description1[0])

            return ans4



if __name__ == '__main__':
    app.run(port=5000,debug=True)