from django.urls import path
from kingadmin import views
urlpatterns=[
    path('',views.app_index)
]