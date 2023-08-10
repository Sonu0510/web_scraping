from bs4 import BeautifulSoup
import requests

url = "https://www.flipkart.com/clothing-and-accessories/topwear/shirt/men-shirt/formal-shirt/pr?sid=clo,ash,axc,mmk,bk1&otracker=categorytree&otracker=nmenu_sub_Men_0_Formal%20Shirts"
r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, "html.parser")

# To get title of the HTML page
title  =soup.title
# print(title.string)

# Commonly used types of objects in beatifulsoup
# print(type(title.string)) -- Navigable String
# print(type(title)) -- Tag
# print(type(soup)) -- BeautifulSoup
# 4. Comment

# Print all anchor tags
anchor_tags = soup.find_all("a")
# print(anchor_tags)
all_links = set()
# To print all the links in given html page
for link in anchor_tags:
    if(link.get("href") != "#"):
        linkText = link.get("href")
        all_links.add(linkText)
        # print(linkText)

for text in all_links:
    print(text)



# Print all p tags
paragraphs = soup.find_all("p")
# print(paragraphs)


# print(soup.get_text())


# To print first paragraph
# print(soup.find("p"))

# To get text only
# print(soup.find("p").get_text())

# To print all the paragraph with given class name
# print(soup.find_all("p", class_="_2-N8zT"))




