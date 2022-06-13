from django.urls import path
from .views import team_view

urlpatterns = [
    path('', team_view, name='team_view')
]
