from django.conf.urls import url

from .import views

app_name = "polls"

urlpatterns = [
    url(r"^$", views.index, name="index"),
    #url(r"^result/(?P<pgroup>[-\w]+)/$", views.result, name="result"),
    # url(r"^bc/(?P<form>[-\w]+)/$", views.boundaryConditions, name="boundaryConditions"),
]
