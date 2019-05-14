"""
주어진 수가 2의 n승으로 표현되는지 체크하는 함수를 만들어 보세요.

첫번째 기여자: 10점
성능 향상 기여자: 5점
"""

def check_bin(i):
  if i <= 0:
    return False
  while i > 2:
    r = i % 2
    if r == 1:
      return False
    i = i / 2
  return True

def check_test():
  for i in range(0,100):
    print(i, check_bin(i)) 

check_test()
