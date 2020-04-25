from django.conf.urls import url
from . import view

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import staticfiles
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', view.hello),
    url(r'^To_Register', view.To_Register),
    url(r'^Return_Login', view.Return_Login),
    url(r'^register', view.register),
    url(r'^success', view.success),
    url(r'^login$', view.login),
    url(r'^Login_Out', view.Login_Out),
    url(r'^i_project',view.i_project),
    url(r'^project', view.project),
    url(r'^to_appointment', view.to_appointment),
    url(r'^back', view.back),
    url(r'^search', view.search),
    url(r'^appoint1', view.appoint1),
]


urlpatterns += staticfiles_urlpatterns()