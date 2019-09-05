from django.urls import path
from kewayy_app import views


app_name = 'kewayy_app'

urlpatterns = [
    path('', views.index, name='index')
]