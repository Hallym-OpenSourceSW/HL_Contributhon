    
def average(nums):
    sum = 0
    i = 0
    for n in nums:
      sum += n
      i += 1
    avg = sum / i
    print(avg)

# 평균값은 22.857142857142858 이여야 함.
average([2, 4, 6, 8, 20, 50, 70]) 

