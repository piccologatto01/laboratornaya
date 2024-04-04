import socket
import pickle
import os
import time


def send_changes(folder, host, port):
    '''
    Данная функция отправляет изменения или
    состояние этой папки программе 1
    :param folder: первая папка
    :param host: хост (localhost)
    :param port: порт от 1025 до 65000
    :return:
    '''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #протокол TCP
        s.connect((host, port))

        files = os.listdir(folder)
        data = pickle.dumps(files)
        s.sendall(data)


if __name__ == "__main__":
    folder = r"C:\Users\Documents\testfolder1" #путь к папке
    host = '127.0.0.1'
    port = 61111 #номер хосета

    while True:
        send_changes(folder, host, port)
        time.sleep(10)  # отправка каждые 10 секунд
