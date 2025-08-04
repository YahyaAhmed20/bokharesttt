
from django.urls import path

from . import views


app_name = 'menu'

urlpatterns = [
    path('', views.menu, name='menu'),

   
    path('category/<int:category_id>/', views.category_items, name='category_items'),  # عرض عناصر التصنيف

    path('cart/', views.cart, name='cart'),

  
    path('order-summary/<int:item_id>/', views.order_summary, name='order_summary'),
    path('remove/<int:item_id>/', views.remove_item, name='remove_item'),  # ✅ لازم دي تبقى موجودة

    path('update-item/<int:item_id>/', views.update_item, name='update_item'),

    path('complete-order/', views.complete_order, name='complete_order'),

]