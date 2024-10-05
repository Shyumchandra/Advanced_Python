import re
text="the quick brown fox jumps over the lazy dog"
re_sub=re.sub("dog","cat",text)
print(re_sub)
matches=re.findall("the",text)
print(matches)
match=re.search(r"\b\w*q\w*\b",text)
if match:
    print(match.group())
    
print()

email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
text = "Contact me at example@email.com or info@another.net."

matches = re.findall(email_regex, text)
print(matches)