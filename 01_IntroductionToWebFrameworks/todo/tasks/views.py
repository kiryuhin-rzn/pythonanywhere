from django.http import HttpResponse

from django.views import View


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        # TODO: Импорты следует делать в начале файла, в конце файла должна быть одна пустая строка:)
        import random
        # TODO: Хорошо!
        #  Если делать более профессионально, то лучше сначала задать шаблоны вида
        #  LI_TEMPLATE = '<li>{}</li>'
        #  и
        #  UL_TEMPLATE = '<ul>{}</ul>'
        #  и наполнять их при помощи метода format()
        #  Предлагаю попробовать. Если не получится, то я подскажу:)
        #  Также нейминг должен говорить о том за что отвечает переменная:)
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



