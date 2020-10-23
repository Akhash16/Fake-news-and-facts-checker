from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup
import validators
from newsapi import NewsApiClient
from googleapiclient.discovery import build
import pickle
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

app = Flask(__name__)

with open('model.pickle', 'rb') as mod:
    model = pickle.load(mod)


@app.route("/")
def hello():
    return "Working!"


@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    resp = MessagingResponse()
    # Create reply

    # resp.message("Title is: {}".format(title))
    if (msg == " " or msg == '0'):
        resp.message('''Hi Hello ! \n This is Jazzy - A News Detection Bot \n I am capable of doing some Tasks! \n Type a Number to navigate: \n 1.Article checking \n 2.Article Summarization \n 3.Facts checking \n 4.Url Expander \n Share me \n https://wa.me/+14155238886?text=join came-poor ''')


    switch(msg)
        case 1:
            resp.message("Enter the Url of the article")
            valid = validators.url(msg)
            if valid == True:
                my_url = msg
                req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
                uClient = urlopen(req)
                page_html = uClient.read()
                uClient.close()
                page_soup = soup(page_html, 'html.parser')
                title = page_soup.h1.text

                newsapi = NewsApiClient(api_key='cc8998f479954041b5f845f0b4491050')
                news_sources = newsapi.get_sources()
                top_headlines = newsapi.get_top_headlines(q=title, language='en', )
                all_articles = newsapi.get_everything(q=title, language='en', )

                source2 = []
                description2 = []
                if(top_headlines['articles'] != [] and all_articles['articles'] != []):
                    for article in all_articles['articles']:
                        source2.append(article['source']['name'])
                        description2.append(article['description'])
                    resp.message('The news is REAL')
                    resp.message(source2[0])
                    resp.message(description2[0])
                else:
                    pred = model.predict([title])
                    ans = "The news is mostly " + pred[0]
                    resp.message(ans)


            else:
                print("The Url does not exists !")
            break
        case 2:
            pass
            break
        case 3:
            resp.message('''Type a word or short sentence (in English) related to the fact or news you want to check, and we’ll send you the related results.\n 👀 Example: If you’ve read a news about anything, type the news headlines or a short sentence like: does iphone 12 series are packed without chargers?''')
            list_of_stopwords = list(stopwords.words('english'))
            tokenized_text = word_tokenize(msg)
            clean_msg = ''
            for word in tokenized_text:
                word = word.lower()
                if not word in list_of_stopwords and word != '.' and word != "''" and word != "``" and word != ']' and word != '!' and word != '%' and word != '&' and word != '?' and word != '//' and word != ';' and word != '|' and word != ' ' and word != "'" and word != '"' and word != '[' and word != '@' and word != ',' and word != '#' and word != '..' and word != '-' and word != '(' and word != ')' and word != '...' and word != '/' and word != ':':
                    clean_msg += word + ' '

            API_KEY = 'AIzaSyBEbc15F1s35_bgvC8eupXt0MpGkV92PnA'
            SERVICE = build("factchecktools", "v1alpha1", developerKey=API_KEY)
            userQuery = clean_msg
            request1 = SERVICE.claims().search(query=userQuery)
            response = request1.execute()

            result = response['claims'][0]['claimReview'][0]['textualRating']
            website = response['claims'][0]['claimReview'][0]['publisher']['name']
            url = response['claims'][0]['claimReview'][0]['url']
            resp.message(result)
            resp.message(website)
            resp.message(url)

            if not bool(response):

                source1 = []
                description1 = []
                newsapi = NewsApiClient(api_key='cc8998f479954041b5f845f0b4491050')
                news_sources = newsapi.get_sources()
                query = msg
                tokenized_text1 = word_tokenize(query)
                word_count = len(tokenized_text1)
                clean_msg1 = ''
                count = 0
                for word in tokenized_text1:
                    word = word.lower()
                    if not word in list_of_stopwords and word != '.' and word != "''" and word != "``" and word != ']' and word != '!' and word != '%' and word != '&' and word != '?' and word != '//' and word != ';' and word != '|' and word != ' ' and word != "'" and word != '"' and word != '[' and word != '@' and word != ',' and word != '#' and word != '..' and word != '-' and word != '(' and word != ')' and word != '...' and word != '/' and word != ':':
                        clean_msg1 += word + ' '
                all_articles = newsapi.get_everything(q=clean_msg1, sort_by='relevancy', language='en', )

                if (all_articles['articles'] not =[]):

                    for article in all_articles['articles']:
                        source1.append(article['source']['name'])
                        description1.append(article['description'])
                    for i in range(len(source1)):
                        for j in range(word_count):
                            if (tokenized_text[j] in description1[i]):
                                count = count + 1;
                                if (count >= word_count / 2):
                                    newsapi_source = source1[i]
                                    newsapi_description = description1[i]
                                    break

                    resp.message('The news is REAL')
                    resp.message(newsapi_source)
                    resp.message(newsapi_description)

#                     text = input()
        #                     words = ['what ', 'who ', 'why ', 'how ', 'Is ']
        #                     questions = []
        #                     for word in words:
        #                         if word == 'Is ' and text.find('is')>0:
        #                             word_list = text.split()
        #                             new = ' '.join([i for i in word_list if i not in 'is'])
        #                             questions.append('Is ' + new + ' ?')
        #                         else:
        #                             questions.append(word + text + ' ?')

            temp = user_text.split()
            word_count1 = len(temp)
            processed_text = '+'.join(temp)

            my_url = f'https://www.google.com/search?q={processed_text}'
            req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
            uClient = urlopen(req)
            page_html = uClient.read()
            uClient.close()
            page_soup = soup(page_html, 'html.parser')

            container = page_soup.find_all('div', {'class': 'BNeawe s3v9rd AP7Wnd'})

            list_of_stopwords = list(stopwords.words('english'))
            tokenized_user_text = word_tokenize(user_text)
            clean_user_text = []
            for word in tokenized_user_text:
                word = word.lower()
                if not word in list_of_stopwords and word != '.' and word != "''" and word != "``" and word != ']' and word != '!' and word != '%' and word != '&' and word != '?' and word != '//' and word != ';' and word != '|' and word != ' ' and word != "'" and word != '"' and word != '[' and word != '@' and word != ',' and word != '#' and word != '..' and word != '-' and word != '(' and word != ')' and word != '...' and word != '/' and word != ':':
                    clean_user_text.append(word)

            for i in range(len(container)):
                tokenized_result = word_tokenize(container[i].text)
                clean_result = ''
                clean_searches = []
                    for word in tokenized_user_text:
                        word = word.lower()
                        if not word in list_of_stopwords and word != '.' and word != "''" and word != "``" and word != ']' and word != '!' and word != '%' and word != '&' and word != '?' and word != '//' and word != ';' and word != '|' and word != ' ' and word != "'" and word != '"' and word != '[' and word != '@' and word != ',' and word != '#' and word != '..' and word != '-' and word != '(' and word != ')' and word != '...' and word != '/' and word != ':':
                            clean_result = word + ' '
                            clean_searches.append(clean_result)

            count1 = 0
            for i in range(len(clean_searches)):
                for j in range(len(clean_user_text)):
                    if (clean_user_text[j] in clean_searches[i]):
                        count1 = count1 + 1;
                    if (count1 >= word_count1 / 2):
                        resp.message(container[0].text)
            break

        case 4:
            pass
            break

        default:
            resp.message("press 0 to main menu")

    return str(resp)


if __name__ == "__main__":
    app.run()
