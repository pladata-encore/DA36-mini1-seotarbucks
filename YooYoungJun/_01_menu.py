'''
# Coffee 카테고리
kiosk.add_menu_item(Beverage("아메리카노", 4500, "Coffee"))
kiosk.add_menu_item(Beverage("카페라떼", 5000, "Coffee"))
kiosk.add_menu_item(Beverage("돌체라떼", 5900, "Coffee"))
kiosk.add_menu_item(Beverage("카페모카", 5500, "Coffee"))
kiosk.add_menu_item(Beverage("바닐라라떼", 5500, "Coffee"))


# Non-Caffeine 카테고리
kiosk.add_menu_item(Beverage("허니 레몬티", 5000, "Non-Caffeine"))
kiosk.add_menu_item(Beverage("유자차", 5500, "Non-Caffeine"))
kiosk.add_menu_item(Beverage("피지오", 5900, "Non-Caffeine"))
kiosk.add_menu_item(Beverage("초코", 5500, "Non-Caffeine"))
kiosk.add_menu_item(Beverage("오렌지쥬스", 5000, "Non-Caffeine"))

# Blended 카테고리
kiosk.add_menu_item(Beverage("망고 블렌디드", 6000, "Blended"))
kiosk.add_menu_item(Beverage("딸기 요거트 블렌디드", 6500, "Blended"))
kiosk.add_menu_item(Beverage("제주그린티 프라프치노", 6800, "Blended"))
kiosk.add_menu_item(Beverage("자바칩 프라프치노", 7000, "Blended"))
kiosk.add_menu_item(Beverage("피치 블렌디드", 7000, "Blended"))


# 커스텀

#샷
kiosk.add_custom(Customized("샷추가", 500, "Shot"))
kiosk.add_custom(Customized("연하게", 0, "Shot"))
kiosk.add_custom(customized("연하게", 0, "Shot"))



#얼음
kiosk.add_custom(customized("적게", 0, "ICED"))
kiosk.add_custom(customized("많게", 0, "ICED"))
#온도

kiosk.add_custom(customized("덜뜨겁게", 0, "temp"))
kiosk.add_custom(customized("더뜨겁게", 0, "temp"))

#사이즈
kiosk.add_custom(customized("톨", 0, "size"))
kiosk.add_custom(customized("그란데", 0, "size"))
kiosk.add_custom(customized("벤티", 0, "size"))

#당도
kiosk.add_custom(customized("덜달게", 0, "sugar_cnt"))
kiosk.add_custom(customized("더달게", 0, "sugar_cnt"))

# 컵(텀블러 유무) - cup
kiosk.add_custom(customized("개인컵", 0, "cup"))
kiosk.add_custom(customized("일회용컵", 0, "cup"))
kiosk.add_custom(customized("매장컵", 0, "cup"))

디카페인 - decaffeine
kiosk.add_custom(customized("디카페인", 0, "caffeine"))

휘핑 - whipping
kiosk.add_custom(customized("없이", 0, "whipping"))
kiosk.add_custom(customized("적게", 0, "whipping"))
kiosk.add_custom(customized("많게", 0, "whipping"))
'''