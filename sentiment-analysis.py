#!/usr/bin/env python3

# import libraries
from textblob import TextBlob

# sentences
sentence = "Hey I'm Good"

# TextBlob in pass parameter
text = TextBlob(sentences)

# Check polarity
plrty = text.sentiment.polarity

# print polarity
print(pltry)

if plrty == 0:
    print("good")
elif plrty > 0:
    print(:"positive sentence")
elif plrty < 0:
    print("bad sentence")        
