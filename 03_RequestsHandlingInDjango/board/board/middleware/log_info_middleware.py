from django.core.files import File
import time


# TODO: Класс должен быть обособлен от остального кода на 2 пустые строки:)
class UserInfoTime:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        t = time.ctime()
        # TODO: Код должен работать на любом компьютере и/или сервере, а не только вашем
        my_file = open('c:/djangoproekt/python_django/03_RequestsHandlingInDjango/board/board/middleware/file.txt', 'a')
        my_file.write(t)
        # TODO: Забыли "()"
        my_file.close

        response = self.get_response(request)

        return response

class UserInfoIp:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        ip = request.META.get('REMOTE_ADDR')
        my_file = open('c:/djangoproekt/python_django/03_RequestsHandlingInDjango/board/board/middleware/file.txt', 'a')
        my_file.write(ip)
        my_file.close

        response = self.get_response(request)

        return response

class UserInfoMethod:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'GET':
            my_file = open('c:/djangoproekt/python_django/03_RequestsHandlingInDjango/board/board/middleware/file.txt', 'a')
            my_file.write('GET')
            my_file.close
        if request.method == 'POST':
            my_file = open('c:/djangoproekt/python_django/03_RequestsHandlingInDjango/board/board/middleware/file.txt', 'a')
            my_file.write('POST')
            my_file.close

        response = self.get_response(request)

        return response



