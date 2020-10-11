from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializers


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializers
