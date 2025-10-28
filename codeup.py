# 6056 : [기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력하기(설명)(py)
a, b = input().split()
a = bool(int(a))
b = bool(int(b))

print((a and (not b)) or ((not a) and b))