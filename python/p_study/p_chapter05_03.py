# Chapter05-03
# 일급 함수(일급 객체)
# 클로저 기초
# 외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근(액세스) 가능

# 클로저(Closure) 사용
def closure_ex1():
    # Free variable (자유변수)
    series = [] # averager 외부에 존재
    # 클로저 영역
    def averager(v):
        # series = [] # 주석 해제 후 확인
        series.append(v)
        print('inner >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    return averager

avg_closure1 = closure_ex1()

print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))

print()
print()

# function inspection

print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__))
print()
print(avg_closure1.__code__.co_freevars) # 자유변수 확인 = series
print()
print(dir(avg_closure1.__closure__[0]))
print()
print(avg_closure1.__closure__[0].cell_contents)

print()
print()

# 잘못된 클로저 사용
def closure_ex2():
    # Free variable
    cnt = 0
    total = 0
    def averager(v):
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure2 = closure_ex2()

# print(avg_closure2(10)) # 예외


# Nonlocal -> Free variable
def closure_ex3():
    # Free variable
    cnt = 0
    total = 0
    def averager(v):
        nonlocal cnt, total # 변수를 로컬변수가 아니라고 인식
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure3 = closure_ex3()

print(avg_closure3(15))
print(avg_closure3(35))
print(avg_closure3(40))
