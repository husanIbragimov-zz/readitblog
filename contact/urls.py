from django.urls import path
from .views import contact_view

urlpatterns = [
    path('', contact_view, name='contact_view'),
]
