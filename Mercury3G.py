from serial import Serial
import time
import libscrc


# ser = serial.Serial('COM4', 9600, timeout=10)
class Mercury3G:

    def __init__(self, port, baudrate=9600, timeout=10):
        self.serial = Serial(port, baudrate, timeout)

    def show(self):
        print('123')


mercury = Mercury3G()
mercury.show()

# def call():
#     # number = "+7"
#     # message = "Hello World"
#
#     moxa = serial.Serial("COM4", 9600, timeout=10)
#     # phone.open()
#     moxa.isOpen()
#     try:
#         time.sleep(1)
#         # moxa.write(b'\x41\x54\x5A\x0D')
#         moxa.write(b'ATZ\r')
#         time.sleep(1)
#         moxa.write(b'ATE0\r')
#         time.sleep(1)
#         moxa.write(b'ATE0\r')
#         time.sleep(1)
#         moxa.write(b'ATE0\r')
#         time.sleep(1)
#         moxa.write(b'AT+CBST=71,0,1')
#         time.sleep(1)
#         moxa.write(b'ATD9298015730')
#         time.sleep(1)
#         moxa.write(bytes([26]))
#         time.sleep(1)
#         print(moxa.read(64))
#     finally:
#         moxa.close()
# call()

# def sms():
#     recipient = "+79185800000"
#     message = "Hello World"
#
#     phone = serial.Serial("COM4", 9600, timeout=10)
#     # phone.open()
#     phone.isOpen()
#     try:
#         time.sleep(1)
#         phone.write(b'ATZ\r')
#         time.sleep(1)
#         phone.write(b'AT+CMGF=1\r')
#         time.sleep(1)
#         phone.write(b'AT+CMGS="' + recipient.encode() + b'"\r')
#         time.sleep(1)
#         phone.write(message.encode() + b"\r")
#         time.sleep(1)
#         phone.write(bytes([26]))
#         time.sleep(1)
#         print(phone.read(64))
#     finally:
#         phone.close()
# print(bytes([26]))
# str_b = bytes(b'AT+CBST=71,0,1')
# print(bytes(str))
# for i in str_b:
#     print(i)
# print(b'AT+CBST=71,0,1')

# print(b'41542B434253543D37312C302C310D'.decode())
# print('\r'.encode())
