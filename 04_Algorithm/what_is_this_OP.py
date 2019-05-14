def operator(xinput, yinput):

    while yinput:
        ca = xinput & yinput
        xinput = xinput ^ yinput
        yinput = ca << 1
    return xinput

def test():
  for i in range(0, 100):
    for j in range(0, 100):
      if operator(i, j) != i+j:
        print("false")
        
test()

# 답: 양수와 0 덧셈

