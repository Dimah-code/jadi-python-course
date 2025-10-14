# Exercise: Web Scraping with Python

## Description

In this project, you are going to use the **web scraping** technique to extract information from a website. 
You need to collect information such as **page title, a specific class, and an image** from a web page.

## Objective
Your goal is to extract the following data from a given website (e.g. a bookstore):

- Web page title 
- Information inside a specific class (e.g. book or product title) 
- Image link to the book or product's image(URL)
- Using `requests` and `BeautifulSoup` libraries

## Steps

### 1. Installing prerequisites
```bash
pip install requests beautifulsoup4

### 2. Website connection

Connect to the website using the requests library.

### 3. HTML parsing

Use BeautifulSoup to parse HTML and extract data.

### 4. Extract data

Page's title

Data from the specified class

Image's URL

### 5. Print result

Finally print results

## Input

A URL from the target website

An HTML class for data extraction

## Output

Web page title

List of extracted titles

List of image URLs

## Example Output

```txt
    Title:  دانلود و خرید کتاب صوتی اول عاشق خودت باش
    Author:  مارک رکلاو
    Image URL:  https://img.taaghche.com/audioCover/165476.jpg?w=200
    Category:  موفقیت و خودیاری


## Technologies Used

Python 3

requests

BeautifulSoup (bs4)

## Goal

Understanding HTML structure and extracting information from websites with Python.