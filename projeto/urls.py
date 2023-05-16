
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

# default of python is snake_case


def my_view(request):
    return HttpResponse("Uma linda string")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("sobre/", my_view)
]
