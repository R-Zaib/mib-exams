"""
def wrap_content_in_html(title, header, content, output_file):

    # Create the HTML structure
    html_content = f"""
    <html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        <h1>{header}</h1>
        <p>{content}</p>
    </body>
    </html>
    """

    # Save the content to an HTML file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_content)

    print(f"Content saved to {output_file}")

# Example usage
title = "Sample Page"
header = "Welcome to the Sample Page"
content = "This is an example of wrapping content in HTML and saving it to a file."
output_file = "sample_page.html"
wrap_content_in_html(title, header, content, output_file)

"""