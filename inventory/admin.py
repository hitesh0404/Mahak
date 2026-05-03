from django.contrib import admin
from .models import Brand,Category,Product,ProductImages
from django.utils.html import format_html
admin.site.register([Brand,Category,ProductImages])


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview')
    def image_preview(self, obj):
        print(obj.image.url)
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px;"/>', obj.image.url)
        return "No Image"
    
    image_preview.short_description = 'Preview'