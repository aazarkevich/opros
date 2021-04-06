import socket
import libscrc
import datetime


class mercury:

    dictTabl = [["0", r"\x01\x01\x01\x01\x01\x01\x01\01"], # запрос на авторизацию
                ['1', r"\x05\x00\x00"],# запрос на сумму энергии и мощности
                ['2', r"\x05\x40\x00"],
                ['3',r"\x06\x02\x06\xa6\x10"]]
    __energy = 0
    an_exception = {'7098469': '169','105334': '134'}
    def __init__(self, id, ip,port):
        self.serial_number = id
        for i in self.an_exception:
            if id == i:
                id = self.an_exception[i]
            
        # print(123)
        if len(id) <= 3:
            id = id
        elif int(id[-3:]) > 240:
            id = id[-2:]
        else:
            id = id[-3:]

        if int(id) <= 15:
            self.id = r'\x0' + str(hex(int(id)))[2:6] # перевод серийного номера из 10 -> 16
        else:
            self.id = r'\x' + str(hex(int(id)))[2:6]
        self.ip = ip
        self.port = port
        # self.kef = kef
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__sock.connect((self.ip, self.port))

    def __strToByte(self, string): # перевод из strByte -> Byte
        string = string.encode()
        string = string.decode('unicode-escape').encode('ISO-8859-1')
        return string

    def crcProtokol(self, zaprosStr): # CRC протокол
        zaprosIdStr = self.id + zaprosStr
        zaprosIdByte = self.__strToByte(zaprosIdStr)
        crc16 = str(hex(libscrc.modbus(zaprosIdByte))[2:6])
        if len(crc16) < 4:
            crc16 = '0' + crc16
        zaprosIdStr += r'\x' + crc16[2:4] + r'\x' + crc16[0:2]
        # print(zaprosIdStr)
        zaprosId = self.__strToByte(zaprosIdStr)
        return zaprosId

    def connect(self, kodZapros):
        autoRiz = self.crcProtokol(self.dictTabl[0][1])
        if kodZapros == 0:
            return self.executeZapros(autoRiz)

        if kodZapros == 1:
            zapros = self.crcProtokol(self.dictTabl[2][1])
            d1 = self.executeZapros(autoRiz) # Ответ на авторизацию
            data = self.executeZapros(zapros) # Ответ на показания на текущие сутки
            d2 = self.executeZapros(self.crcProtokol(self.dictTabl[1][1])) #ответ на показания от сброса
            return self.serial_number, self.energy_reset_sum(d2,0), self.power_sum(d2,0), self.energy_reset_sum(d2,1) - self.energy_reset_sum(data, 1), \
                   self.energy_reset_sum(data, 1), self.power_sum(data, 1),'-',datetime.datetime.now().strftime("%m-%d-%Y") # '-' - отображение ошибки

        if kodZapros == 2:
            zaprosStr = self.dictTabl[kodZapros][1]
            zapros = self.crcProtokol(zaprosStr)
            d1 = self.executeZapros(autoRiz) # Ответ на авторизацию
            data = self.executeZapros(zapros) # ответ на запрос показаний в байтах
            return self.energy_reset_sum(data, 0), self.power_sum(data, 0)


    def executeZapros(self, autoRiz = 0, zapros = 0): # выполнение запроса
        if zapros != 0:
            self.__sock.send(zapros)
            self.__sock.settimeout(20)
            # self.__sock.close()
            return self.__sock.recv(1024)
        else:
            self.__sock.send(autoRiz)
            self.__sock.settimeout(20)
            # self.__sock.close()
            return self.__sock.recv(1024)

    def energy_reset_sum(self, data_byte, x = 1):
        pokazaniya = data_byte[2:3] + data_byte[1:2] + data_byte[4:5] + data_byte[3:4] #
        integerPokaz = int.from_bytes(pokazaniya, byteorder='big') # перевод из 16 -> 10 целой части
        if x == 1:
            pokazFloat = float(integerPokaz / 1000)
            return pokazFloat # показания за тек сутки в Int
        if x == 0:
            pokazFloat = float(integerPokaz / 1000)
            pokazStr = str(pokazFloat)#
            return pokazStr

    def power_sum(self, data_byte, x = 1):
        power = data_byte[10:11] + data_byte[9:10] + data_byte[12:13] + data_byte[11:12] # реактивная мощность
        # powerRez = 0
        powerInt = int.from_bytes(power, byteorder='big') #
        if x == 1:
            powerFloat = float( powerInt / 1000)
            return powerFloat # энергия за тек сутки Int
        if x == 0: # энергия за тек сутки
            powerFloat = float(powerInt / 1000)
            powerStr = str(powerFloat)
            return powerStr
        # print(id)

if __name__ == "__main__":
    # mer = mercury('7098469', '192.168.143.12', 35716)
    # print(mer.connect(1))
    pass
    # print(float(int(rez) / 1000 ))