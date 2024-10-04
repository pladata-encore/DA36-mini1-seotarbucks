



class Menu:
    """
    - 커피 : 온도(Hot/Iced), 사이즈, 얼음량, 당도, 컵(텀블러 유무), 수량, 디카페인, [상품명, 샷(연하게, 보통, 진하게(샷추가+500) ), 가격 ]
    - 음료 : 온도(Hot/Iced), 사이즈, 얼음량, 당도, 컵(텀블러 유무), 수량, [상품명, 휘핑 유무, 가격]
    [변수명 정리]
    - 카테고리
        커피 - Coffee
        음료 - NonCoffee
    - 옵션
        상품명 - name
        온도 - temp
        사이즈 - size
        얼음량 - amnt_ice
        당도 - sugar_cnt
        컵(텀블러 유무) - cup
        수량 - quantity
        디카페인 - decaffein
        샷 - shot
        휘핑 - whipping
    - 기본값(옵션X, 설정값)
        가격 - price
    """
    """
    스타벅스(starbucks.xlsx)엑셀 가격표(price)시트를 생성후 가격표 시트를 불러오고 싶다...
    가격표 시트에는 (메뉴 고유 번호, 메뉴명, 가격(**사이즈별 가격**) )
    불러온 가격표는 읽는 것만 가능.
    옵션 선택 후 사이즈/텀블러 할인/추가옵션선택 에 따라 결제 금액 계산하고싶다...
    그걸 장바구니 가격에 넣고 수량/할인유무 에 따른 최종 결제 금액을 계산하고싶다...
    계산된 최종결제 금액을 스타벅스(starbucks.xlsx)에 매출액 시트를 생성후 집어넣고싶다.
    매출액 시트에는 (메뉴명, 수량, 매출액,....)
    ??손님이 할인(적립)쿠폰을 사용해서 결제했다고 해도 매출액엔 변경없음..??
    -> 변경없다. 매출액 시트에 할인금액? 넣을까....?????
    """
    next_id = 1
    # price = 5000  # TODO 가격표를 만들어서 엑셀파일 시트로 만들고 싶다....!!
                  # TODO 가격표 시트에 있는 가격을 불러와서 알아서 계산되게 하고싶다...!!

    def __init__(self,menu_name, temp=None, size=None, amnt_ice=None, sugar_cnt=None, cup=None, quantity=None, price=None):
        self.__id = Menu.next_id
        self.__menu_name = menu_name
        self.__temp = temp
        self.__size = size
        self.__amnt_ice = amnt_ice
        self.__sugar_cnt = sugar_cnt
        self.__cup = cup
        self.__quantity = quantity
        self.__price = price
        Menu.next_id += 1

    def get_id(self):
        return self.__id

    def get_price(self):
        return self.__price
    def set_price(self, price):
        self.__price = price

    def get_name(self):
        return self.__menu_name
    def set_name(self, menu_name):
        self.__menu_name = menu_name

    def get_temp(self):
        return self.__temp
    def set_temp(self, temp):
       self.__temp = temp

    def get_size(self):
        return self.__size
    def set_size(self, size):
       self.__size = size

    def get_amnt_ice(self):
        return self.__amnt_ice
    def set_amnt_ice(self, amnt_ice):
       self.__amnt_ice = amnt_ice

    def get_sugar_cnt(self):
        return self.__sugar_cnt
    def set_sugar_cnt(self, sugar_cnt):
       self.__sugar_cnt = sugar_cnt

    def get_cup(self):
        return self.__cup
    def set_cup(self, cup):
       self.__cup = cup

    def get_quantity(self):
        return self.__quantity
    def set_quantity(self, quantity):
       self.__quantity = quantity

    def __repr__(self):
        return f"""
{self.__id}번 상품명: {self.__menu_name} HOT/ICED: {self.get_temp()} 사이즈: {self.__size} 얼음량: {self.__amnt_ice} 당도: {self.__sugar_cnt} 컵: {self.__cup} 수량: {self.__quantity}개
"""
