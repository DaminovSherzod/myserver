from django.contrib import admin
from django.urls import path
from myapp.views import home, add_product


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home ),
    path('add_product/',add_product)

]
