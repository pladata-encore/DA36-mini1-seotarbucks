from typing import final

from stbk_menu import StarBucks_Menu
from stbk_entity import Welcome, FinalPage

if __name__ == '__main__':
    Welcome().welcome_page()
    Welcome().where_menu()
    #---------------------
    stbk_menu = StarBucks_Menu()
    shopping_bag = stbk_menu.main_menu()
    print(shopping_bag)
    print('주문완료')
    #--------------------
    final_page = FinalPage()
    print('계산시작')
    price = final_page.cart_price_sum(shopping_bag)
    print(price)
    #-------------------------
    carrier = final_page.carrier_sel()
    print(carrier)
    #--------------------------
    final_price = final_page.calculation(carrier, price)
    # print(final_price)
    # --------------------------
    final_page.membership()
    #-----------------------
    final_page.payment()
    final_page.receipt()

    Welcome().byebye()








