from django.shortcuts import render


def catalog(request):
    # <h1>Каталог товаров</h1>
    return render(request, 'shop/catalog.html')


def orders(request):
    # <h1>Заказы</h1>
    return render(request, 'shop/orders.html')


def order_create(request):
    # <h1>Оформление заказа</h1>
    return render(request, 'shop/order_create.html')
