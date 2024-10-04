from stbk_service import StarBucks_Service
from rich.table import Column, Table

table = Table(show_header=True, header_style="bold magenta")


class StarBucks_Menu:
    def __init__(self):
        self.stbk_service = StarBucks_Service()

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
                    order = self.stbk_service.coffee_menu()
                    shopping_bag.append(order)

                # 논커피
                case '2':
                    order = self.stbk_service.noncoffee_menu()
                    shopping_bag.append(order)

                # 블렌디드
                case '3':
                    order = self.stbk_service.blended_menu()
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
                    stbks = self.stbk_service.find_all()
                    print(stbks)
                    print('😀😀매출정보를 불러왔습니다.😀😀')
                # 매출 액셀로 내보내기
                case '2':
                    stbks = self.stbk_service.find_all()
                    self.stbk_service.push(stbks)
                case '0':
                    return
                case _:
                    print('>> 잘못 선택 하셨습니다.')