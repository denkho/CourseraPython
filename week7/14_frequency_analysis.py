fin = open('input_frequency_analysis.txt', 'r')
text = fin.read().split()

answer = dict()

for word in text:
    answer[word] = answer.get(word, 1) + 1

sorted_answer = sorted(answer.items(), key=lambda i: (-i[1], i[0]))

for word in sorted_answer:
    print(word[0])

fin.close()
