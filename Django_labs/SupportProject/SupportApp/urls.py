from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ticket_view, name='ticket'),
]
