## 다음 정의된 operator가 하는 기능은 무엇인가?

def operator(x, y):

    while y:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x

# 답: XX
