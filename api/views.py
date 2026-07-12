from .serializers import ProductSerializers,BrandSerializers
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from inventory.models import Product,Brand
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .permissions import IsAdminOrReadOnly
from rest_framework import generics
@api_view(["GET"]) 
@permission_classes([AllowAny])
def api_products_view(request):
    p = Product.objects.all() 
    serializer = ProductSerializers(p,many = True)
    return Response(serializer.data,status=200)

class ProductAPI(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = ProductSerializers
    queryset = Product.objects.all()

    # def perform_create(self, serializer):
    #     brand_id = self.request.POST.get("brand")
    #     brand = Brand.objects.get(id=brand_id)
    #     serializer.save(brand = brand )

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = ProductSerializers
    queryset = Product.objects.all()


class BrandViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = BrandSerializers
    queryset = Brand.objects.all()