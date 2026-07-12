from rest_framework import serializers
from inventory.models import Product,Brand

class ProductSerializers(serializers.ModelSerializer):
    brand = serializers.HyperlinkedRelatedField(
        view_name="brands-detail",         
        queryset=Brand.objects.all()       
    )
    class Meta:
        model = Product
        fields = "__all__"
    
class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
    
