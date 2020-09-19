from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup as soup
import validators
from newsapi import NewsApiClient
from googleapiclient.discovery import build

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')


    resp = MessagingResponse()
    # Create reply
    

    #resp.message("Title is: {}".format(title))
    if(msg == "hi" or msg == 'Hi'):
        resp.message("FAKE NEWS DETECTOR AND FACTS CHECKER:\n1.Article checker \n 2.Facts checker")
    elif(msg == '1'):
        resp.message("Enter the URL of the article")
    elif(msg == '2'):
        resp.message("Enter the fact or a short sentence")
    #resp.message("You said: {}".format(msg))
    else:
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
            if(top_headlines['articles'] == []  and all_articles['articles'] == []):
                resp.message("The news is FAKE")
            else:
                resp.message('The news is REAL')


        else:
            API_KEY='AIzaSyBEbc15F1s35_bgvC8eupXt0MpGkV92PnA'
            SERVICE=build("factchecktools","v1alpha1",developerKey=API_KEY)
            userQuery=msg
            
            request1=SERVICE.claims().search(query=userQuery)
            response=request1.execute()


            if not bool(response):
                
                source1 = []
                newsapi = NewsApiClient(api_key='cc8998f479954041b5f845f0b4491050')
                news_sources = newsapi.get_sources()

                all_articles = newsapi.get_everything(q = msg, language = 'en',)
                for article in all_articles['articles']:
                    source1.append(article['source']['name'])
                

                if(all_articles['articles'] == []):
                    resp.message("The news is FAKE")
                else:
                    resp.message('The news is REAL')
                    resp.message(source1[0])
                

            else:
                result  = response['claims'][0]['claimReview'][0]['textualRating']
                website = response['claims'][0]['claimReview'][0]['publisher']['name']
                url = response['claims'][0]['claimReview'][0]['url']
                resp.message(result)
                resp.message(website)
                resp.message(url) 

            

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
