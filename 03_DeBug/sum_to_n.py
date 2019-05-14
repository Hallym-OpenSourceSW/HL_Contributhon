## 1부터 n까지의 합을 구하는 프로그램

def sum_a(a):
    b = 0
    for i in range(1,a):
        b+=i
    return b


# 예제 실습
print(sum_a(10)) # 1부터 10까지의 합 55이 나오면 성공
print(sum_a(100)) # 1부터 100까지의 합 5050이 나오면 성공


#수정

def sum_a(a):
    b = 0
    for i in range(1,a+1):
        b+=i
    return b


# 예제 실습
print(sum_a(10)) # 1부터 10까지의 합 55이 나오면 성공
print(sum_a(100)) # 1부터 100까지의 합 5050이 나오면 성공
