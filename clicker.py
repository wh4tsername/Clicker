from import_modules import *
from main_window import *
from shop_window import *
from help_window import *
from game_over_window import *
from victory_window import *


# 1) saving and loading game_data from file (useless due to play time) -
# 2) global timer and waves(timing) +
# 3) waves conditions +
# 4) graphics(main, shop) +
# 5) in-game economy +


class GameData:
    def __init__(self):
        # constants
        self.price_inc_rate = 2.25
        self.price_inc_rate_light_units = 1.5
        self.delay_wave1 = 90
        self.delay_wave2 = 90
        self.delay_wave3 = 90
        self.delay_wave4 = 120

        # wave conditions
        self.light_numb_wave1 = 2
        self.heavy_numb_wave1 = 0
        self.light_numb_wave2 = 6
        self.heavy_numb_wave2 = 1
        self.light_numb_wave3 = 3
        self.heavy_numb_wave3 = 3
        self.light_numb_wave4 = 8
        self.heavy_numb_wave4 = 3

        # non-const
        self.game_is_over = False
        self.clicks = 0
        self.click_rate = 1
        self.auto_clicker_cost = 700
        self.auto_clicker_rate = 0
        self.increase_rate_cost = 150
        self.number_of_light_units = 0
        self.light_unit_cost = 50
        self.number_of_heavy_units = 0
        self.heavy_unit_cost = 300
        self.current_wave = 1
        self.current_time = self.delay_wave1
        self.current_light_numb_enemies = self.light_numb_wave1
        self.current_heavy_numb_enemies = self.heavy_numb_wave1

    def set_default(self):
        self.game_is_over = False
        self.clicks = 0
        self.click_rate = 1
        self.auto_clicker_cost = 700
        self.auto_clicker_rate = 0
        self.increase_rate_cost = 150
        self.number_of_light_units = 0
        self.light_unit_cost = 50
        self.number_of_heavy_units = 0
        self.heavy_unit_cost = 300
        self.current_wave = 1
        self.current_time = self.delay_wave1
        self.current_light_numb_enemies = self.light_numb_wave1
        self.current_heavy_numb_enemies = self.heavy_numb_wave1


class App(QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.game_data = GameData()
        self.window = MainWindow(self, self.game_data)

    def open_shop(self):
        self.shop_window = ShopWindow(self.game_data)

    def open_help(self):
        self.help_window = HelpWindow()

    def game_over(self):
        self.game_data.game_is_over = True
        self.game_over_window = GameOverWindow()

    def victory(self):
        self.game_data.game_is_over = True
        self.victory_window = VictoryWindow()


if __name__ == "__main__":
    clicker = App()
    sys.exit(clicker.exec_())
