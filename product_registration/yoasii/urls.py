from django.contrib import admin
from django.urls import path, include
from productregistration import urls as product_registration_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product_registration', include(product_registration_urls)),
]
