from django.shortcuts import render, get_object_or_404
from .models import Category, Food
from order.models import Feedback
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin


def food_list(request, category_id=None):
    category = None
    foods = Food.objects.filter(available=True)
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        foods = Food.objects.filter(category=category, available=True)

    paginator = Paginator(foods, 15)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        foods = paginator.page(page)
    except (EmptyPage, InvalidPage):
        foods = paginator.page(paginator.num_pages)

    return render(request, 'restaurant/category.html', {'category':category, 'foods':foods})    

def food_detail(request, category_id, food_id):
    food = get_object_or_404(Food, category_id=category_id, id=food_id)
    return render(request, 'restaurant/food.html', {'food':food})

# displayed when manager login to 'update menu'
class FoodCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'restaurant.add_food'
    model = Food
    fields = ('name', 'description', 'price', 'category','stock', 'image')
    template_name = 'restaurant/food_new.html' 