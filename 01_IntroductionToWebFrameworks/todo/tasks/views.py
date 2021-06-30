from django.http import HttpResponse

from django.views import View


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        # TODO: Под произвольным выводом дел подразумевается вывод дел в случайном порядке. Предлагаю доработать:)
        import random
        h = ["<li>Установить django</li>",
             "<li>Запустить сервер</li>",
             "<li>Порадоваться результату</li>",
             "<li>Рано радоваться</li>",
             "<li>Попить чай</li>"
             ]
        random.shuffle(h)
        a = []
        for i in h:
            a.append(i)
        return HttpResponse(a)



