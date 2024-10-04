from rich.progress import track
import time

# from abc import ABC, abstractmethod
# 부모 클래스(공통된 옵션(속성)/메소드) 선언
class StarBucks:
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

    def __init__(self,menu_name, temp=None, size=None, amnt_ice=None, sugar_cnt=None, cup=None, quantity=None, price = None):
        self.__id = StarBucks.next_id
        self.__menu_name = menu_name
        self.__temp = temp
        self.__size = size
        self.__amnt_ice = amnt_ice
        self.__sugar_cnt = sugar_cnt
        self.__cup = cup
        self.__quantity = quantity
        self.__price = price


        StarBucks.next_id += 1

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
{self.__id}번, 상품명:{self.__menu_name}, 사이즈:{self.__size}, 얼음량:{self.__amnt_ice}, 당도:{self.__sugar_cnt}, 컵:{self.__cup}, 수량:{self.__quantity}개, 가격:{self.__price}
"""
# 자식(상품)클래스 선언 - 카테고리
class Coffee(StarBucks):
    def __init__(self, menu_name, temp, size, amnt_ice, sugar_cnt, cup, decaffein, shot, quantity):
        super().__init__(menu_name, temp, size, amnt_ice, sugar_cnt, cup, quantity)
        self.__decaffein = decaffein
        self.__shot = shot
    def get_decaffein(self):
        return self.__decaffein
    def set_decaffein(self, decaffein):
       self.__decaffein = decaffein
    def get_shot(self):
        return self.__shot
    def set_shot(self, shot):
       self.__shot = shot
       # # 마진 계산 - 커피 모두 0.05 라고 가정.
       # def calculate_margin(self):
       #     return self.price * .05
    def __repr__(self):
        return f"""
{super().__repr__()}\n디카페인 선택: {self.__decaffein}
샷:{self.__shot}
{'-'*30}
"""
"""
1. 마진=판매가격-공급가액
2. 마진율=(판매가격-공급가액)/판매가격×100%
3. 판매가격=공급가액/(1-마진율)
"""
class NonCoffee(StarBucks):
    def __init__(self, name, temp, size, amnt_ice, sugar_cnt, cup,whipping, quantity):
        super().__init__( name, temp, size, amnt_ice, sugar_cnt, cup, quantity)
        self.__whipping = whipping
    def get_whipping(self):
        return self.__whipping
    def set_whipping(self, whipping):
        self.__whipping = whipping
    # # 마진 계산 - 음료 모두 0.08 라고 가정.
    # def calculate_margin(self):
    #     return self.price * .08
    def __repr__(self):
        return f"""
{super().__repr__()}\n휘핑: {self.__whipping}
{'-'*30}
"""

class Shopping_bag:
    orders = []
    def __init__(self):
        pass

    def add_shopping_bag( order):
        Shopping_bag.orders.append(order)
        return Shopping_bag.orders




class Final_page:

    skt = 0.1
    kt = 0.1
    lgu = 0.05
    members = {'2074':2}
    order_nums = 0


    def __init__(self):
        pass

    def total_price_cal(self,bags):
        total_price = 0
        for item in bags:
            total_price += item.get_price * item.get_quantity
        print(total_price)
        return total_price


    ''' 통신사 확인
    1. skt
    2. kt
    3. lgu
    '''

    def carrier_sel(self):
        print('사용하고 계신 통신사를 선택해 주세요.')
        str_carrier_menu = '''
1. SKT (10% 할인)
2. KT   (10% 할인)
3. LGU (5% 할인)
4. 해당없음.
'''
        input_carrier = input(str_carrier_menu)
        return input_carrier

    def calculation(self, carrier, total_price): # 통신사 없을 시 추가 해야함

        match carrier:
            case '1':
                discount_price = total_price * (1-Final_page.skt)
            case '2':
                discount_price = total_price * (1-Final_page.kt)
            case '3':
                discount_price = total_price * (1-Final_page.lgu)
            case '4':
                print('해당되는 할인 항목이 없습니다.')
                discount_price = total_price
            case _:
                print('잘못된 통신사입니다.')
                return 0

        return discount_price

    def payment(self):      # 1) 결제가능 제한시간, 2) 일정시간(3초) 후 결제완료 메세지 표출
        method = input('결제 수단을 선택하세요\n1)신용카드 ,2)현금결제, 3)각종 pay\n')
        flag = 1

        match method:
            case '1':   # 신용카드
                print('카드를 칩 리더기에 넣어주세요')
                for i in track(range(3)):
                    time.sleep(0.5)

            case '2':   # 현금결제
                print('카운터에서 결제 해주세요')
            case '3':   # 삼성, 애플 pay
                print('핸드폰을 테그에 접촉해주세요')
                for i in track(range(3)):
                    time.sleep(0.5)
            case _:
                print('잘못된 선택입니다.')
                flag = 0

        if flag != '0':
            print('Requesting transaction....')
            time.sleep(0.5)
            print('Waiting for response....')
            time.sleep(0.2)
            print('Data transmit successful....')
            time.sleep(0.5)
            print('Receiving encrypted transaction data....')
            time.sleep(0.1)
            print('Transaction was successful....')
            time.sleep(0.2)

            print('성장적으로 결제 되었습니다.')
        return flag


    def membership(self):
            member = input('멤버쉽 있으신가요?? 1. yes, 2. no\n>>')
            flag = 1

            match member:
                case '1' :
                    # cell_number = input('핸드폰 번호를 입력해주세요')        # try except 가능
                    Final_page.add_point(self)
                case '2':
                    mem_join = input('멤버쉽에 가입하시겠습니까? [1=y]/2=n \n>>')
                    if mem_join != '2':
                        Final_page.join_member(self)
                    else :
                        print('결제화면으로 이동합니다.')
                case _:
                    print('잘못 누르셨습니다.')
                    flag = 0

            return flag

    def add_point(self):
        cell_number = input('핸드폰 번호를 입력해주세요\n>>')
        try :
            Final_page.members[cell_number] += 1 # members : 멤버쉽 딕셔너리들, 값들은 숫자여야 함.
            print(f'1포인트 적립이 완료 되었습니다. {cell_number}님의 현재 포인트는 {Final_page.members[cell_number]} 포인트 입니다.')
        except:
            print('등록되지 않은 회원입니다. 회원가입을 진행합니다.')
            Final_page.join_member(self)
            # Final_page.members[cell_number] = 1
            # print(f'1포인트 적립이 완료되었습니다. {cell_number}님의 현재 포인트는 {Final_page.members[cell_number]} 포인트 입니다.')


    def join_member(self):
        cell_number = input('핸드폰 번호를 입력해주세요\n>>')
        if cell_number in Final_page.members:
            Final_page.members[cell_number] += 1  # members : 멤버쉽 딕셔너리들, 값들은 숫자여야 함.
            print('가입된 회원 정보가 있습니다.')
            print(f'1포인트 적립이 완료 되었습니다. {cell_number}님의 현재 포인트는 {Final_page.members[cell_number]} 포인트 입니다.')
        else:
            Final_page.members[cell_number] = 1    # 딕셔너리에 멤버 추가
            print(f'회원가입이 완료되었습니다. {cell_number}님의 현재 포인트는 {Final_page.members[cell_number]} 포인트 입니다.')

    def receipt(self):
        print('주문이 완료 되었습니다. 감사합니다.')
        Final_page.order_nums += 1
        print(f'주문번호는 {Final_page.order_nums}번 입니다. ')






