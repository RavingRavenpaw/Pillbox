class Adafruit_CharLCD(object):
    """Class to simply pass on all LCD related commands."""

    def __init__(self):
        pass

    def Adafruit_CharLCD(self, rs=1, en=2, d4=3, d5=4, d6=5, d7=6, cols=16, lines=2, backlight=None,
                    invert_polarity=True,
                    enable_pwm=False,
                    gpio="whatever!",
                    pwm="nope!",
                    initial_backlight=1.0):
        pass

    def home(self):
        pass

    def clear(self):
        pass

    def set_cursor(self, col, row):
        pass

    def enable_display(self, enable):
        pass

    def show_cursor(self, show):
        pass

    def blink(self, blink):
        pass

    def move_left(self):
        pass

    def move_right(self):
        pass

    def set_left_to_right(self):
        pass

    def set_right_to_left(self):
        pass

    def autoscroll(self, autoscroll):
        pass

    def message(self, text):
        pass

    def set_backlight(self, backlight):
        pass

    def write8(self, value, char_mode=False):
        pass

    def create_char(self, location, pattern):
        pass

    def _pulse_enable(self):
        pass

    def _pwm_duty_cycle(self, intensity):
        pass
