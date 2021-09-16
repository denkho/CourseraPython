fin = open('input.txt', 'r')

number_of_pairs = int(fin.readline())
word_pairs = dict()

for _ in range(number_of_pairs):
    pair = fin.readline().split()
    word_pairs[pair[0]] = pair[1]

word_to_find = fin.readline()

if word_to_find in word_pairs:
    print(word_pairs[word_to_find])
else:
    for word in word_pairs:
        if word_pairs[word] == word_to_find:
            print(word_pairs[word])

fin.close()
