import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import uic
from ex import DataManager

data_manager = DataManager()

class second(QDialog):
    def __init__(self, team_1, team_2):
        super().__init__()
        self.ui = uic.loadUi("second_ui.ui", self)

        self.team_1 = team_1
        self.team_2 = team_2

        # 초기값 지정
        self.one = 0
        self.two = 0


        self.show()

    def per(self):
        win_lose_1 = []
        win_lose_2 = []

        for i in range(5):
            win_lose_1.append(data_manager.show_data(self.team_2[i],self.team_1[i]))
            win_lose_2.append(data_manager.show_data(self.team_1[i],self.team_2[i]))

        # 승률 출력
        self.top_win.setText(f'{self.team_1[0]} {win_lose_1[0]}% vs {self.team_2[0]} {win_lose_2[0]}%')
        self.jun_win.setText(f'{self.team_1[1]} {win_lose_1[1]}% vs {self.team_2[1]} {win_lose_2[1]}%')
        self.mid_win.setText(f'{self.team_1[2]} {win_lose_1[2]}% vs {self.team_2[2]} {win_lose_2[2]}%')
        self.ad_win.setText(f'{self.team_1[3]} {win_lose_1[3]}% vs {self.team_2[3]} {win_lose_2[3]}%')
        self.sup_win.setText(f'{self.team_1[4]} {win_lose_1[4]}% vs {self.team_2[4]} {win_lose_2[4]}%')

        # 팀 승 출력
        self.win_1.setText(f'{self.one}')
        self.win_2.setText(f'{self.two}')

        

    def win(self):
        self.one += 1
        self.win_1.setText(f'{self.one}')

        for i in range(5):
            # 기존 데이터 로드
            data_manager.load_from_excel('data.xlsx')
            data_manager.fix_data_win(self.team_2[i])
            data_manager.fix_data_lose(self.team_1[i])
            data_manager.save_to_excel('data.xlsx')

    def lose(self):
        self.two += 1
        self.win_2.setText(f'{self.two}')

        for i in range(5):
            # 기존 데이터 로드
            data_manager.load_from_excel('data.xlsx')
            data_manager.fix_data_win(self.team_1[i])
            data_manager.fix_data_lose(self.team_2[i])
            data_manager.save_to_excel('data.xlsx')

class first(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("first_ui.ui", self)

    def slot(self):
        # 두번째 창 실행
        team_1 = []
        team_2 = []

        # 팀원 이름 입력
        team_1.append(self.top_1.text())
        team_1.append(self.jun_1.text())
        team_1.append(self.mid_1.text())
        team_1.append(self.ad_1.text())
        team_1.append(self.sup_1.text())

        team_2.append(self.top_2.text())
        team_2.append(self.jun_2.text())
        team_2.append(self.mid_2.text())
        team_2.append(self.ad_2.text())
        team_2.append(self.sup_2.text())

        for i in range(5):
            # 기존 데이터 로드
            data_manager.load_from_excel('data.xlsx')
            data_manager.add_data(team_1[i], team_2[i])
            data_manager.add_data(team_2[i], team_1[i])
            data_manager.save_to_excel('data.xlsx')

        self.w = second(team_1, team_2)
        self.w.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = first()
    window.show()
    sys.exit(app.exec_())
