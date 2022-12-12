import django.urls
from . import views

urlpatterns = [
    django.urls.path('', views.post_list, name='post_list'),
]