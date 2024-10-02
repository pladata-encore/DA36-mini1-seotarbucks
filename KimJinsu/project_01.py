# 미니 프로젝트1
# data convention : [카테고리, 상품명, 온도, 사이즈, 수량, togo, [옵션]]


class test:

    def __init__(self, menu, price, quantity):
        self.menu = menu
        self.price = price
        self.quantity = quantity

    def cal_total(self):
        return self.price * self.quantity

class Main_menu:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


    def display_menu(self):
        menu = '''
1. 커피
2. 음료
3. 블랜디드
        '''
        choice = input(menu)
        match choice:
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass


    def input_order


        print('1. 아메리카노 \n2. 라떼')
        self.name = input('메뉴 선택 :')





class Shopping_bag:
    orders = []
    def __init__(self):
        pass

    def add_shopping_bag(self, order):
        Shopping_bag.orders.append(order)
        return 1






class discnt_page:

    skt = 0.1
    kt = 0.1
    lgu = 0.05
    members = {}
    order_nums = 1


    def __init__(self):
        pass

    def total_price_cal(self):
        total_price = 0
        for item in Shopping_bag.orders:
            total_price += item.price * item.quantity
        return total_price


    ''' 통신사 확인
    1. skt
    2. kt
    3. lgu
    '''

    def calculation(self, carrier, total_price): # 통신사 없을 시 추가 해야함

        match carrier:
            case '1':
                discount_price = total_price * discnt_page.skt
            case '2':
                discount_price = total_price * discnt_page.kt
            case '3':
                discount_price = total_price * discnt_page.lgu
            case _:
                print('잘못된 통신사입니다.')
                return 0

        return discount_price

    def payment(self):      # 1) 결제가능 제한시간, 2) 일정시간(3초) 후 결제완료 메세지 표출
        method = input('결제 수단을 선택하세요 1)신용카드 ,2)현금결제, 3)각종 pay')
        flag = 1

        match method:
            case '1':   # 신용카드
                print('카드를 칩 리더기에 넣어주세요')
            case '2':   # 현금결제
                print('카운터에서 결제 해주세요')
            case '3':   # 삼성, 애플 pay
                print('핸드폰을 테그에 접촉해주세요')
            case _:
                print('잘못된 선택입니다.')
                flag = 0

        if flag != 0:
            print('성장적으로 결제 되었습니다.')
        return flag


    def membership(self):
            member = input('멤버쉽 있으신가요?? 1. yes, 2. no')
            flag = 1

            match member:
                case '1' :
                    cell_number = input('핸드폰 번호를 입력해주세요')        # try except 가능
                    discnt_page.add_point(cell_number)
                case '2':
                    mem_join = input('멤버쉽에 가입하시겠습니까? [y]/n')
                    if mem_join != 'n':

                        mem_number = input('핸드폰 번호를 입력해주세요')
                    else :
                        print('결제화면으로 이동합니다.')
                case _:
                    print('잘못누르셨습니다.')
                    flag = 0

            return flag

    def add_point(self, cell_number):
        discnt_page.members[cell_number] += 1 # members : 멤버쉽 딕셔너리들, 값들은 숫자여야 함.
        print('적립이 완료 되었습니다.')

    def join_member(self,cell_number):
        discnt_page.members[cell_number] = 1    # 딕셔너리에 멤버 추가
        print('회원가입이 완료되었습니다.')

    def receipt(self):
        print('주문이 완료 되었습니다. 감사합니다.')
        discnt_page.order_nums += 1







tt = test('a',3000,3 )
result = tt.cal_total()

print(result)



