"""
배열을 입력 받아서 배열내에 있는 "0" 들을 모두 뒷부분으로 옮기는 알고리즘을 만들어 보세요!
단, 배열내에 "0"이 아닌 요소들의 순서는 지켜져야 합니다.

    moveZeros(["false", 1, 0, 1, 2, 0, 1, 3, "a"])
    returns => ["false", 1, 1, 2, 1, 3, "a", 0, 0]
    
"""


def moveZeros(array):
    result = []
    zeros = 0

    # your code
    # your code
    
    return result
    
print(moveZeros(["false", 1, 0, 1, 2, 0, 1, 3, "a"]))  ## ['false', 1, 1, 2, 1, 3, 'a', 0, 0]


def moveZeros(array):
    result = []
    zeros = 0
    cnt=array.count(0)
    for i in array:
        if(i!=0):
            result.append(i)
    for i in range(cnt):
        result.append(0)
    
    
    return result
    
print(moveZeros(["false", 1, 0, 1, 2, 0, 1, 3, "a"]))  ## ['false', 1, 1, 2, 1, 3, 'a', 0, 0]
