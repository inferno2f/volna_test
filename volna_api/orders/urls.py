from django.urls import path, include
from rest_framework import routers

from orders.views import OrderViewSet


app_name = 'orders'

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
