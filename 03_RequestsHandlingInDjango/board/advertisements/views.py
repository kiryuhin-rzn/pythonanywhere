from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .forms import AdvertisementForm
from django.http import HttpResponse



# TODO: Слишком большой отступ. Двух пустых строк достаточно
class Advertisements(View):
    def get(self, request):
        advertisements = [
            'Мастер на час',
            'Выведение из запоя',
            'Услуги экскаватора-погрузчика, гидромолота, ямобура'
        ]
        form = AdvertisementForm()

        return render(request, 'advertisements/advertisement_list.html', {'form': form,
                                                                          # TODO: Следует выровнять:)
        'advertisements': advertisements})

    def post(self, request):
        # TODO: Как вариант, можно у этого класса задать атрубут счетчик
        #  и увеличивать его при каждом вызове этого метода:)

        return HttpResponse("<h2>Запрос на создание новой записи успешно выполнен!</h2>")


class Contacts(TemplateView):
    template_name = 'contacts/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Бесплатные объявления в вашем городе'
        context['title'] = 'Бесплатные объявления'
        context['address'] = 'Адрес: г. Рязань, ул. Гоголя, д. 13'
        context['telephone'] = 'телефон: 8(800)000-00-17'
        context['e_mail'] = 'gogol@gmail.com'

        return context


class About(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = '"ООО Рога и копыта"'
        context['title'] = 'Бесплатные объявления'
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
