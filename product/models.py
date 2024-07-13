from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(unique=True, max_length=150)
    featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(unique=True, max_length=250)
    featured = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    thumbnail = models.ImageField(upload_to='product_thumbnails')
    thumbnail_2 = models.ImageField(upload_to='product_thumbnails')
    description = models.TextField(null=True, blank=True, default='N/A')
    in_stock = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return self.title
    
    @property
    def related(self):
        return self.category.products.all().exclude(pk=self.pk)
    



class Slider(models.Model):
    title = models.CharField(max_length=50)
    banner = models.ImageField(upload_to='banners')
    show = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class ShowOffer(models.Model):
    coupon_code = models.CharField(max_length=20)
    free_shipping = models.CharField(max_length=20)
    student_discount_amount = models.CharField(max_length=20)
    discount_amount = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    show = models.BooleanField(default=True)
    
    def str__(self):
        return self.coupon_code


class BrandLogo(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='brand_logo')
    created_date = models.DateTimeField(auto_now_add=True)
    show = models.BooleanField(default=True)
    
    def str__(self):
        return self.title
    

class Featured(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='feature_logo')
    description = models.TextField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    show = models.BooleanField(default=True)
    
    def str__(self):
        return self.title