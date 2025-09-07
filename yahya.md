ده views بتاعي from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404
from .models import Category,MenuItem
from django.shortcuts import redirect
from .forms import OrderForm

from django.views.decorators.csrf import csrf_exempt

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
    
    
def order_summary(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))

        cart = request.session.get('cart', [])

        # تحقق هل العنصر موجود مسبقاً
        found = False
        for cart_item in cart:
            if cart_item['id'] == item.id:
                cart_item['quantity'] += quantity
                cart_item['total'] = float(item.price) * cart_item['quantity']
                found = True
                break

        if not found:
            cart.append({
                'id': item.id,
                'name': item.name,
                'price': float(item.price),
                'quantity': quantity,
                'total': float(item.price) * quantity
            })

        request.session['cart'] = cart
        request.session.modified = True  # تأكد إنه يتم حفظ التغيير

        return redirect('menu:cart')

    return render(request, 'menu/order_summary.html', {'item': item})


def cart(request):
    cart = request.session.get('cart', [])
    total_price = sum(item['total'] for item in cart)
    
    return render(request, 'menu/cart.html', {
        'cart': cart,
        'total_price': total_price
    })


    
def remove_item(request, item_id):
    cart = request.session.get('cart', [])

    cart = [item for item in cart if str(item['id']) != str(item_id)]

    request.session['cart'] = cart
    return redirect('menu:cart')



def update_item(request, item_id):
    if request.method == 'POST':
        new_quantity = request.POST.get('quantity')
        if new_quantity:
            cart = request.session.get('cart', [])
            for item in cart:
                if str(item['id']) == str(item_id):
                    item['quantity'] = int(new_quantity)
                    item['total'] = item['price'] * item['quantity']
                    break
            request.session['cart'] = cart
            request.session.modified = True  # مهم جدًا
    return redirect('menu:cart')


def complete_order(request):
    cart = request.session.get('cart', [])
    total_price = sum(item['total'] for item in cart)

    if not cart:
        return redirect('menu:cart')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.items = "\n".join(
                [f"{item['name']} (x{item['quantity']}) - {item['total']} EGP" for item in cart]
            )
            order.total_price = total_price
            order.save()

            request.session['cart'] = []
            request.session.modified = True

            return render(request, 'menu/order_success.html', {'order': order})
    else:
        form = OrderForm()

    return render(request, 'menu/complete_order.html', {
        'form': form,
        'cart': cart,
        'total_price': total_price,
    })