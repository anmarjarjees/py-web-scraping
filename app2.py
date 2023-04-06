# importing the required libraries:
import requests 
from bs4 import BeautifulSoup

# url = 'https://www.brainyquote.com/topics/motivational-quotes'
url = 'https://www.goodreads.com/quotes'
# Inspect the website content:

# Creating a request to get a response:
response = requests.get(url)

# parsing the HTML document: beautifulSoup and lxml
soup = BeautifulSoup(response.content, 'lxml') # using lxml parser

# testing
# print(soup) # ok

# Starting with parsing/getting the specific data from the website:
"""
copied element from the inspection window:

<div class="quoteText">
      “Be yourself; everyone else is already taken.”
  <br>  ―
  <span class="authorOrTitle">
    Oscar Wilde
  </span>
</div>
"""

quotes = soup.find_all('div', class_='quoteText')
# if no match => returns and empty list  []

# test:
# print(quotes)

# Getting only the text contents:
# for quote in quotes:
#     print(quote.text)

"""
OUTPUT:
the text (quote) + "-" + the author name
:-(
"""

# Getting the authors names only:
authors = soup.find_all('span', class_='authorOrTitle')

# print their names:
# for author in authors:
#     print(author.text)

# print the quote with the author name (Yes, it's already printed)!
# for i in range(0, len(quotes)):
#     print ("Full Contents: " + quotes[i].text)
#     print ("Author: " + authors[i].text)

# grabbing the tags
"""
NOTE:
Each Quote has different number of tags, so it's hard to determine the end of each quote tags:
Copied Element:

<div class="greyText smallText left">
     tags:
       <a href="/quotes/tag/attributed-no-source">attributed-no-source</a>,
       <a href="/quotes/tag/be-yourself">be-yourself</a>,
       <a href="/quotes/tag/gilbert-perreira">gilbert-perreira</a>,
       <a href="/quotes/tag/honesty">honesty</a>,
       <a href="/quotes/tag/inspirational">inspirational</a>,
       <a href="/quotes/tag/misattributed-oscar-wilde">misattributed-oscar-wilde</a>,
       <a href="/quotes/tag/quote-investigator">quote-investigator</a>
</div>
"""
div_tags = soup.find_all('div',class_='greyText')


# for tag_div in div_tags:
#     print (tag_div.find_all('a'))
"""
OUTPUT:
[
    <a href="/quotes/tag/attributed-no-source">attributed-no-source</a>, 
    <a href="/quotes/tag/be-yourself">be-yourself</a>, 
    <a href="/quotes/tag/gilbert-perreira">gilbert-perreira</a>, 
    <a href="/quotes/tag/honesty">honesty</a>, 
    <a href="/quotes/tag/inspirational">inspirational</a>, 
    <a href="/quotes/tag/misattributed-oscar-wilde">misattributed-oscar-wilde</a>, 
    <a href="/quotes/tag/quote-investigator">quote-investigator</a>
]

[
    <a href="/quotes/tag/attributed-no-source">attributed-no-source</a>, 
    <a href="/quotes/tag/best">best</a>,
    <a href="/quotes/tag/life">life</a>, 
    <a href="/quotes/tag/love">love</a>, 
    <a href="/quotes/tag/misattributed-marilyn-monroe">misattributed-marilyn-monroe</a>, 
    <a href="/quotes/tag/mistakes">mistakes</a>, 
    <a href="/quotes/tag/out-of-control">out-of-control</a>, 
    <a href="/quotes/tag/truth">truth</a>, <a href="/quotes/tag/worst">worst</a>
]
"""

# Advanced loops#1: for printing the related tags for each quote:
# for tag_div in div_tags:
#     a_list = tag_div.find_all('a')
#     for tag in a_list:
#         print (tag.text)


# Advanced loops for printing the quotes with their related tags:
for i in range(0, len(quotes)):
    print ("Full Contents: " + quotes[i].text)
    print ("Author: " + authors[i].text)
    # div_tags = soup.find_all('div',class_='greyText') # (NOT HELPFUL IN THIS LOOP)
    # quote_tags_list = div_tags[i]
    # print (quote_tags_list)
    # # for quote_tag in quote_tags_list:
    # #      print ("Tags: " + authors[i].text) 
    print("*******")