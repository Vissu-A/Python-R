from django.conf.urls import url
from library.views import welcome,register,loggingout

urlpatterns = [
    url(r'^$',welcome),
    url(r'^register/',register),
    url(r'^logout/',loggingout),
]