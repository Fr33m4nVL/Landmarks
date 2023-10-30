from django.urls import path

from .views import ExcursionList

urlpatterns = [
    path('', ExcursionList.as_view(), name='excursions'),
]