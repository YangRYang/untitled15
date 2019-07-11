from django.urls import path
from kingadmin import views
urlpatterns=[
    path('',views.app_index),
    path('<str:app>/<str:model>/',views.table_obj_list,name = 'table_obj_list'),
    path('<str:app>/<str:model>/add/',views.table_obj_list_add,name = 'table_obj_list_add')
]