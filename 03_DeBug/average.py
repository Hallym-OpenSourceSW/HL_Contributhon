def average(nums):
    sum = 0
    n = 0
    for i in nums:
      sum += i
      n += 1

    avg = sum / n
    print(avg)

# 평균값은 22.857142857142858 이여야 함.
average([2, 4, 6, 8, 20, 50, 70]) 
