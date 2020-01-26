#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


# In[7]:


def get_daum_news_title(news_id):
    url = 'https://news.v.daum.net/v/{}'.format(news_id)
    resp = requests.get(url)
    
    soup = BeautifulSoup(resp.text)
    
    title_tag = soup.select_one('h3.tit_view')
    if title_tag:
        return title_tag.get_text()
    return ""


# ### 영화 메인 정보 크롤링 함수 (메인 Tab)

# In[8]:


def get_daum_movie_title(movie_id):
    url = 'https://movie.daum.net/moviedb/main?movieId={}'.format(movie_id)
    resp = requests.get(url)
    
    soup = BeautifulSoup(resp.text)
    
    title_tag = soup.select_one('h2.tit_rel')
    if title_tag:
        return title_tag.get_text()
    return ""


# In[9]:


## 크롤링 결과 확인

get_daum_movie_title(2725)


# ### 영화 댓글 크롤링 함수 (평점 Tab)

# In[4]:


def get_daum_movie_review(movie_id):
    url = 'https://movie.daum.net/moviedb/grade?movieId={}&type=netizen&page={}'.format(movie_id, page)
    reviews = []
    page = 1
    
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text)
    netizen = soup.select_one('p.desc_review')
    
    
    if netizen:
        return netizen.get_text()
    return ""
    
    reviews.append(netizen)
    page += 1


# In[5]:


get_daum_movie_review(2725)


# 여기서는 page에 1을 기본으로 주고 밑에서 +1로 계속 추가 시키면서 하려고 한 건데 전혀 진행이 안됨...
# 그래서 위에 get_daum_movie_review(movie_id, page)를 넣고
# get_daum_movie_review(2725, 1) 로 실행을 하면
# 1개만 받아와지고 거기서 끝나는데 뭐가 문제인지를 모르겠엄...

# In[15]:


url = 'https://movie.daum.net/moviedb/grade?movieId=2725&type=netizen&page=2'
resp = requests.get(url)
soup = BeautifulSoup(resp.text)
review_number = soup.select_one('span.txt_menu')
print(review_number)


# 여기서는 798이란 숫자만 나타내고 싶은데 어떻게 지우고 798만 가지고 와야 할지를 모르겠음...
# 인터넷 보니깐 html로 가져와서 하는데 json 사용해서 바꾸고 가져와야 하는 건가?? 
