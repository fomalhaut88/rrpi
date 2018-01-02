import warnings

try:
    import RPi.GPIO as GPIO
except ImportError:
    warnings.warn("module RPi.GPIO not imported")


def set_bcm_mode():
    GPIO.setmode(GPIO.BCM)


def set_board_mode():
    GPIO.setmode(GPIO.BOARD)


def clean_up():
    GPIO.cleanup()


def get_gpio_value(value):
    return GPIO.HIGH if value else GPIO.LOW


class PinError(Exception):
    pass


class Pin:
    used = set()

    def __init__(self, number):
        if number in self.__class__.used:
            raise PinError("pin {} already in use".format(number))

        self._number = number
        self.__class__.used.add(number)

    def __del__(self):
        self.__class__.used.remove(self._number)

        if not self.__class__.used:
            clean_up()

    @property
    def number(self):
        return self._number


class PinOut(Pin):
    def __init__(self, number, initial=0):
        super().__init__(number)
        gpio_initial = get_gpio_value(initial)
        GPIO.setup(number, GPIO.OUT, initial=gpio_initial)

    def set(self, value):
        gpio_value = get_gpio_value(value)
        GPIO.output(self._number, gpio_value)


class PinIn(Pin):
    def __init__(self, number):
        super().__init__(number)
        GPIO.setup(number, GPIO.IN)

    def get(self):
        return int(GPIO.input(self._number))
