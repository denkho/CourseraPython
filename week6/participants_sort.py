'''
Известно, что фамилии всех участников — различны. 
Сохраните в массивах список всех участников и выведите его, 
отсортировав по фамилии в лексикографическом порядке. При 
выводе указываете фамилию, имя участника и его балл.

Используйте для ввода и вывода файлы input_pass_grade.txt и output.txt
с указанием кодировки utf8. Например, для чтения откройте 
файл с помощью open('input_pass_grade.txt', 'r', encoding='utf8').
'''

participants_list = list()

with open('input_participatns_sort.txt', 'r', encoding='utf-8') as data_file:
    for line in data_file:
        line = line.split()
        participants_list.append([line[0], line[1], line[3]])

participants_list.sort()

with open('output_participatns_sort.txt', 'w', encoding='utf-8') as data_file:
    for line in participants_list:
        line = ' '.join(line)
        data_file.write(line)
        data_file.write('\n')
