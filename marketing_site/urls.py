from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from products.views import product_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", product_list, name="home"),
]

