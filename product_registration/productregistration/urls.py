from django.urls import path, include

from productregistration.views import RegistrationProductApiView

urlpatterns = [
    path('', RegistrationProductApiView.as_view()),
]