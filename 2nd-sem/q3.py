""" 
scrape the wikipedia page for chess. Using for example an Xpath expression, search for the "Rules" section. Create a custom html
with a template for the scraped content
"""

import requests
from bs4 import BeautifulSoup

url = f"https://en.wikipedia.org/wiki/Chess"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser") # parse html content

if response.status_code != 200:
    print(f"Error: Unable to fetch page, status code {response.status_code}")
    
    
rules_heading = soup.find(id="Rules")
content_in_rules = ""
for sibling in rules_heading.find_next_siblings():
        if sibling.name == "h2":  # Stop if we reach the next section
            break
        if sibling.name == "p":
            content_in_rules += str(sibling)
        







