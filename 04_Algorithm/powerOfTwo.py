"""
주어진 수가 2의 n승으로 표현되는지 체크하는 함수를 만들어 보세요.

첫번째 기여자: 10점
성능 향상 기여자: 5점
"""

def powerOfTwo(n):
    while n % 2 == 0:
        n = n / 2
    return n == 1


## for testing
print(powerOfTwo(2))
print(powerOfTwo(4))
print(powerOfTwo(64))
print(powerOfTwo(512))
print(powerOfTwo(1023))

"""
주어진 수가 2의 n승으로 표현되는지 체크하는 함수를 만들어 보세요.
첫번째 기여자: 10점
성능 향상 기여자: 5점
"""

def powerOfTwo(n):
    cnt=0
    while n % 2 == 0:
        n = n / 2
        cnt+=1;
    return cnt


## for testing
print(powerOfTwo(2))
print(powerOfTwo(4))
print(powerOfTwo(64))
print(powerOfTwo(512))
print(powerOfTwo(1023))
