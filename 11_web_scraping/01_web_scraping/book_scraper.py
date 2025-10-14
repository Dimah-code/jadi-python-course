# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = "https://taaghche.com/audiobook/165476/%D8%A7%D9%88%D9%84-%D8%B9%D8%A7%D8%B4%D9%82-%D8%AE%D9%88%D8%AF%D8%AA-%D8%A8%D8%A7%D8%B4"
req = requests.get(url)

req.raise_for_status()

soup = BeautifulSoup(req.text, "html.parser")

page_title = soup.select_one("title")
image = soup.select_one("#book-image")
title = soup.select_one(".bookHeader_bookTitleContainer__7Z98p > h1:nth-child(1)")
author = soup.select_one(
    "div.bookHeader_bookInfo__panht:nth-child(1) > span:nth-child(2) > a:nth-child(1) > span:nth-child(1)"
)
category = soup.select_one(".categories_link__aXiRr")

print("Page title: ", page_title.text.strip())
print("Title: ", title.text.strip())
print("Author: ", author.text.strip())
print("Image URL: ", image["src"])
print("Category: ", category.text.strip())
