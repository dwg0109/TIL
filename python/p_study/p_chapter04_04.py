# Chapter04-04
# 파이썬 심화
# 시퀀스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 X, Set -> 중복 허용 X
# Dict 및 Set 심화

# immutable Dict (수정이 불가능한 dictionary)

from unicodedata import name  # 지능형 집합(Comprehending Set)
from dis import dis  # 선언 최적화
from types import MappingProxyType  # immutable Dict (수정이 불가능한 dictionary)

d = {'key1': 'value1'}

# Read Only
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))
print(d is d_frozen, d == d_frozen)

# 수정 불가
# d_frozen['key1'] = 'value2' -> 에러 도출

# 수정 가능
d['key2'] = 'value2'

print(d)

print()
print()

s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}  # 중복 허용 X
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set()  # 공집합  # {} -> dictionary로 인식
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})  # 읽기 전용

# 추가
s1.add('Melon')

# 추가 불가
# s5.add('Melon')

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

# 선언 최적화
# 바이트 코드 -> 파이썬 인터프리터 실행

print('------')
print(dis('{10}'))  # 더 빠른 선언

print('------')
print(dis('set([10])'))

# 지능형 집합(Comprehending Set)

print('------')

print({name(chr(i), '') for i in range(0, 256)})
