from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)  # ✅ ترتيب مخصص


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['order']

class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.price}"
    
    class Meta:
        ordering = ['name']
        
        
class Order(models.Model):
    DELIVERY_CHOICES = [
        ('pickup', 'استلام من الفرع'),
        ('delivery', 'توصيل للمنزل'),
    ]

    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    landmark = models.CharField(max_length=100, blank=True)
    delivery_method = models.CharField(max_length=10, choices=DELIVERY_CHOICES)
    items = models.TextField()  # هنسجّل المنتجات كنص
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"