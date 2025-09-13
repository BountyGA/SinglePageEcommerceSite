from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product, Category

def product_list(request):
    products_qs = Product.objects.all().order_by("-id")
    categories = Category.objects.all()

    # Search
    query = request.GET.get("q")
    if query:
        products_qs = products_qs.filter(name__icontains=query) | products_qs.filter(description__icontains=query)

    # Filter by category
    category_filter = request.GET.get("category")
    if category_filter and category_filter != "all":
        products_qs = products_qs.filter(category__id=category_filter)

    # Pagination
    paginator = Paginator(products_qs, 8)
    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)

    context = {
        "products": products,
        "categories": categories,
        "query": query,
        "selected_category": category_filter,
    }
    return render(request, "products/index.html", context)
