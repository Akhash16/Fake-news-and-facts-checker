from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup as soup
import validators
from newsapi import NewsApiClient

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
    if(msg == "hi"):
        resp.message("FAKE NEWS DETECTOR AND FACTS CHECKER:\n1.Article checker \n 2.Facts checker")
    if(msg == '1'):
        resp.message("Enter the URL of the article")
    if(msg == '2'):
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
            pass


    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
