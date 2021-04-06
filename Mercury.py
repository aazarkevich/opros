import libscrc
import datetime


class Mercury:
    COMMANDS_MERCURY = {'autorization': r"\x01\x01\x01\x01\x01\x01\x01\01",  # запрос на авторизацию
                        'energy_reset_sum_and_power_sum': r"\x05\x00\x00",  # запрос на сумму энергии и мощности
                        'energy_day': r"\x05\x40\x00",  # запрос начало тек суток
                        '3': r"\x06\x02\x06\xa6\x10"}

    def __init__(self, serial_number: str):
        self.serial_number = serial_number
        self.network_adress = self.__serial_number_to_networ_adress(serial_number)

    def __serial_number_to_networ_adress(self, serial_number):
        """Нахождение сетевого адреса счетчика из серийного номера"""
        if len(serial_number) <= 3:
            network_adress = serial_number
        elif int(serial_number[-3:]) > 240:
            network_adress = serial_number[-2:]
        else:
            network_adress = serial_number[-3:]
        return network_adress

# mercury = Mercury('123456189')
# print(mercury.network_adress)
# print(mercury.COMMANDS_MERCURY['autorization'])
