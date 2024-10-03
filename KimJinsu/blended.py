# blended menu
from typing import Final

from stbk_entity import StarBucks
from project_01 import Shopping_bag, Final_page
import time


class BlendedMenu:

    def __init__(self):
        self.entity = StarBucks
        self.shopping_bag = Shopping_bag()
        self.discnt_pg = Final_page()

    def blended_menu():
        blended_menu_list = {
            1: ('녹차 프라투치노', 6500),
            2: ('자바칩 프라푸치노', 7000),
            3: ('피치 아사이 리프레셔', 6000),
            4: ('딸기 아사이 리프레셔', 6000),
            5: ('망고 리프레셔', 6000)
        }
        blended_menu_str = """
---------Blended Menu--------
1. 녹차 프라푸치노         =======     6500원
2. 자바칩 프라푸치노        =========   7000원
3. 피치 아사이 리프레셔     =========    6000 원
4. 딸기 아사이 리프레셔     ======       6000 원
5. 망고 리프레셔           ====         6000 원
0. 이전으로 돌아가기
----------------------------          
선택:>>"""

        re_flag=1
        while True:
            menu_name = int(input(blended_menu_str))
            add_on = 0

            if menu_name in blended_menu_list:
                print(f'{blended_menu_list[menu_name][0]}를 선택하셨습니다.')

                qntt = int(input('수량을 입력해 주세요\n>>'))

                swt_list=['120%','100%','80%']

                swt = int(input('''
당도를 입력해주세요 
1=120% (+300)
2=100%
3=80%
>>'''))

                if swt == 1:
                    add_on += 300

                size_list=['Tall', 'Grande', 'Venti']
                size = int(input(''' 
사이즈를 입력해주세요
1 = Tall(+0)
2 = Grande(+700)
3 = Venti(+1000)
>>'''))
                if size == 2:
                    add_on += 700
                elif size == 3:
                    add_on += 1000

                ice_list = ['Extra','Normal','Less']
                ice = int(input('''
얼음양을 입력해주세요.
1 = Extra
2 = Normal
3 = Less
>>'''))
            else:
                print('잘못 선택하셨습니다. 다시 선택해주세요')


            print(f'{blended_menu_list[menu_name][0]} {qntt}개, 당도는 {swt_list[swt-1]}, 사이즈는 {size_list[size-1]}를 선택하셨습니다 ')

            order = StarBucks(blended_menu_list[menu_name][0])
            # order.set_name(coffee_menu_list[menu_name][0])
            order.set_quantity(qntt)
            order.set_size(size_list[size-1])
            order.set_amnt_ice(ice_list[ice-1])
            order.set_sugar_cnt(swt_list[swt-1])
            order.set_price((blended_menu_list[menu_name][1] + add_on) * qntt)

            # print(order)

            bags = Shopping_bag.add_shopping_bag(order)
            print("장바구니에 추가 되었습니다.")
            print(bags)

            re_flag = input('더 주문하시겠어요? [y=1/n=0]')

            if re_flag == '0':
                break

        return cart_price_sum(bags)

def cart_price_sum(bags):
    sum_price=0
    for order_price in bags:
        sum_price += order_price.get_price()
        # print(sum_price)

    # print(sum_price)
    return sum_price





# blended_menu()
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
================================================================================

''')

input('계속하려면 엔터를 눌러주세요...')


tot_price = BlendedMenu.blended_menu()

old_price = tot_price

print(old_price)
print('='*50)
user_carrier = Final_page.carrier_sel(999)

final_price = Final_page.calculation(999, user_carrier, tot_price)
print(f'최종할인 적용된 금액은 {old_price} - {old_price-final_price} = {final_price}원 입니다')
print(f'{old_price-final_price}원 할인받으셨습니다.')
print("="*50)
Final_page.membership(999)
Final_page.payment(999)
Final_page.receipt(999)



'''
prolog
09/30
- 코딩 시작

10/01
- 할인, 결제, 멤버쉽 등 마지막 결제 단계에서 필요한 메소트 및 class 작성


10/02
- 지금까지 작성했던 내용 팀원들과의 회의. feedback 및 comments 수렴.
blended menu 작업 시작
-예진님이 작업한 Starbucks class 및 entity class를 바탕으로 간략하게 구현
- class간의 인스턴스 교환, 등 몇가지 궁금한점 생김.


10/03

- blended 메뉴 작업 및 수정, 보완.
- class간의 인자로 일단 999 사용.
- 결제 및 할인, 멤버쉽관련 작업내용과 합침.
- rich import.

TODO
- 장바구니 표현
- 다른 결제수단 확인
- 멤버들 정보 저장 및 가져오기

'''