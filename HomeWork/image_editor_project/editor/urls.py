from django.urls import path

from . import views

urlpatterns = [
    path('', views.edit_image_view, name='edit_image'),
    path('reset/', views.reset_view, name='reset'),
]
