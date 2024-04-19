from django.urls import path, include
from .import views
from .views import FoodCreateView 

app_name = 'restaurant'

urlpatterns = [
    path('', views.food_list, name = 'all_foods'),
    path('order/', include('order.urls')),
    path('<uuid:category_id>/', views.food_list, name = 'foods_by_category'),
    path('<uuid:category_id>/<uuid:food_id>/', views.food_detail, name = 'food_detail'),
    path('new/', FoodCreateView.as_view(), name='food_create'),
]