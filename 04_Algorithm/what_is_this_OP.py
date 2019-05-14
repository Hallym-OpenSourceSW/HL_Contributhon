## 다음 정의된 operator가 하는 기능은 무엇인가?

def operator(xinput, yinput):

    while yinput:
        ca = xinput & yinput #and 연산자
        xinput = xinput ^ yinput #xor 연산자
        yinput = ca << 1 #비트 연산자
    return xinput

# 답: XX

