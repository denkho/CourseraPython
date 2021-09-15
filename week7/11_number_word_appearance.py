with open('input_word_appearance.txt', 'r') as f:
    text = f.readlines()
    text_list = list()
    for line in text:
        text_list.extend(line.split())

count_dict = dict()

for i in range(len(text_list)):
    if text_list[i] not in count_dict:
        count_dict[text_list[i]] = 0
        print(0, end=' ')
    else:
        count_dict[text_list[i]] += 1
        print(count_dict[text_list[i]], end=' ')
