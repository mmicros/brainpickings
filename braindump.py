#! /usr/bin/python3
import requests
from bs4 import BeautifulSoup as bs

posts = []
linked_posts = {}

def get_all_posts():
    list_of_posts = ["https://www.brainpickings.org/wp-sitemap-posts-post-1.xml",
                     "https://www.brainpickings.org/wp-sitemap-posts-post-2.xml",
                     "https://www.brainpickings.org/wp-sitemap-posts-post-3.xml"]

    for l in list_of_posts:
        req = requests.get(l)
        if req:
            soup=bs(req.text)
        
        tags = soup.find_all("loc")
        for tag in tags:
            posts.append(tag.text)


def get_linked_posts():
    for post in posts:
        links=[]
        print(f"post:{post}")
        req = requests.get(post)
        if req:
            soup=bs(req.text)
        
        link_tags = soup.find("div","post_content").find_all('a')

        for link_tag in link_tags:
            if(link_tag.has_attr('href') and ("https://www.brainpickings.org/2" in link_tag['href'])):
                links.append(link_tag['href'])
                print("\t"+link_tag['href'])
        linked_posts[post]=links
        

get_all_posts()
print(len(posts))
get_linked_posts()

# sanity check (can be deleted later)
f = open("dict.txt","a")
f.write(linked_posts)
f.close

