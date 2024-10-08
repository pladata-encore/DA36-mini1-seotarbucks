# DA36-mini1-seotarbucks


<!-- 유영준 start -->

2 . 목차설명
1. 개발과정
2. 요구사항 명세
3. 사용 코드 설명
4. 시연

배경 및 사전조사
키오스크


<!-- 유영준 end -->

<!-- 이예진 start -->
## **요구 사항 명세** 
### ~ 사용자 메뉴 ~

5. 커피, 논-커피 선택 시 Hot/Cold 옵션 화면을 보여주세요.
    1. 블렌디드 선택 시 Hot/Cold 옵션 화면을 보여주지 마세요.
6. Hot/Cold 옵션에서 Cold 선택 시 얼음 양을 선택하는 옵션 화면을 보여주세요.
    1. Cold 선택 시 가격이 500원 추가되게 해주세요.
7. 수량을 입력하는 옵션 화면을 보여주세요.
8. 당도, 사이즈를 입력하는 옵션 화면을 보여주세요.
	1. 당도 를 더 달게 하거나 사이즈를 업그레이드 하면 추가금이 발생하게 해주세요.
9. 옵션을 모두 선택하였다면 선택한 메뉴가 한번에 보이게 해주세요.
10. 메뉴를 추가로 선택할지 물어보는 창이 나오게 해주세요.
11. 메뉴 추가 시 3번부터 다시 실행되게 해주세요.
	1. 메뉴 추가가 없을 시 장바구니 화면을 보여주세요.
12. 장바구니를 확인 했다면 결제 화면을 보여주세요.
13. 결제 화면에서는 통신사 할인 여부를 선택하는 화면을 보여주세요.
	1. 통신사 할인 선택 시 할인이 적용된 결제 내역 화면을 보여주세요.
14. 확인이 완료되었다면 멤버쉽 적립 여부를 물어보는 화면을 보여주세요.
	1. 멤버쉽이 있다면 포인트 적립을 해주세요.
	2. 멤버쉽이 없다면 회원가입 여부를 물어봐 주세요.
	3. 회원가입을 원하시면 번호를 물어봐서 가입을 도와드리고 적립도 진행해 주세요.
15. 결제 수단을 물어보는 화면을 보여주세요.
16. 결제가 완료되면 주문 번호가 나온 후 키오스크가 종료되게 해주세요.


## **요구 사항 명세**  
### ~ 관리자 메뉴 ~
1. 카테고리 화면에서 화면에 표시되지는 않지만 특별한 키를 누르면 관리자 모드 화면을 보여주세요. 
2. 관리자 모드에 들어가기 위해서는 비밀번호를 입력하게 해주세요.
3. 비밀번호가 맞다면 **매출 정보 조회, 매출 정보 엑셀 내보내기, sort by, Statistics** 가 있는 관리자 모드가 나옵니다. 
    1. **매출정보 조회** 선택 시 주문 번호 순으로 정렬된 매출 내역을 보여주세요.
    2. **매출 정보 엑셀 내보내기** 선택 시 3-1번에 나온 정보를 엑셀로 만들어주세요.
    3. **Sort By** 선택 시 **메뉴명, Hot/Cold, to-go, 결제수단, 멤버쉽 회원, 통신사 할인**별로 정렬된 매출 내역을 보여주세요.
    4. **Statistics** 선택 시 **음료, 사이즈, Hot/Cold, 결제수단, 통신사할인, to-go**별로 매출내역 통계를 보여줍니다.


## **Flow Chart**
![img.png](img.png)

### class 별
![img_1.png](img_1.png)


<!-- 이예진 end -->

<!-- 김진수 start -->
## 4. 코드 구조
### 4.1 Welcome page.





<img src="welcome.png" alt="drawing" width="50%"/>

<!-- 김진수 end -->

## ☕서타벅스 시연영상☕
#### 팀원들의 유튜브에 올라온 영상과 같은 영상입니다.
[![서타벅스의 시연영상](data:image/png;base64,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)](https://youtu.be/PY3MDnb6CKo?si=PmUeraXGG7QE6KHl)

[유영준의 채널에서 보기](https://youtu.be/PY3MDnb6CKo?si=PmUeraXGG7QE6KHl)
<br>
[이예진의 채널에서 보기](https://www.youtube.com/watch?v=udePw6s6B4Y&t=28s)
<br>


## ☁️서타벅스 팀원들의 소감☁️


### 🔷 김진수

<br>

### 🔷 유영준

<br>

### 🔷 이예진

