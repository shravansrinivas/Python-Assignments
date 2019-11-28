words=["party","com"]
import re
text="lets go to party"
print(text.split(" "))
for word in words:
    if word in text.split():
        text=text.replace(word,"***")
print(text)