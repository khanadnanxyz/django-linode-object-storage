from django.contrib import admin

from product.models import Product, ProductsImage, Image

admin.site.register(Product)
admin.site.register(Image)
admin.site.register(ProductsImage)
