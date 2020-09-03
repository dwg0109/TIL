# Chapter02-03
# 파이썬 심화
# 클래스 메소드, 인스턴스 메소드, 스테이틱 메소드

# 기본 인스턴스 메소드

# 클래스 선언
class Car(object):
    """
    Car Class
    Author : Kim
    Date : 2020.09.03
    Description : Class, Static, Instance Method
    """

    # 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        #self.car_count = 10
        self._details = details

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    # Instance Method(인스턴스 메소드)
    # self : 객체의 고유한 속성 값 사용
    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    # Instance Method
    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))

    # Instance Method
    def get_price_culc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    # Class Method
    # cls == Car(class)
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.price_per_raise = per
        print('Succeed! price increased.')

    # Static Method
    @staticmethod
    def is_bmw(inst): #inst : 임의의 값, 자유롭게 설정 가능
        if inst._company == 'Bmw':
            return 'OK! This car is {}.'.format(inst._company)
        return 'Sorry. This car is not Bmw.'


# 자동차 인스턴스
car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})

# 기본 정보
print(car1)
print(car2)
print()

# 전체 정보
car1.detail_info()
car2.detail_info()
print()

#가격정보(직접 접근) -> 좋은 방법이 아님
print(car1._details.get('price'))
print(car2._details['price'])
print()

# 가격 정보(인상 전)
print(car1.get_price())
print(car2.get_price())
print()

# 가격 인상(클래스 메소드 미사용)(직접 접근)
Car.price_per_raise = 1.4

# 가격 정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())
print()

# 가격 인상(클래스 메소드 사용)
Car.raise_price(1.6)
print()

# 가격 정보(인상 후 : 클래스메소드)
print(car1.get_price_culc())
print(car2.get_price_culc())
print()

# 인스턴스로 호출(스테이틱)
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))

# 클래스로 호출(스테이틱)
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))
