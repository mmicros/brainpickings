
#! /usr/bin/python3
import requests
from bs4 import BeautifulSoup as bs
import subprocess

posts = ["https://www.brainpickings.org/wp-sitemap-posts-post-1.xml",
         "https://www.brainpickings.org/wp-sitemap-posts-post-2.xml",
         "https://www.brainpickings.org/wp-sitemap-posts-post-3.xml"]
n=1
for post in posts:
    req = requests.get(post)
    if req:
        soup=bs(req.text)
    
    tags = soup.find_all("loc")
    for i in tags:
        print(i.text)
    print(f"finished post {n}")
    n=n+1
