from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def main(a):
    return HttpResponse('<h1>Hello World</h1>')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main )
]
