# Пирожок в столовой стоит A рублей и B копеек. Определите, сколько рублей и копеек нужно заплатить за N пирожков.
# Формат ввода
# Программа получает на вход три числа: A, B, N —  целые, неотрицательные, не превышают 10000.
# Формат вывода
# Программа должна вывести два числа: стоимость покупки в рублях и копейках.

roubles = int(input())
kopecks = int(input())
number_of_pies = int(input())

kopecks_all = roubles * 100 + kopecks
price_in_kopecks = kopecks_all * number_of_pies

print(price_in_kopecks // 100, price_in_kopecks % 100)
