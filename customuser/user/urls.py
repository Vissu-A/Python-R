from django.conf.urls import url
from user.views import register,logingview

urlpatterns = [
    url(r'^$',logingview),
    url(r'^register/',register),
]
