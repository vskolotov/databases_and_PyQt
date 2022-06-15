from tabulate import tabulate
from hw1_2 import host_range_ping


def host_range_ping_tab():
    """
        Запрос диапазона ip адресов, проверка их доступности, вывод результатов в табличном виде
        :param
        :return:
    """
    res_dict = host_range_ping(True)
    print()
    print(tabulate([res_dict], headers='keys', tablefmt='pipe', stralign='center'))


if __name__ == "__main__":
    host_range_ping_tab()
