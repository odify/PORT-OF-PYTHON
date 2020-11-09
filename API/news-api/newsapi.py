#!/usr/bin/env python3

import requests
import os
import datetime
import pyfiglet


result = pyfiglet.figlet_format("News API\n")
print(result)
os.system("date")
print("\n") # describtion-row


_NEWS_API = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey="


def fetch_bbc_news(bbc_news_api_key: str) -> None:
    # fetching a list of articles in json format
    bbc_news_page = requests.get(_NEWS_API + bbc_news_api_key).json()
    # each article in the list is a dict
    for news, article in enumerate(bbc_news_page["articles"], 1):
        print(f"{news}.) {article['title']}")


if __name__ == "__main__":
    fetch_bbc_news(bbc_news_api_key="f6a267260a564dc08d40a90e1a8be145")
