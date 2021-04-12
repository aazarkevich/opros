import psycopg2
from datetime import datetime
from collections import defaultdict


class PostgresOpros:
    CONST_DATABASE = "mercury2020"
    CONST_USER = "postgres"
    CONST_PASSWORD = ''
    CONST_HOST = "192.168.143.177"
    CONST_PORT = "5432"

    def __init__(self):
        self.connect = psycopg2.connect(database=self.CONST_DATABASE, user=self.CONST_USER,
                                        password=self.CONST_PASSWORD,
                                        host=self.CONST_HOST, port=self.CONST_PORT)
        # self.cursor = self.connect.cursor()

    def find_all_from_res(self, number_res):
        cursor = self.connect.cursor()
        if number_res == '1':
            cursor.execute('SELECT serial_number, ip, port FROM device_mercury_v ORDER BY parent_id_tp, id')
        elif number_res == '2':
            cursor.execute('SELECT serial_number, ip, port FROM device_mercury_z ORDER BY parent_id_tp, id')
        elif number_res == '3':
            cursor.execute('SELECT serial_number, ip, port, id FROM device_mercury_s ORDER BY parent_id_tp, id')
        elif number_res == '4':
            cursor.execute('SELECT serial_number, ip, port FROM device_mercury_u ORDER BY parent_id_tp, id')
        elif number_res == '5':
            cursor.execute('SELECT serial_number, ip, port FROM device_mercury_u ORDER BY parent_id_tp, id')

        ls_device_res = [row for row in cursor]
        return ls_device_res

    def insert(self, number_res: int, data_result_oprosa: dict):

        cursor = self.connect.cursor()

        with cursor as cursor:
            if number_res == '1':
                cursor.execute("INSERT INTO public.data_mercury_v (serial_number, energy_reset_sum, "
                               "power_sum, energy_day_start, energy_day, power_day, error, date) VALUES " + "("
                               + str(data_result_oprosa['serial_number']) + ",'" + str(
                    data_result_oprosa['energy_reset_sum']) + "','" + str(data_result_oprosa['power_sum']) +
                               "','" + str(data_result_oprosa['energy_day_start']) + "','" + str(
                    data_result_oprosa['energy_day']) + "','" + str(data_result_oprosa['power_day'])
                               + "','" + str(data_result_oprosa['error']) + "','" + str(
                    data_result_oprosa['date']) + "')")
            elif number_res == '2':
                cursor.execute("INSERT INTO public.data_mercury_z (serial_number, energy_reset_sum, "
                               "power_sum, energy_day_start, energy_day, power_day, error, date) VALUES " + "("
                               + str(data_result_oprosa['serial_number']) + ",'" + str(
                    data_result_oprosa['energy_reset_sum']) + "','" + str(data_result_oprosa['power_sum']) +
                               "','" + str(data_result_oprosa['energy_day_start']) + "','" + str(
                    data_result_oprosa['energy_day']) + "','" + str(data_result_oprosa['power_day'])
                               + "','" + str(data_result_oprosa['error']) + "','" + str(
                    data_result_oprosa['date']) + "')")
            elif number_res == '3':
                cursor.execute("INSERT INTO public.data_mercury_s (serial_number, energy_reset_sum, "
                               "power_sum, energy_day_start, energy_day, power_day, error, date) VALUES " + "("
                               + str(data_result_oprosa['serial_number']) + ",'" + str(
                    data_result_oprosa['energy_reset_sum']) + "','" + str(data_result_oprosa['power_sum']) +
                               "','" + str(data_result_oprosa['energy_day_start']) + "','" + str(
                    data_result_oprosa['energy_day']) + "','" + str(data_result_oprosa['power_day'])
                               + "','" + str(data_result_oprosa['error']) + "','" + str(
                    data_result_oprosa['date']) + "')")
            elif number_res == '4':
                cursor.execute("INSERT INTO public.data_mercury_u (serial_number, energy_reset_sum, "
                               "power_sum, energy_day_start, energy_day, power_day, error, date) VALUES " + "("
                               + str(data_result_oprosa['serial_number']) + ",'" + str(
                    data_result_oprosa['energy_reset_sum']) + "','" + str(data_result_oprosa['power_sum']) +
                               "','" + str(data_result_oprosa['energy_day_start']) + "','" + str(
                    data_result_oprosa['energy_day']) + "','" + str(data_result_oprosa['power_day'])
                               + "','" + str(data_result_oprosa['error']) + "','" + str(
                    data_result_oprosa['date']) + "')")
            elif number_res == '5':
                cursor.execute("INSERT INTO public.data_mercury_test (serial_number, energy_reset_sum, "
                               "power_sum, energy_day_start, energy_day, power_day, error, date) VALUES " + "("
                               + str(data_result_oprosa['serial_number']) + ",'" + str(
                    data_result_oprosa['energy_reset_sum']) + "','" + str(data_result_oprosa['power_sum']) +
                               "','" + str(data_result_oprosa['energy_day_start']) + "','" + str(
                    data_result_oprosa['energy_day']) + "','" + str(data_result_oprosa['power_day'])
                               + "','" + str(data_result_oprosa['error']) + "','" + str(
                    data_result_oprosa['date']) + "')")

        self.connect.commit()
        # self.connect.close()
        # test = [row for row in self.cursor]
        # return test

    def last_date_value(self, number_res):
        cursor = self.connect.cursor()

        if number_res == '1':
            cursor.execute(
                'SELECT date FROM data_mercury_v where id in (select max(id) from data_mercury_v)')  # последняя дата записи в БД
        elif number_res == '2':
            cursor.execute(
                'SELECT date FROM data_mercury_z where id in (select max(id) from data_mercury_z)')  # последняя дата записи в БД
        elif number_res == '3':
            cursor.execute(
                'SELECT date FROM data_mercury_s where id in (select max(id) from data_mercury_s)')  # последняя дата записи в БД
        elif number_res == '4':
            cursor.execute(
                'SELECT date FROM data_mercury_u where id in (select max(id) from data_mercury_u)')  # последняя дата записи в БД
        elif number_res == '5':
            cursor.execute(
                'SELECT date FROM data_mercury_test where id in (select max(id) from data_mercury_test)')  # последняя дата записи в БД

        try:
            last_date = str(cursor.fetchone()[0])
            return last_date
        except TypeError:
            return '1111-11-11'

    def all_device_gsm(self):
        cursor = self.connect.cursor()
        cursor.execute('SELECT phone, serial_number FROM public.test_call_mercury LIMIT 5')
        devices = [row for row in cursor]
        return devices

# postgres = PostgresOpros()
# print(postgres.all_device_gsm())
# postgres = PostgresOpros()
# d = dict()
# print(postgres.insert(number_res=1,data_result_oprosa=d))
# print(postgres.find_all_from_res(1))
# print(postgres.last_date_value('1'))
# a = [{'serial_number': '10182420', 'energy_reset_sum': '14267.485', 'power_sum': '5204.276', 'energy_day_start': '14264.644', 'energy_day': 2.841, 'power_day': 0.892, 'error': '-', 'date': '04-01-2021'}, {'serial_number': '7093737', 'energy_reset_sum': '34473.195', 'power_sum': '15171.049', 'energy_day_start': '34470.163', 'energy_day': 3.032, 'power_day': 1.35, 'error': '-', 'date': '04-01-2021'}, {'serial_number': '5387599', 'energy_reset_sum': '0', 'power_sum': '0', 'energy_day_start': '0', 'energy_day': '0', 'power_day': '0', 'error': '-', 'date': '03-30-2021'}, {'serial_number': '3392150', 'energy_reset_sum': '0', 'power_sum': '0', 'energy_day_start': '0', 'energy_day': '0', 'power_day': '0', 'error': '-', 'date': '03-30-2021'}, {'serial_number': '10698952', 'energy_reset_sum': '0', 'power_sum': '0', 'energy_day_start': '0', 'energy_day': '0', 'power_day': '0', 'error': '-', 'date': '03-30-2021'}, {'serial_number': '26027954', 'energy_reset_sum': '1373.254', 'power_sum': '265.364', 'energy_day_start': '-12717.45', 'energy_day': 14090.704, 'power_day': 0.0, 'error': '-', 'date': '04-01-2021'}, {'serial_number': '15741289', 'energy_reset_sum': '0', 'power_sum': '0', 'energy_day_start': '0', 'energy_day': '0', 'power_day': '0', 'error': '-', 'date': '03-30-2021'}, {'serial_number': '104179', 'energy_reset_sum': '117626.586', 'power_sum': '36732.95', 'energy_day_start': '117622.08799999999', 'energy_day': 4.498, 'power_day': 1.36, 'error': '-', 'date': '04-01-2021'}, {'serial_number': '105382', 'energy_reset_sum': '59358.003', 'power_sum': '15606.817', 'energy_day_start': '59353.691', 'energy_day': 4.312, 'power_day': 0.665, 'error': '-', 'date': '04-01-2021'}, {'serial_number': '105378', 'energy_reset_sum': '44929.469', 'power_sum': '13877.685', 'energy_day_start': '44928.988999999994', 'energy_day': 0.48, 'power_day': 0.132, 'error': '-', 'date': '04-01-2021'}, {'serial_number': '27408914', 'energy_reset_sum': '3600.476', 'power_sum': '263.963', 'energy_day_start': '-9244.851999999999', 'energy_day': 12845.328, 'power_day': 0.0, 'error': '-', 'date': '04-01-2021'}, {'serial_number': '16945102', 'energy_reset_sum': '0', 'power_sum': '0', 'energy_day_start': '0', 'energy_day': '0', 'power_day': '0', 'error': '-', 'date': '03-30-2021'}, {'serial_number': '13043920', 'energy_reset_sum': '0', 'power_sum': '0', 'energy_day_start': '0', 'energy_day': '0', 'power_day': '0', 'error': '-', 'date': '03-30-2021'}, {'serial_number': '68671', 'energy_reset_sum': '35362.897', 'power_sum': '11023.738', 'energy_day_start': '35361.632999999994', 'energy_day': 1.264, 'power_day': 0.224, 'error': '-', 'date': '04-01-2021'}, {'serial_number': '69314', 'energy_reset_sum': '40361.723', 'power_sum': '9325.495', 'energy_day_start': '40360.345', 'energy_day': 1.378, 'power_day': 0.345, 'error': '-', 'date': '04-01-2021'}, {'serial_number': '24119829', 'energy_reset_sum': '154.33', 'power_sum': '11.579', 'energy_day_start': '153.04700000000003', 'energy_day': 1.283, 'power_day': 0.16, 'error': '-', 'date': '04-01-2021'}, {'serial_number': '100925', 'energy_reset_sum': '0', 'power_sum': '0', 'energy_day_start': '0', 'energy_day': '0', 'power_day': '0', 'error': '-', 'date': '03-30-2021'}, {'serial_number': '101904', 'energy_reset_sum': '4987.38', 'power_sum': '1465.843', 'energy_day_start': '4987.079', 'energy_day': 0.301, 'power_day': 0.117, 'error': '-', 'date': '04-01-2021'}, {'serial_number': '37877008', 'energy_reset_sum': '2457.107', 'power_sum': '411.295', 'energy_day_start': '2455.205', 'energy_day': 1.902, 'power_day': 0.051, 'error': '-', 'date': '04-01-2021'}, {'serial_number': '37877208', 'energy_reset_sum': '1078.67', 'power_sum': '664.623', 'energy_day_start': '1077.634', 'energy_day': 1.036, 'power_day': 0.567, 'error': '-', 'date': '04-01-2021'}, {'serial_number': '40302080', 'energy_reset_sum': '386.387', 'power_sum': '0.762', 'energy_day_start': '386.05', 'energy_day': 0.337, 'power_day': 0.0, 'error': '-', 'date': '04-01-2021'}, {'serial_number': '40272041', 'energy_reset_sum': '435.54', 'power_sum': '34.938', 'energy_day_start': '434.776', 'energy_day': 0.764, 'power_day': 0.014, 'error': '-', 'date': '04-01-2021'}, {'serial_number': '32315579', 'energy_reset_sum': '14426.03', 'power_sum': '13582.195', 'energy_day_start': '14418.791000000001', 'energy_day': 7.239, 'power_day': 7.26, 'error': '-', 'date': '04-01-2021'}, {'serial_number': '42938123', 'energy_reset_sum': '483.319', 'power_sum': '52.466', 'energy_day_start': '482.987', 'energy_day': 0.332, 'power_day': 0.0, 'error': '-', 'date': '04-01-2021'}, {'serial_number': '42938337', 'energy_reset_sum': '30.453', 'power_sum': '0.233', 'energy_day_start': '30.335', 'energy_day': 0.118, 'power_day': 0.0, 'error': '-', 'date': '04-01-2021'}, {'serial_number': '7094030', 'energy_reset_sum': '46045.987', 'power_sum': '26960.715', 'energy_day_start': '46045.034', 'energy_day': 0.953, 'power_day': 0.353, 'error': '-', 'date': '04-01-2021'}, {'serial_number': '102645', 'energy_reset_sum': '30006.002', 'power_sum': '10563.033', 'energy_day_start': '30004.802', 'energy_day': 1.2, 'power_day': 0.343, 'error': '-', 'date': '04-01-2021'}, {'serial_number': '219012', 'energy_reset_sum': '31297.136', 'power_sum': '10111.855', 'energy_day_start': '31292.267', 'energy_day': 4.869, 'power_day': 0.871, 'error': '-', 'date': '04-01-2021'}, {'serial_number': '14770377', 'energy_reset_sum': '13215.078', 'power_sum': '183.033', 'energy_day_start': '13214.396999999999', 'energy_day': 0.681, 'power_day': 0.0, 'error': '-', 'date': '04-01-2021'}, {'serial_number': '16945289', 'energy_reset_sum': '34741.629', 'power_sum': '2141.791', 'energy_day_start': '34740.096', 'energy_day': 1.533, 'power_day': 0.003, 'error': '-', 'date': '04-01-2021'}, {'serial_number': '4436099', 'energy_reset_sum': '107.728', 'power_sum': '0.265', 'energy_day_start': '102.292', 'energy_day': 5.436, 'power_day': 0.001, 'error': '-', 'date': '04-01-2021'}]
# for data in a:
#     print(data)
    # postgres.insert(number_res='5', data_result_oprosa=data)
# print(postgres.insert(number_res='5',data_result_oprosa=a))
# print(
#     len(a)
# )