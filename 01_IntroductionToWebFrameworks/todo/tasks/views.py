from django.http import HttpResponse

from django.views import View


class ToDoView(View):



    def get(self, request, *args, **kwargs):
        import random
        
        spisokdel = ["Установить django",
                     "Запустить сервер",
                     "Порадоваться результату",
                     "Рано радоваться",
                     "Попить чай"
                     ]
        random.shuffle(spisokdel)
        a = []
        for i in spisokdel:
            a.append(i)

        return HttpResponse(
            "<ul>"
                "<li>{}</li>".format(a[0]),
                "<li>{}</li>".format(a[1]),
                "<li>{}</li>".format(a[2]),
                "<li>{}</li>".format(a[3]),
                "<li>{}</li>".format(a[4]),
            "</ul>")
