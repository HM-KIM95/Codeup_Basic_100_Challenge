# 6057 : [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기(설명)(py)
a, b = input().split()
a = int(a)
b = int(b)

print((bool(not a)) and (bool(not b)) or (bool(a) and bool(b)))