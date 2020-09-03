# Chapter02-02
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 클래스 재 선언
class Car():
    #__doc__로 확인 가능
    """
    Car Class
    Author : Kim
    Date : 2020.09.03
    """

    # 클래스 변수(모든 인스턴스가 공유)
    car_count = 0

    def __init__(self, company, details):
        self._company = company
        #self.car_count = 10
        self._details = details
        Car.car_count += 1

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    def __del__(self):
        Car.car_count -= 1

# Self 의미
car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color' : 'Silver', 'horsepower': 300, 'price': 6000})

# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company) #값 비교
print(car1 is car2) #id 값 비교

# dir & __dict__ 확인
print(dir(car1)) #메소드 확인 가능
print(dir(car2))

print()
print()

print(car1.__dict__) #값을 확인 가능
print(car2.__dict__)

# Doctring
print(Car.__doc__) #설명을 확인하는 것
print()

# 실행
car1.detail_info()
Car.detail_info(car1) #동일
print()
car2.detail_info()
Car.detail_info(car2)

# 비교
print(car1.__class__, car2.__class__)
print(id(car1.__class__) == id(car3.__class__)) #클래스 자체의 id

# 에러
# Car.detail_info() => 에러 출력

print()

# 공유 확인
print(Car.__dict__)
print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)
print(dir(car1))

# 접근
print(car1.car_count)
print(Car.car_count)

#삭제
del car2

#삭제 확인
print(car1.car_count)
print(Car.car_count)

# 인스턴스 네임스페이스 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))
# 있으면 바로 인스턴스 변수 출력, 없으면 클래스 변수를 찾아서 있으면 출력, 아무것도 존재하지 않으면 에러
