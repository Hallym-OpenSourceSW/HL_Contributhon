## Sorting Algorithm 만들기
## 첫번째 기여자 10점
## 매 성능 향상시 2점
import timeit


def sort(collection):
  """최고의 성능을 가진 정렬 알고리즘을 만들어 보세요 ! """

  if len(collection) <= 1:
    return collection
  pivot = collection[len(collection) // 2]  # 가장 중간에 있는 값 = pivot을 기준으로 비교
  less_arr, equal_arr, bigger_arr = [], [], []
  for num in collection:
    if num < pivot:
      less_arr.append(num)
    elif num > pivot:
      bigger_arr.append(num)
    else:
      equal_arr.append(num)

  collection = sort(less_arr) + equal_arr + sort(bigger_arr)
  return collection


# 메인 함수
collection = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

start = timeit.default_timer()
collection = sort(collection)
stop = timeit.default_timer()
print(stop - start)
print(collection)


# 나의 수행 시간
# 9.784899999999708e-05
