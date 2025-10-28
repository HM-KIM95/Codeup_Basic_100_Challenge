# 6045 : [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기(설명)(py)

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

d = a + b + c
e = format(d/3, ".2f")

print(d, e)