from django.shortcuts import render, redirect, get_object_or_404

from .models import Cart, CartItem
from store.models import Product


def get_cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=get_cart_id(request))
        cart_item = CartItem.objects.filter(cart=cart, is_active=True)
        for item in cart_item:
            total += (item.product.our_price * item.quantity)
            quantity += item.quantity

        tax = (total * 0.2)
        grand_total = total + tax
    except Exception as e:
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_item,
        'tax': tax,
        'grand_total': grand_total
    }

    return render(request, 'store/cart.html', context)


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=get_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=get_cart_id(request)
        )
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('cart:cart')


def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=get_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart:cart')


def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id=get_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart:cart')
