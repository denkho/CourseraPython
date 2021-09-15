import sys

text = sys.stdin.read()
text = list(text.split())
print(len(set(text)))
