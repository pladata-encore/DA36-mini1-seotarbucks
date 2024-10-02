# blended menu
from stbk_entity import StarBucks

def blended_menu():
    blended_menu_list = {
        1: ('녹차 프라투치노', 6500),
        2: ('자바칩 프라푸치노', 7000),
        3: ('피치 아사이 리프레셔', 6000),
        4: ('딸기 아사이 리프레셔', 6000),
        5: ('망고 리프레셔', 6000)
    }
    blended_menu_str = """
---------Coffee Menu--------
1. 녹차 프라푸치노         =======     6500원
2. 자바칩 프라푸치노        =========   7000원
3. 피치 아사이 리프레셔     =========    6000 원
4. 딸기 아사이 리프레셔     ======       6000 원
5. 망고 리프레셔           ====         6000 원
0. 이전으로 돌아가기
----------------------------          
선택:                    """


    while True:
        menu_name = int(input(blended_menu_str))

        if menu_name in blended_menu_list:
            print(f'{blended_menu_list[menu_name][0]}를 선택하셨습니다.')
            # order = StarBucks
            #
            # order.set_name(name=coffee_menu_list[menu_name][0])

            qntt = int(input('수량을 입력해주세요'))
            # order.set_quantity(qntt)

            swt_list=['120%','100%','80%']

            swt = int(input('''
            당도를 입력해주세요 
            1=120% 
            2=100%
            3=80%
            >'''))
            # order.set_sugar_cnt(swt)
            size_list=['Tall', 'Grande', 'Venti']
            size = int(input('''
            사이즈를 입력해주세요
            1 = Tall
            2 = Grande
            3 = Venti
            >>'''))
        else:
            print('잘못 선택하셨습니다. 다시 선택해주세요')

        print(f'{blended_menu_list[menu_name][0]} {qntt}개, 당도는 {swt_list[swt-1]}, 사이즈는 {size_list[size-1]}를 선택하셨습니다 ')

        order = StarBucks(blended_menu_list[menu_name][0])
        # order.set_name(coffee_menu_list[menu_name][0])
        order.set_quantity(qntt)
        order.set_size(size_list[size-1])

        print(order)




blended_menu()