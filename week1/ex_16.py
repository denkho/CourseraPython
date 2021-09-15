# Электронные часы показывают время в формате h:mm:ss,
# то есть сначала записывается количество часов (число от 0 до 23),
# потом обязательно двузначное количество минут, затем обязательно
# двузначное количество секунд. Количество минут и секунд при
# необходимости дополняются до двузначного числа нулями.
# С начала суток прошло N секунд. Выведите, что покажут часы.

seconds_begin = int(input())
hours = seconds_begin // 3600 % 24
minutes = seconds_begin % 3600 // 60
minutes1 = minutes // 10
minutes2 = minutes % 10
seconds = seconds_begin % 3600 % 60
seconds1 = seconds // 10
seconds2 = seconds % 10
print(hours, str(minutes1) + str(minutes2),
      str(seconds1) + str(seconds2), sep=":")
