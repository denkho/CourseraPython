def wonder_num():
    for num in range(10, 100):
        if ((num // 10) * (num % 10)) * 2 == num:
            print(num)


wonder_num()
