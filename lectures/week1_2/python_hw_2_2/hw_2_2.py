# 문제
# 슈퍼마켓의 상품을 관리하기 위한 클래스를 정의하고, 요구 사항에 맞춰 코드를 작성하시오.

# 요구사항
# Product 클래스를 정의한다.
# Product의 인스턴스 수를 기록할 수 있는 클래스 변수 product_count를 정의하고, 0을 할당한다.
# 생성자 메서드를 정의한다.
# 생성자 메서드는 상품의 이름(name)과 가격(price)을 인자로 받는다.
# 각 인스턴스는 고유한 이름과 가격을 담을 수 있는 name과 price 변수를 가지고, 인자로 넘겨받은 값을 할당받는다.
# 인스턴스가 생성될 때마다 product_count가 1 증가해야 한다.
# 상품의 정보를 출력하는 display_info 인스턴스 메서드를 정의한다.
# 2개 이상의 인스턴스를 생성하고, 각 인스턴스의 정보를 출력한다.
# Product 클래스의 product_count를 출력한다.

# 아래에 코드를 작성하시오.

class Product:
    product_count = 0 # 클래스 변수는 이 클래스로 만들어질 모든 인스턴스들이 공통으로 가지는 속성이다.
    # Product의 인스턴스 수를 기록할 수 있는 클래스 변수 product_count를 정의하고, 0을 할당한다.
    # 생성자 메서드를 정의한다.
    # 생성자 메서드는 상품의 이름(name)과 가격(price)을 인자로 받는다.
        # 인스턴스 메서드는 인스턴스가 쓸 것이다.
        # 그럼, 당연히 인스턴스에 대한 정보도 알고 있어야 할 것이다.
            # 따라서 항상 첫번째 매개변수는 self
    def __init__(self, name, price): # 인스턴스 메서드 정의 방식과 동일하다.
        # 각 인스턴스는 고유한 이름과 가격을 담을 수 있는 name과 price 변수를 가지고, 인자로 넘겨받은 값을 할당받는다.
        self.name = name
        self.price = price
        # 인스턴스가 생성될 때마다 product_count가 1 증가해야 한다.
            # product_count는 클래스 변수다.
            # 따라서, 인스턴스가 직접적으로 클래스 변수를 변화시키지 않는다.
        # Product.product_count = (Product.product_count + 1)
        Product.product_count += 1

    # 상품의 정보를 출력하는 display_info 인스턴스 메서드를 정의한다.
    def display_info(self):
        # 이 함수의 본 역할은? 상품의 정보를 출력하는 것!
        print(f"상품명: {self.name}, 가격: {self.price}")

# 인스턴스 생성과 할당 과정을 단계별로 나눠 보자면
# 1. 인스턴스 생성
p1 = Product('사과', 1000)
p2 = Product('바나나', 1500)
p1.display_info()
p2.display_info()

print(f"총 상품 수: {Product.product_count}")