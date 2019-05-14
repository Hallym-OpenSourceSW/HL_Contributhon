# 절대값을 고려하여 주어진 리스트에서 최대값을 찾는 프로그램입니다.
# 에러를 찾아주세요!

def absMax(x):
    """
    #>>>absMax([0,5,1,11])
    11
    >>absMax([3,-10,-2])
    -10
    """
    j =x[0]
    for i in x:
        if abs(i) > abs(j):
            j = i
    return j


a = [1,2,-11]
print(absMax(a)) # = -11
