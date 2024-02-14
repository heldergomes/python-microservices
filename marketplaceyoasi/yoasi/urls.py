from django.contrib import admin
from django.urls import path, include
from marketplace import urls as marketplace_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('marketplace/', include(marketplace_urls)),
]
