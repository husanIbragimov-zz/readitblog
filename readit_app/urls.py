from django.urls import path
from .views import home_view, article_list, article_detail

app_name = 'readit'

urlpatterns = [
    path('', home_view, name='home_view'),
    path('blog/', article_list, name='article_list'),
    path('detail/<slug:slug>/', article_detail, name='article_detail'),
]
