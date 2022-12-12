from django.urls import path
from .views import CoffeeListView, CoffeeDetailView,CoffeeUpdateView,CoffeeDeleteView,CoffeeCreateView
urlpatterns = [
    path('',CoffeeListView.as_view(),name='coffee_list'),
    path('<int:pk>',CoffeeDetailView.as_view(),name='coffee_detail'),
    path('update/<int:pk>',CoffeeUpdateView.as_view(),name='coffee_update'),
    path('delete/<int:pk>',CoffeeDeleteView.as_view(),name='coffee_delete'),
    path('create',CoffeeCreateView.as_view(),name='coffee_create'),
]