from django.shortcuts import render, redirect
from .models import (
    Phone,
    Screen,
    Brand
)

order_items = [
    'Сортировать по названию',
    'Сортировать по цене убывание',
    'Сортировать по цене возрастание'
]

def home(request, order=0):
    attribute = 'name_phone' if order == 0 else 'price' if order == 2 else '-price'
    phones = Phone.objects.all().order_by(attribute).order_by('price')
    order_title = order_items[order]
    brands = Brand.objects.all()
    memories = [item.memory for item in phones]

    return render(request, 'index.html', { 
        'phones': phones,
        'order_title': order_title,
        'order_items': [(index, value) for index, value in enumerate(order_items) if index != order],
        'brands': brands,
        'memories': set(sorted(memories)),
    })

def cart(request):
    carts = Phone.objects.filter(cart=True)

    return render(request, 'cart.html', { 'carts': carts })

def add_cart(request, id):
    phone = Phone.objects.get(pk=id)
    phone.cart = not phone.cart
    phone.save()

    return redirect('home')

def delete_cart(request, id):
    phone = Phone.objects.get(pk=id)
    phone.cart = False
    phone.save()

    return redirect('cart')

def filter_by_memory(request, memory, order=0):
    order_title = order_items[order]
    phones = Phone.objects.all().filter(memory=memory).order_by('price')
    order_title = order_items[order]
    brands = Brand.objects.all()
    memories = [item.memory for item in Phone.objects.all()]
    
    return render(request, 'index.html', { 
        'phones': phones,
        'order_title': order_title,
        'order_items': [(index, value) for index, value in enumerate(order_items) if index != order],
        'brands': brands,
        'memories': set(sorted(memories))
    })
    
def filter_by_brand(request, brand, order=0):
    order_title = order_items[order]
    order_title = order_items[order]
    brands = Brand.objects.all()
    phones = Phone.objects.filter(brand_id=brand).order_by('price')
    memories = [item.memory for item in Phone.objects.all()]
    
    new_phones = []
    
    for item in Phone.objects.all():
        if str(item.brand_id) == brand:
            new_phones.append(item)
            
    
    return render(request, 'index.html', { 
        'phones': new_phones,
        'order_title': order_title,
        'order_items': [(index, value) for index, value in enumerate(order_items) if index != order],
        'brands': brands,
        'memories': set(sorted(memories))
    })
    
def get_current_phone(request, id):
    phone = Phone.objects.get(pk=id)
    screens = Screen.objects.filter(phone_id=id)
    # brand = Phone.objects.get()
    
    id = 0
    new_screens = {}
    
    for value in screens:
        id += 1
        new_screens[id] = value
    
    return render(request, 'phone.html', { 'phone': phone, 'screens': new_screens })

def filter_by_price(request, price_from=480, price_to=1500, order=0):
    order_title = order_items[order]
    order_title = order_items[order]
    brands = Brand.objects.all()
    phones = Phone.objects.all().order_by('price')
    
    # query = request.GET
    # min = query('min')
    # max = query('max')
    
    new_phones = []
    
    for phone in phones:
        if phone.price >= price_from and phone.price <= price_to:
            new_phones.append(phone)
    
    memories = [item.memory for item in Phone.objects.all()]
    
    return render(request, 'index.html', { 
        'phones': new_phones,
        'order_title': order_title,
        'order_items': [(index, value) for index, value in enumerate(order_items) if index != order],
        'brands': brands,
        'memories': set(sorted(memories)),
        'min': min,
        'max': max
    })