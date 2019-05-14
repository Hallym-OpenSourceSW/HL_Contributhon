## 다음 정의된 operator가 하는 기능은 무엇인가?

def operator(xinput, yinput):

    while yinput:
        ca = xinput & yinput
        xinput = xinput ^ yinput
        yinput = ca << 1
    return xinput

# 답: xinput에 yinput만큼 더해서 리턴하는 함수
