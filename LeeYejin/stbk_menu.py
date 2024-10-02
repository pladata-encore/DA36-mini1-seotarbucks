from stbk_service import StarBucks_Service
class StarBucks_Menu:
    def __init__(self):
        self.stbk_service = StarBucks_Service()
    def main_menu(self):
        menu_str = """
----------메뉴---------
1. Coffee (커피)
2. Non-Coffee (음료)
0. 주문 종료
----------------------
선택:        """
        while True:
            choice = input(menu_str)

            match choice:
                # 커피
                case '1':
                    self.stbk_service.coffee_menu()

                # 논커피
                case '2':
                    pass

                # 관리자 모드 실행
                case '-1':
                    password = input('>> 관리자 모드를 실행합니다.\n비밀번호를 입력하세요.\n비밀번호 :')
                    manager_password = '1234'
                    if password == manager_password:
                        self.manager_mode()
                    else:
                        print('>> 비밀번호를 틀렸습니다.')

                case '0':
                    return

                case _:
                    print('>> 잘못 선택하셨습니다.')

    def print_stbks(self, stbks):
        if len(stbks) > 0:
            print(f'{'-'*10}0000년 00월 00일 매출전표{'-'*10}')
            for stbk in stbks:
                print(f'{stbk}')
                # print(f'{stbk.get_id()}\t{stbk.get_name()}\t{stbk.get_price()}')
        else:
            print('😥😥조회된 결과가 없습니다.😥😥')












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
                    self.print_stbks(stbks)
                    print('😀😀매출정보를 불러왔습니다.😀😀')
                # 매출 액셀로 내보내기
                case '2':
                    stbks = self.stbk_service.find_all()
                    self.stbk_service.push(stbks)
                case '0':
                    return
                case _:
                    print('>> 잘못 선택 하셨습니다.')


