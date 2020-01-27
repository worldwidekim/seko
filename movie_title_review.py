#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests
from bs4 import BeautifulSoup


# In[7]:


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


## kp) 여기 "page" 가 function argument로 들어있어야 됌.
def get_daum_movie_review(movie_id, page):
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


# 총 리뷰 숫자만 뽑아서 가져오는 새로운 함수
def get_daum_movie_review_number(movie_id, page):
    url = 'https://movie.daum.net/moviedb/grade?movieId={}&type=netizen&page={}'.format(movie_id, page)

    resp = requests.get(url)
    soup = BeautifulSoup(resp.text)
    netizen = soup.select_one("span.txt_menu")

    if netizen:
        return netizen.get_text()
    return ""

    reviews.append(netizen)
    page += 1
