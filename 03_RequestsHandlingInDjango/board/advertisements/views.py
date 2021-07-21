from django.shortcuts import render
from django.views import View


def advertisement_list(request, *args, **kwargs):
    advertisements = [
        'Мастер на час',
        'Выведение из запоя',
        'Услуги экскаватора-погрузчика, гидромолота, ямобура'
    ]
    return render(request, 'advertisements/advertisement_list.html', {})


class Advertisements(View):
    def get(self, request):
        advertisements = [
            'Мастер на час',
            'Выведение из запоя',
            'Услуги экскаватора-погрузчика, гидромолота, ямобура'
        ]
        return render(request, 'advertisements/advertisement_list.html', {'advertisements': advertisements})
    def post(self, request):
        meter = 0
        post_message = 'Запрос на создание новой записи успешно выполнен!'
        return render(request, 'advertisements/advertisement_list.html', {'post_message': post_message}, {'meter': meter})
        meter += 1

class Contacts(View):
    def get(self, request):
        contacts = [
            'Адрес: г. Рязань, ул. Гоголя, д. 13',
            'телефон: 8(800)000-00-17',
            'электронная почта: gogol@gmail.com'
        ]
        return render(request, 'contacts/contacts.html', {'contacts': contacts})

class About(View):
    def get(self, request):
        about = '"ООО Рога и копыта" - оказание всех видов услуг'
        return render(request, 'about/about.html', {'about': about})


class General(View):
    def get(self, request):
        advertisements = [
            'Услуги электрика',
            'Услуги грузчика',
            'Услуги экскаватора-погрузчика, гидромолота, ямобура',
            'Услуги тракториста'
        ]
        regions = [
            'Москва',
            'Санкт-Петербург',
            'Рязань',
            'Новосибирск',
            'Горький'
        ]
        return render(request, 'general/general.html', {'advertisements': advertisements, 'regions': regions})




