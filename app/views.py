from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView
from .models import Advertisements
from .tasks import text, printer, hello
#
# # Create your views here.
# def index_(request):
#     text.delay(5)
#     printer.delay(10)
#     hello.delay()
#     return render(request, "index.html")

class IndexView(View):
     def get(self, request):
          #text.delay()
          # printer.delay(3)
          #hello.delay()
     # return render(request, "index.html")
          return HttpResponse('Hello!')

class AppsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Advertisements
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-apps_datetime'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'apps.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'apps'
    paginate_by = 10  # вот так мы можем указать количество записей на странице
    # hello.delay()
    #logger.warning("Получаем обычный запрос")

    #logger.info("The value of id is ")
    # Переопределяем функцию получения списка новостей

    def get_queryset(self):
        # pprint(self.context_object_name.title())
        # Получаем обычный запрос
        #logger.warning("Получаем обычный запрос")
        # queryset = super().get_queryset()
        #queryset = Advertisements.objects.filter(typePost='NW')
        queryset = Advertisements.objects.all()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        #self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров

        #return self.filterset.qs
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        #context['filterset'] = self.filterset
        return context

class AppsCreate(PermissionRequiredMixin, CreateView):
            #система  аутентификации
            permission_required = ('Advertisements.add_post',)
            # определяем форму
            #form_class = AdvertisementsForm
            #  отвечает за перепосыл при ограничении доступа
            raise_exception = True
            # Модель всё та же, но мы хотим получать информацию по отдельной новости
            model = Advertisements
            # определяем поля
            fields = '__all__'
            # Используем другой шаблон
            template_name = 'apps_create.html'
            # Название объекта, в котором будет выбранный пользователем новость
            context_object_name = 'create'
            success_url = reverse_lazy('apps_list')
            # hello.delay()
            #send_mail_c.delay()

            def form_valid(self, form):
                apps = form.save(commit=False)
                #apps.author = 1
                # hello.delay()
                #send_mail_c.delay()
                return super().form_valid(form)

            # def get_absolute_url(self):
            #  self   return f'/news/{self.name}/'
