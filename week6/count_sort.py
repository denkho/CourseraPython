def count_sort(n: list):
    cnt_nums = [0] * 101

    for num in nums:
        cnt_nums[num] += 1

    result = ''
    for num in range(101):
        result += (str(num) + ' ') * cnt_nums[num]
    return result


nums = list(map(int, input().split()))
print(count_sort(nums))
