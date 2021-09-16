number_of_pairs = int(input())
word_pairs = dict()

for _ in range(number_of_pairs):
    pair = input().split()
    word_pairs[pair[0]] = pair[1]

word_to_find = input()
answer = ''

for key, value in word_pairs.items():
    if word_to_find == key:
        answer = value
        break
    elif word_to_find == value:
        answer = key
        break

print(answer)
