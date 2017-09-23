#!__*__coding:utf-8__*__

import os
import sys
import urllib.parse
import json
import csv
import requests
import html
from bs4 import BeautifulSoup
import urllib
from selenium import webdriver
import time
from konlpy_api import MyKonlpy

CLIENT_ID = "RjvotaEwT3oTy_y8umFg"
CLIENT_SECRET_ID = "54rlJdeY2L"
BLOG_SEARCH_URL = "https://openapi.naver.com/v1/search/blog.json?query="
NEWS_SEARCH_URL = "https://openapi.naver.com/v1/search/news.json?query="
MAX_RESULT = 200

BROWSER = 'D://chromedriver_win32/chromedriver.exe'

MY_Twitter = None
DRIVER = None

def get_nouns(comment):
    global  MY_Twitter
    if MY_Twitter is None:
        MY_Twitter = MyKonlpy()
    k = MY_Twitter.get_nouns(comment)
    return " ".join(k)


def remove_html_tag(my_string):
    a = BeautifulSoup(my_string, 'html.parser')
    text = a.get_text("\n")
    return remove_space(text)


def remove_space(my_content):
    result = ""
    for i in my_content.splitlines():
        if i.strip() == "":
            pass
        else:
            x = " ".join(i.split())
            result += x
            result += "\n"
    return result


def get_query(keyword, x, type="blog"):
    global BLOG_SEARCH_URL, NEWS_SEARCH_URL
    print("get_query function")

    encText = urllib.parse.quote(keyword)
    if type == "news":
        url = NEWS_SEARCH_URL + encText + "&display=100&start=" + x# json 결과
    elif type == "blog":
        url = BLOG_SEARCH_URL + encText + "&display=100&start=" + x

    naver_headers = {}
    naver_headers["X-Naver-Client-Id"] = CLIENT_ID
    naver_headers["X-Naver-Client-Secret"] = CLIENT_SECRET_ID
    response = requests.get(url, headers=naver_headers, cookies={})
    rescode = response.status_code

    if(rescode==200):
        response_body = response.text
        return response_body
    else:
        print("Error Code:" + rescode)


def run_naver_search_from_blog(keyword):
    print("run_naver_search_from_blog function")

    fout = open("naver_blog_result_%s.csv" % keyword, "w", encoding="utf=8", newline= "")
    csv_writer = csv.writer(fout)

    for i in range(1, MAX_RESULT, 100):
        a = get_query(keyword, str(i), type="blog")
        b = json.loads(a, encoding="utf-8")

        for x in b["items"]:
            rx = []
            rx.append(remove_html_tag(x["title"]))
            rx.append(x["link"])
            rx.append(x["bloggername"])
            rx.append(x["bloggerlink"])
            rx.append(x["postdate"])
            rx.append(remove_html_tag(x["description"]))

            if x["link"].find("blog.naver.com") >= 0:
                content = get_naver_blog_crawling(x["link"])
            else:
                content = ""
                pass
            rx.append(content)
            csv_writer.writerow(rx)
    fout.close()


def get_naver_blog_crawling(url):
    x = urllib.parse.urlparse(url)
    host_address = "%s://%s/" % (x.scheme, x.netloc)
    url = html.unescape(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.find(id="mainFrame")
    if result is None:
        return False
    else:
        level2_url = result["src"]
        level2_url = urllib.parse.urljoin(host_address, level2_url)
        response = requests.get(level2_url)
        level2_soup = BeautifulSoup(response.text, 'html.parser')
        level2_result = level2_soup.find(id="postListBody")
        if level2_result == None:
            content = ""
        else:
            content = level2_result.get_text("\n")
            content = remove_space(content)
        return content


def run_naver_search_from_news(keyword):
    print("run_naver_search_from_news function")

    fout = open("naver_news_result_%s.csv" % keyword, "w", encoding="utf=8", newline= "")
    csv_writer = csv.writer(fout)

    for i in range(1, MAX_RESULT, 100):
        a = get_query(keyword, str(i), type="news")
        b = json.loads(a, encoding="utf-8")

        for x in b["items"]:
            rx = []
            rx.append(remove_html_tag(x["title"]))
            rx.append(x["link"])
            rx.append(x["originallink"])
            rx.append(remove_html_tag(x["description"]))
            rx.append(x["pubDate"])
            print("link is" + x["link"])

            if x["link"].find("news.naver.com") >= 0:
                (content, comment, comment_nouns) = get_naver_news_crawling(x["link"])
            else:
                content = ""
                comment = ""
                comment_nouns = ""
                pass
            rx.append(content)
            rx.append(comment)
            rx.append(comment_nouns)
            csv_writer.writerow(rx)
    fout.close()


def get_naver_news_crawling(url):
    global DRIVER, BROWSER

    if DRIVER is None:
        DRIVER = webdriver.Chrome(BROWSER)
    DRIVER.get(url)
    time.sleep(2)

    html = DRIVER.page_source
    current_url = DRIVER.current_url

    bs = BeautifulSoup(html, 'html.parser')
    print(current_url)
    if current_url.find("entertain.naver.com") >= 0:
        find_id = "articeBody"
    elif current_url.find("news.naver.com") >= 0:
        find_id = "articleBodyContents"
    else:
        find_id = "none"
    main_result = bs.find(id=find_id)

    if main_result != None:
        for rs in main_result(["script", "style"]):
            rs.decompose()
        main_result_content = remove_space(main_result.get_text("\n"))

        contents = bs.find_all("span", {"class": "u_cbox_contents"})
        comment_result = []

        for i in contents:
            comment_result.append(remove_space(i.get_text("\n")))

        comment_result_string_1 = "\n".join(comment_result)
        comment_result_string_2 = " ".join(comment_result)
        comment_nouns_result_string = get_nouns(comment_result_string_2)
        return (main_result_content, comment_result_string_1, comment_nouns_result_string)
    else:
        return ("",  "",  "")