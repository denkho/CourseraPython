'''
Во входном файле (вы можете читать данные из sys.stdin, подключив библиотеку sys) записан текст.
Словом считается последовательность непробельных символов идущих подряд, слова разделены одним
или большим числом пробелов или символами конца строки. Определите, сколько различных слов
содержится в этом тексте.
Формат ввода
Вводится текст.
Формат вывода
Выведите ответ на задачу.
'''

def count_number_words():
    f = open('02_input.txt', 'r')
    text = f.readlines()
    f.close()
    words = set()

    for line in text:
        line = line.strip().split()
        for word in line:
            words.add(word)

    out = open('output.txt', 'w')
    out.write(str(len(words)))
    out.close()

count_number_words()
