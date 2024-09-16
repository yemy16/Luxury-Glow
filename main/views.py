from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product

def show_main(request):
    product_entries = Product.objects.all()
    context = {
        'app' : 'Luxury Glow',
        'name': 'Yemima Clara Nainggolan',
        'kelas': 'PBP B',
        'product_entries' : product_entries
    }

    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
