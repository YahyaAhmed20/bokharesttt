from django.contrib import admin
from .models import Category, MenuItem,Order

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')          # نعرض الاسم والترتيب
    list_editable = ('order',)                # نخلي order قابل للتعديل من الليستة
    ordering = ('order',)                     # ترتيب الكاتيجوري نفسه في لوحة التحكم

class MenuItemAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'category', 'price', 'is_available')
    list_filter = ('category', 'is_available')

admin.site.register(Category, CategoryAdmin)
admin.site.register(MenuItem, MenuItemAdmin)



admin.site.register(Order)
