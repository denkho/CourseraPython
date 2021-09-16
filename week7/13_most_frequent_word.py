fin = open('input.txt', 'r')

text = fin.readlines()
words = list()

for line in text:
    words.extend(line.split())

count_words = dict()

for word in words:
    count_words[word] = count_words.get(word, 0) + 1

print(sorted(count_words, key=lambda x: (-count_words[x], x))[0])

fin.close()
