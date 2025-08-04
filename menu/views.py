from django.shortcuts import render,get_object_or_404
from .models import Category,MenuItem

# Create your views here.

def menu(request):
    
    categories = Category.objects.all().order_by('order')


    return render(request, 'menu/menu.html',{'categories': categories})



def category_items(request, category_id):
    """عرض العناصر الخاصة بتصنيف معين"""
    category = get_object_or_404(Category, id=category_id)
    items = MenuItem.objects.filter(category=category, is_available=True)
    return render(request, 'menu/category_items.html', {
        'category': category,
        'items': items
    })