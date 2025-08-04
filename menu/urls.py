
from django.urls import path

from . import views


app_name = 'menu'

urlpatterns = [
    path('', views.menu, name='menu'),

   
    path('category/<int:category_id>/', views.category_items, name='category_items'),  # عرض عناصر التصنيف


    
]