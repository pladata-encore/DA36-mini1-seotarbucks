from stbk_entity import Menu
import pickle



class StarBucks_Repository:

    def __init__(self):
        print('StarBucksRepository 인스턴스가 생성되었습니다.')

        try:
            with open('seotabucks.pkl', 'rb') as f:
                self.stbks = pickle.load(f)

                if len(self.stbks) > 0:
                    # Diary.next_id 값을 마지막 일기 아이디 +1로 지정
                    Menu.next_id = self.stbks[-1].get_id() + 1

                print('> diary.pickle이 로드되었습니다.')
        except FileNotFoundError:
            # 파일이 존재하지 않는 경우
            self.stbks = []

    def __del__(self):
        """
        소멸자 메소드 : 인스턴스가 메모리에서 해제될때 호출되는 메소드
        """
        with open('diary.pkl', 'wb') as f:
            pickle.dump(self.stbks, f)
            print('❤️❤️매출내역을 성공적으로 저장했습니다. 다음에 만나요❤️❤️')


    def find_all(self):
        return self.stbks