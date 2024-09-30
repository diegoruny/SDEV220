from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def menu(request):
    menu_items = [
        {'name': 'Espresso', 'price': 2.50},
        {'name': 'Cappuccino', 'price': 3.00},
        {'name': 'Latte', 'price': 3.50},
        {'name': 'Mocha', 'price': 4.00},
    ]
    return render(request, 'core/menu.html', {'menu_items': menu_items})

def contact(request):
    return render(request, 'core/contact.html')