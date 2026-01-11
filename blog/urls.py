from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/',views.blogDetail, name ='blog_Detail'),
]