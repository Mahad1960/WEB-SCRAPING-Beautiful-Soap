# FOR INSTALLATION : pip install requests-html.
# from requests_html import HTMLSession
# But bs4 is much better than requests_html.
from bs4 import BeautifulSoup
with open("PRACTICE FILE.html","r") as f:
    html=f.read()
soup=BeautifulSoup(html,"html.parser")
# print(soup.prettify())                  # It prettifies your code.
# print("TITLE:",soup.title)              # It tells you the title of your code.
# print("TITLE TEXT:",soup.title.text)    # It tells you the text of your title.
# print("1st PARAGRAPH:",soup.p)          # It tells you the 1st paragraph "<p> tag".
# print("CLASS ATTRIBUTE OF 1st PARAGRAPH:",soup.p["class"])  # Access class attribute of 1st paragraph.
# print("1st LINK:",soup.a)               # It returns the first link "<a> tag" found in the HTML document.
# print("All LINKS:",soup.find_all("a"))  # It returns all links "<a> tag" found in the HTML document.
# print(soup.find(id="3057"))             # Returns a list of all matching elements.
# for link in soup.find_all("a"):
#     print(link.get("href"))   # Fetches the value of the href attribute (i.e., the URL) & prints the URL to the console.
