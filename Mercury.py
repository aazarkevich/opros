import libscrc
import datetime


class Mercury:
    """
    Формат запрос на взаимодействие с меркурий 230:
    Сетевой адрес(1 байт) + Код запроса(1 байт) + CRC(2 байта)
    """
    COMMANDS_MERCURY = {'autorization': r"\x01\x01\x01\x01\x01\x01\x01\01",  # запрос на авторизацию
                        'energy_reset_and_power_sum': r"\x05\x00\x00",  # запрос на сумму энергии и мощности
                        'energy_day': r"\x05\x40\x00",  # запрос начало тек суток
                        '3': r"\x06\x02\x06\xa6\x10"}

    def __init__(self, serial_number: str):
        """Серийный номер счетчика"""
        if not isinstance(serial_number, str):
            raise TypeError(str(type(serial_number)) + ' can not cast to str ')
        self.serial_number = serial_number
        network_adress = self._serial_number_to_networ_adress(serial_number)
        self.network_adress_hex = self._converted_decimal_to_hex(network_adress)

    def _serial_number_to_networ_adress(self, serial_number):
        """Нахождение сетевого адреса счетчика из серийного номера"""
        if len(serial_number) <= 3:
            network_adress = serial_number
        elif int(serial_number[-3:]) > 240:
            network_adress = serial_number[-2:]
        else:
            network_adress = serial_number[-3:]
        return network_adress

    def _converted_decimal_to_hex(self, decimal):
        if int(decimal) <= 15:
            result = r'\x0' + str(hex(int(decimal)))[2:6]  # перевод серийного номера из 10 -> 16
        else:
            result = r'\x' + str(hex(int(decimal)))[2:6]

        return result

    @staticmethod
    def str_to_byte(string):
        """перевод из strByte -> Byte"""
        string = string.encode()
        string = string.decode('unicode-escape').encode('ISO-8859-1')
        return string

    def _crc(self, command: str):
        """генерация CRC протокола"""
        networ_adress_byte = self.str_to_byte(self.network_adress_hex + command)
        crc16 = str(hex(libscrc.modbus(networ_adress_byte))[2:6])
        if len(crc16) < 4:
            crc16 = '0' + crc16
        query = self.network_adress_hex + command + r'\x' + crc16[2:4] + r'\x' + crc16[0:2]
        query_byte = self.str_to_byte(query)
        return query_byte



    @property
    def autorization(self):
        """Код запроса для авторизации"""
        return self._crc(self.COMMANDS_MERCURY['autorization'])

    @property
    def energy_reset_and_power_sum(self):
        return self._crc(self.COMMANDS_MERCURY['energy_reset_and_power_sum'])

    @property
    def energy_day(self):
        return self._crc(self.COMMANDS_MERCURY['energy_day'])


# mercury = Mercury('123456189')
# print(mercury.energy_reset_sum_and_power_sum)
# print(type(mercury.network_adress))
# print(mercury.COMMANDS_MERCURY['autorization'])
# print(Mercury.str_to_byte(mercury.COMMANDS_MERCURY['autorization']))
# b'\xbd\x01\x01\x01\x01\x01\x01\x01\x01\x1a\xd6'
