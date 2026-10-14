from rest_framework.generics import ListAPIView

from app.models import Product
from app.serializers import ProductModelSerializer


class ProductListAPIView(ListAPIView):
    serializer_class = ProductModelSerializer
    queryset = Product.objects.all()