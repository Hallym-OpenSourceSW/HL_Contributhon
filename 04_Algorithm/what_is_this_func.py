"""
다음 기술된 함수가 주어진 정수형 변수 XInput에 대해서 시행하는 기능은 무엇인가?
"""

def whatisThisFunction(XInput):
    YOutput = 0
    while XInput:
        XInput &= (XInput-1)
        YOutput += 1
    return YOutput


# 답: 2의 배수인지 확인(2의 배수일 경우 1을 반환)
