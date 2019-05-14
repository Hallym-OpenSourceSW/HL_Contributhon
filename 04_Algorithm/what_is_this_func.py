"""
다음 기술된 함수가 주어진 정수형 변수 XInput에 대해서 시행하는 기능은 무엇인가?
"""

def whatisThisFunction(XInput):
    YOutput = 0
    while XInput:
        XInput &= (XInput-1)
        YOutput += 1
    return YOutput


# 답: XInput의 나누어지는 숫자의 갯수의 갯수를 구하는 함수(소수 판별기)

