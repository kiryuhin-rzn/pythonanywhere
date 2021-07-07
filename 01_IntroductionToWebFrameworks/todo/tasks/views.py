from django.http import HttpResponse

from django.views import View

import random

class ToDoView(View):


    def get(self, request, *args, **kwargs):

        LI_TEMPLATE = "<li>{}</li>"
        UL_TEMPLATE = "<ul>{}</ul>"

        catalog = ["Установить django",
                   "Запустить сервер",
                   "Порадоваться результату",
                   "Рано радоваться",
                   "Попить чай"]

        random.shuffle(catalog)
        front_catalog = str()
        for i in catalog:
            front_catalog += LI_TEMPLATE.format(i)

        return HttpResponse(UL_TEMPLATE.format(front_catalog))
