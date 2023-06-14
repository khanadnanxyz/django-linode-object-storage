from django.db import models
from django.utils.text import slugify


class Image(models.Model):
    image = models.ImageField(upload_to="products")
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.created)


class Product(models.Model):
    CATEGORY_CHOICES = [
        ("toys", "toys"),
        ("foods", "foods"),
        ("cosmetics", "cosmetics"),
        ("fashion", "fashion")
    ]
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=255, blank=False)
    category = models.CharField(max_length=9, choices=CATEGORY_CHOICES)
    featured_image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='featured_image', blank=False,
                                       null=False)
    thumbnail_image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='thumbnail_image', blank=False,
                                        null=False)
    block_image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='block_image', blank=False,
                                    null=False)
    slug = models.CharField(max_length=80, blank=False, null=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return "%s" % (self.name)


class ProductsImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return "%s" % (self.product.name)
