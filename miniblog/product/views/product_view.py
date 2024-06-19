from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from product.models import Category
from product.forms import ProductForm
from product.repositories.product import ProductRepository

repo = ProductRepository()

def product_list(request):
    productos = repo.get_all()
    return render(
        request,
        'products/list.html',
        dict(
            products=productos
        )
    )

def product_detail(request, id):
    producto = repo.get_by_id(id=id)
    return render(
        request,
        'products/detail.html',
        {"product":producto}
    )

def product_delete(request, id):
    producto = repo.get_by_id(id=id)
    repo.delete(producto=producto)
    return redirect('product_list')

@login_required(login_url='login')
def product_update(request, id):
    product = repo.get_by_id(id=id)
    categorias = Category.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        id_category = request.POST.get('id_category')
        category = Category.objects.get(id=id_category)

        repo.update(
            producto=product,
            nombre=name,
            precio=price,
            descripcion=description,
            stock=stock,
            categoria=category
        )
        return redirect('product_detail', product.id)

    return render(
        request,
        'products/update.html',
        dict(
            categories=categorias,
            product=product
        )
    )

def product_create(request):
    form = ProductForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            producto_nuevo = repo.create(
                nombre=form.cleaned_data['name'],
                descripcion=form.cleaned_data['description'],
                precio=form.cleaned_data['price'],
                cantidades=form.cleaned_data['stock'],
                categoria=form.cleaned_data['category']
            )
            return redirect('product_detail', producto_nuevo.id)


    # TODO: reemplazar esta linea por el repositorio de categorias
    categorias = Category.objects.all()
    return render (
        request,
        'products/create.html',
        {'form':form}
    )

def index_view(request):
    return render(
        request,
        'index/index.html'
    )