from django.urls import path
from . import views

urlpatterns = [
    # path('', views.start, name='start'),
    path('', views.character_creation, name='character_creation'),
    path('page_1/', views.page_1, name='page_1'),
    path('page_2_choice_follow/', views.page_1, name='page_2_choice_follow'),
    path('page_2_choice_run/', views.page_1, name='page_2_choice_run'),
    path('page_2_choice_shout/', views.page_1, name='page_2_choice_shout'),

]