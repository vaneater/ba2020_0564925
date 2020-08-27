from django.urls import path
from . import views

urlpatterns = [
    # path('', views.start, name='start'),
    path('', views.character_creation, name='character_creation'),
    path('page_1/', views.page_1, name='page_1'),
    path('page_1/page_2_choice_follow/', views.page_2_choice_follow, name='page_2_choice_follow'),
    path('page_1/page_2_choice_run/', views.page_2_choice_run, name='page_2_choice_run'),
    path('page_1/page_2_choice_shout/', views.page_2_choice_shout, name='page_2_choice_shout'),
    path('page_1/page_2_choice_follow/page_3_choice_help/', views.page_3_choice_help, name='page_3_choice_help'),
    path('page_1/page_2_choice_follow/page_3_choice_ask/', views.page_3_choice_ask, name='page_3_choice_ask'),
    path('page_1/page_2_choice_follow/page_3_choice_leave/', views.page_3_choice_leave, name='page_3_choice_leave'),
    path('page_1/page_2_choice_run/page_3_choice_help/', views.page_3_choice_help, name='page_3_choice_help'),
    path('page_1/page_2_choice_run/page_3_choice_ask/', views.page_3_choice_ask, name='page_3_choice_ask'),
    path('page_1/page_2_choice_run/page_3_choice_leave/', views.page_3_choice_leave, name='page_3_choice_leave'),
    path('page_1/page_2_choice_shout/page_3_choice_help/', views.page_3_choice_help, name='page_3_choice_help'),
    path('page_1/page_2_choice_shout/page_3_choice_ask/', views.page_3_choice_ask, name='page_3_choice_ask'),
    path('page_1/page_2_choice_shout/page_3_choice_leave/', views.page_3_choice_leave, name='page_3_choice_leave'),

]