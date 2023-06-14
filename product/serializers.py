from rest_framework import serializers
from .models import Product, Image, ProductsImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image', 'created')


class ProductSerializer(serializers.ModelSerializer):
    featured_image = serializers.CharField(read_only=True, source='featured_image.image')
    featured_image_id = serializers.PrimaryKeyRelatedField(queryset=Image.objects.all(), source='featured_image',
                                                           write_only=True)
    thumbnail_image = serializers.CharField(read_only=True, source='thumbnail_image.image')
    thumbnail_image_id = serializers.PrimaryKeyRelatedField(queryset=Image.objects.all(), source='thumbnail_image',
                                                            write_only=True)
    block_image = serializers.CharField(read_only=True, source='block_image.image')
    block_image_id = serializers.PrimaryKeyRelatedField(queryset=Image.objects.all(), source='block_image',
                                                        write_only=True)

    class Meta:
        model = Product
        fields = (
            'name', 'description', 'category', 'featured_image', 'featured_image_id', 'thumbnail_image',
            'thumbnail_image_id', 'block_image', 'block_image_id', 'slug', 'price', 'date')


class ProductsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsImage
        fields = '__all__'
