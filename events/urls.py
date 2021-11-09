from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.events_list, name="list"),
    path('create', views.event_create, name="create"),
    path('<slug>', views.event_detail, name="detail"),
]
