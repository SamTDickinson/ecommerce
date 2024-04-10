from .models import Category, Subcategory


def category_menu_link(request):
    links = Category.objects.all()
    return dict(category_links=links)


def subcategory_menu_link(request, category_slug=None):
    links = Subcategory.objects.all().filter(category_name=category_slug)
    return dict(links=links)
