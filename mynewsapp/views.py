from django.shortcuts import render
from newsapi import NewsApiClient

def index(request):
    news_api = NewsApiClient(api_key = '3c2b202ab37b488dbaeae16c69a9d77e')
    top = news_api.get_top_headlines(sources = 'bbc-news')

    l = top['articles']
    desc = []
    news = []
    img = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news,desc,img)

    return render(request,'index.html',context ={"mylist":mylist})
