from django.urls import path

from marketplace.views import ProductApiView
from marketplace.views import SellerApiView

urlpatterns = [
    path('products', ProductApiView.as_view()),
    path('sellers', SellerApiView.as_view()),
]