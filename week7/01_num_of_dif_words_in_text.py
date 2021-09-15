f = open('input_num_of_dif_words.txt', 'r')
text = f.readlines()
words = set()

for line in text:
    line = line.split()
    for word in line:
        words.add(word)

out = open('output.txt', 'w')
out.write(str(len(words)))

out.close()
f.close()
