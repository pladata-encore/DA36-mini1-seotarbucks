from abc import ABC, abstractmethod


# 부모 클래스(공통된 옵션(속성)/메소드) 선언
from rich.progress import track
import time, os
from rich.console import Console
from rich.table import Column, Table




class StarBucks(ABC):
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
        self.__id = StarBucks.next_id
        self.__menu_name = menu_name
        self.__temp = temp
        self.__size = size
        self.__amnt_ice = amnt_ice
        self.__sugar_cnt = sugar_cnt
        self.__cup = cup
        self.__quantity = quantity
        self.__price = price
        # self.__sv = StarBucks.price * int(quantity)
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
    # @abstractmethod
    # def calculate_margin(self):
    #     pass
#     def __repr__(self):
#         return f"""
# {self.__id}번
# 상품명: {self.__menu_name}
# HOT/ICED: {self.__temp}
# 사이즈: {self.__size}
# 얼음량: {self.__amnt_ice}
# 당도: {self.__sugar_cnt}
# 컵: {self.__cup}
# 수량: {self.__quantity}개
# """



class FinalPage:
    def __init__(self):
        pass

    def cart_price_sum(self,bags):
        sum_price = 0
        for order_price in bags:
            sum_price += order_price.get_price()

        return sum_price

    def shopping_list(self, shopping_bag, price):
        size_list = ['Tall', 'Grande', 'Venti']
        temp_list = ['HOT', 'ICED']
        ice_list = ['Extra', 'Normal', 'Less']
        swt_list = ['120%', '100%', '80%']
        sum_quantity=0

        for item in shopping_bag:
            sum_quantity += item.get_quantity()


        os.system('cls')
        table = Table(title="========== 내 장바구니 ===========", show_header=True, header_style="bold magenta", show_footer=True)
        table.add_column('Selction', 'Total',width=10, justify='center')
        table.add_column('Menu', width=50, justify='left')
        table.add_column('Quantity', f'{sum_quantity}',width=10, justify='center')
        table.add_column('Price', f'{price}',width=10, justify='center')


        # print(item.get_size())

        for n, item in enumerate(shopping_bag):
            table.add_row(f'{n+1}',f'{item.get_size()} {item.get_temp()} {item.get_name()} {item.get_sugar_cnt()}',f'{item.get_quantity()}',
                                                                                       f'{item.get_price()}')


        console = Console()
        console.print(table)

    def shopping_list2(self, shopping_bag, price, discnt_price):
        size_list = ['Tall', 'Grande', 'Venti']
        temp_list = ['HOT', 'ICED']
        ice_list = ['Extra', 'Normal', 'Less']
        swt_list = ['120%', '100%', '80%']
        sum_quantity=0

        for item in shopping_bag:
            sum_quantity += item.get_quantity()


        os.system('cls')
        table = Table(title="========== 내 장바구니 ===========", show_header=True, header_style="bold magenta", show_footer=True)
        table.add_column('Selction', 'Final Price',width=15, justify='center',footer_style='bold red')
        table.add_column('Menu', width=50, justify='left')
        table.add_column('Quantity', f'{sum_quantity}',width=10, justify='center')
        table.add_column('Price', f'{price}',width=10, justify='center')
        table.add_column('Discount', f'{discnt_price-price}',width=10, justify='center',footer_style='red')
        table.add_column('Price', f'{discnt_price}',width=10, justify='center',footer_style='blink bold red on cyan')


        # print(item.get_size())

        for n, item in enumerate(shopping_bag):
            table.add_row(f'{n+1}',f'{item.get_size()} {item.get_temp()} {item.get_name()} {item.get_sugar_cnt()}',f'{item.get_quantity()}',
                                                                                       f'{item.get_price()}','')

        console = Console()
        console.print(table)

    def carrier_sel(self):

        # os.system('cls')
        table = Table(title="========== 통신사 선택 ==========", show_header=True, header_style="bold magenta")
        table.add_column('Selction', width=10, justify='center')
        table.add_column('Carrier', width=30, justify='left')
        table.add_column('Discount Rate', width=10, justify='center')

        table.add_row('1', 'SKT', '10%')
        table.add_row('2', 'KT', '10%')
        table.add_row('3', 'LG U+', '5%')
        table.add_row('0', '해당없음', '0%')

        console = Console()
        console.print(table)

        input_carrier = input('사용하고 계신 통신사를 선택해 주세요.>>')
        return input_carrier

    skt = 0.1
    kt = 0.1
    lgu = 0.05

    order_nums = 0

    def calculation(self, carrier, total_price): # 통신사 없을 시 추가 해야함

        match carrier:
            case '1':
                discount_price = total_price * (1-FinalPage.skt)
            case '2':
                discount_price = total_price * (1-FinalPage.kt)
            case '3':
                discount_price = total_price * (1-FinalPage.lgu)
            case '0':
                print('해당되는 할인 항목이 없습니다.')
                discount_price = total_price
            case _:
                print('해당되는 할인 항목이 없습니다.')
                discount_price = total_price





        return discount_price

    def payment(self):      # 1) 결제가능 제한시간, 2) 일정시간(3초) 후 결제완료 메세지 표출

        os.system('cls')
        table = Table(title="========== 결제 수단 선택 ==========", show_header=True, header_style="bold magenta")
        table.add_column('Selction', width=10, justify='center')
        table.add_column('Payment Method', width=30, justify='left')


        table.add_row('1', '신용카드')
        table.add_row('2', '현금결제')
        table.add_row('3', '각종 pay')


        console = Console()
        console.print(table)

        method = input('결제 수단을 선택하세요.>>')
        flag = 1

        os.system('cls')

        match method:
            case '1':   # 신용카드
                print('카드를 칩 리더기에 넣어주세요')
                for i in track(range(3)):
                    time.sleep(0.5)

            case '2':   # 현금결제
                print('카운터에서 결제 해주세요')
                time.sleep(0.5)
                print('감사합니다!')
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

    members = {'20745440': 2}

    def membership(self):

        os.system('cls')
        table = Table(title="========== Membership ==========", show_header=True, header_style="bold magenta")
        table.add_column('Selction', width=10, justify='center')
        table.add_column('Membership', width=40, justify='left')


        table.add_row('1', 'Yes')
        table.add_row('2', 'No')

        console = Console()
        console.print(table)

        member = input('멤버쉽 있으신가요??>>')
        flag = 1

        match member:
            case '1' :
                # cell_number = input('핸드폰 번호를 입력해주세요')        # try except 가능
                FinalPage.add_point(999)
            case '2':
                mem_join = input('\t멤버쉽에 가입하시겠습니까? [1=y]/2=n \n>>')
                if mem_join != '2':
                    FinalPage.join_member(999)
                else :
                    print('\t결제화면으로 이동합니다.')
            case _:
                print('잘못 누르셨습니다.')
                flag = 0

        return flag

    def add_point(self):
        cell_number = input('핸드폰 번호를 입력해주세요\n>>')
        try :
            FinalPage.members[cell_number] += 1 # members : 멤버쉽 딕셔너리들, 값들은 숫자여야 함.
            print(f'1포인트 적립이 완료 되었습니다. {cell_number}님의 현재 포인트는 {FinalPage.members[cell_number]} 포인트 입니다.')
        except:
            print('등록되지 않은 회원입니다. 회원가입을 진행합니다.')
            FinalPage.join_member(999)
            # Final_page.members[cell_number] = 1
            # print(f'1포인트 적립이 완료되었습니다. {cell_number}님의 현재 포인트는 {Final_page.members[cell_number]} 포인트 입니다.')


    def join_member(self):
        cell_number = input('핸드폰 번호를 입력해주세요\n>>')
        if cell_number in FinalPage.members:
            FinalPage.members[cell_number] += 1  # members : 멤버쉽 딕셔너리들, 값들은 숫자여야 함.
            print('가입된 회원 정보가 있습니다.')
            print(f'1포인트 적립이 완료 되었습니다. {cell_number}님의 현재 포인트는 {FinalPage.members[cell_number]} 포인트 입니다.')
        else:
            FinalPage.members[cell_number] = 1    # 딕셔너리에 멤버 추가
            print(f'회원가입이 완료되었습니다. {cell_number}님의 현재 포인트는 {FinalPage.members[cell_number]} 포인트 입니다.')

    def receipt(self):
        print('\t주문이 완료 되었습니다.')
        FinalPage.order_nums += 1
        print(f'\n\t주문번호는 {FinalPage.order_nums}번 입니다. ')


class Welcome:
    def __init__(self):
        pass
    def welcome_page(self):
        print('''
=================================================================================
__        __         _                                         _               
\ \      / /   ___  | |   ___    ___    _ __ ___     ___      | |_    ___      
 \ \ /\ / /   / _ \ | |  / __|  / _ \  | '_ ` _ \   / _ \     | __|  / _ \     
  \ V  V /   |  __/ | | | (__  | (_) | | | | | | | |  __/     | |_  | (_) |    
   \_/\_/     \___| |_|  \___|  \___/  |_| |_| |_|  \___|      \__|  \___/                                                
 ____                   _                    _                      _          
/ ___|    ___    ___   | |_    __ _   _ __  | |__    _   _    ___  | | __  ___ 
\___ \   / _ \  / _ \  | __|  / _` | | '__| | '_ \  | | | |  / __| | |/ / / __|
 ___) | |  __/ | (_) | | |_  | (_| | | |    | |_) | | |_| | | (__  |   <  \__ \\
|____/   \___|  \___/   \__|  \__,_| |_|    |_.__/   \__,_|  \___| |_|\_\ |___/


================================================================================

''')
        input('계속하려면 엔터를 눌러주세요...')

    def where_menu(self):


        table = Table(title="========== 어디서 드시나요?? ==========", show_header=True, header_style="bold magenta")
        table.add_column('Selction', width=10, justify='center')
        table.add_column('선   택', width=40, justify='center')

        table.add_row('1', 'Dine-in (매장)')
        table.add_row('2', 'To-Go (포장)')
        table.add_row('0', '직원 호출')


        console = Console()
        console.print(table)

        where = input("해당 번호를 입력해주세요>>")





    def byebye(self):
        str_bye = '''
                    (  )   (   )  )
                 ) (   )  (  (
                 ( )  (    ) )
                 _____________
                <_____________> ___
                |             |/ _ \\
                |               | | |
                |               |_| |
             ___|             |\___/
            /    \___________/    \\
            \_____________________/    
        '''
        print(str_bye)
        print('☕☕ 서-타-벅스를 이용해 주셔서 감사합니다. ☕☕')

