# Program 1: Check if a string has only octal digits
import re

strings = ['789', '123', '004']
for s in strings:
	if re.fullmatch(r'[0-7]+', s):
		print(f"{s} contains only octal digits.")
	else:
		print(f"{s} does NOT contain only octal digits.")

# Program 2: Extract user id, domain name and suffix from email addresses
emails = [
	'zuck@facebook.com',
	'sunder33@goog1e.com',
	'jeff42@amazon.com'
]
for email in emails:
	match = re.match(r'([\w\d]+)@([\w\d]+)\.([\w]+)', email)
	if match:
		print(match.groups())

# Program 3: Split an irregular sentence into proper words
sentence = 'A, very very; irregular sentence'
words = re.split(r'[;,. ]+', sentence)
words = [w for w in words if w]
print(words)

# Program 4: Clean up tweet to contain only user's message
tweet = "Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/1bwejØpxOd cc: @garybernhardt #rstats"
tweet_clean = re.sub(r'RT|cc:|http\S+|@\w+|#\w+|[!.,:;]', '', tweet)
tweet_clean = re.sub(r'\s+', ' ', tweet_clean).strip()
print(tweet_clean)

# Program 5: Extract all text portions between tags from HTML page
import requests
url = "https://raw.githubusercontent.com/selva86/datasets/master/sample.html"
r = requests.get(url)
html = r.text
texts = re.findall(r'>\s*([^<>]+?)\s*<', html)
texts = [t.strip() for t in texts if t.strip()]
print(texts)

# Program 6: Identify words that begin and end with the same character
words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'as']
for word in words:
	if re.match(r'^(.).+\1$', word) or re.match(r'^(.{1})$', word):
		print(word)
