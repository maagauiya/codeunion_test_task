from django.urls import path, include
from rest_framework import routers

from . import views as views


router = routers.SimpleRouter()

router.register(r'currency', views.CurrencyViewSet, basename="currency")

urlpatterns = [
    path('', include(router.urls)),

]
