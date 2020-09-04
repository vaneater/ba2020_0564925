from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_start, name='first_start'),
    path('first_start/character_creation/', views.character_creation, name='character_creation'),
    path('page_1/', views.page_1, name='page_1'),
    path('page_1/page_2_choice_follow/', views.page_2_choice_follow, name='page_2_choice_follow'),
    path('page_1/page_2_choice_run/', views.page_2_choice_run, name='page_2_choice_run'),
    path('page_1/page_2_choice_shout/', views.page_2_choice_shout, name='page_2_choice_shout'),

    path('page_1/survived/', views.survived, name='survived'),
    path('page_1/page_3_choice_leave/death/', views.death, name='death'),
    path('', views.delete, name='delete'),

    #    path('page_1/page_2_choice_follow/page_3_choice_book/', views.page_3_choice_book, name='page_3_choice_book'),
    #   path('page_1/page_2_choice_follow/page_3_choice_sword/', views.page_3_choice_sword, name='page_3_choice_sword'),
    #  path('page_1/page_2_choice_follow/page_3_choice_leave/', views.page_3_choice_leave, name='page_3_choice_leave'),
    # path('page_1/page_2_choice_run/page_3_choice_book/', views.page_3_choice_book, name='page_3_choice_book'),
    #    path('page_1/page_2_choice_run/page_3_choice_sword/', views.page_3_choice_sword, name='page_3_choice_sword'),
    #   path('page_1/page_2_choice_run/page_3_choice_leave/', views.page_3_choice_leave, name='page_3_choice_leave'),
    #  path('page_1/page_2_choice_shout/page_3_choice_book/', views.page_3_choice_book, name='page_3_choice_book'),
    # path('page_1/page_2_choice_shout/page_3_choice_sword/', views.page_3_choice_sword, name='page_3_choice_sword'),
    #    path('page_1/page_2_choice_shout/page_3_choice_leave/', views.page_3_choice_leave, name='page_3_choice_leave'),
    #   path('page1/page_2_choice_shout/death/', views.page_3_choice_book, name='page_3_choice_book'),
    #  path('page1/page_2_choice_shout/death/', views.page_3_choice_sword, name = 'page_3_choice_sword'),

]
