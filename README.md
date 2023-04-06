# Py-Web-Scraping
Quick demo about using **Web Scraping with Python**.

# Instructions for running this repo locally:
1. Download the all the files into a single folder with any name you prefer:
    - app1.py
    - app2.py
    - requirements.txt
2. Create a virtual environment (venv)
    - python3 -m venv "venv_name"
3. Activate your virtual environment
    - venv_name\Scripts\activate
4. pip install requirements.txt
5. If you want to deactivate the virtual environment when you are done
    - deactivate

---
NOTE: If you need any help or refreshment in using "Virtual Environment" and "pip install" commands, you can check my repo ["python-modules-packages"](https://github.com/anmarjarjees/python-modules-packages)
---

# Web Scraping:
Is one of the way to be used for collecting data online. Getting (scraping) data from a website, like getting the data about the headings, the posts in a web page. For example going to a news website and getting the data about head news, the market, the weather, etc...

Web Scraping Can be used by Search Engines to get a data from a website to analyze its contents and what types of information it has. Or getting some data to be used. Notice that some websites allow web scraping and some don't. 

## Web Scraping Steps:
The main steps for "Web Scraping":
1. GET => Sending a request (get query) to a website with get query
    -  This request will return an HTML document that contains all the information in that website
2. Parsing => Parsing the returned HTML document, by extracting the wanted content and ignore the rest
3. Extracting => Extracting the wanted data by isolating them from the website and save/store it in any format we prefer

## Libraries for Web Scraping 
Python has various types of libraries that can be used for different purposes, with Web Scraping, we have different libraries:
- Selenium
- Requests
- BeautifulSoup
- Pandas
- lxml

### Web Scraping Libraries to be used:
For a basic understanding of a web scraping, we can use:
- Requests => the basic initial library to make an HTTP request to a website which is creating the GET query
    - [Requests: HTTP for Humans](https://requests.readthedocs.io/en/latest/)
    - [requests 2.28.2](https://pypi.org/project/requests/)
- lxml => for processing HTML and XML, is a Pythonic binding for the C libraries libxml2 and libxsl. It is unique in that it combines the speed and XML feature completeness of these libraries with the simplicity of a native Python API
    - [lxml - XML and HTML with Python](https://lxml.de/)
    - [lxml 4.9.2](https://pypi.org/project/lxml/)
- BeautifulSoup => the major one to generate a readable HTML document
    - [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    - [beautifulsoup4 4.11.2](https://pypi.org/project/beautifulsoup4/)

After receiving the package, we can decide whether to save it as CSV or as an HTML for example.

# The initial steps for preparing the project:
1. First, install and activate the virtual library
2. Then, install the required libraries
3. Finally, start coding

## Prepare your environment:
As we discussed before, it will be a good practice to create a virtual environment, then install and run the required packages inside it. For more details and explanations refer to the read me fie for this repo ["Python Modules and Packages"](https://github.com/anmarjarjees/python-modules-packages).

> python -m venv ws_env

The virtual library is named "ws_env"

## Install the required libraries:
1. Installing ["requests"](https://pypi.org/project/requests/) library for GET query (HTTP Request):
    > pip install requests

2. Installing ["lxml"](https://pypi.org/project/lxml/) library for processing the HTML contents
    > pip install lxml

3. Installing ["beautifulsoup4"](https://pypi.org/project/beautifulsoup4/) for scraping information from web pages by creating a parsed and navigable HTML document
    > pip install beautifulsoup4

### Notes to review:
- To activate your VENV:
    > <VENV_NAME>\Scripts\activate
- You can run this command to list the custom installed packages:
    > pip freeze
- You can run this command to list the default installed packages + the custom ones:
    > pip list

## Coding:
1- Importing the "requests" and "bs4"
2- Requesting for a website
3- Using BS to parse the received content
4- Continue the rest by reading the code file

# Before Coding:
- Install and activate the virtual environment:
- Install the required pancakes

|***:computer: Code Files***|
|:---:|
|***1- Code File: app1.py***|
|***2- Code File: app2.py***|

