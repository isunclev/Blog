from django.urls import path
from . import views

# start with blog
urlpatterns = [
    path('update_comment', views.update_comment, name='update_comment'),
]