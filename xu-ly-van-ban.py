import re

# a = "Sentence  with     weird    whitespaces"
# a = re.sub(' +', ' ', a)
# print(a)
text = [""]
while True:
    try:
        str = input()
        text[len(text)] = str
    except EOFError:
        break
print(text)
