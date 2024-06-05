import re

def find_pattern_finditer(text):
    pattern = r'[A-Za-z]\d{2}' #raw string
    matches = re.finditer(pattern, text)
    
    result = [match.group() for match in matches]
    
    return result


text = "A12 is a code, but B34 is not the same as C56."
print(find_pattern(text))



#finall
def find_pattern_findall(text):
    pattern = r'[A-Za-z]\d{2}(?=\s|$)'
    return re.findall(pattern, text)

text = "A12 is a code, but B34 is not the same as C56."
print(find_pattern_findall(text))  # ['A12', 'B34', 'C56']



def find_pattern_compile(text):
    pattern = re.compile(r'[A-Za-z]\d{2}')
    return pattern.findall(text)

text = "A12 is a code, but B34 is not the same as C56."
print(find_pattern_compile(text))  # ['A12', 'B34', 'C56']
