from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:id>/', views.recipes, name="recipe"),
    path('category/<int:category_id>/', views.category, name="category"),
]