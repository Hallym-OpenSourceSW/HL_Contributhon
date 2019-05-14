## Searching Algorithm 만들기
## 첫번째 기여자 10점
## 매 성능 향상시 2점
import timeit


def search(collection, key):
  # collection: Array 데이터
  # key: 찾고자하는 값
  
    """최고의 성능을 가진 탐색 알고리즘을 만들어 보세요 ! """
  

    
    if key in collection:
        index = key
    else :
        index=-1
    return index  # 찾고자하는 값이 array에 있을때 array의 index를 반환, array에 찾고자하는 값이 없다면 -1 반환


# 메인 함수
collection = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
key = 22

start = timeit.default_timer()
index = search(collection, key)
stop = timeit.default_timer()
print(stop - start)
print(index)


# 나의 수행 시간
# 1.1947000000012142e-05
