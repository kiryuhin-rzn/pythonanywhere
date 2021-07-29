from board.settings import BASE_DIR
import os
import time


class Info_TimeIpMethod:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        time_request = time.ctime()
        ip = request.META.get('REMOTE_ADDR')
        if request.method == 'GET':
            my_file = open(os.path.join(os.path.dirname(__file__), 'log/log_file.txt'), 'a')
            my_file.write('GET')
            my_file.close()
        if request.method == 'POST':
            my_file = open(os.path.join(os.path.dirname(__file__), 'log/log_file.txt'), 'a')
            my_file.write('POST')
            my_file.close()
        file_log = open(os.path.join(os.path.dirname(__file__), 'log/log_file.txt'), 'a')
        file_log.write(time_request)
        file_log.write(ip)
        file_log.close()

        response = self.get_response(request)

        return response
