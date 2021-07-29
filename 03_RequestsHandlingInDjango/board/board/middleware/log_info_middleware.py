from board.settings import BASE_DIR
import os
import time


# TODO: Объедините три класса в один
class UserInfoTime:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        time_request = time.ctime()
        # TODO: Такой путь создает файл в директории с исполняемым файлом.
        #  В пути должна быть директория log, которую сначала следует создать:)
        file_log = open(os.path.join(os.path.dirname(__file__), 'log_file.txt'), 'a')
        file_log.write(time_request)
        file_log.close()

        response = self.get_response(request)

        return response


class UserInfoIp:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        my_file = open(os.path.join(os.path.dirname(__file__), 'log_file.txt'), 'a')
        my_file.write(ip)
        my_file.close()

        response = self.get_response(request)

        return response


class UserInfoMethod:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'GET':
            my_file = open(os.path.join(os.path.dirname(__file__), 'log_file.txt'), 'a')
            my_file.write('GET')
            my_file.close()
        if request.method == 'POST':
            my_file = open(os.path.join(os.path.dirname(__file__), 'log_file.txt'), 'a')
            my_file.write('POST')
            my_file.close()

        response = self.get_response(request)

        return response
