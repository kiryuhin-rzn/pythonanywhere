from django.http import HttpResponse

from django.views import View


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        # TODO: Под произвольным выводом дел подразумевается вывод дел в случайном порядке. Предлагаю доработать:)
        return HttpResponse('<ul>'
                            '<li>Установить python</li>'
                            '<li>Установить django</li>'
                            '<li>Запустить сервер</li>'
                            '<li>Порадоваться результату</li>'
							'<li>Рано радоваться</li>'
                            '</ul>')
