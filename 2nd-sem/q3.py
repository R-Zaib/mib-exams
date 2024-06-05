from bs4 import BeautifulSoup
import requests

def scrape_recipes(section_title):

    url = f"wikipedia_url"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser") # parse html content

    if response.status_code != 200:
        return f"Error: Unable to fetch page, status code {response.status_code}"
    
    header = soup.find(id=section_title.replace(" ", "_"))
    
    content = []
    for sibling in header.find_next_siblings():
        if sibling.name == "h2":  # Stop if we reach the next section
            break
        content.append(str(sibling))
    # abc = soup.find_all("a", class_="block md:hover:opacity")

    section_content = "\n".join(content)
    
    return section_content



# url =
section_title = "Techniques"
section_content = scrape_wikipedia_section(url, section_title)

print(section_content)




""" 

# Wrap content in basic HTML structure
    html_content = f"""
    <html>
    <head>
        <title>{section_title}</title>
    </head>
    <body>
        <h1>{section_title}</h1>
        {section_content}
    </body>
    </html>
    """

    # Save the content to an HTML file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_content)

    print(f"Content saved to {output_file}")
    
"""