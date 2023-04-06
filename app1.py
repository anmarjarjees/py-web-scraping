# Import the requests library:
"""
NOTE: 
If you get the error: "requests" could not be resolved from source Pylance"
From Select the Interpreter (you can click it from the VS Code status bar)
> Make sure to select the recommended settings for the current VENV Interpreter
> Don't select the global python interpreter
"""
import requests 
from bs4 import BeautifulSoup
# Link: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# Link to the website to scrape:
"""
Some websites might not allow you to grab their info:
and you will see this error for example:
<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>Microsoft-Azure-Application-Gateway/v2</center>
</body>
</html>
"""
# url = "https://www.heartandstroke.ca/healthy-living"
url = "https://www.health.harvard.edu/blog"
# url = "https://www.pluralsight.com/blog/technology"
# url = "https://www.freecodecamp.org/news/"
"""
Creating a requests object:
.get() function => Sends a GET request and return a "Response" object
"""
# using "res" or "response" by convention
res = requests.get(url)
# Link: https://docs.python-requests.org/en/latest/user/quickstart/#response-content


# test: check if we can get a response from this website:
# https://www.health.harvard.edu/blog
# print(res) 
# <Response [200]>
# 200 OK => The request succeeded


# test: check if we can get a response from this website:
# https://www.heartandstroke.ca/healthy-living
# <Response [403]>
# 403 Forbidden => The client does not have access rights to the content; 

# Link: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

"""
Q) How to see the page code and contents?
A) Using res.text
print(res.text)
will print all the HTML code
"""

# Using BeautifulSoup to parse the data:
# https://beautiful-soup-4.readthedocs.io/en/latest/#troubleshooting
# Constructor Constructor
"""
Examples:
> BeautifulSoup(html_doc, 'html.parser')
> BeautifulSoup(res.content, 'html.parser')
> BeautifulSoup(res.text, 'lxml') <=> we need to pip install lxml if we want to use it (next example)

NOTE:
Lxml is recommended for large or complex HTML documents, it has better performance regarding the speed of parsing. 
HTML Parser is good for small projects when processing a small amount of data, it's considered to be easy to use.
"""
soup = BeautifulSoup(res.content, 'html.parser')

# testing the type of "soup" variable:
print(type(soup)) # <class 'bs4.BeautifulSoup'>

# print(soup) # print the page in a formatted HTML page

"""
IMPORTANT NOTE TO RECAP:

Remember that we used this import statement:
> from bs4 import BeautifulSoup

So we can access the class "BeautifulSoup" immediately:
> BeautifulSoup(res.content, 'html.parser')

If we use this import statement:
import bs4

So we can access the class "BeautifulSoup" by specifying the module "bs4":
> bs4.BeautifulSoup(res.content, 'html.parser')

for more information, you can review my lecture about "Modules and Packages":
Link: https://github.com/anmarjarjees/python-modules-packages
"""


"""
Website Inspection:
- We will be focusing on the contents within the body tag
- We need to right click the website and inspect its contents (HTML elements and attributes)
- Point to the section of the content that you want to grab (will be highlighted when hovering)
- Get every instance (element) of the wanted part

"""
# using prettify() method: Pretty-print this PageElement as a string.
# print(soup.prettify()) # print the page in a good formatted HTML page

# try the soup methods:
"""
soup.title
# <title>The Dormouse's story</title>

soup.title.name
# u'title'

soup.title.string
# u'The Dormouse's story'

soup.title.parent.name
# u'head'

soup.p
# <p class="title"><b>The Dormouse's story</b></p>
"""

# print(soup.title)
# <title> Harvard Health Blog - Live a Healthier Lifestyle - Harvard Health</title>

# print(soup.title.name) # return the name of the tag/element (without its content) => title

# print(soup.title.parent.name) # return the parent element name of the "title" => head

# print(soup.title.parent) # return the full parent element of the "title" => head and all its contents


# More practice:
# **************
"""
Inspect the HTML contents:
.find() method: Look in the children of this PageElement and find the "first" PageElement that matches the given criteria.

.find_all() method: Look in the children of this PageElement and find "all" PageElements that match the given criteria.
"""
# getting the headings of the blogs 
heading = soup.find('h2', class_='text-2xl')
# print(heading)
# will return the first title in the page:
"""
<h2 class="text-2xl font-bold mb-1 leading-tight mt-2 group-hover:text-red group-focus:text-red transition-colors duration-200">Prostate cancer in transgender women</h2>
"""

# printing the text/content of the h2 element:
# print(heading.text)
# Prostate cancer in transgender women

headings = soup.find_all('h2', class_='text-2xl')
# print(headings)
# Will return a list of all the heading2 with class "text-2xl" in the page:
"""
[
    <h2 class="text-2xl font-bold mb-1 leading-tight mt-2 group-hover:text-red group-focus:text-red transition-colors duration-200">Prostate cancer in transgender women</h2>,

    <h2 class="text-2xl font-bold mb-1 leading-tight mt-2 group-hover:text-red group-focus:text-red transition-colors duration-200">Why eat lower on the seafood chain?</h2>,

    <h2 class="text-2xl font-bold mb-1 leading-tight mt-2 group-hover:text-red group-focus:text-red transition-colors duration-200">Can long COVID affect the gut?</h2>, 

    <h2 class="text-2xl font-bold mb-1 leading-tight mt-2 group-hover:text-red group-focus:text-red transition-colors duration-200">When replenishing fluids, does milk beat water?</h2>,

    and so on...
]
"""

# trying to print the headings text only:
# print(headings.text)
"""
AttributeError: ResultSet object has no attribute 'text'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?
"""
# Solution: using for in loop:
# print("Main Headings:")
# for heading in headings:
#     print (heading.text)
"""
Prostate cancer in transgender women
Why eat lower on the seafood chain?
Can long COVID affect the gut?
When replenishing fluids, does milk beat water?
Safe, joyful movement for people of all weights
Slowing down racing thoughts
and so on...
"""

"""
Going down: 
Tags may contain strings and other tags. These elements are the tag’s children. 
Link: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#going-down

In this page, we have the p elements for each article inside a "div" element of class="prose"
Link: https://www.geeksforgeeks.org/beautifulsoup-find-all-children-of-an-element/
"""

# div = soup.find('div', {'class': 'prose'})
# children = div.findChildren('p')
"""
<p>The increasing size and visibility of the transgender population has implications for public health. Hormone treatment given to transgender women lowers the overall risk of prostate cancer, but the risk of a trans woman developing the disease is not zero.</p>
"""
# print(children)
"""
[<p>The increasing size and visibility of the transgender population has implications for public health. Hormone treatment given to transgender women lowers the overall risk of prostate cancer, but the risk of a trans woman developing the disease is not zero.</p>]
"""

# for child in children:
#     print(child)
"""
<p>The increasing size and visibility of the transgender population has implications for public health. Hormone treatment given to transgender women lowers the overall risk of prostate cancer, but the risk of a trans woman developing the disease is not zero.</p>
"""

"""
Other Methods:
Here are the methods we would be taking a look at:

findChild
findChildren
contents
children
descendants
"""

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#contents-and-children
div_list = soup.find_all('div', {'class': 'prose'})
# for div in div_list:
#     print (div)
"""
<div class="prose mt-4">
    <p>
    The increasing size and visibility of the transgender population has implications for public health. Hormone treatment given to transgender women lowers the overall risk of prostate cancer, but the risk of a trans woman developing the disease is not zero.
    </p>
</div>  

<div class="prose mt-4">
    <p>
    Cutting back on red meat and replacing it with poultry or seafood is a good choice because those are healthier sources of protein — and better for the environment. Choosing seafood that is lower on the food chain can amplify those benefits.
    </p>
</div>

and so on for the rest of the divs...
"""

# for div in div_list:
#     print (div.findChild('p'))
"""
Printing the child full p element of each div:
<p>
The increasing size and visibility of the transgender population has implications for public health. Hormone treatment given to transgender women lowers the overall risk of prostate cancer, but the risk of a trans woman developing the disease is not zero.
</p>

<p>
Cutting back on red meat and replacing it with poultry or seafood is a good choice because those are healthier sources of protein — and better for the environment. Choosing seafood that is lower on the food chain can amplify those benefits.
</p>

<p>
By now millions of people around the world have been infected with the virus that causes COVID-19. Some of them have experienced lingering effects like low energy and brain fog; could gastrointestinal problems be another aftereffect of the virus?
</p>
"""

# Link: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#string


"""
Working with select():
https://www.crummy.com/software/BeautifulSoup/bs4/doc/#history-of-css-selector-support
"""
p_list = soup.select('div.prose p')
print(type(p_list)) # <class 'bs4.element.ResultSet'>

"""
The code below will output all the full p elements:
"""
# for p in p_list:
    # print (p)

# ******************
# for p in p_list:
#     print (p.contents)
"""
['The increasing size and visibility of the transgender population has implications for public health. Hormone treatment given to transgender women lowers the overall risk of prostate cancer, but the risk of a trans woman developing the disease is not zero.']

['Cutting back on red meat and replacing it with poultry or seafood is a good choice because those are healthier sources of protein — and better for the environment. Choosing seafood that is lower on the food chain can amplify those benefits.']
"""


# **********************
"""
The code below for returning the text inside the list
"""
# for p in p_list:
#     print (p.contents[0])
"""
The increasing size and visibility of the transgender population has implications for public health. Hormone treatment given to transgender women lowers the overall risk of prostate cancer, but the risk of a trans woman developing the disease is not zero.

Cutting back on red meat and replacing it with poultry or seafood is a good choice because those are healthier sources of protein — and better for 
the environment. Choosing seafood that is lower on the food chain can amplify those benefits.
"""

# **********************
# Or even much much easier! :-) :-)
for p in p_list:
    print ("\n"+p.text)
"""
This will output only the text inside the p element:
The increasing size and visibility of the transgender population has implications for public health. Hormone treatment given to transgender women lowers the overall risk of prostate cancer, but the risk of a trans woman developing the disease is not zero.

Cutting back on red meat and replacing it with poultry or seafood is a good choice because those are healthier sources of protein — and better for 
the environment. Choosing seafood that is lower on the food chain can amplify those benefits.
"""