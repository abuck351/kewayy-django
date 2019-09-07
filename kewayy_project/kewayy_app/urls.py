from django.urls import path
from kewayy_app import views


app_name = 'kewayy_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('story/<slug:story_slug>/', views.show_story, name='show_story'),
    path('stories/', views.show_all_stories, name='show_all_stories'),
]