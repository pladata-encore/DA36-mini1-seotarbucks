import time
from typing import final

from pygments.lexers import q

from stbk_menu import StarBucks_Menu
from stbk_repository import StarBucks_Repository
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
                shopping_bag = stbk_menu.main_menu(flag)

                if shopping_bag == 999:
                    print('찾아주셔서 감사합니다. 좋은 하루 되세요~')
                    break
                # print(shopping_bag)

                #--------------------
                final_page = FinalPage()

                price = final_page.cart_price_sum(shopping_bag) # 할인적용 전 가격
                final_page.shopping_list(shopping_bag,price)
                # print(price)

                #-------------------------
                carrier = final_page.carrier_sel()

                #--------------------------
                final_price = final_page.calculation(carrier, price)    # 통신사 할인 후

                final_page.shopping_list2(shopping_bag, price, final_price )
                # Console.print(f'총{final_price}원을 결제합니다',style='blink')

                console.print(f'총 {final_price}원을 결제합니다'.rjust(110),style='bold green')
                input('주문정보가 맞으면 엔터를 눌러주세요.'.rjust(65))


                # print(final_price)
                # --------------------------
                cell_number = final_page.membership()
                #-----------------------
                pymnt_mthd=final_page.payment()

                for drink in shopping_bag:
                    # print(drink)
                    # input()
                    drink.set_mbr(cell_number)
                    drink.set_carrier(carrier)  #'1':sk,'2':kt,'3':lgu '0':NA
                    drink.set_pymnt(pymnt_mthd) #'1':신용카드,'2':현금,'3':기타pay '0':NA
                    StarBucks_Repository.sales_statement.append(drink)

                os.system('cls')
                final_page.receipt()
                Welcome().byebye()

                # result=StarBucks_Repository.sales_statement[0].get_name()
                # print(type(result), result)



                break

            case '0':
                print('저희가 도와드릴께요~잠시만 기다려주세요~')
                break

            case _:
                print('잘못된 선택입니다.')
                time.sleep(1)











