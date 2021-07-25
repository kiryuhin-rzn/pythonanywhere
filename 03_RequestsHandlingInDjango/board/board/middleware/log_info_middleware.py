import os
from board.settings import BASE_DIR
import time


class UserInfoTime:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        t = time.ctime()
        my_file = open(os.path.join(os.path.dirname(__file__), 'file.txt'), 'a')
        my_file.write(t)
        my_file.close()

        response = self.get_response(request)

        return response


class UserInfoIp:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        my_file = open(os.path.join(os.path.dirname(__file__), 'file.txt'), 'a')
        my_file.write(ip)
        my_file.close()

        response = self.get_response(request)

        return response


class UserInfoMethod:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'GET':
            my_file = open(os.path.join(os.path.dirname(__file__), 'file.txt'), 'a')
            my_file.write('GET')
            my_file.close()
        if request.method == 'POST':
            my_file = open(os.path.join(os.path.dirname(__file__), 'file.txt'), 'a')
            my_file.write('POST')
            my_file.close()

        response = self.get_response(request)

        return response

