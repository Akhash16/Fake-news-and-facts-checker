from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def title_extraction(msg):
    my_url = msg
    req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
    uClient = urlopen(req)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html,'html.parser')
    title = page_soup.h1.text
    return title
