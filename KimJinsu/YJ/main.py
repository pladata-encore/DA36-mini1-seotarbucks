import time
from typing import final

from stbk_menu import StarBucks_Menu
from stbk_entity import Welcome, FinalPage
import os

if __name__ == '__main__':
    Welcome().welcome_page()
    os.system('cls')
    Welcome().where_menu()
    os.system('cls')
    #---------------------
    stbk_menu = StarBucks_Menu()
    os.system('cls')
    shopping_bag = stbk_menu.main_menu()
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
    input('주문정보가 맞으면 엔터를 눌러주세요.')
    # print(final_price)
    # --------------------------
    final_page.membership()
    #-----------------------
    final_page.payment()
    os.system('cls')
    final_page.receipt()
    Welcome().byebye()








