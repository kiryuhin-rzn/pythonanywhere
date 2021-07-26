from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


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

    # TODO: Работает?:)
    def post(self, request):
        meter = 0
        post_message = 'Запрос на создание новой записи успешно выполнен!'
        # TODO: Код не должен выходить за вертикальную линию справа
        return render(request, 'advertisements/advertisement_list.html', {'post_message': post_message}, {'meter': meter})
        # TODO: Код ниже никогда не будет исполнен
        meter += 1


class Contacts(TemplateView):
    template_name = 'contacts/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Бесплатные объявления в вашем городе'
        context['title'] = 'Бесплатные объявления'
        # TODO: 1) Код не должен выходить за вертикальную линию справа
        #  2) Следует адрес, телефон и мыло записывать в разные ключи
        context['discription'] = 'Адрес: г. Рязань, ул. Гоголя, д. 13, телефон: 8(800)000-00-17, электронная почта: gogol@gmail.com'

        return context


class About(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        # TODO: Лишнее дублирование кода
        context = super().get_context_data(**kwargs)
        context = super().get_context_data(**kwargs)
        context['name'] = '"ООО Рога и копыта"'
        context['title'] = 'Бесплатные объявления'
        # TODO: Аналогично
        context['discription'] = 'Оказываем все виды услуг'

        return context


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

