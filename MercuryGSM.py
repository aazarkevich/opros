from serial import Serial
import time
from Mercury import Mercury


# ser = serial.Serial('COM4', 9600, timeout=10)
class MercuryGSM(Mercury):

    def __init__(self, serial_number, number_phone):
        super().__init__(serial_number=serial_number)
        self.number_phone = number_phone
        self.serial = Serial("COM4", 9600, timeout=20)

    @property
    def __generation_querys_connections(self):
        connection = {'ATZ': b'ATZ\r',
                      'ATE0': b'ATE0\r',
                      'AT+CBST': b'AT+CBST=71,0,1\r',
                      'ATD': b'ATD' + self.number_phone.encode() + b'\r'
                      }
        return connection

    def connection(self):
        for query in self.__generation_querys_connections.values():
            self.serial.write(query)
            time.sleep(1)
            self.serial.read(64)
            time.sleep(1)

    def close(self):
        self.serial.close()

    def get_values_and_power(self):
        self.connection()
        self.serial.write(self.autorization)
        time.sleep(1)
        self.serial.read(1024)
        time.sleep(1)
        self.serial.write(self.energy_reset_and_power_sum)
        data = self.serial.read(1024)
        self.close()
        return dict(values=self._converted_values_to_string(data), power=self._converted_power_to_string(data))

    def _converted_values_to_string(self, data_byte):
        values_hex = data_byte[2:3] + data_byte[1:2] + data_byte[4:5] + data_byte[3:4]  #
        values = int.from_bytes(values_hex, byteorder='big')  # перевод из 16 -> 10 целой части
        values = float(values / 1000)
        return str(values)

    def _converted_power_to_string(self, data_byte):
        power_hex = data_byte[10:11] + data_byte[9:10] + data_byte[12:13] + data_byte[11:12]  # реактивная мощность
        power = int.from_bytes(power_hex, byteorder='big')  #
        power = float(power / 1000)
        return str(power)


mercury = MercuryGSM(serial_number='27', number_phone='89298015730')

# mercury.show()
print(mercury.get_values_and_power())
# print(mercury.energy_reset_and_power_sum)
# foo = b'\x1B\x09\x00\x59\xEE\x02\x00\xB6\x08\x06\x00\x3F\xF1\x00\x00\x52\x98\x40\x52'
# print(mercury.converted_values_to_string(foo))
# foo = str(b'\x1b\x05\xcbC')
# bar = foo.split('\\')
# print(foo.split('\\'))
# print(int.from_bytes(b'\xcbC\x05', byteorder='big'))

# b'\x1b\x05\xcbC'
# 133.05155
