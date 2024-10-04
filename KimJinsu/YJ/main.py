import time
from typing import final

from stbk_menu import StarBucks_Menu
from stbk_entity import Welcome, FinalPage
import os
from rich.console import Console

console = Console()

if __name__ == '__main__':
    Welcome().welcome_page()


    while True:
        flag = Welcome().where_menu()
        match flag:
            case "1" | '2':
                os.system('cls')


                #---------------------
                stbk_menu = StarBucks_Menu()
                os.system('cls')
                shopping_bag = stbk_menu.main_menu()

                if shopping_bag == 999:
                    print('찾아주셔서 감사합니다. 좋은 하루 되세요~')
                    break
                # print(shopping_bag)

                #--------------------
                final_page = FinalPage()

                price = final_page.cart_price_sum(shopping_bag)
                final_page.shopping_list(shopping_bag,price)
                # print(price)

                #-------------------------
                carrier = final_page.carrier_sel()

                #--------------------------
                final_price = final_page.calculation(carrier, price)

                final_page.shopping_list2(shopping_bag, price, final_price )
                # Console.print(f'총{final_price}원을 결제합니다',style='blink')

                console.print(f'총 {final_price}원을 결제합니다'.rjust(110),style='bold green')
                input('주문정보가 맞으면 엔터를 눌러주세요.'.rjust(65))


                # print(final_price)
                # --------------------------
                final_page.membership()
                #-----------------------
                final_page.payment()
                os.system('cls')
                final_page.receipt()
                Welcome().byebye()
                break

            case '0':
                print('저희가 도와드릴께요~잠시만 기다려주세요~')
                break

            case _:
                print('잘못된 선택입니다.')
                time.sleep(1)











