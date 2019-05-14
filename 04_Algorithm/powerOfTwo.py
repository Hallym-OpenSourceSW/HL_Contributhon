"""
주어진 수가 2의 n승으로 표현되는지 체크하는 함수를 만들어 보세요.

첫번째 기여자: 10점
성능 향상 기여자: 5점
"""

def digitNum(XInput):
    YOutput = 0
    while XInput:
        XInput &= (XInput-1)
        YOutput += 1
    return YOutput
  

N = int(input('N = '))

if (digitNum(N) == 1) :
  print('OK')
else :
  print('NOK')
