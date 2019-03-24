from import_modules import *


class ExitButton(QPushButton):
    def __init__(self, window):
        super().__init__("Exit shop", window)
        self.width = 70
        self.height = 25
        self.top = window.height - self.height - 5
        self.left = window.width - self.width - 5
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.clicked.connect(window.close)


class IncreaseRateButton(QPushButton):
    def __init__(self, window, game_data):
        super().__init__("Increase pts / click", window)
        self.game_data = game_data
        self.width = 120
        self.height = 25
        self.top = 85
        self.left = 5
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.clicked.connect(self.increase_rate_button_clicked)

    def increase_rate_button_clicked(self):
        if self.game_data.clicks >= self.game_data.increase_rate_cost\
                and not self.game_data.game_is_over:
            self.game_data.clicks -= self.game_data.increase_rate_cost
            self.game_data.increase_rate_cost = \
                int(self.game_data.increase_rate_cost *
                    self.game_data.price_inc_rate)
            self.game_data.increase_rate_cost -= \
                self.game_data.increase_rate_cost % 10
            if self.game_data.click_rate >= 15:
                self.game_data.click_rate += 5
            elif self.game_data.click_rate >= 5:
                self.game_data.click_rate += 2
            else:
                self.game_data.click_rate += 1


class IncreaseRateCostDisplay(QLCDNumber):
    def __init__(self, window, game_data):
        self.game_data = game_data
        super().__init__(window)
        self.width = 119
        self.height = 25
        self.top = 60
        self.left = 5
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.setDigitCount(10)
        self.counter_update_timer = QtCore.QTimer()
        self.counter_update_timer.timeout.connect(
            self.display_increase_rate_cost)
        self.counter_update_timer.start(100)

    def display_increase_rate_cost(self):
        self.display(self.game_data.increase_rate_cost)


class BuyAutoClickerButton(QPushButton):
    def __init__(self, window, game_data):
        super().__init__("Buy autoclicker", window)
        self.game_data = game_data
        self.width = 120
        self.height = 25
        self.top = 30
        self.left = 5
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.clicked.connect(self.auto_clicker_buy_button_clicked)

    def auto_clicker_buy_button_clicked(self):
        if self.game_data.clicks >= self.game_data.auto_clicker_cost\
                and not self.game_data.game_is_over:
            self.game_data.clicks -= self.game_data.auto_clicker_cost
            self.game_data.auto_clicker_cost = \
                int(self.game_data.auto_clicker_cost *
                    self.game_data.price_inc_rate)
            self.game_data.auto_clicker_cost -= \
                self.game_data.auto_clicker_cost % 10
            if self.game_data.auto_clicker_rate == 0:
                self.game_data.auto_clicker_rate = 3
            else:
                self.game_data.auto_clicker_rate *= 2


class AutoClickerCostDisplay(QLCDNumber):
    def __init__(self, window, game_data):
        self.game_data = game_data
        super().__init__(window)
        self.width = 119
        self.height = 25
        self.top = 5
        self.left = 5
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.setDigitCount(10)
        self.counter_update_timer = QtCore.QTimer()
        self.counter_update_timer.timeout.connect(
            self.display_autoclicker_cost)
        self.counter_update_timer.start(100)

    def display_autoclicker_cost(self):
        self.display(self.game_data.auto_clicker_cost)


class BuyLightUnitButton(QPushButton):
    def __init__(self, window, game_data):
        super().__init__("Buy light unit", window)
        self.game_data = game_data
        self.width = 120
        self.height = 25
        self.top = 140
        self.left = 5
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.clicked.connect(self.light_unit_buy_button_clicked)

    def light_unit_buy_button_clicked(self):
        if self.game_data.clicks >= self.game_data.light_unit_cost and \
                self.game_data.number_of_light_units < 8\
                and not self.game_data.game_is_over:
            self.game_data.clicks -= self.game_data.light_unit_cost
            self.game_data.light_unit_cost = \
                int(self.game_data.light_unit_cost *
                    self.game_data.price_inc_rate_light_units)
            self.game_data.light_unit_cost -= \
                self.game_data.light_unit_cost % 10
            self.game_data.number_of_light_units += 1


class LightUnitCostDisplay(QLCDNumber):
    def __init__(self, window, game_data):
        self.game_data = game_data
        super().__init__(window)
        self.width = 119
        self.height = 25
        self.top = 115
        self.left = 6
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.setDigitCount(10)
        self.counter_update_timer = QtCore.QTimer()
        self.counter_update_timer.timeout.connect(
            self.display_light_unit_cost)
        self.counter_update_timer.start(100)

    def display_light_unit_cost(self):
        self.display(self.game_data.light_unit_cost)


class BuyHeavyUnitButton(QPushButton):
    def __init__(self, window, game_data):
        super().__init__("Buy heavy unit", window)
        self.game_data = game_data
        self.width = 120
        self.height = 25
        self.top = 195
        self.left = 5
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.clicked.connect(self.heavy_unit_buy_button_clicked)

    def heavy_unit_buy_button_clicked(self):
        if self.game_data.clicks >= self.game_data.heavy_unit_cost and \
                self.game_data.number_of_heavy_units < 3 \
                and not self.game_data.game_is_over:
            self.game_data.clicks -= self.game_data.heavy_unit_cost
            self.game_data.heavy_unit_cost = \
                int(self.game_data.heavy_unit_cost *
                    self.game_data.price_inc_rate)
            self.game_data.heavy_unit_cost -= \
                self.game_data.heavy_unit_cost % 10
            self.game_data.number_of_heavy_units += 1


class HeavyUnitCostDisplay(QLCDNumber):
    def __init__(self, window, game_data):
        self.game_data = game_data
        super().__init__(window)
        self.width = 119
        self.height = 25
        self.top = 170
        self.left = 5
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.setDigitCount(10)
        self.counter_update_timer = QtCore.QTimer()
        self.counter_update_timer.timeout.connect(
            self.display_heavy_unit_cost)
        self.counter_update_timer.start(100)

    def display_heavy_unit_cost(self):
        self.display(self.game_data.heavy_unit_cost)


class LightUnitPic(QLabel):
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
            "img/light_units/light_unit{}.png".format(
                self.game_data.number_of_light_units + 1)))


class HeavyUnitPic(QLabel):
    def __init__(self, window, game_data):
        super().__init__(window)
        self.game_data = game_data
        self.width = 132
        self.height = 108
        self.top = 112
        self.left = 130
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.counter_update_timer = QtCore.QTimer()
        self.counter_update_timer.timeout.connect(self.set_pic)
        self.counter_update_timer.start(100)

    def set_pic(self):
        self.setPixmap(QPixmap(
            "img/heavy_units/heavy_unit{}.png".format(
                self.game_data.number_of_heavy_units + 1)))


class LightDescriptionPic(QLabel):
    def __init__(self, window):
        super().__init__(window)
        self.width = 132
        self.height = 108
        self.top = 4
        self.left = 262
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.setPixmap(QPixmap("img/light_units/light_unit_description.png"))


class LightDescriptionText(QLabel):
    def __init__(self, window):
        super().__init__(window)
        self.width = 132
        self.height = 108
        self.top = 4
        self.left = 262
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.setText("Power: 100 pts\nHealth: 100 hp")
        self.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


class HeavyDescriptionPic(QLabel):
    def __init__(self, window):
        super().__init__(window)
        self.width = 132
        self.height = 108
        self.top = 112
        self.left = 262
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.setPixmap(QPixmap("img/heavy_units/heavy_unit_description.png"))


class HeavyDescriptionText(QLabel):
    def __init__(self, window):
        super().__init__(window)
        self.width = 132
        self.height = 108
        self.top = 112
        self.left = 262
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.setText("Power: 500 pts\nHealth: 500 hp")
        self.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


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


class ShopWindow(QMainWindow):
    def __init__(self, game_data):
        super().__init__()
        self.game_data = game_data
        self.top = 0
        self.left = 400
        self.width = 400
        self.height = 300
        self.title = "Shop"
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width,
                          self.height)
        self.move(self.left, self.top)

        # pictures
        self.light_unit_pic = LightUnitPic(self, self.game_data)
        self.heavy_unit_pic = HeavyUnitPic(self, self.game_data)
        self.light_description_pic = LightDescriptionPic(self)
        self.heavy_description_pic = HeavyDescriptionPic(self)

        # text
        self.light_description_txt = LightDescriptionText(self)
        self.heavy_description_txt = HeavyDescriptionText(self)

        # frame
        self.frame = Frame(self)

        # buttons
        self.buy_auto_clicker_button = BuyAutoClickerButton(self, game_data)
        self.increase_rate_button = IncreaseRateButton(self, game_data)
        self.buy_light_unit_button = BuyLightUnitButton(self, game_data)
        self.buy_heavy_unit_button = BuyHeavyUnitButton(self, game_data)
        self.exit_button = ExitButton(self)

        # displays
        self.auto_clicker_cost_display = AutoClickerCostDisplay(self,
                                                                game_data)
        self.increase_rate_cost_display = IncreaseRateCostDisplay(self,
                                                                  game_data)
        self.light_unit_cost_display = LightUnitCostDisplay(self,
                                                            game_data)
        self.heavy_unit_cost_display = HeavyUnitCostDisplay(self,
                                                            game_data)

        self.show()
