from django.urls import path
from kewayy_app import views


app_name = 'kewayy_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('stories/', views.show_all_stories, name='show_all_stories'),
    path('stories/create/', views.create_story, name='create_story'),
    path('stories/<slug:story_slug>/', views.show_story, name='show_story'),
    path('stories/<slug:story_slug>/create_test_case/', views.create_test_case, name='create_test_case'),
    path('test_case/<int:test_case_id>/edit/', views.edit_test_case, name='edit_test_case'),
    path('test_case/<int:test_case_id>/delete/', views.delete_test_case, name='delete_test_case'),
]