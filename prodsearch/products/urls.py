from django.urls import path

from .views import IndexView

app_name = 'products'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
