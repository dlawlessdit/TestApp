from django.urls import path

from lab6app.views import *

app_name = 'lab6app'
urlpatterns = [
    path('', index, name='home'),
    path('index', index, name='index'),
    path('index2', index, name='index2'),
    path('index3', index, name='index3'),
    path('index4', index, name='index4'),
    path('index5', index, name='index5'),
    path('testlang', testlang, name='testlang'),
    path('portfolio-2', portfolio, name='portfolio-2'),
    path('portfolio-3', portfolio, name='portfolio-3'),
    path('portfolio-4', portfolio, name='portfolio-4'),
    path('portfolio-detail', portfolio, name='portfolio-detail'),

]

