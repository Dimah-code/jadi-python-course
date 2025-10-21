# Exercise: Web Scraping with Python

## Description

In this project, you are going to use the **web scraping** technique to extract information from a website. 
You need to collect information such as **page title, a specific class, and an image** from a web page.

## Your Goal:

Your goal is to extract the following data from a given website (e.g. a bookstore):

- Web page title 
- Information inside a specific class (e.g. book or product title) 
- Image link to the book or product's image(URL)
- Using `requests` and `BeautifulSoup` libraries

## Steps

### 1. Installing prerequisites
```bash
    pip install requests beautifulsoup4
```

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
    Page Title: Products – ScrapeMe

    Titles:

    - Bulbasaur 

    - Ivysaur 

    - Venusaur 

    - Charmander 

    - Charmeleon 

    - Charizard 

    - Squirtle 

    - Wartortle 

    - Blastoise 

    - Caterpie 

    - Metapod 

    - Butterfree 

    - Weedle 

    - Kakuna 

    - Beedrill 

    - Pidgey 


    Image URLs:

    - https://scrapeme.live/wp-content/uploads/2018/08/001-350x350.png 

    - https://scrapeme.live/wp-content/uploads/2018/08/002-350x350.png 

    - https://scrapeme.live/wp-content/uploads/2018/08/003-350x350.png 

    - https://scrapeme.live/wp-content/uploads/2018/08/004-350x350.png 

    - https://scrapeme.live/wp-content/uploads/2018/08/005-350x350.png 

    - https://scrapeme.live/wp-content/uploads/2018/08/006-350x350.png 

    - https://scrapeme.live/wp-content/uploads/2018/08/007-350x350.png 

    - https://scrapeme.live/wp-content/uploads/2018/08/008-350x350.png 

    - https://scrapeme.live/wp-content/uploads/2018/08/009-350x350.png 

    - https://scrapeme.live/wp-content/uploads/2018/08/010-350x350.png 

    - https://scrapeme.live/wp-content/uploads/2018/08/011-350x350.png 

    - https://scrapeme.live/wp-content/uploads/2018/08/012-350x350.png 

    - https://scrapeme.live/wp-content/uploads/2018/08/013-350x350.png 

    - https://scrapeme.live/wp-content/uploads/2018/08/014-350x350.png 

    - https://scrapeme.live/wp-content/uploads/2018/08/015-350x350.png 

    - https://scrapeme.live/wp-content/uploads/2018/08/016-350x350.png 

```

## Technologies Used

Python 3

requests

BeautifulSoup (bs4)

## Goal

Understanding HTML structure and extracting information from websites with Python.