# list of dicts: categories title, description, 
# get random articles
# then for each random article, query for 2 more similar articles like that article
# then for each articles give relevant information (title, description, )

# query based on category / location

import json
import requests

# track what articles they've been reading -> information from frontend
def get_api_key():
    with open("news.json") as f:
        data = json.load(f)

    return data["api_key"]

def get_base_url():
    with open("news.json") as f:
        data = json.load(f)
    
    return data["base_url"]

def get_latest_news(search=None, category=None, location="Australia"):
    """ 
        Gets the latest news for a particular search, catergory or location
    """

    api_key = get_api_key()
    base_url = get_base_url()
    
    if search == None:
        query = base_url + f'everything?q='

    # search_keywords = "Texas heatwave and energy crunch curtails Bitcoin mining"
    search_keywords = "Crosby, Stills and Nash return to Spotify after COVID-19 misinformation boycott"
    query = base_url+f'everything?q={search_keywords}&apiKey={api_key}'
    response = requests.get(query)
    print(response.json()['articles'])
    # for word in search_keywords.split():
    #     keyword = word
    #     query = base_url+f'everything?q="{keyword}"&apiKey={api_key}'
    #     response = requests.get(query)
    #     print(response.json()['articles'][2])
        # for article in response.json()['articles'][2]:
        #     print('---')
        #     print('Title: ', article['title'])
        #     print('From: ', article['source']['name'])
        #     print('Description: ', article['description'])
    # https://newsapi.org/v2/everything?q=bitcoin&apiKey=API_KEY
    # https://newsapi.org/v2/?q=bitcoin&apiKey=f1db92c3cee347cf85bc56c4226da4ab
    # print(query)
    # response = requests.get(query)
    # print(len(response.json()['articles']))
    # print(response.json()['articles'])

if __name__ == "__main__":
    print(get_latest_news())