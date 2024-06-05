import re

def find_pattern(text):
    # Define the regex pattern: a letter followed by two digits and then a space or end of string
    pattern = r'[A-Z, a-z]\d{2}'
    
    # Find all substrings that match the pattern
    matches = re.findall(pattern, text)
    
    return matches

# Example usage
text = "A12 is a code, but B34 is not the same as C56. Lets see z22 now."
print(find_pattern(text))
