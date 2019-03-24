from import_modules import *
from shop_window import *
from help_window import *


class Timer(QtCore.QTimer):
    def __init__(self, window, game_data):
        super().__init__(window)
        self.window = window
        self.game_data = game_data
        self.time_left = window.game_data.current_time
        self.timeout.connect(self.update_time_and_wave)
        self.start(1000)

    def update_time_and_wave(self):
        if self.game_data.game_is_over:
            return
        if self.time_left > 0:
            self.time_left -= 1

        if self.time_left != -1:
            minutes = int(self.time_left / 60)
            seconds = self.time_left - 60 * minutes
            self.window.timer_display.set_text("{}:".format(minutes)
                                               + "0" * (2 - len(str(seconds)))
                                               + "{}".format(seconds))
        else:
            if self.window.wave.is_enough_power():
                self.window.app.victory()
                self.victory()
            else:
                self.window.app.game_over()
                self.game_over()

        if self.time_left == 0:
            if not(self.window.wave.is_enough_power()):
                self.window.app.game_over()
                self.game_over()
            elif self.game_data.current_wave == 1:
                self.time_left = self.game_data.delay_wave2
                self.game_data.current_wave += 1
                self.window.wave.wave_is_over()
                self.game_data.current_light_numb_enemies = \
                    self.game_data.light_numb_wave2
                self.game_data.current_heavy_numb_enemies = \
                    self.game_data.heavy_numb_wave2
            elif self.game_data.current_wave == 2:
                self.time_left = self.game_data.delay_wave2
                self.game_data.current_wave += 1
                self.window.wave.wave_is_over()
                self.game_data.current_light_numb_enemies = \
                    self.game_data.light_numb_wave3
                self.game_data.current_heavy_numb_enemies = \
                    self.game_data.heavy_numb_wave3
            elif self.game_data.current_wave == 3:
                self.time_left = self.game_data.delay_wave2
                self.game_data.current_wave += 1
                self.window.wave.boss_is_coming()
                self.game_data.current_light_numb_enemies = \
                    self.game_data.light_numb_wave4
                self.game_data.current_heavy_numb_enemies = \
                    self.game_data.heavy_numb_wave4
            elif self.game_data.current_wave == 4:
                self.time_left = -1
                self.window.wave.wave_is_over()

        self.game_data.current_time = self.time_left

    def set_default(self):
        self.time_left = self.game_data.current_time

    def game_over(self):
        self.window.timer_display.set_text("Game over")

    def victory(self):
        self.window.timer_display.set_text("Victory!")


class ExitButton(QPushButton):
    def __init__(self, window):
        super().__init__("Exit", window)
        self.width = 85
        self.height = 25
        self.top = window.height - self.height - 5
        self.left = window.width - self.width - 5
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.clicked.connect(qApp.quit)


class TimerDisplay(QPushButton):
    def __init__(self, window):
        super().__init__(window)
        self.width = 85
        self.height = 25
        self.top = window.height - self.height - 5
        self.left = window.width - self.width - 95
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)

    def set_text(self, current_time):
        self.setText(current_time)


class ShopButton(QPushButton):
    def __init__(self, window, game_data):
        super().__init__("Shop", window)
        self.game_data = game_data
        self.width = 85
        self.height = 25
        self.top = window.height - self.height - 5
        self.left = window.width - self.width - 185
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.clicked.connect(window.app.open_shop)


class NewGameButton(QPushButton):
    def __init__(self, window, game_data):
        super().__init__("New game", window)
        self.width = 85
        self.height = 25
        self.top = window.height - self.height - 30
        self.left = window.width - self.width - 5
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.clicked.connect(game_data.set_default)
        self.clicked.connect(window.timer.set_default)


class Wave(QPushButton):
    def __init__(self, window, game_data):
        super().__init__(window)
        self.window = window
        self.game_data = game_data
        self.width = 85
        self.height = 25
        self.top = window.height - self.height - 30
        self.left = window.width - self.width - 95
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.display_wave)
        self.timer.start(1000)

    def display_wave(self):
        if self.game_data.current_wave == 4:
            self.setText("Boss battle")
        else:
            self.setText("Wave {}".format(self.game_data.current_wave))

    def wave_is_over(self):
        if self.game_data.current_wave == 4:
            self.setText("Boss battle is over")
        else:
            self.setText("Wave {} is over".format(self.game_data.current_wave))

    def boss_is_coming(self):
        self.setText("Boss is coming")

    def is_enough_power(self):
        hero_power = self.game_data.number_of_light_units + \
            self.game_data.number_of_heavy_units * 5
        enemy_power = self.game_data.current_light_numb_enemies + \
            self.game_data.current_heavy_numb_enemies * 5
        if hero_power >= enemy_power:
            return True
        else:
            return False


class HelpButton(QPushButton):
    def __init__(self, window, game_data):
        super().__init__("Help", window)
        self.game_data = game_data
        self.width = 85
        self.height = 25
        self.top = window.height - self.height - 30
        self.left = window.width - self.width - 185
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.clicked.connect(window.app.open_help)


class MainButton(QPushButton):
    def __init__(self, window, game_data):
        super().__init__("Click", window)
        self.game_data = game_data
        self.width = 120
        self.height = 25
        self.top = window.height - self.height - 5
        self.left = 4
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.clicked.connect(self.main_button_clicked)

    def main_button_clicked(self):
        if not self.game_data.game_is_over:
            self.game_data.clicks += self.game_data.click_rate


class MainCounter(QLCDNumber):
    def __init__(self, window, game_data):
        self.game_data = game_data
        super().__init__(window)
        self.width = 119
        self.height = 25
        self.top = window.height - self.height - 30
        self.left = 4
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.setDigitCount(10)
        self.counter_update_timer = QtCore.QTimer()
        self.counter_update_timer.timeout.connect(self.display_clicks)
        self.counter_update_timer.start(100)
        self.auto_clicker_update_timer = QtCore.QTimer()
        self.auto_clicker_update_timer.timeout.connect(self.auto_clicker)
        self.auto_clicker_update_timer.start(
            100)

    def display_clicks(self):
        self.display(self.game_data.clicks)

    def auto_clicker(self):
        if not self.game_data.game_is_over:
            self.game_data.clicks += self.game_data.auto_clicker_rate * 0.1


class ClickRateDisplay(QLCDNumber):
    def __init__(self, window, game_data):
        self.game_data = game_data
        super().__init__(window)
        self.width = 120
        self.height = 25
        self.top = 30
        self.left = 4
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.setDigitCount(10)
        self.counter_update_timer = QtCore.QTimer()
        self.counter_update_timer.timeout.connect(
            self.display_click_rate)
        self.counter_update_timer.start(100)

    def display_click_rate(self):
        self.display(self.game_data.click_rate)


class ClickRateLabel(QLabel):
    def __init__(self, window):
        super().__init__(window)
        self.width = 119
        self.height = 25
        self.top = 5
        self.left = 5
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.setText("Points per click")
        self.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.setFrameStyle(QLabel.Box)


class AutoClickerRateDisplay(QLCDNumber):
    def __init__(self, window, game_data):
        self.game_data = game_data
        super().__init__(window)
        self.width = 120
        self.height = 25
        self.top = 85
        self.left = 4
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.setDigitCount(10)
        self.counter_update_timer = QtCore.QTimer()
        self.counter_update_timer.timeout.connect(
            self.display_auto_clicker_rate)
        self.counter_update_timer.start(100)

    def display_auto_clicker_rate(self):
        self.display(self.game_data.auto_clicker_rate)


class AutoClickerRateLabel(QLabel):
    def __init__(self, window):
        super().__init__(window)
        self.width = 119
        self.height = 25
        self.top = 60
        self.left = 5
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.setText("Auto clicker rate")
        self.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.setFrameStyle(QLabel.Box)


class NumberOfLightUnitsDisplay(QLCDNumber):
    def __init__(self, window, game_data):
        self.game_data = game_data
        super().__init__(window)
        self.width = 120
        self.height = 25
        self.top = 140
        self.left = 4
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.setDigitCount(10)
        self.counter_update_timer = QtCore.QTimer()
        self.counter_update_timer.timeout.connect(
            self.display_number_of_light_units)
        self.counter_update_timer.start(100)

    def display_number_of_light_units(self):
        self.display(self.game_data.number_of_light_units)


class NumberOfLightUnitsLabel(QLabel):
    def __init__(self, window):
        super().__init__(window)
        self.width = 119
        self.height = 25
        self.top = 115
        self.left = 5
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.setText("Light units alive")
        self.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.setFrameStyle(QLabel.Box)


class NumberOfHeavyUnitsDisplay(QLCDNumber):
    def __init__(self, window, game_data):
        self.game_data = game_data
        super().__init__(window)
        self.width = 120
        self.height = 25
        self.top = 195
        self.left = 4
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.setDigitCount(10)
        self.counter_update_timer = QtCore.QTimer()
        self.counter_update_timer.timeout.connect(
            self.display_number_of_heavy_units)
        self.counter_update_timer.start(100)

    def display_number_of_heavy_units(self):
        self.display(self.game_data.number_of_heavy_units)


class NumberOfHeavyUnitsLabel(QLabel):
    def __init__(self, window):
        super().__init__(window)
        self.width = 119
        self.height = 25
        self.top = 170
        self.left = 5
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.setText("Heavy units alive")
        self.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.setFrameStyle(QLabel.Box)


class HeroLightPic(QLabel):
    def __init__(self, window, game_data):
        super().__init__(window)
        self.game_data = game_data
        self.width = 132
        self.height = 108
        self.top = 4
        self.left = 130
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.counter_update_timer = QtCore.QTimer()
        self.counter_update_timer.timeout.connect(self.set_pic)
        self.counter_update_timer.start(100)

    def set_pic(self):
        self.setPixmap(QPixmap(
            "img/hero_light{}.png".format(
                self.game_data.number_of_light_units)))


class HeroHeavyPic(QLabel):
    def __init__(self, window, game_data):
        super().__init__(window)
        self.game_data = game_data
        self.width = 132
        self.height = 108
        self.top = 112
        self.left = 130
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.set_pic)
        self.timer.start(100)

    def set_pic(self):
        self.setPixmap(QPixmap(
            "img/hero_heavy{}.png".format(
                self.game_data.number_of_heavy_units)))


class EnemyLightPic(QLabel):
    def __init__(self, window):
        super().__init__(window)
        self.window = window
        self.width = 132
        self.height = 108
        self.top = 4
        self.left = 262
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.set_pic)
        self.timer.start(100)

    def set_pic(self):
        if self.window.game_data.current_wave == 1:
            self.setPixmap(QPixmap(
                "img/enemy_light{}.png".format(
                    self.window.game_data.light_numb_wave1)))
        if self.window.game_data.current_wave == 2:
            self.setPixmap(QPixmap(
                "img/enemy_light{}.png".format(
                    self.window.game_data.light_numb_wave2)))
        if self.window.game_data.current_wave == 3:
            self.setPixmap(QPixmap(
                "img/enemy_light{}.png".format(
                    self.window.game_data.light_numb_wave3)))
        if self.window.game_data.current_wave == 4:
            self.setPixmap(QPixmap("img/boss1.png"))


class EnemyHeavyPic(QLabel):
    def __init__(self, window):
        super().__init__(window)
        self.window = window
        self.width = 132
        self.height = 108
        self.top = 112
        self.left = 262
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.set_pic)
        self.timer.start(100)

    def set_pic(self):
        if self.window.game_data.current_wave == 1:
            self.setPixmap(QPixmap(
                "img/enemy_heavy{}.png".format(
                    self.window.game_data.heavy_numb_wave1)))
        if self.window.game_data.current_wave == 2:
            self.setPixmap(QPixmap(
                "img/enemy_heavy{}.png".format(
                    self.window.game_data.heavy_numb_wave2)))
        if self.window.game_data.current_wave == 3:
            self.setPixmap(QPixmap(
                "img/enemy_heavy{}.png".format(
                    self.window.game_data.heavy_numb_wave3)))
        if self.window.game_data.current_wave == 4:
            self.setPixmap(QPixmap("img/boss2.png"))


class Frame(QLabel):
    def __init__(self, window):
        super().__init__(window)
        self.width = 265
        self.height = 218
        self.top = 3
        self.left = 130
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.setFrameStyle(QLabel.Box)


class MainWindow(QMainWindow):
    def __init__(self, app, game_data):
        super().__init__()
        self.app = app
        self.game_data = game_data
        self.top = 0
        self.left = 0
        self.left = 0
        self.width = 400
        self.height = 300
        self.title = "Hard Commando Clicker"
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width,
                          self.height)
        self.move(self.left, self.top)

        # pictures
        self.hero_light_pic = HeroLightPic(self, self.game_data)
        self.hero_heavy_pic = HeroHeavyPic(self, self.game_data)
        self.enemy_light_pic = EnemyLightPic(self)
        self.enemy_heavy_pic = EnemyHeavyPic(self)

        # frame
        self.frame = Frame(self)

        # main counter
        self.main_counter = MainCounter(self, self.game_data)

        # game_timer
        self.timer = Timer(self, self.game_data)

        # buttons
        self.main_button = MainButton(self, self.game_data)
        self.shop_button = ShopButton(self, self.game_data)
        self.exit_button = ExitButton(self)
        self.timer_display = TimerDisplay(self)
        self.help_button = HelpButton(self, self.game_data)
        self.new_game_button = NewGameButton(self, self.game_data)
        self.wave = Wave(self, self.game_data)

        # displays
        self.click_rate_display = ClickRateDisplay(self, self.game_data)
        self.auto_clicker_rate_display = AutoClickerRateDisplay(self,
                                                                self.game_data)
        self.heavy_units_display = NumberOfHeavyUnitsDisplay(self,
                                                             self.game_data)
        self.light_units_display = NumberOfLightUnitsDisplay(self,
                                                             self.game_data)

        # labels
        self.click_rate_label = ClickRateLabel(self)
        self.auto_clicker_rate_label = AutoClickerRateLabel(self)
        self.click_rate_label1 = NumberOfHeavyUnitsLabel(self)
        self.auto_clicker_rate_label1 = NumberOfLightUnitsLabel(self)

        self.show()

    def __del__(self):
        qApp.quit()
