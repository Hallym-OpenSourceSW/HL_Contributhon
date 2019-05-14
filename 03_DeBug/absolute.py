# 절대값을 찾는 함수 구현 및 테스트입니다. 어디가 잘못된 걸까요 ?

def absVal(num)
    """
    Function to fins absolute value of numbers.
    >>absVal(-5)
    5
    >>absVal(0)
    0
    """
    if Num < 0:
        return -num
    else:
        return num

print(absVal(-34)) # = 34

def absVal(num):
    if num < 0:
        return -num
    else:
        return num


print(absVal(-34)) # = 34
