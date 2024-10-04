from stbk_service import StarBucks_Service
from stbk_entity import Menu


class StarBucks_Menu:
    def __init__(self):
        self.stbk_service = StarBucks_Service()

    def welcome(self):
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
        togo_str = '''
--------- 어디에서 드시나요? ---------
1. Dine-in (매장)
2. To-Go (포장)
0. 직원 호출
-----------------------------------       
선택 >> '''
        where = input(togo_str)
        # 관리자 모드 실행
        if where == '-1':
            password = input('>> 관리자 모드를 실행합니다.\n비밀번호를 입력하세요.\n비밀번호 :')
            manager_password = '1234'
            if password == manager_password:
                self.manager_mode()
            else:
                print('>> 비밀번호를 틀렸습니다.')

    def manager_mode(self):
        manager_mode = """
        -----------매니저 관리 모드------------
        1. 매출 정보 조회
        2. 매출 정보 엑셀내보내기
        0. 종료  
        -------------------------------------
        선택:                      """
        while True:
            manager_choice = input(manager_mode)
            match manager_choice:
                # 매출 정보 조회
                case '1':
                    self.stbk_service.find_all()
                    print('😀😀매출정보를 불러왔습니다.😀😀')

                # 매출 액셀로 내보내기
                case '2':
                    stbks = self.stbk_service.find_all()
                    self.stbk_service.push(stbks)
                case '0':
                    return
                case _:
                    print('>> 잘못 선택 하셨습니다.')



    def main_menu(self):

        shopping_bag=[]

        menu_str = """
----------메뉴---------
1. Coffee (커피)
2. Non-Coffee (음료)
3. Blended (블렌디드)
0. 주문 종료
----------------------
선택: """
        while True:
            choice = input(menu_str)

            match choice:
                # 커피
                case '1':
                    order = self.coffee_menu()
                    shopping_bag.append(order)

                # 논커피
                case '2':
                    order = self.noncoffee_menu()
                    shopping_bag.append(order)

                # 블렌디드
                case '3':
                    order = self.blended_menu()
                    shopping_bag.append(order)

                case '0':
                    return

                case _:
                    print('>> 잘못 선택하셨습니다.')

            re_flag = input('\t더 주문하시겠어요? [y=1/n=0]')
            if re_flag == '0':
                # print(shopping_bag)
                break
        return shopping_bag

    def coffee_menu(self):
        add_on = 0
        coffee_menu_list = {
            1: ('아메리카노', 4500),
            2: ('카페라떼', 5000),
            3: ('돌체라떼', 5900),
            4: ('카페모카', 5500),
            5: ('캬라멜마끼아또', 5900)
        }
        coffee_menu_str = """
            ---------Coffee Menu--------
            1. 아메리카노 ======= 4500원
            2. 카페라떼 ========= 5000원
            3. 돌체라떼 ========= 5500원
            4. 바닐라 라떼 ====== 5500원
            5. 카라멜마키아토 ==== 5500원
            0. 이전으로 돌아가기
            ----------------------------          
            선택:  """

        menu_name = int(input(coffee_menu_str))

        if menu_name in coffee_menu_list:
            print(f'{coffee_menu_list[menu_name][0]}를 선택하셨습니다.')
            temp_list = ['HOT', 'ICED']
            temp = int(input("""
            ----HOT / ICED----
            1. HOT
            2. ICED (+500 원)    
            선택:    """))
            if temp == 2:
                add_on += 500

            qntt = int(input('\n수량을 입력해주세요\n'))

            swt_list = ['120%', '100%', '80%']
            swt = int(input('''
            ----당도----
            1. 더 달게(120% + 300원)
            2. 보통(100%)
            3. 덜 달게(80%)
            선택: '''))
            if swt == 1:
                add_on += 300

            # order.set_sugar_cnt(swt)
            size_list = ['Tall', 'Grande', 'Venti']
            size = int(input('''
            ----사이즈----
            1. Tall (+0 원)
            2. Grande (+700 원)
            3. Venti (+1000 원)
            선택: '''))
            if size == 2:
                add_on += 700
            elif size == 3:
                add_on += 1000

            print(
                f'{coffee_menu_list[menu_name][0]} {temp_list[temp - 1]} {qntt}개, 당도는 {swt_list[swt - 1]}, 사이즈는 {size_list[size - 1]}를 선택하셨습니다 ')

            order = Menu(coffee_menu_list[menu_name][0], Menu.set_temp(temp_list[temp -1]), Menu.set_size(size_list[size - 1]), Menu.set_quantity(qntt), Menu.set_sugar_cnt(swt), Menu.set_price((coffee_menu_list[menu_name][1] + add_on) * qntt)  )
            # # order.set_name(coffee_menu_list[menu_name][0])
            # order.set_temp(temp)
            # order.set_quantity(qntt)
            # order.set_size(size_list[size - 1])
            # order.set_sugar_cnt(swt)
            # order.set_price((coffee_menu_list[menu_name][1] + add_on) * qntt)
            return order

        elif menu_name == 0:
            return

        else:
            print('잘못 선택하셨습니다. 다시 선택해주세요')
            return self.coffee_menu()



    def noncoffee_menu(self):
        blended_menu_list = {
            1: ('녹차 라테', 6500),
            2: ('라이트 자몽 피지오', 5800),
            3: ('복숭아 아이스 티', 5900),
            4: ('딸기에이드', 5500),
            5: ('레몬에이드', 5500)
        }
        blended_menu_str = """
            ---------Blended Menu--------
            1. 녹차 라테             =========     6500 원
            2. 라이트 자몽 피지오     =========     5800 원
            3. 복숭아 아이스 티      =========     5900 원
            4. 딸기에이드           =========     5500 원
            5. 레몬에이드           =========     5500 원
            0. 이전으로 돌아가기
            ----------------------------          
            선택:>>"""

        re_flag = 1
        menu_name = int(input(blended_menu_str))
        add_on = 0

        if menu_name in blended_menu_list:
            print(f'{blended_menu_list[menu_name][0]}를 선택하셨습니다.')

            qntt = int(input('수량을 입력해 주세요\n>>'))

            swt_list = ['120%', '100%', '80%']

            swt = int(input('''

            ---- 당도를 입력해주세요 ---- 
            1=120% (+300)
            2=100%
            3=80%
            >>'''))

            if swt == 1:
                add_on += 300

            size_list = ['Tall', 'Grande', 'Venti']
            size = int(input(''' 
            ---- 사이즈를 입력해주세요. ----
            1 = Tall(+0)
            2 = Grande(+700)
            3 = Venti(+1000)
            >>'''))
            if size == 2:
                add_on += 700
            elif size == 3:
                add_on += 1000

            ice_list = ['Extra', 'Normal', 'Less']
            ice = int(input('''
            ---- 얼음양을 입력해주세요. ----
            1 = Extra
            2 = Normal
            3 = Less
            >>'''))
        elif menu_name == 0:
            return
        else:
            print('잘못 선택하셨습니다. 다시 선택해주세요')
            return self.blended_menu()

        print(
            f'{blended_menu_list[menu_name][0]} {qntt}개, 당도는 {swt_list[swt - 1]}, 사이즈는 {size_list[size - 1]}를 선택하셨습니다 ')

        order = StarBucks(blended_menu_list[menu_name][0])
        order.set_quantity(qntt)
        order.set_size(size_list[size - 1])
        order.set_amnt_ice(ice_list[ice - 1])
        order.set_sugar_cnt(swt_list[swt - 1])
        order.set_price((blended_menu_list[menu_name][1] + add_on) * qntt)

        return order




    def blended_menu(self):
        blended_menu_list = {
            1: ('녹차 프라투치노', 6500),
            2: ('자바칩 프라푸치노', 7000),
            3: ('피치 아사이 리프레셔', 6000),
            4: ('딸기 아사이 리프레셔', 6000),
            5: ('망고 리프레셔', 6000)
        }
        blended_menu_str = """
    ---------Blended Menu--------
    1. 녹차 프라푸치노          =========     6500 원
    2. 자바칩 프라푸치노        =========     7000 원
    3. 피치 아사이 리프레셔     =========     6000 원
    4. 딸기 아사이 리프레셔     =========     6000 원
    5. 망고 리프레셔           =========     6000 원
    0. 이전으로 돌아가기
    ----------------------------          
    선택:>>"""

        re_flag = 1
        menu_name = int(input(blended_menu_str))
        add_on = 0

        if menu_name in blended_menu_list:
            print(f'{blended_menu_list[menu_name][0]}를 선택하셨습니다.')

            qntt = int(input('\t수량을 입력해 주세요\n>>'))

            swt_list = ['120%', '100%', '80%']

            swt = int(input('''

    ---- 당도를 입력해주세요 ---- 
    1 = 더 달게 120% (+300원)
    2 = 보통 100%
    3 = 덜 달게 80%
    >>'''))

            if swt == 1:
                add_on += 300

            size_list = ['Tall', 'Grande', 'Venti']
            size = int(input(''' 
    ---- 사이즈를 입력해주세요. ----
    1 = Tall(+0원)
    2 = Grande(+700원)
    3 = Venti(+1000원)
    >>'''))
            if size == 2:
                add_on += 700
            elif size == 3:
                add_on += 1000

            ice_list = ['Extra', 'Normal', 'Less']
            ice = int(input('''
    ---- 얼음양을 입력해주세요. ----
    1 = Extra
    2 = Normal
    3 = Less
    >>'''))
        elif menu_name == 0:
            return
        else:
            print('잘못 선택하셨습니다. 다시 선택해주세요')
            return self.blended_menu()

        print(
            f'{blended_menu_list[menu_name][0]} {qntt}개, 당도는 {swt_list[swt - 1]}, 사이즈는 {size_list[size - 1]}를 선택하셨습니다 ')

        order = StarBucks(blended_menu_list[menu_name][0])
        # order.set_name(coffee_menu_list[menu_name][0])
        order.set_quantity(qntt)
        order.set_size(size_list[size - 1])
        order.set_amnt_ice(ice_list[ice - 1])
        order.set_sugar_cnt(swt_list[swt - 1])
        order.set_price((blended_menu_list[menu_name][1] + add_on) * qntt)
        return order
