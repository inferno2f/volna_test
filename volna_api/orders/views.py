from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from orders.constants import SUCCESS, FAILURE
from orders.models import Order
from orders.serializers import OrderSerializer


class OrderViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id',)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(SUCCESS, status=status.HTTP_201_CREATED)
        return Response(FAILURE, status=status.HTTP_400_BAD_REQUEST)
