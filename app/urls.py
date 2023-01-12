from django.urls import path, include
from .views import AppsList, AppsCreate

urlpatterns = [
    #path('index/', IndexView.as_view()),
    path('', AppsList.as_view(), name='apps_list'),
    path('account/', include("accounts.urls")),  # Добавили эту строчку
    path('accounts/', include("allauth.urls")),
    path('apps/create/', AppsCreate.as_view(), name='apps_create'),

]
