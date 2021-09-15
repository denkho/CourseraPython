number_towns = int(input())
distance_towns = list(map(int, input().split()))
number_shelters = int(input())
distance_shelters = list(map(int, input().split()))

towns = list()
shelters = list()
result_distance = list()

for i in range(len(distance_towns)):
    towns.append((distance_towns[i], i + 1))
towns.sort()

for i in range(len(distance_shelters)):
    shelters.append((distance_shelters[i], i + 1))
shelters.sort()

i, j = 0, 0
while i < len(towns) and j < len(shelters) - 1:
    if abs(towns[i][0] - shelters[j][0]) < \
            abs(towns[i][0] - shelters[j + 1][0]):
        result_distance.append((towns[i][1], shelters[j][1]))
        i += 1
    else:
        j += 1

while i < len(towns):
    result_distance.append((towns[i][1], shelters[j][1]))
    i += 1

result_distance.sort()
for i in range(len(result_distance)):
    print(result_distance[i][1], end=" ")

# решение не проходит по времени
# i = 0
# while i < len(towns):
#     j = 0
#     min_dist = abs(towns[i][0] - shelters[j][0])
#     result_distance.append(shelters[j][1])
#     while j < len(shelters):
#         next_dist = abs(towns[i][0] - shelters[j][0])
#         if min_dist >= next_dist:
#             min_dist = next_dist
#             result_distance.pop()
#             result_distance.append(shelters[j][1])
#         j += 1
#     i += 1
