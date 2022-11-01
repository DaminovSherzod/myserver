from django.contrib import admin
from django.urls import path
from myapp.views import home, add_product, get_all_company, get_company_by_name


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home ),
    path('add_product/',add_product),
    path('company/', get_all_company),
    path('company/<str:company>/', get_company_by_name, name='company')

]
