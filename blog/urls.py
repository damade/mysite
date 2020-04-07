from django.urls import path

from . import views

urlpatterns = [
    path('post/', views.posts, name='posts'),
    path('comments/', views.comments, name='comments'),
    # path('contact/', views.contact, name='Contact')
]
