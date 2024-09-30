# 미니 프로젝트1
# data convention : [카테고리, 상품명, 온도, 사이즈, 수량, togo, [옵션]]


class test:

    def __init__(self, menu, price, quantity):
        self.menu = menu
        self.price = price
        self.quantity = quantity

    def cal_total(self):
        return self.price * self.quantity



class discnt_page:

    skt = 0.1
    kt = 0.1
    lgu = 0.05
    members = {}
    order_nums = 1


    def __init__(self):
        pass


''' 통신사 확인
1. skt
2. kt
3. lgu
'''

    def calculation(self, carrier, total_price):
        match carrier:
            case '1':
                discount_price = total_price * discnt.skt
            case '2':
                discount_price = total_price * discnt.kt
            case '3':
                discount_price = total_price * discnt.lgu
            case _:
                print('잘못된 통신사입니다.')

    def payment(self):
        method = input('결제 수단을 선택하세요')

        match method:
            case '1':   # 신용카드
                print('카드를 칩 리더기에 넣어주세요')
            case '2':   # 현금결제
                print('카운터에서 결제 해주세요')
            case '3':   # 삼성, 애플 pay
                print('핸드폰을 테그에 접촉해주세요')
            case _:
                print('잘못된 선택입니다.')


    def membership(self):
            member = input('멤버쉽 있으신가요??')

            match member:
                case '1' :
                    cell_number = input('핸드폰 번호를 입력해주세요')        # try except 가능
                    add_point(cell_number)
                case '2':
                    mem_join = input('멤버쉽에 가입하시겠습니까? [y]/n')
                    if mem_join != 'n':

                        mem_number = input('핸드폰 번호를 입력해주세요')
                    else :
                        print('결제화면으로 이동합니다.')
                case _:
                    print('잘못누르셨습니다.')

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
results.append(result)
print(results)



