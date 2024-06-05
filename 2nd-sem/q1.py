import re

def find_pattern(text):
    pattern = r'[A-Z, a-z]\d{2}'
    
    matches = re.findall(pattern, text)
    
    return matches


text = "A12 is a code, but B34 is not the same as C56. Lets see z02 now."
print(find_pattern(text))
